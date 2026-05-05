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

## 当前结论

二维码贴图本身没有问题：Pillow 直接贴图，不经过大模型。

二维码定位已从"基础连通域 + 单一 ring 假设"升级为：

1. 列/行覆盖率重切 + `side = min(w, h)` 正方形归一化（防漏字撑高）；
2. 通用 ring 一致性 + 高对比度（不预设颜色）；
3. 纯白块直通路径（兼容无深色 ring 的海报）；
4. 可选的 `qr_ring_color_hint` 仅作软加分项，不再是硬依赖。

3 张候选图全部 auto-detected，pytest 通过，debug 图可供人工复核。下次新海报失败时优先看 debug 图调阈值，必要时可补充 fixture 锁定行为。
