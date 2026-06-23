# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A workflow tool for producing weekly Toastmasters meeting posters (1080x1920 vertical PNG for WeChat). The pipeline: configure event JSON → generate image-generation prompts → call Codex/GPT Image to create AI poster candidates → overlay real QR code (and optionally official logo) onto the AI-generated poster.

## Agent Conversation Rule

When the user provides a meeting theme, date, speaker, speaker bio, and speaker image in chat and asks to generate a poster, the agent MUST directly call the available image generation capability to create the main poster candidate. Do not create the main poster locally with Pillow, HTML/CSS, SVG, canvas, or deterministic layout code. Local scripts are only for preparing prompts, saving AI candidates into `outputs/<slug>/`, and overlaying real QR/logo assets.

## Commands

```bash
# Setup
python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt

# Generate 3 prompt variants for AI image generation
python scripts/poster.py prepare --event events/<slug>.json

# Overlay real logo + QR onto AI-generated poster (primary flow)
python scripts/poster.py finalize --event events/<slug>.json --candidate 1
```

## Architecture

Single script (`scripts/poster.py`) with two subcommands:

- **prepare**: Reads event JSON → generates `outputs/<slug>/prompt.md` containing 3 prompt variants (clean training poster, premium editorial, attention-grabbing). Each variant shares a common base prompt built from `poster_copy` fields.
- **finalize**: Takes an AI-generated full poster (`candidate-ai-clean-N.png`), auto-detects the blank QR region via flood-fill heuristics (`detect_qr_blank_box`), then pastes the real QR image. Optionally overlays official logo if `layout.logo_mode` is `official_overlay`.

## Key Design Decisions

- Event configuration drives everything: theme, copy, visual direction, layout coordinates, and asset paths all live in `events/<slug>.json`. The script itself should not need per-event changes.
- AI handles Chinese typography and brand area by default (`logo_mode: ai`). Only QR is mechanically overlaid to avoid AI-generated fake QR codes.
- `qr_auto_detect: true` uses pixel-based flood-fill to find the blank white square left by the AI in the lower-left region, falling back to `qr_box` coordinates if detection fails.
- Candidate naming: `candidate-ai-clean-{1,2,3}.png` for AI-generated full posters.

## Event JSON Structure

See `examples/event.example.json` for the full schema. Key sections: `slug`, `theme`, `subtitle`, `speaker`, `event`, `club`, `poster_copy` (benefits, visual_direction, visual_keywords, reference_direction), `assets` (paths relative to repo root), `layout` (logo/QR positioning and auto-detect config), `style` (accent/brand colors).
