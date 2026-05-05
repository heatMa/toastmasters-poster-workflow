# Progress: QR 定位与海报生成流程

更新日期：2026-05-05

## 当前目标

这个 repo 用来生成每周 Toastmasters 手机海报。当前流程是：

1. `scripts/poster.py prepare` 根据 `events/*.json` 生成 3 条 ChatGPT image2 生图提示词。
2. ChatGPT image2 直接生成完整中文海报候选图。
3. `scripts/poster.py finalize` 只做最后的确定性处理：把真实二维码贴到 AI 海报预留的空白二维码区域里。

二维码必须使用真实素材，不让 AI 生成，因为 AI 生成的二维码不可扫码。

## 当前文件

- 主脚本：`/Users/rongbo/Documents/New project 3/scripts/poster.py`
- 本期配置：`/Users/rongbo/Documents/New project 3/events/2026-05-10-meeting-872.json`
- 本期输出目录：`/Users/rongbo/Documents/New project 3/outputs/2026-05-10-meeting-872/`
- 真实二维码素材：`/Users/rongbo/Documents/New project 3/assets/qr/vibrant-wechat-qr.jpg`
- 当前最终图：`/Users/rongbo/Documents/New project 3/outputs/2026-05-10-meeting-872/final-poster-ai-clean.png`

## 已尝试的二维码定位方案

### 方案 1：手写 `layout.qr_box`

最早做法是在 event JSON 里手写二维码坐标：

```json
"qr_box": [74, 1618, 150, 150]
```

脚本用 Pillow 直接把真实二维码 resize 后贴到这个矩形里。这个过程不经过大模型。

问题：

- AI 每次生成的二维码空白块位置、大小都会有细微变化。
- 手写坐标只能适配一张候选图。
- 如果 AI 画了虚线框或占位文字，手写坐标和视觉框不一致时，二维码看起来就不居中。

### 方案 2：提示词要求只留空白块

后面调整了生图提示词：

- 不让 AI 画虚线框。
- 不让 AI 写“放置二维码”等占位字。
- 只在左下角留一个干净白色方块，供真实二维码覆盖。

这个方向是对的，因为减少了“视觉框”和脚本坐标不一致的问题。

但如果仍然使用手写 `qr_box`，只要 AI 生成的白块稍有偏移，二维码仍会歪。

### 方案 3：Pillow 自动识别白色空白块

当前脚本已实现一个基础自动检测函数：

```python
detect_qr_blank_box(poster, search_region)
```

位置：

```text
/Users/rongbo/Documents/New project 3/scripts/poster.py
```

核心逻辑：

1. 先把 AI 候选图标准化成 `1080x1920`。
2. 只搜索左下角区域，当前配置是：

```json
"qr_search_region": [0, 1450, 360, 1845]
```

3. 用 Pillow 遍历像素，筛选近白色、低饱和像素：

```python
red >= 210 and green >= 210 and blue >= 210
max(red, green, blue) - min(red, green, blue) <= 45
```

4. 对白色像素做连通区域分析。
5. 过滤候选白块：

- 面积足够大。
- 宽高不能太小。
- 宽高比接近正方形：`0.75 <= aspect <= 1.35`。
- 填充率足够高：`fill >= 0.65`。

6. 选得分最高的白块作为二维码框。
7. 检测失败时 fallback 到 `layout.qr_box`。

当前 `finalize_ai()` 会打印实际使用的二维码框，例如：

```text
QR box: (54, 1592, 189, 184) (auto-detected)
QR box: (74, 1618, 150, 150) (configured fallback)
```

### 当前检测结果

对现有 3 张 `candidate-ai-clean-*` 的测试结果大致是：

- `candidate-ai-clean-1.png`：能自动识别，约为 `(54, 1592, 189, 184)`。
- `candidate-ai-clean-2.png`：能自动识别，但框高宽略不稳定，约为 `(58, 1591/1592, 203, 183/184)`。
- `candidate-ai-clean-3.png`：自动识别失败，回退到手写坐标 `(74, 1618, 150, 150)`。

## 当前问题

现在的方法还不够鲁棒。用户肉眼观察后指出：第 2 张和第 3 张二维码空白块的比例其实一致，只是大小不同。

当前算法只粗略考虑了“接近正方形”，没有充分利用这几个稳定特征：

- 白块一定在底部蓝色信息栏的左侧。
- 白块外圈应该被深蓝背景包围，而不是白色收益卡片或顶部 logo。
- 白块本身应是一个整体的浅色圆角方块。
- 第 2 张和第 3 张的白块比例一致，只是尺寸不同，所以检测后应该做正方形归一化，而不是直接使用原始连通区域宽高。

因此，第 3 张失败并不代表思路错，而是当前评分条件太弱、后处理不够。

## 不建议优先使用 GPT 识别坐标

可以把三张图发给 GPT vision，让它返回二维码空白块坐标。GPT 对这种视觉定位通常能看懂。

但不建议作为默认主流程，原因是：

- 坐标不一定像本地算法一样可复现。
- 每次 finalize 都要调用大模型，慢且有成本。
- 需要额外处理模型坐标误差。
- 这个问题本质是规则明确的图像处理任务，用 Pillow 就能做得稳定。

更合理的方式：

- 主流程用本地图像处理自动识别。
- GPT vision 只作为调试手段，或在本地检测失败时辅助分析，而不是每张海报都调用。

## 下一步推荐计划

### 1. 增强候选白块评分

当前只看白色连通块自身。下一版应增加“周围背景”判断：

- 对候选白块向外扩展一个 ring，例如 12 到 20 px。
- 统计 ring 里的深蓝像素比例。
- 底部二维码空白块应该有较高的蓝色背景包围比例。
- 顶部 logo、白色收益卡片、人物边缘等白色区域会被过滤掉。

推荐蓝色判断可以先用简单条件：

```python
blue > red + 20
blue > green + 5
blue >= 90
red <= 120
```

也可以结合深蓝条件：

```python
red < 80 and green < 140 and blue > 120
```

### 2. 检测后做正方形归一化

不要直接使用连通区域的原始 `(w, h)`。

推荐做法：

1. 找到白块原始 bbox。
2. 计算中心点：

```python
cx = left + width / 2
cy = top + height / 2
```

3. 取统一边长：

```python
side = max(width, height)
```

4. 生成归一化方框：

```python
x = round(cx - side / 2)
y = round(cy - side / 2)
box = (x, y, side, side)
```

这样第 2/3 张“比例一致但大小不同”的情况会更稳定，二维码也更容易真正居中。

### 3. 放宽和动态化搜索区域

当前搜索区域是固定：

```json
[0, 1450, 360, 1845]
```

建议默认改成相对尺寸推导：

```text
left = 0
top = 0.72 * poster_height
right = 0.42 * poster_width
bottom = 0.97 * poster_height
```

对 `1080x1920` 即约：

```text
[0, 1382, 454, 1862]
```

这样能覆盖不同候选图里略微移动的左下角二维码区。

### 4. 增加 mask 形态学修复

Pillow 不用 OpenCV 也可以做简单形态学。

推荐对二值 mask 做一次轻量修复：

```python
from PIL import ImageFilter

mask_image = mask_image.filter(ImageFilter.MaxFilter(5))
mask_image = mask_image.filter(ImageFilter.MinFilter(5))
```

这样可以把白块里的轻微阴影、圆角渐变、抗锯齿导致的小断裂连起来。

### 5. 输出 debug 图

建议给 finalize 增加一个可选 debug 输出，例如：

```text
outputs/2026-05-10-meeting-872/qr-detection-debug-candidate-1.png
```

debug 图上画出：

- 搜索区域。
- 所有候选白块。
- 最终选中的二维码框。

这样之后调参数时不用靠猜。

### 6. 保留 fallback

即使自动检测增强后，也应该继续保留：

```json
"qr_box": [74, 1618, 150, 150]
```

自动检测失败时明确打印：

```text
QR box: (74, 1618, 150, 150) (configured fallback)
```

这样至少不会中断海报生成。

## 推荐的实现顺序

1. 在 `detect_qr_blank_box()` 中加入 blue-ring 背景评分。
2. 返回前做正方形归一化。
3. 把默认搜索区域改得更宽一点，或支持相对区域。
4. 增加 debug 图输出。
5. 用 3 张 `candidate-ai-clean-*` 分别跑 finalize，确认都能 auto-detect，不再 fallback。
6. 最后再生成 `final-poster-ai-clean.png`。

## 当前结论

二维码贴图本身没有问题：它是 Pillow 直接贴图，不经过大模型。

真正需要优化的是“如何稳定找到 AI 预留的白色二维码空白块”。当前基础连通区域算法能跑通第 1 张，但第 2/3 张还不够稳。下一步应把“白块自身特征”升级为“白块 + 深蓝底部栏上下文 + 正方形归一化”的组合检测。
