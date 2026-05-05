"""Locate the QR placeholder on an AI-generated poster via a Kimi-style vision API.

Returns the same `(x, y, w, h)` absolute-pixel tuple as `detect_qr_blank_box`
in `poster.py`, so the two detectors are interchangeable.
"""

from __future__ import annotations

import base64
import io
import json
import re
from typing import Any

import numpy as np
from PIL import Image

try:
    import requests
except ImportError as exc:
    requests = None
    _IMPORT_ERROR = exc
else:
    _IMPORT_ERROR = None


SYSTEM_PROMPT = (
    "You are a precise UI coordinate detector. "
    "Output ONLY valid JSON. No prose, no markdown fences."
)


def _build_user_prompt(crop_w: int, crop_h: int) -> str:
    return (
        f"This crop is {crop_w}x{crop_h} pixels from the lower-left of a Chinese "
        "Toastmasters poster. Find the WHITE SQUARE BLOCK reserved for a QR code: "
        "a clean near-white square (often surrounded by a dark blue or colored ring/border). "
        "Return JSON with PIXEL coordinates relative to THIS image, top-left origin: "
        '{"found": true, "x": <int>, "y": <int>, "w": <int>, "h": <int>}. '
        'If no such square exists, return {"found": false}. '
        "Do not return percentages. Do not add any other text."
    )


def _encode_image(crop: Image.Image, jpeg_quality: int) -> str:
    buf = io.BytesIO()
    crop.save(buf, format="JPEG", quality=jpeg_quality)
    return base64.b64encode(buf.getvalue()).decode("ascii")


def _extract_json_object(text: str) -> dict[str, Any] | None:
    """Pull the first balanced {...} block out of model output and parse it."""
    if not text:
        return None
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```[a-zA-Z0-9]*\n?", "", text)
        text = re.sub(r"\n?```$", "", text)
    depth = 0
    start = -1
    for i, ch in enumerate(text):
        if ch == "{":
            if depth == 0:
                start = i
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0 and start >= 0:
                snippet = text[start : i + 1]
                try:
                    return json.loads(snippet)
                except json.JSONDecodeError:
                    return None
    return None


def _normalize_to_square(
    rx: int, ry: int, rw: int, rh: int, crop_w: int, crop_h: int
) -> tuple[int, int, int, int]:
    """Convert returned bbox to a square centered on the original bbox, clamped to crop."""
    cx = rx + rw / 2
    cy = ry + rh / 2
    side = max(rw, rh)
    side = min(side, min(crop_w, crop_h))
    nx = round(cx - side / 2)
    ny = round(cy - side / 2)
    nx = max(0, min(int(nx), crop_w - side))
    ny = max(0, min(int(ny), crop_h - side))
    return nx, ny, int(side), int(side)


def _pixel_sanity_check(
    crop: Image.Image, box: tuple[int, int, int, int]
) -> tuple[bool, float, float]:
    """Sample the center 60% of the box and require it to be mostly near-white.

    Instead of strict uniformity (std), we count the percentage of pixels
    that are near-white (all channels > 210). This tolerates the common case
    where the model's bounding box is slightly larger than the actual white
    square and bleeds a few pixels into the surrounding dark-blue ring.
    """
    nx, ny, side, _ = box
    inset = max(1, side // 5)
    region = np.asarray(
        crop.crop((nx + inset, ny + inset, nx + side - inset, ny + side - inset))
        .convert("RGB")
    )
    if region.size == 0:
        return False, 0.0, 0.0
    median = float(np.median(region))
    # Percentage of near-white pixels (all channels > 210)
    near_white = np.all(region > 210, axis=2)
    white_ratio = float(np.mean(near_white))
    return (median > 220.0 and white_ratio >= 0.55), median, white_ratio


def detect_qr_box_with_vision(
    poster: Image.Image,
    search_region: tuple[int, int, int, int],
    *,
    config: dict[str, Any],
    api_key: str,
    debug_sink: dict[str, Any] | None = None,
) -> tuple[int, int, int, int] | None:
    """Ask the Kimi vision API to locate the QR placeholder.

    `search_region` is `(left, top, right, bottom)` on the full 1080x1920 poster.
    Only the cropped region is sent to the model. On any failure (network, JSON,
    sanity check) returns None so the caller can fall through to pixel detection
    or the configured `qr_box`.
    """
    if requests is None:
        if debug_sink is not None:
            debug_sink["vision_error"] = f"requests not installed: {_IMPORT_ERROR}"
        return None

    left, top, right, bottom = search_region
    crop = poster.crop((left, top, right, bottom)).convert("RGB")
    crop_w, crop_h = crop.size

    jpeg_quality = int(config.get("jpeg_quality", 85))
    base_url = str(config.get("base_url", "")).rstrip("/")
    if not base_url:
        if debug_sink is not None:
            debug_sink["vision_error"] = "qr_vision.base_url is empty"
        return None
    # Auto-append /v1 if the URL does not already end with a version segment.
    if not re.search(r"/v\d+$", base_url):
        base_url += "/v1"
    url = f"{base_url}/chat/completions"

    payload = {
        "model": config.get("model", "k2.6"),
        "temperature": 0,
        "max_tokens": int(config.get("max_tokens", 200)),
        "thinking": {"type": "disabled"},
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": _build_user_prompt(crop_w, crop_h)},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{_encode_image(crop, jpeg_quality)}"
                        },
                    },
                ],
            },
        ],
    }
    x_client = str(config.get("x_client", "claude-code"))
    user_agent = str(config.get("user_agent", "claude-code/1.0"))
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "x-client": x_client,
        "User-Agent": user_agent,
    }
    timeout = float(config.get("timeout_seconds", 30))

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=timeout)
    except requests.RequestException as exc:
        if debug_sink is not None:
            debug_sink["vision_error"] = f"http_request_failed: {exc}"
        return None

    if response.status_code != 200:
        if debug_sink is not None:
            debug_sink["vision_error"] = (
                f"http_status={response.status_code} body={response.text[:300]!r}"
            )
        return None

    try:
        body = response.json()
        content = body["choices"][0]["message"]["content"]
    except (ValueError, KeyError, IndexError, TypeError) as exc:
        if debug_sink is not None:
            debug_sink["vision_error"] = f"response_parse_failed: {exc}"
        return None

    if debug_sink is not None:
        debug_sink["vision_raw_response"] = content

    parsed = _extract_json_object(content)
    if parsed is None:
        if debug_sink is not None:
            debug_sink["vision_error"] = "no_json_object_in_response"
        return None
    if not parsed.get("found"):
        if debug_sink is not None:
            debug_sink["vision_error"] = "model_reported_not_found"
        return None

    try:
        rx = int(parsed["x"])
        ry = int(parsed["y"])
        rw = int(parsed["w"])
        rh = int(parsed["h"])
    except (KeyError, TypeError, ValueError) as exc:
        if debug_sink is not None:
            debug_sink["vision_error"] = f"missing_or_bad_coords: {exc}"
        return None

    if rw <= 0 or rh <= 0 or rw > crop_w * 2 or rh > crop_h * 2:
        if debug_sink is not None:
            debug_sink["vision_error"] = (
                f"implausible_size rw={rw} rh={rh} crop=({crop_w},{crop_h})"
            )
        return None

    nx, ny, side, _ = _normalize_to_square(rx, ry, rw, rh, crop_w, crop_h)
    if side < 30:
        if debug_sink is not None:
            debug_sink["vision_error"] = f"side_too_small={side}"
        return None

    ok, median, white_ratio = _pixel_sanity_check(crop, (nx, ny, side, side))
    if debug_sink is not None:
        debug_sink["vision_relative_box"] = (nx, ny, side, side)
        debug_sink["vision_pixel_stats"] = {"median": median, "white_ratio": white_ratio}
    if not ok:
        if debug_sink is not None:
            debug_sink["vision_error"] = (
                f"pixel_sanity_failed median={median:.1f} white_ratio={white_ratio:.2f}"
            )
        return None

    return (left + nx, top + ny, side, side)
