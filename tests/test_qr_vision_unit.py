"""Unit tests for qr_vision: mock the HTTP layer and verify parsing/normalization.

These tests do not hit the real Kimi API. They patch `qr_vision.requests.post`
to return canned responses so failure modes (timeout, HTTP errors, malformed
JSON, AI lying about a non-white box) all stay in CI.
"""

from __future__ import annotations

from unittest.mock import patch, MagicMock

import pytest
from PIL import Image, ImageDraw

import qr_vision


SEARCH_REGION = (0, 1450, 360, 1900)
CONFIG = {
    "enabled": True,
    "model": "kimi-for-coding",
    "base_url": "https://api.kimi.com/coding/",
    "api_key_env": "KIMI_API_KEY",
    "x_client": "claude-code",
    "user_agent": "claude-code/1.0",
    "timeout_seconds": 5,
    "jpeg_quality": 85,
    "max_tokens": 512,
}
API_KEY = "sk-test-fake"


def _make_poster_with_white_block(
    block_xy: tuple[int, int] = (60, 1610), block_side: int = 160
) -> Image.Image:
    """Return a 1080x1920 dark-blue poster with a near-white square at given pos."""
    poster = Image.new("RGBA", (1080, 1920), (0, 65, 120, 255))
    draw = ImageDraw.Draw(poster)
    bx, by = block_xy
    draw.rectangle(
        (bx, by, bx + block_side, by + block_side),
        fill=(248, 248, 248, 255),
    )
    return poster


def _mock_response(content: str, status_code: int = 200) -> MagicMock:
    response = MagicMock()
    response.status_code = status_code
    response.text = content if status_code != 200 else "OK"
    response.json.return_value = {
        "choices": [{"message": {"content": content}}]
    }
    return response


def test_success_returns_absolute_pixel_box():
    poster = _make_poster_with_white_block(block_xy=(60, 1610), block_side=160)
    # Model returns coords RELATIVE to the cropped search region.
    # crop = poster.crop((0,1450,360,1900)); block at (60, 160) inside crop, side 160.
    payload = '{"found": true, "x": 60, "y": 160, "w": 160, "h": 160}'
    sink: dict = {}
    with patch("qr_vision.requests.post", return_value=_mock_response(payload)) as post:
        box = qr_vision.detect_qr_box_with_vision(
            poster, SEARCH_REGION, config=CONFIG, api_key=API_KEY, debug_sink=sink
        )
    assert box is not None
    x, y, w, h = box
    # Absolute coords = relative + (left=0, top=1450)
    assert (x, y) == (60, 1610)
    assert w == h == 160
    # Sink populated with raw response and stats for debug image.
    assert sink["vision_raw_response"] == payload
    assert "vision_pixel_stats" in sink
    # URL should be base_url stripped + /chat/completions
    called_url = post.call_args.args[0]
    assert called_url == "https://api.kimi.com/coding/v1/chat/completions"


def test_found_false_returns_none():
    poster = _make_poster_with_white_block()
    payload = '{"found": false}'
    sink: dict = {}
    with patch("qr_vision.requests.post", return_value=_mock_response(payload)):
        box = qr_vision.detect_qr_box_with_vision(
            poster, SEARCH_REGION, config=CONFIG, api_key=API_KEY, debug_sink=sink
        )
    assert box is None
    assert sink["vision_error"] == "model_reported_not_found"


def test_markdown_fence_is_stripped():
    poster = _make_poster_with_white_block(block_xy=(60, 1610), block_side=160)
    payload = '```json\n{"found": true, "x": 60, "y": 160, "w": 160, "h": 160}\n```'
    with patch("qr_vision.requests.post", return_value=_mock_response(payload)):
        box = qr_vision.detect_qr_box_with_vision(
            poster, SEARCH_REGION, config=CONFIG, api_key=API_KEY
        )
    assert box == (60, 1610, 160, 160)


def test_extra_prose_around_json_is_tolerated():
    poster = _make_poster_with_white_block(block_xy=(60, 1610), block_side=160)
    payload = (
        "Sure, here is the bounding box: "
        '{"found": true, "x": 60, "y": 160, "w": 160, "h": 160} '
        "Hope this helps."
    )
    with patch("qr_vision.requests.post", return_value=_mock_response(payload)):
        box = qr_vision.detect_qr_box_with_vision(
            poster, SEARCH_REGION, config=CONFIG, api_key=API_KEY
        )
    assert box == (60, 1610, 160, 160)


def test_http_500_returns_none():
    poster = _make_poster_with_white_block()
    sink: dict = {}
    with patch(
        "qr_vision.requests.post",
        return_value=_mock_response("internal error", status_code=500),
    ):
        box = qr_vision.detect_qr_box_with_vision(
            poster, SEARCH_REGION, config=CONFIG, api_key=API_KEY, debug_sink=sink
        )
    assert box is None
    assert "http_status=500" in sink["vision_error"]


def test_request_timeout_returns_none():
    import requests as real_requests

    poster = _make_poster_with_white_block()
    sink: dict = {}
    with patch(
        "qr_vision.requests.post",
        side_effect=real_requests.exceptions.Timeout("read timed out"),
    ):
        box = qr_vision.detect_qr_box_with_vision(
            poster, SEARCH_REGION, config=CONFIG, api_key=API_KEY, debug_sink=sink
        )
    assert box is None
    assert sink["vision_error"].startswith("http_request_failed")


def test_rectangle_bbox_normalized_to_square():
    """Model returns a non-square bbox; detector should re-center as a square."""
    poster = _make_poster_with_white_block(block_xy=(60, 1610), block_side=160)
    # Slightly-rectangular returned bbox (e.g. 150x180 around the same center).
    payload = '{"found": true, "x": 65, "y": 150, "w": 150, "h": 180}'
    with patch("qr_vision.requests.post", return_value=_mock_response(payload)):
        box = qr_vision.detect_qr_box_with_vision(
            poster, SEARCH_REGION, config=CONFIG, api_key=API_KEY
        )
    assert box is not None
    x, y, w, h = box
    assert w == h, "must be square after normalization"
    # Center near the original block center (~(140, 1690))
    cx = x + w / 2
    cy = y + h / 2
    assert abs(cx - 140) <= 6
    assert abs(cy - 1690) <= 6


def test_out_of_bounds_coords_are_clamped():
    """Model returns coords that overflow the crop; detector must clamp."""
    poster = _make_poster_with_white_block(block_xy=(60, 1610), block_side=160)
    # Crop is 360x450; ask for a 200x200 box starting at (250, 350): right edge 450 > 360.
    payload = '{"found": true, "x": 250, "y": 350, "w": 200, "h": 200}'
    sink: dict = {}
    with patch("qr_vision.requests.post", return_value=_mock_response(payload)):
        box = qr_vision.detect_qr_box_with_vision(
            poster, SEARCH_REGION, config=CONFIG, api_key=API_KEY, debug_sink=sink
        )
    # Either clamps and the pixel sanity check fails (returning None), or it
    # clamps to a region that happens to be uniform enough; both are acceptable
    # since the detector must NEVER return coords that exceed the search region.
    if box is not None:
        x, y, w, h = box
        assert 0 <= x and 0 <= y
        assert x + w <= SEARCH_REGION[2]
        assert y + h <= SEARCH_REGION[3]


def test_pixel_sanity_rejects_non_white_box():
    """Even if the model returns valid JSON, a box pointing at a non-white area must fail."""
    poster = _make_poster_with_white_block(block_xy=(60, 1610), block_side=160)
    # Point the box at a region of solid blue background (not the white block).
    payload = '{"found": true, "x": 250, "y": 30, "w": 80, "h": 80}'
    sink: dict = {}
    with patch("qr_vision.requests.post", return_value=_mock_response(payload)):
        box = qr_vision.detect_qr_box_with_vision(
            poster, SEARCH_REGION, config=CONFIG, api_key=API_KEY, debug_sink=sink
        )
    assert box is None
    assert "pixel_sanity_failed" in sink["vision_error"]
    # Stats should show low white_ratio.
    assert sink["vision_pixel_stats"]["white_ratio"] < 0.55


def test_garbage_response_returns_none():
    poster = _make_poster_with_white_block()
    sink: dict = {}
    with patch(
        "qr_vision.requests.post",
        return_value=_mock_response("definitely not json"),
    ):
        box = qr_vision.detect_qr_box_with_vision(
            poster, SEARCH_REGION, config=CONFIG, api_key=API_KEY, debug_sink=sink
        )
    assert box is None
    assert sink["vision_error"] == "no_json_object_in_response"


def test_missing_coords_returns_none():
    """found=true but x/y/w/h missing — must fail gracefully."""
    poster = _make_poster_with_white_block()
    payload = '{"found": true, "x": 60}'
    sink: dict = {}
    with patch("qr_vision.requests.post", return_value=_mock_response(payload)):
        box = qr_vision.detect_qr_box_with_vision(
            poster, SEARCH_REGION, config=CONFIG, api_key=API_KEY, debug_sink=sink
        )
    assert box is None
    assert sink["vision_error"].startswith("missing_or_bad_coords")


def test_request_payload_shape():
    """Verify model name, temperature, and image data URI are sent correctly."""
    poster = _make_poster_with_white_block(block_xy=(60, 1610), block_side=160)
    payload = '{"found": true, "x": 60, "y": 160, "w": 160, "h": 160}'
    with patch(
        "qr_vision.requests.post", return_value=_mock_response(payload)
    ) as post:
        qr_vision.detect_qr_box_with_vision(
            poster, SEARCH_REGION, config=CONFIG, api_key=API_KEY
        )
    body = post.call_args.kwargs["json"]
    assert body["model"] == "kimi-for-coding"
    assert body["temperature"] == 0
    assert body["max_tokens"] == 512
    assert body["thinking"] == {"type": "disabled"}
    user_msg = body["messages"][1]
    image_part = user_msg["content"][1]
    assert image_part["type"] == "image_url"
    assert image_part["image_url"]["url"].startswith("data:image/jpeg;base64,")
    headers = post.call_args.kwargs["headers"]
    assert headers["Authorization"] == f"Bearer {API_KEY}"
    assert headers["x-client"] == "claude-code"
    assert headers["User-Agent"] == "claude-code/1.0"
