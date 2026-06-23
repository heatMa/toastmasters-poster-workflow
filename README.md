# Toastmasters 手机海报工作流

这个仓库用于制作每周 Toastmasters 演讲会议的手机海报。默认产物是 `1080x1920` 的竖版 PNG，适合微信聊天、朋友圈和公众号预览。

核心原则：

- ChatGPT image2 / Codex 内置 GPT Image 能力直接生成完整中文海报设计，但海报正文只能使用用户明确提供或确认的信息；不得自行补充“你将收获”、课程收益、嘉宾介绍、行动语或其他未提供文案。
- 当用户在 Codex 对话框里提供本期主题、日期、嘉宾、嘉宾介绍和图片并要求“生成海报”时，Codex 必须直接调用 GPT Image 生成候选图；不得使用本地 Pillow/HTML/CSS/SVG 重新排版整张海报。
- 官方 Toastmasters Logo 和二维码不交给 AI 仿制，最后由本地脚本覆盖真实素材。
- 每期默认先生成 3 个完整海报候选，再选 1 个进行最终落版。
- 有嘉宾照片时，生图提示词必须明确要求尽量保持原始照片：不重画五官、脸型、发型、肤色、服装和姿态，只允许抠图、换背景和适度融入版式。

## 目录

```text
assets/
  speakers/       # 主讲人照片
  brand/          # Toastmasters Logo、俱乐部 Logo 等
  qr/             # 微信公众号二维码
examples/
  event.example.json
outputs/
  <slug>/
    prompt.md
    candidate-ai-clean-1.png
    candidate-ai-clean-2.png
    candidate-ai-clean-3.png
    final-poster-ai-clean.png
scripts/
  poster.py
```

## 安装

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 每期制作流程

1. 复制示例配置：

```bash
cp examples/event.example.json events/<新会议>.json
```

2. 把主讲人照片、Logo、二维码放到 `assets/` 下，并更新 `events/<新会议>.json` 里的路径和活动信息。

换主题时只改活动 JSON，不改 `scripts/poster.py`。主题、收益点、视觉关键词和风格方向都放在 `poster_copy` 里。

3. 生成 3 个候选生图提示词：

```bash
python scripts/poster.py prepare --event events/<新会议>.json
```

这会创建 `outputs/<slug>/prompt.md`。如果是在 Codex 对话里制作海报，Codex 应直接调用 GPT Image 生成完整中文海报候选，并保存为：

```text
outputs/<slug>/candidate-ai-clean-1.png
outputs/<slug>/candidate-ai-clean-2.png
outputs/<slug>/candidate-ai-clean-3.png
```

4. 选择最好的一张候选图，覆盖真实 Logo 和二维码：

```bash
python scripts/poster.py finalize --event events/<新会议>.json --candidate 1
```

最终图会输出到：

```text
outputs/<slug>/final-poster-ai-clean.png
```

## 输入配置

查看 [examples/event.example.json](examples/event.example.json)。常用字段：

- `slug`：本期输出目录名，建议用日期和会议编号。
- `theme`：海报主标题。
- `subtitle`：副标题或短句，可为空。
- `speaker.name`：主讲人姓名。
- `speaker.title`：主讲人身份。
- `speaker.bio`：一句话介绍。
- `event.time`：会议时间。
- `event.location`：会议地点。
- `club.name`：俱乐部名称。
- `club.meeting_number`：第几次会议。
- `assets.logo`：Toastmasters 或俱乐部 Logo 图片路径。
- `assets.qr`：公众号二维码图片路径。
- `assets.speaker_photo`：主讲人参考照片路径，用于生图参考。
- `poster_copy.reference_direction`：固定版式/风格参考，例如“清爽蓝白培训海报、右侧主讲人肖像、底部深蓝信息栏”。
- `poster_copy.visual_direction`：本期整体视觉方向，例如主题应传达什么气质、避免什么误区。
- `poster_copy.visual_keywords`：本期视觉关键词，例如图形隐喻、图标、场景元素。
- `poster_copy.benefits`：仅当用户明确提供“你将收获”或收益点时填写；没有提供时不要编造，也不要在海报中生成该模块。
- `poster_copy.call_to_action`：扫码报名行动语。
- `layout.logo_mode`：默认 `ai`，保留生图生成的顶部品牌区；设置为 `official_overlay` 时才覆盖官方 Logo。
- `layout.logo_box`：最终覆盖官方 Logo 的位置，格式为 `[x, y, width, height]`。
- `layout.qr_box`：最终覆盖二维码的位置，格式为 `[x, y, width, height]`。
- `layout.qr_padding`：二维码贴图内边距，默认建议 `0`，让真实二维码按 box 中心直接贴上。

## 质量检查

最终交付前检查：

- AI 生成的中文文字无错字、无缺字。
- 海报中没有出现用户未提供或未确认的信息，尤其是“你将收获”、课程收益、嘉宾介绍、行动语等容易被模型补全的内容。
- 嘉宾照片尽量接近原始照片，不应明显改变五官、脸型、发型、服装或气质。
- 二维码清晰且可扫码。
- 二维码来自原始素材，AI 候选里只应留干净空白区，不应有虚线框或占位字。
- Logo 默认使用 AI 生成的整体品牌区；如需官方严谨版本，再用 `logo_mode: official_overlay`。
- 标题、时间、地点在手机屏幕上一眼可读。
- 视觉和主题强相关，不只是泛科技背景。
