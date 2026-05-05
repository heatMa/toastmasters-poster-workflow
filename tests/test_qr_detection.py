"""Regression tests for QR-blank-square auto-detection.

Each candidate image bakes in a specific failure mode the detector must handle:
  candidate-1: clean QR blank surrounded by solid deep-blue info bar (ring path)
  candidate-2: QR blank surrounded by gradient-blue info bar (ring path,
               permissive consistency)
  candidate-3: no deep ring -- QR area sits on a light background
               (pure-white-block fallback path)

Expected centers / sides were verified visually after the new detector
landed; tolerances allow for minor algorithmic drift but flag real
regressions.
"""

from pathlib import Path

import pytest
from PIL import Image

from poster import POSTER_SIZE, _hex_to_rgb, cover_image, detect_qr_blank_box


ROOT = Path(__file__).resolve().parents[1]
SLUG = "2026-05-10-meeting-872"
CANDIDATE_DIR = ROOT / "outputs" / SLUG
SEARCH_REGION = (0, 1450, 360, 1900)
RING_HINT = _hex_to_rgb("#004165")

EXPECTED = {
    "candidate-ai-clean-1.png": {
        "center": (148, 1683),
        "side": 183,
        "ring_passes": True,
    },
    "candidate-ai-clean-2.png": {
        "center": (159, 1683),
        "side": 183,
        "ring_passes": True,
    },
    "candidate-ai-clean-3.png": {
        "center": (156, 1805),
        "side": 190,
        "pure_white_block": True,
    },
}


def _load_poster(name: str) -> Image.Image:
    path = CANDIDATE_DIR / name
    with Image.open(path) as image:
        return cover_image(image, POSTER_SIZE).convert("RGBA")


@pytest.mark.parametrize("name", list(EXPECTED.keys()))
def test_detects_qr_blank(name: str) -> None:
    expected = EXPECTED[name]
    poster = _load_poster(name)
    sink: dict = {}
    box = detect_qr_blank_box(
        poster,
        SEARCH_REGION,
        ring_hint_rgb=RING_HINT,
        debug_sink=sink,
    )
    assert box is not None, (
        f"{name}: detector returned None; debug={sink}"
    )

    x, y, w, h = box
    cx = x + w / 2.0
    cy = y + h / 2.0
    ex_cx, ex_cy = expected["center"]
    assert abs(cx - ex_cx) <= 8, (
        f"{name}: center x off by {cx - ex_cx:.1f}px (got {cx}, want {ex_cx})"
    )
    assert abs(cy - ex_cy) <= 8, (
        f"{name}: center y off by {cy - ex_cy:.1f}px (got {cy}, want {ex_cy})"
    )
    assert abs(w - expected["side"]) <= 12, (
        f"{name}: width off by {w - expected['side']}px (got {w}, want {expected['side']})"
    )
    assert w == h, f"{name}: detector must return a square (got {w}x{h})"

    selected = sink["selected"]
    if expected.get("ring_passes"):
        assert selected["ring_passes"], (
            f"{name}: expected ring-based selection, got {selected}"
        )
    if expected.get("pure_white_block"):
        assert selected["pure_white_block"], (
            f"{name}: expected pure-white-block selection, got {selected}"
        )
