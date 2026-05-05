#!/usr/bin/env python3
"""Prepare image prompts and compose Toastmasters mobile posters."""

from __future__ import annotations

import argparse
import json
import re
import textwrap
from collections import deque
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps


POSTER_SIZE = (1080, 1920)
DEFAULT_ACCENT = "#F2C76E"
DEFAULT_BRAND = "#004165"


@dataclass(frozen=True)
class EventPaths:
    root: Path
    output_dir: Path
    prompt_file: Path
    final_file: Path
    ai_final_file: Path
    ai_clean_final_file: Path


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_event(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    validate_event(data)
    return data


def validate_event(data: dict[str, Any]) -> None:
    required = [
        ("slug",),
        ("theme",),
        ("speaker", "name"),
        ("speaker", "title"),
        ("speaker", "bio"),
        ("event", "time"),
        ("event", "location"),
        ("club", "name"),
        ("club", "meeting_number"),
        ("assets", "speaker_photo"),
        ("assets", "logo"),
        ("assets", "qr"),
    ]
    missing = []
    for keys in required:
        current: Any = data
        for key in keys:
            if not isinstance(current, dict) or not current.get(key):
                missing.append(".".join(keys))
                break
            current = current[key]
    if missing:
        raise SystemExit("Missing required field(s): " + ", ".join(missing))

    slug = str(data["slug"])
    if not re.fullmatch(r"[A-Za-z0-9._-]+", slug):
        raise SystemExit("slug can only contain letters, numbers, dots, underscores, and hyphens")


def event_paths(event: dict[str, Any]) -> EventPaths:
    root = repo_root()
    output_dir = root / "outputs" / event["slug"]
    return EventPaths(
        root=root,
        output_dir=output_dir,
        prompt_file=output_dir / "prompt.md",
        final_file=output_dir / "final-poster.png",
        ai_final_file=output_dir / "final-poster-ai.png",
        ai_clean_final_file=output_dir / "final-poster-ai-clean.png",
    )


def resolve_asset(root: Path, value: str) -> Path:
    path = Path(value)
    if not path.is_absolute():
        path = root / path
    return path


def check_assets(event: dict[str, Any], root: Path, strict: bool) -> list[str]:
    warnings = []
    for label, value in event["assets"].items():
        path = resolve_asset(root, value)
        if not path.exists():
            message = f"{label}: missing file {path}"
            if strict:
                raise SystemExit(message)
            warnings.append(message)
            continue
        try:
            with Image.open(path) as image:
                width, height = image.size
        except Exception as exc:  # noqa: BLE001
            message = f"{label}: cannot open {path} ({exc})"
            if strict:
                raise SystemExit(message)
            warnings.append(message)
            continue
        if label == "speaker_photo" and min(width, height) < 900:
            warnings.append(f"{label}: photo is {width}x{height}; use a clearer portrait if possible")
        if label == "qr" and min(width, height) < 360:
            warnings.append(f"{label}: QR is {width}x{height}; 600px+ is safer for print and sharing")
    return warnings


def content_warnings(event: dict[str, Any]) -> list[str]:
    poster_copy = event.get("poster_copy", {})
    warnings = []
    if not poster_copy.get("benefits"):
        warnings.append("poster_copy.benefits is missing; add this event's specific \"你将收获\" items")
    if not poster_copy.get("visual_keywords"):
        warnings.append("poster_copy.visual_keywords is missing; prompt will use generic theme-related visual metaphors")
    if not poster_copy.get("visual_direction"):
        warnings.append("poster_copy.visual_direction is missing; prompt will use a generic event-poster direction")
    if not poster_copy.get("reference_direction"):
        warnings.append("poster_copy.reference_direction is missing; prompt will use a generic clean training-poster reference")
    return warnings


def format_benefits(benefits: Any) -> str:
    if not benefits:
        return "- （请在 poster_copy.benefits 中补充本期具体收获点）"

    lines = []
    for item in benefits:
        if isinstance(item, dict):
            title = str(item.get("title", "")).strip()
            description = str(item.get("description", "")).strip()
            if title and description:
                lines.append(f"- {title}：{description}")
            elif title:
                lines.append(f"- {title}")
        elif item:
            lines.append(f"- {item}")
    return "\n".join(lines) if lines else "- （请在 poster_copy.benefits 中补充本期具体收获点）"


def format_visual_keywords(keywords: Any) -> str:
    if isinstance(keywords, list) and keywords:
        return "、".join(str(keyword) for keyword in keywords if str(keyword).strip())
    if isinstance(keywords, str) and keywords.strip():
        return keywords.strip()
    return "围绕本期主题生成相关视觉隐喻，避免无关装饰。"


def prompt_variants(event: dict[str, Any]) -> list[tuple[str, str]]:
    speaker = event["speaker"]
    theme = event["theme"]
    subtitle = event.get("subtitle", "")
    event_info = event["event"]
    club = event["club"]
    poster_copy = event.get("poster_copy", {})
    benefits_text = format_benefits(poster_copy.get("benefits"))
    visual_keywords = format_visual_keywords(poster_copy.get("visual_keywords"))
    visual_direction = poster_copy.get(
        "visual_direction",
        f"Create visual metaphors that match the event theme “{theme}” and support public speaking, communication, and growth.",
    )
    reference_direction = poster_copy.get(
        "reference_direction",
        'clean modern public-speaking training poster, speaker portrait, large left-side title, structured guest intro, "你将收获" benefits row, deep-blue bottom information bar, elegant icons, generous spacing, premium but clear.',
    )
    call_to_action = poster_copy.get("call_to_action", "扫码报名，一起开启表达之旅！")
    footer = poster_copy.get("footer", "TOASTMASTERS 国际演讲俱乐部")
    base = f"""
Use case: ads-marketing
Asset type: complete 1080x1920 vertical Chinese mobile poster for WeChat sharing
Primary request: Design a polished, complete Toastmasters event poster in Chinese. The poster must feel more like a finished premium training/event poster than a background template.
Reference direction: {reference_direction}
Input image: Use the provided speaker portrait as the main person. Preserve recognizable facial structure, hairstyle, age, and professional business presence. Keep one person only.
Official brand/QR handling: You may create a polished Toastmasters-style top brand area and icon as part of the complete poster. Do not create any QR code. In the lower-left event bar, reserve one clean blank white square area for a real QR code overlay; do not draw a dashed frame, do not draw a fake QR, and do not write placeholder words such as “放置二维码” inside that blank square.
Top header layout: Put the Toastmasters-style icon on the top-left. Put “{club["name"]} / {club["meeting_number"]}” directly to the right of that icon in the same compact header row or header area. Do not add a separate English brand slogan or generic Chinese tagline; the icon already communicates the Toastmasters brand. Do not repeat the club name and meeting number again above the main title.
Exact Chinese copy to include:
- 顶部品牌行: {club["name"]} / {club["meeting_number"]}
- 主标题: {theme}
- 副标题: {subtitle}
- 分享嘉宾: {speaker["name"]}
- 嘉宾身份: {speaker["title"]}
- 嘉宾介绍: {speaker["bio"]}
- 你将收获:
{benefits_text}
- 时间: {event_info["time"]}
- 地点: {event_info["location"]}
- 费用: {event_info.get("fee", "")}
- 行动语: {call_to_action}
- 页脚: {footer}
Theme visual direction: {visual_direction}
Theme visual keywords: {visual_keywords}
Typography: Chinese text must be readable, high-contrast, and professionally aligned. Use bold dark-blue title typography, smaller clean body text, consistent spacing, no chaotic text blocks.
Hard constraints: no extra people, no distorted face, no fake QR code, no dashed QR placeholder frame, no QR placeholder text, no watermark, no random unreadable text, no unrelated icons.
"""
    variants = [
        (
            "candidate-ai-clean-1 清爽培训海报",
            base
            + """
Composition: Closest to the provided reference poster. Light blue-white gradient, right-side full-height speaker, left-side large title, mid-lower guest intro, four benefit cards, bottom deep-blue event bar.
Mood: clean, bright, credible, inviting, high-end public training poster.
""",
        ),
        (
            "candidate-ai-clean-2 高级杂志感完整海报",
            base
            + """
Composition: More premium editorial and spacious. Keep a refined light background, strong portrait presence, large title, and elegant theme-related visual metaphors. Information hierarchy must remain very clear.
Mood: executive, premium, modern, polished, still readable on mobile.
""",
        ),
        (
            "candidate-ai-clean-3 强主题传播吸睛版",
            base
            + """
Composition: Stronger theme expression. Add tasteful visual elements from the configured theme keywords around the speaker, while preserving readable blocks for all event copy.
Mood: memorable, energetic, intelligent, premium, optimized for attracting attention in WeChat feeds.
""",
        ),
    ]
    return [(title, textwrap.dedent(prompt).strip()) for title, prompt in variants]


def write_prompts(event: dict[str, Any], paths: EventPaths, warnings: Iterable[str]) -> None:
    paths.output_dir.mkdir(parents=True, exist_ok=True)
    sections = [
        "# 生图提示词",
        "",
        "把下面 3 条提示词分别交给 ChatGPT image2 / 生图工具生成完整中文海报。生成结果保存为 `candidate-ai-clean-1.png`、`candidate-ai-clean-2.png`、`candidate-ai-clean-3.png`。",
        "",
        "注意：中文排版和顶部品牌区交给生图模型完成；二维码仍然在最后由脚本覆盖，避免二维码被 AI 仿制。",
        "",
    ]
    warnings = list(warnings)
    if warnings:
        sections.extend(["## 素材检查提醒", ""])
        sections.extend([f"- {warning}" for warning in warnings])
        sections.append("")

    for index, (title, prompt) in enumerate(prompt_variants(event), start=1):
        sections.extend(
            [
                f"## {title}",
                "",
                "```text",
                prompt,
                "```",
                "",
                f"保存为：`outputs/{event['slug']}/candidate-ai-clean-{index}.png`",
                "",
            ]
        )
    paths.prompt_file.write_text("\n".join(sections), encoding="utf-8")


def find_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/Hiragino Sans GB.ttc",
        "/System/Library/Fonts/STHeiti Light.ttc",
        "/Library/Fonts/Arial Unicode.ttf",
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
        "/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for candidate in candidates:
        if candidate and Path(candidate).exists():
            return ImageFont.truetype(candidate, size=size)
    return ImageFont.load_default()


def hex_to_rgba(value: str, alpha: int = 255) -> tuple[int, int, int, int]:
    value = value.strip().lstrip("#")
    if len(value) != 6:
        value = DEFAULT_ACCENT.lstrip("#")
    return (int(value[0:2], 16), int(value[2:4], 16), int(value[4:6], 16), alpha)


def cover_image(image: Image.Image, size: tuple[int, int]) -> Image.Image:
    return ImageOps.fit(image.convert("RGB"), size, method=Image.Resampling.LANCZOS, centering=(0.5, 0.5))


def rounded_rectangle_mask(size: tuple[int, int], radius: int) -> Image.Image:
    mask = Image.new("L", size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, size[0], size[1]), radius=radius, fill=255)
    return mask


def fit_within(image: Image.Image, max_size: tuple[int, int]) -> Image.Image:
    image = image.convert("RGBA")
    image.thumbnail(max_size, Image.Resampling.LANCZOS)
    return image


def fit_cover_transparent(image: Image.Image, max_size: tuple[int, int]) -> Image.Image:
    return fit_within(image, max_size)


def box_from_layout(event: dict[str, Any], key: str, default: list[int]) -> tuple[int, int, int, int]:
    raw = event.get("layout", {}).get(key, default)
    if not isinstance(raw, list) or len(raw) != 4:
        raw = default
    x, y, width, height = [int(value) for value in raw]
    return x, y, width, height


def region_from_layout(event: dict[str, Any], key: str, default: list[int]) -> tuple[int, int, int, int]:
    raw = event.get("layout", {}).get(key, default)
    if not isinstance(raw, list) or len(raw) != 4:
        raw = default
    left, top, right, bottom = [int(value) for value in raw]
    return left, top, right, bottom


def _hex_to_rgb(value: str | None) -> tuple[int, int, int] | None:
    if not value:
        return None
    text = str(value).strip().lstrip("#")
    if len(text) != 6:
        return None
    try:
        return int(text[0:2], 16), int(text[2:4], 16), int(text[4:6], 16)
    except ValueError:
        return None


def _luma(rgb: np.ndarray) -> np.ndarray:
    return 0.299 * rgb[..., 0] + 0.587 * rgb[..., 1] + 0.114 * rgb[..., 2]


def detect_qr_blank_box(
    poster: Image.Image,
    search_region: tuple[int, int, int, int],
    *,
    ring_hint_rgb: tuple[int, int, int] | None = None,
    debug_sink: dict[str, Any] | None = None,
) -> tuple[int, int, int, int] | None:
    """Detect the clean blank square the AI poster reserves for the QR overlay.

    Generic, color-agnostic ring judgment: a candidate white patch must be
    enclosed by a ring whose pixels are color-consistent and high-contrast vs
    white. We do *not* assume the ring is blue or any specific color. The
    optional ring_hint_rgb is only a soft scoring boost.
    """
    left, top, right, bottom = search_region
    width, height = poster.size
    left = max(0, min(left, width - 1))
    top = max(0, min(top, height - 1))
    right = max(left + 1, min(right, width))
    bottom = max(top + 1, min(bottom, height))

    crop = poster.convert("RGB").crop((left, top, right, bottom))
    arr = np.asarray(crop, dtype=np.uint8)
    crop_h, crop_w = arr.shape[:2]

    min_channel = arr.min(axis=2)
    max_channel = arr.max(axis=2)
    raw_white = (min_channel >= 210) & ((max_channel - min_channel) <= 45)

    mask_image = Image.fromarray((raw_white.astype(np.uint8) * 255))
    closed_image = mask_image.filter(ImageFilter.MaxFilter(3)).filter(ImageFilter.MinFilter(3))
    mask = np.asarray(closed_image) > 0

    seen = np.zeros_like(mask)
    components: list[tuple[int, int, int, int, int]] = []
    for start_y in range(crop_h):
        row = mask[start_y]
        for start_x in range(crop_w):
            if not row[start_x] or seen[start_y, start_x]:
                continue
            queue: deque[tuple[int, int]] = deque()
            queue.append((start_x, start_y))
            seen[start_y, start_x] = True
            x_lo = x_hi = start_x
            y_lo = y_hi = start_y
            area = 0
            while queue:
                x, y = queue.popleft()
                area += 1
                if x < x_lo:
                    x_lo = x
                if x > x_hi:
                    x_hi = x
                if y < y_lo:
                    y_lo = y
                if y > y_hi:
                    y_hi = y
                for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if 0 <= nx < crop_w and 0 <= ny < crop_h and mask[ny, nx] and not seen[ny, nx]:
                        seen[ny, nx] = True
                        queue.append((nx, ny))
            components.append((area, x_lo, y_lo, x_hi, y_hi))

    candidates: list[dict[str, Any]] = []
    for area, x_lo, y_lo, x_hi, y_hi in components:
        bbox_w = x_hi - x_lo + 1
        bbox_h = y_hi - y_lo + 1
        if area < 3000 or bbox_w < 70 or bbox_h < 70:
            continue
        aspect = bbox_w / bbox_h
        if not 0.55 <= aspect <= 1.8:
            continue
        fill = area / (bbox_w * bbox_h)
        if fill < 0.55:
            continue

        sub_mask = mask[y_lo : y_hi + 1, x_lo : x_hi + 1]
        col_cov = sub_mask.mean(axis=0)
        row_cov = sub_mask.mean(axis=1)
        col_threshold = max(0.85, float(col_cov.max()) * 0.85)
        row_threshold = max(0.85, float(row_cov.max()) * 0.85)
        cols_ok = np.where(col_cov >= col_threshold)[0]
        rows_ok = np.where(row_cov >= row_threshold)[0]
        if cols_ok.size < 60 or rows_ok.size < 60:
            continue
        core_x_lo = x_lo + int(cols_ok.min())
        core_x_hi = x_lo + int(cols_ok.max())
        core_y_lo = y_lo + int(rows_ok.min())
        core_y_hi = y_lo + int(rows_ok.max())
        core_w = core_x_hi - core_x_lo + 1
        core_h = core_y_hi - core_y_lo + 1
        if core_w < 60 or core_h < 60:
            continue

        side = min(core_w, core_h)
        center_x = (core_x_lo + core_x_hi) / 2.0
        center_y = (core_y_lo + core_y_hi) / 2.0
        sx = int(round(center_x - side / 2.0))
        sy = int(round(center_y - side / 2.0))
        sx = max(0, min(sx, crop_w - side))
        sy = max(0, min(sy, crop_h - side))

        ring_pad = 16
        buffer_pad = 4
        rx0 = max(0, sx - ring_pad)
        ry0 = max(0, sy - ring_pad)
        rx1 = min(crop_w, sx + side + ring_pad)
        ry1 = min(crop_h, sy + side + ring_pad)
        ring_mask_arr = np.zeros((crop_h, crop_w), dtype=bool)
        ring_mask_arr[ry0:ry1, rx0:rx1] = True
        bx0 = max(0, sx - buffer_pad)
        by0 = max(0, sy - buffer_pad)
        bx1 = min(crop_w, sx + side + buffer_pad)
        by1 = min(crop_h, sy + side + buffer_pad)
        ring_mask_arr[by0:by1, bx0:bx1] = False
        ring_count = int(ring_mask_arr.sum())
        if ring_count < 200:
            continue

        ring_pixels = arr[ring_mask_arr].astype(np.int16)
        ring_median = np.median(ring_pixels, axis=0)
        consistency = float(np.mean(np.abs(ring_pixels - ring_median).sum(axis=1)))
        ring_luma = float(_luma(ring_median[None, :])[0])
        contrast = 255.0 - ring_luma

        ring_passes = consistency <= 150.0 and contrast >= 60.0

        core_inset = max(8, side // 4)
        cs_x0 = sx + core_inset
        cs_y0 = sy + core_inset
        cs_x1 = sx + side - core_inset
        cs_y1 = sy + side - core_inset
        if cs_x1 > cs_x0 and cs_y1 > cs_y0:
            core_sample = arr[cs_y0:cs_y1, cs_x0:cs_x1]
            core_min = float(core_sample.min())
            core_median = float(np.median(core_sample))
        else:
            core_min = 0.0
            core_median = 0.0
        pure_white_block = (
            core_median >= 245.0
            and core_min >= 200.0
            and fill >= 0.95
            and side >= 140
            and 0.8 <= (core_w / core_h) <= 1.25
        )

        if not ring_passes and not pure_white_block:
            continue

        square_score = 1.0 - abs(1.0 - (core_w / core_h))
        fill_score = min(fill, 1.0)
        size_score = min((side * side) / 40000.0, 1.0)
        consistency_score = max(0.0, 1.0 - consistency / 150.0)
        contrast_score = min(contrast / 120.0, 1.0)
        hint_score = 0.0
        ring_hint_distance: float | None = None
        if ring_hint_rgb is not None:
            hint = np.asarray(ring_hint_rgb, dtype=np.float64)
            ring_hint_distance = float(np.linalg.norm(ring_median - hint))
            hint_score = max(0.0, 1.0 - ring_hint_distance / 120.0)

        score = (
            square_score * 1.6
            + fill_score * 1.0
            + size_score * 0.8
            + consistency_score * 1.0
            + contrast_score * 1.0
            + hint_score * 0.4
            + (2.0 if ring_passes else 0.0)
            + (0.5 if pure_white_block else 0.0)
        )

        candidates.append(
            {
                "score": score,
                "box": (left + sx, top + sy, side, side),
                "raw_bbox": (left + x_lo, top + y_lo, bbox_w, bbox_h),
                "core_bbox": (left + core_x_lo, top + core_y_lo, core_w, core_h),
                "fill": fill,
                "aspect": aspect,
                "consistency": consistency,
                "contrast": contrast,
                "ring_median": tuple(int(c) for c in ring_median),
                "ring_hint_distance": ring_hint_distance,
                "ring_passes": ring_passes,
                "pure_white_block": pure_white_block,
                "core_min": core_min,
                "core_median": core_median,
                "score_components": {
                    "square": square_score,
                    "fill": fill_score,
                    "size": size_score,
                    "consistency": consistency_score,
                    "contrast": contrast_score,
                    "hint": hint_score,
                },
            }
        )

    if debug_sink is not None:
        debug_sink["search_region"] = (left, top, right, bottom)
        debug_sink["candidates"] = candidates
        debug_sink["raw_components"] = [
            (left + x_lo, top + y_lo, x_hi - x_lo + 1, y_hi - y_lo + 1, area)
            for area, x_lo, y_lo, x_hi, y_hi in components
        ]

    if not candidates:
        return None

    best = max(candidates, key=lambda item: item["score"])
    if debug_sink is not None:
        debug_sink["selected"] = best
    return best["box"]


def paste_asset_box(
    poster: Image.Image,
    image: Image.Image,
    box: tuple[int, int, int, int],
    padding: int,
    background: tuple[int, int, int, int] | None,
    radius: int,
) -> None:
    x, y, width, height = box
    if background is not None:
        bg = Image.new("RGBA", (width, height), background)
        mask = rounded_rectangle_mask((width, height), radius)
        poster.paste(bg, (x, y), mask)

    fitted = fit_cover_transparent(image, (width - padding * 2, height - padding * 2))
    paste_x = x + (width - fitted.width) // 2
    paste_y = y + (height - fitted.height) // 2
    poster.alpha_composite(fitted, (paste_x, paste_y))


def bool_from_layout(event: dict[str, Any], key: str, default: bool = False) -> bool:
    value = event.get("layout", {}).get(key, default)
    return bool(value)


def draw_gradient_overlay(base: Image.Image) -> Image.Image:
    width, height = base.size
    overlay = Image.new("RGBA", base.size, (0, 0, 0, 0))
    pixels = overlay.load()
    for y in range(height):
        top_alpha = int(max(0, 120 - y * 0.22))
        bottom_start = int(height * 0.52)
        bottom_alpha = int(210 * max(0, (y - bottom_start) / (height - bottom_start)))
        alpha = max(top_alpha, bottom_alpha)
        for x in range(width):
            pixels[x, y] = (0, 0, 0, alpha)
    return Image.alpha_composite(base.convert("RGBA"), overlay)


def text_width(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont) -> int:
    bbox = draw.textbbox((0, 0), text, font=font)
    return bbox[2] - bbox[0]


def wrap_text(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont, max_width: int) -> list[str]:
    if not text:
        return []
    lines: list[str] = []
    current = ""
    for char in text:
        candidate = current + char
        if char == "\n":
            lines.append(current)
            current = ""
        elif text_width(draw, candidate, font) <= max_width or not current:
            current = candidate
        else:
            lines.append(current)
            current = char
    if current:
        lines.append(current)
    return lines


def draw_text_block(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    font: ImageFont.ImageFont,
    fill: tuple[int, int, int, int],
    max_width: int,
    line_gap: int,
    anchor: str = "la",
) -> int:
    x, y = xy
    lines = wrap_text(draw, text, font, max_width)
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        line_height = bbox[3] - bbox[1]
        if anchor == "ra":
            draw.text((x - text_width(draw, line, font), y), line, font=font, fill=fill)
        else:
            draw.text((x, y), line, font=font, fill=fill)
        y += line_height + line_gap
    return y


def label_size(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont) -> tuple[int, int]:
    bbox = draw.textbbox((0, 0), text, font=font)
    return bbox[2] - bbox[0] + 40, bbox[3] - bbox[1] + 22


def draw_label(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, font: ImageFont.ImageFont, accent: str) -> None:
    x, y = xy
    padding_x = 20
    padding_y = 11
    width, height = label_size(draw, text, font)
    draw.rounded_rectangle((x, y, x + width, y + height), radius=8, fill=hex_to_rgba(accent, 230))
    draw.text((x + padding_x, y + padding_y - 2), text, font=font, fill=(16, 24, 32, 255))


def compose(event: dict[str, Any], candidate_path: Path, output_path: Path) -> None:
    root = repo_root()
    check_assets(event, root, strict=True)
    if not candidate_path.exists():
        raise SystemExit(f"missing candidate image: {candidate_path}")

    style = event.get("style", {})
    accent = style.get("accent_color", DEFAULT_ACCENT)
    brand = style.get("brand_color", DEFAULT_BRAND)

    with Image.open(candidate_path) as candidate:
        poster = cover_image(candidate, POSTER_SIZE)
    poster = draw_gradient_overlay(poster)
    draw = ImageDraw.Draw(poster)

    title_font = find_font(82, bold=True)
    subtitle_font = find_font(30)
    speaker_font = find_font(52, bold=True)
    body_font = find_font(31)
    small_font = find_font(25)
    fee_font = find_font(23)
    meta_font = find_font(32, bold=True)

    margin = 72
    white = (255, 255, 255, 245)
    muted = (225, 232, 238, 235)

    logo_path = resolve_asset(root, event["assets"]["logo"])
    qr_path = resolve_asset(root, event["assets"]["qr"])

    with Image.open(logo_path) as logo_raw:
        logo = fit_within(logo_raw, (260, 150))
    poster.alpha_composite(logo, (margin, 54))

    meeting_label = event["club"]["meeting_number"]
    meeting_label_width, _ = label_size(draw, meeting_label, small_font)
    draw_label(draw, (POSTER_SIZE[0] - margin - meeting_label_width, 70), meeting_label, small_font, accent)

    y = 230
    draw.text((margin, y), event["club"]["name"], font=small_font, fill=muted)
    y += 70
    y = draw_text_block(draw, (margin, y), event["theme"], title_font, white, 850, 16)
    if event.get("subtitle"):
        y += 24
        draw_text_block(draw, (margin, y), event["subtitle"], subtitle_font, muted, 780, 10)

    speaker_y = 1235
    draw.line((margin, speaker_y - 34, margin + 128, speaker_y - 34), fill=hex_to_rgba(accent, 255), width=6)
    draw.text((margin, speaker_y), event["speaker"]["name"], font=speaker_font, fill=white)
    speaker_y += 76
    speaker_y = draw_text_block(draw, (margin, speaker_y), event["speaker"]["title"], body_font, muted, 820, 9)
    speaker_y += 10
    draw_text_block(draw, (margin, speaker_y), event["speaker"]["bio"], body_font, muted, 820, 9)

    panel_top = 1538
    panel = Image.new("RGBA", (POSTER_SIZE[0] - margin * 2, 304), hex_to_rgba(brand, 178))
    panel_mask = rounded_rectangle_mask(panel.size, 24)
    poster.paste(panel, (margin, panel_top), panel_mask)

    with Image.open(qr_path) as qr_raw:
        qr = fit_within(qr_raw, (178, 178))
    qr_bg_size = (204, 204)
    qr_bg = Image.new("RGBA", qr_bg_size, (255, 255, 255, 255))
    qr_bg_mask = rounded_rectangle_mask(qr_bg_size, 14)
    qr_x = POSTER_SIZE[0] - margin - qr_bg_size[0] - 26
    qr_y = panel_top + 21
    poster.paste(qr_bg, (qr_x, qr_y), qr_bg_mask)
    poster.alpha_composite(qr, (qr_x + (qr_bg_size[0] - qr.width) // 2, qr_y + (qr_bg_size[1] - qr.height) // 2))

    text_x = margin + 34
    text_y = panel_top + 34
    draw.text((text_x, text_y), event["event"]["time"], font=meta_font, fill=white)
    text_y += 56
    text_y = draw_text_block(draw, (text_x, text_y), event["event"]["location"], body_font, muted, 600, 8)
    if event["event"].get("fee"):
        text_y += 10
        draw_text_block(draw, (text_x, text_y), event["event"]["fee"], fee_font, muted, 630, 7)
    qr_label = event.get("club", {}).get("wechat_label", "扫码关注公众号")
    label_width = text_width(draw, qr_label, small_font)
    draw.text((qr_x + (qr_bg_size[0] - label_width) // 2, qr_y + qr_bg_size[1] + 8), qr_label, font=small_font, fill=muted)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    poster.convert("RGB").save(output_path, "PNG", optimize=True)


def _save_qr_debug_image(
    poster: Image.Image,
    debug_sink: dict[str, Any],
    selected_box: tuple[int, int, int, int] | None,
    qr_source: str,
    output_path: Path,
) -> None:
    debug_image = poster.convert("RGBA").copy()
    overlay = Image.new("RGBA", debug_image.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    label_font = find_font(20)

    region = debug_sink.get("search_region")
    if region:
        l, t, r, b = region
        draw.rectangle((l, t, r - 1, b - 1), outline=(255, 200, 0, 255), width=4)
        draw.text((l + 6, t + 6), "search region", font=label_font, fill=(255, 200, 0, 255))

    for raw in debug_sink.get("raw_components", []):
        x, y, w, h, _area = raw
        draw.rectangle((x, y, x + w - 1, y + h - 1), outline=(120, 120, 120, 220), width=2)

    for index, candidate in enumerate(debug_sink.get("candidates", [])):
        cx, cy, cw, ch = candidate["raw_bbox"]
        draw.rectangle((cx, cy, cx + cw - 1, cy + ch - 1), outline=(0, 200, 255, 255), width=3)
        bx, by, bw, bh = candidate["box"]
        draw.rectangle((bx, by, bx + bw - 1, by + bh - 1), outline=(255, 80, 220, 255), width=3)
        text = (
            f"#{index} score={candidate['score']:.2f} "
            f"fill={candidate['fill']:.2f} "
            f"cons={candidate['consistency']:.0f} "
            f"contr={candidate['contrast']:.0f}"
        )
        draw.text((bx, max(0, by - 22)), text, font=label_font, fill=(255, 80, 220, 255))

    if selected_box is not None:
        sx, sy, sw, sh = selected_box
        draw.rectangle((sx, sy, sx + sw - 1, sy + sh - 1), outline=(0, 255, 80, 255), width=6)
        draw.text((sx, sy + sh + 8), f"SELECTED ({qr_source})", font=label_font, fill=(0, 255, 80, 255))

    composite = Image.alpha_composite(debug_image, overlay)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    composite.convert("RGB").save(output_path, "PNG", optimize=True)


def finalize_ai(
    event: dict[str, Any],
    candidate_path: Path,
    output_path: Path,
    *,
    debug: bool = False,
    debug_path: Path | None = None,
) -> dict[str, Any]:
    root = repo_root()
    check_assets(event, root, strict=True)
    if not candidate_path.exists():
        raise SystemExit(f"missing AI candidate image: {candidate_path}")

    with Image.open(candidate_path) as candidate:
        poster = cover_image(candidate, POSTER_SIZE).convert("RGBA")

    layout = event.get("layout", {})
    logo_mode = layout.get("logo_mode", "ai")
    logo_box = box_from_layout(event, "logo_box", [52, 42, 295, 135])
    fallback_qr_box = box_from_layout(event, "qr_box", [70, 1648, 170, 170])
    qr_box = fallback_qr_box
    qr_source = "configured fallback"
    debug_sink: dict[str, Any] = {}

    auto_detect = bool_from_layout(event, "qr_auto_detect", True)
    if auto_detect:
        search_region = region_from_layout(event, "qr_search_region", [0, 1450, 360, 1900])
        ring_hint_rgb = _hex_to_rgb(layout.get("qr_ring_color_hint")) or _hex_to_rgb(
            event.get("style", {}).get("brand_color")
        )
        detected_qr_box = detect_qr_blank_box(
            poster,
            search_region,
            ring_hint_rgb=ring_hint_rgb,
            debug_sink=debug_sink,
        )
        if detected_qr_box is not None:
            qr_box = detected_qr_box
            qr_source = "auto-detected"
        else:
            print(
                "[WARN] QR auto-detection found no candidate; falling back to "
                f"layout.qr_box={fallback_qr_box}. Visually verify the final "
                "poster before sharing."
            )

    logo_path = resolve_asset(root, event["assets"]["logo"])
    qr_path = resolve_asset(root, event["assets"]["qr"])

    if logo_mode == "official_overlay":
        logo_background = (255, 255, 255, 238) if bool_from_layout(event, "logo_background", False) else None
        with Image.open(logo_path) as logo_raw:
            paste_asset_box(
                poster,
                logo_raw,
                logo_box,
                padding=int(layout.get("logo_padding", 0)),
                background=logo_background,
                radius=int(layout.get("logo_radius", 0)),
            )
    elif logo_mode != "ai":
        raise SystemExit("layout.logo_mode must be 'ai' or 'official_overlay'")

    with Image.open(qr_path) as qr_raw:
        paste_asset_box(
            poster,
            qr_raw,
            qr_box,
            padding=int(layout.get("qr_padding", 0)),
            background=None,
            radius=0,
        )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    poster.convert("RGB").save(output_path, "PNG", optimize=True)
    print(f"QR box: {qr_box} ({qr_source})")

    if debug and auto_detect:
        target = debug_path or output_path.with_name(f"qr-detection-debug-{candidate_path.stem}.png")
        _save_qr_debug_image(poster, debug_sink, qr_box if qr_source == "auto-detected" else None, qr_source, target)
        print(f"Wrote debug image: {target}")

    return {
        "qr_box": qr_box,
        "qr_source": qr_source,
        "debug": debug_sink,
    }


def prepare_command(args: argparse.Namespace) -> None:
    event = load_event(Path(args.event))
    paths = event_paths(event)
    warnings = check_assets(event, paths.root, strict=False) + content_warnings(event)
    write_prompts(event, paths, warnings)
    print(f"Wrote {paths.prompt_file}")
    if warnings:
        print("Warnings:")
        for warning in warnings:
            print(f"- {warning}")


def compose_command(args: argparse.Namespace) -> None:
    event = load_event(Path(args.event))
    paths = event_paths(event)
    candidate = paths.output_dir / f"candidate-{args.candidate}.png"
    output = Path(args.output) if args.output else paths.final_file
    if not output.is_absolute():
        output = paths.root / output
    compose(event, candidate, output)
    print(f"Wrote {output}")


def finalize_command(args: argparse.Namespace) -> None:
    event = load_event(Path(args.event))
    paths = event_paths(event)
    candidate = Path(args.input) if args.input else paths.output_dir / f"{args.prefix}-{args.candidate}.png"
    if not candidate.is_absolute():
        candidate = paths.root / candidate
    output = Path(args.output) if args.output else paths.ai_clean_final_file
    if not output.is_absolute():
        output = paths.root / output
    finalize_ai(event, candidate, output, debug=bool(getattr(args, "debug", False)))
    print(f"Wrote {output}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Prepare prompts and compose Toastmasters posters")
    subparsers = parser.add_subparsers(dest="command", required=True)

    prepare = subparsers.add_parser("prepare", help="create prompt.md for 3 image-generation candidates")
    prepare.add_argument("--event", required=True, help="path to event JSON")
    prepare.set_defaults(func=prepare_command)

    compose_parser = subparsers.add_parser("compose", help="compose final poster from a selected candidate")
    compose_parser.add_argument("--event", required=True, help="path to event JSON")
    compose_parser.add_argument("--candidate", type=int, choices=[1, 2, 3], default=1, help="candidate number to use")
    compose_parser.add_argument("--output", help="optional output path")
    compose_parser.set_defaults(func=compose_command)

    finalize_parser = subparsers.add_parser("finalize", help="overlay real logo and QR onto an AI-designed full poster")
    finalize_parser.add_argument("--event", required=True, help="path to event JSON")
    finalize_parser.add_argument("--candidate", type=int, choices=[1, 2, 3], default=1, help="AI candidate number to use")
    finalize_parser.add_argument("--prefix", default="candidate-ai-clean", help="AI candidate filename prefix")
    finalize_parser.add_argument("--input", help="optional AI candidate image path")
    finalize_parser.add_argument("--output", help="optional output path")
    finalize_parser.add_argument("--debug", action="store_true", help="save QR-detection debug image alongside the final poster")
    finalize_parser.set_defaults(func=finalize_command)
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
