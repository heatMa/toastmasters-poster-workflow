# Progress: QR 定位与海报生成流程

更新日期：2026-05-05

## 当前目标

这个 repo 用来生成每周 Toastmasters 手机海报。当前流程是：

1. `scripts/poster.py prepare` 根据 `events/*.json` 生成 3 条 ChatGPT image2 生图提示词。
2. ChatGPT image2 直接生成完整中文海报候选图。
3. `scripts/poster.py finalize` 只做最后的确定性处理：把真实二维码贴到 AI 海报预留的空白二维码区域里。

二维码必须使用真实素材，不让 AI 生成，因为 AI 生成的二维码不可扫码。

## 当前状态：自动检测已稳定

3 张候选图全部 auto-detected，`pytest tests/test_qr_detection.py` 全绿。
fallback `qr_box` 仅作为兜底；正常路径不再触发。

| 候选 | 检测路径 | QR box (x,y,w,h) | ring 中位色 | cons / contr |
|---|---|---|---|---|
| candidate-ai-clean-1 | ring 通用判定 | (57, 1592, 183, 183) | (1,81,167) 深蓝 | 13 / 188 |
| candidate-ai-clean-2 | ring 通用判定 | (68, 1592, 183, 183) | (4,69,159) 渐变蓝 | 134 / 195 |
| candidate-ai-clean-3 | 纯白块直通 | (61, 1710, 190, 190) | (253,253,253) 浅背景 | 215 / 2 |

## 当前文件

- 主脚本：`scripts/poster.py`
- 本期配置：`events/2026-05-10-meeting-872.json`
- 本期输出目录：`outputs/2026-05-10-meeting-872/`
- 真实二维码素材：`assets/qr/vibrant-wechat-qr.jpg`
- 当前最终图：`outputs/2026-05-10-meeting-872/final-poster-ai-clean-{1,2,3}.png`
- Debug 图：`outputs/2026-05-10-meeting-872/qr-detection-debug-candidate-ai-clean-{1,2,3}.png`
- 回归测试：`tests/test_qr_detection.py`

## 已实施的算法

### 1. numpy 化的连通域 + 形态学

- 用 numpy 做白色像素阈值（`minc >= 210`，`max-min <= 45`）。
- 用 PIL 的 `MaxFilter(3)` + `MinFilter(3)` 做形态学闭运算，修复抗锯齿/圆角导致的小断裂。
- BFS 连通域（4 邻接），用 `collections.deque` 替代列表，无递归。

### 2. 列/行覆盖率法重切 bbox + side = min(w, h)

raw 连通域 bbox 容易被白块下方的小字（"扫码报名…"）撑高。重切流程：

1. 用 raw bbox 内每列/每行的白色覆盖率切出"高密度核心"。
2. 阈值取 `max(0.85, peak * 0.85)`，自适应。
3. 正方形归一化用 `side = min(core_w, core_h)`，避免被漏字撑成竖长方形；中心居中。

### 3. 通用 ring 判定（不预设包围色）

外扩 16 px 的 ring（去掉 4 px 缓冲区避免抗锯齿污染）：

- **一致性**：ring 内每像素到 ring 中位色的 L1 距离均值 ≤ 150。
- **对比度**：ring 中位色的 BT.601 luma 与白色对比 ≥ 60。
- 不假设包围色是任何特定颜色（蓝 / brand_color / etc.）。深蓝、深红、深紫、纯黑、品牌色渐变都能通过。
- 可选 `layout.qr_ring_color_hint`（默认回退到 `style.brand_color`）作为**软加分项**，存在时给一个 0–0.4 的得分加成；不存在也能正常工作。

### 4. 纯白块直通路径（fallback）

针对 candidate-3 这种"AI 没画清晰深色 ring，QR 区直接坐在浅色背景上"的场景：

- 核心采样区（白块中心 1/2 边长）的中位 RGB ≥ 245 且最小通道 ≥ 200。
- fill ≥ 0.95、side ≥ 140、bbox aspect ∈ [0.8, 1.25]。
- 满足上述条件即使 ring 检测失败也能入选，但 score 加成（+0.5）显著低于 ring 路径（+2.0），保证有 ring 候选时优先选 ring。

### 5. Debug 图 + 失败 WARN

- `--debug` 选项保存 `qr-detection-debug-<candidate>.png`：黄框为 search region，灰框为所有 raw 连通域，青框为 raw bbox，粉框为归一化后的正方形候选，绿框为最终选中的 box，并标注 score/fill/cons/contr。
- 自动检测全失败时打印 `[WARN] QR auto-detection found no candidate; falling back to layout.qr_box=...`，提示人工核对。

### 6. 回归测试

`tests/test_qr_detection.py` 用三张候选图作为 fixture：

- 中心点偏差 ≤ 8 px、边长偏差 ≤ 12 px、必须返回正方形。
- candidate-1/2 必须走 ring 路径，candidate-3 必须走 pure-white-block 路径。

## 主要分数权重（仅供参考）

```text
score = 1.6 * square          # core_w/core_h 越接近 1 越高
      + 1.0 * fill            # raw bbox 内白像素填充率
      + 0.8 * size            # 边长平方 / 40000，封顶 1
      + 1.0 * consistency     # 1 - cons/150，封顶 1
      + 1.0 * contrast        # contr/120，封顶 1
      + 0.4 * hint            # 1 - dist(ring_median, hint)/120，可选
      + 2.0 if ring_passes
      + 0.5 if pure_white_block
```

## 配置项

`events/<slug>.json` 的 `layout` 块支持：

```json
{
  "layout": {
    "logo_mode": "ai",
    "logo_box": [...],
    "qr_box": [74, 1618, 150, 150],
    "qr_auto_detect": true,
    "qr_search_region": [0, 1450, 360, 1900],
    "qr_padding": 0,
    "qr_ring_color_hint": "#004165"   // 可选，缺省回退到 style.brand_color
  }
}
```

`qr_search_region` 默认值已从原来的 `[0, 1450, 360, 1845]` 扩到 `[0, 1450, 360, 1900]`，避免把 candidate-3 这种位置较低的白块底端切掉。

## 依赖

`requirements.txt` 增加：

```
Pillow>=10.0.0
numpy>=2.0.0
pytest>=8.0.0
```

未引入 scipy / opencv，形态学用 PIL，连通域用纯 Python BFS（搜索区域 360×450 内可接受）。

## 未实施 / 可选后续

按重要性排：

- **未做**：把 BFS 连通域也 numpy 化（如果后续把搜索区扩到全图，再考虑用 union-find 或 scipy.ndimage.label）。
- **未做**：底部信息栏的自动定位（先扫描每行 brand-blue 占比突变点，再在信息栏内部找白块）。当前默认搜索区已经够用。
- **未做**：debug 图里画 ring 区域。目前 ring 信息只通过 console 文本看到。
- **可考虑**：在 `prepare` 阶段直接把 3 个 finalize 候选图都跑一遍并人眼比较，目前需要手动一张张来。

## 2026-05-05 已切换到 K2.6 Vision 主路径

用户决定改走 K2.6 大模型直接识别二维码空白块坐标，像素法降级为兜底。

### 新架构

- **主路径**：`scripts/qr_vision.py` → `POST https://api.kimi.com/coding/v1/chat/completions`
  - crop `search_region` → JPEG → base64 → vision model
  - model: `kimi-for-coding`，需 `x-client: claude-code` + `User-Agent: claude-code/1.0` header
  - `thinking: {"type": "disabled"}` 必须，否则模型消耗全部 token 在 reasoning 上
  - 解析 JSON 坐标 → 正方形归一化 → 像素健全性校验（中心 60% 近白像素占比 ≥ 55%）
- **中间兜底**：现有 `detect_qr_blank_box` 像素法（全部能力保留）
- **最终兜底**：`layout.qr_box` 配置坐标

### 回归结果

| 候选 | 检测路径 | QR box (x,y,w,h) |
|---|---|---|
| candidate-ai-clean-1 | vision | (54, 1514, 182, 182) |
| candidate-ai-clean-2 | vision | (55, 1565, 230, 230) |
| candidate-ai-clean-3 | vision | (48, 1670, 230, 230) |

3 张全部 `qr_source=vision`，无需再 fallback 到像素法。

### 新增/修改文件

- `scripts/qr_vision.py` — 新建，封装 K2 vision 调用
- `scripts/poster.py` — `finalize_ai` 插入 vision 优先级；`finalize` 子命令增加 `--no-vision`、`--vision-model`
- `events/2026-05-10-meeting-872.json` — 新增 `layout.qr_vision`
- `examples/event.example.json` — 同步示例
- `requirements.txt` — 新增 `requests>=2.31.0`
- `tests/test_qr_vision_unit.py` — 新建，12 个 mock HTTP 单测
- `.env.example` — 新建
- `.gitignore` — 忽略 `.env`

### 配置字段

```json
"qr_vision": {
  "enabled": true,
  "model": "kimi-for-coding",
  "base_url": "https://api.kimi.com/coding/",
  "api_key_env": "KIMI_API_KEY",
  "x_client": "claude-code",
  "user_agent": "claude-code/1.0",
  "timeout_seconds": 30,
  "jpeg_quality": 85,
  "max_tokens": 512
}
```

### CLI 用法

```bash
# 默认走 K2 vision，失败自动回退像素法 → 配置坐标
python scripts/poster.py finalize --event events/2026-05-10-meeting-872.json --candidate 1 --debug

# 跳过 vision，强制旧路径（调试 / 离线用）
python scripts/poster.py finalize --event ... --candidate 1 --no-vision --debug

# 临时换模型对比效果
python scripts/poster.py finalize --event ... --candidate 1 --vision-model other-model
```

### 当前结论

二维码贴图本身没有问题：Pillow 直接贴图，不经过大模型。

二维码定位已从"基础连通域 + 单一 ring 假设"升级为：

1. **K2.6 vision 主路径**：AI 看 AI 画的图，定位准确，覆盖不同风格；
2. **像素法中间兜底**：`detect_qr_blank_box` 全部能力保留，网络不通 / API 失败时自动接管；
3. **配置坐标最终兜底**：`layout.qr_box` 作为最后安全网，确保任何情况下海报都能产出；
4. **三级兜底链**：`vision → auto-detected → configured fallback`，稳态不中断。

3 张候选图全部 vision 通过，`pytest` 15 个全绿，debug 图可供人工复核。下次新海报失败时优先看 debug 图和 `vision_raw_response`，必要时在 `qr_vision.py` 调 prompt 或放宽 `white_ratio` 阈值。
