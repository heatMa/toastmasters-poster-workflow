# 生图提示词

把下面 3 条提示词分别交给 ChatGPT image2 / 生图工具生成完整中文海报。生成结果保存为 `candidate-ai-clean-1.png`、`candidate-ai-clean-2.png`、`candidate-ai-clean-3.png`。

注意：中文排版和顶部品牌区交给生图模型完成；二维码仍然在最后由脚本覆盖，避免二维码被 AI 仿制。

## 素材检查提醒

- speaker_photo: missing file /Users/rongbo/Documents/New project 3/assets/speakers/speaker.jpg
- logo: missing file /Users/rongbo/Documents/New project 3/assets/brand/toastmasters-logo.png
- qr: missing file /Users/rongbo/Documents/New project 3/assets/qr/wechat-qr.png

## candidate-ai-clean-1 清爽培训海报

```text
Use case: ads-marketing
Asset type: complete 1080x1920 vertical Chinese mobile poster for WeChat sharing
Primary request: Design a polished, complete Toastmasters event poster in Chinese. The poster must feel more like a finished premium training/event poster than a background template.
Reference direction: 清爽蓝白的线下培训活动海报，右侧主讲人肖像，左侧大标题，中下部嘉宾介绍和“你将收获”模块，底部深蓝信息栏，留白充足，专业可信。
Input image: Use the provided speaker portrait as the main person. Preserve recognizable facial structure, hairstyle, age, and professional business presence. Keep one person only.
Official brand/QR handling: You may create a polished Toastmasters-style top brand area and icon as part of the complete poster. Do not create any QR code. In the lower-left event bar, reserve one clean blank white square area for a real QR code overlay; do not draw a dashed frame, do not draw a fake QR, and do not write placeholder words such as “放置二维码” inside that blank square.
Top header layout: Put the Toastmasters-style icon on the top-left. Put “示例 Toastmasters 演讲俱乐部 / 第 123 次会议” directly to the right of that icon in the same compact header row or header area. Do not add a separate English brand slogan or generic Chinese tagline; the icon already communicates the Toastmasters brand. Do not repeat the club name and meeting number again above the main title.
Exact Chinese copy to include:
- 顶部品牌行: 示例 Toastmasters 演讲俱乐部 / 第 123 次会议
- 主标题: 把故事讲成影响力
- 副标题: A Toastmasters Evening of Voice and Leadership
- 分享嘉宾: 张三
- 嘉宾身份: 资深演讲教练 / 企业培训师
- 嘉宾介绍: 用真实故事建立信任，让表达成为领导力。
- 你将收获:
- 掌握表达结构：让内容更清晰
- 提升现场感染力：让听众更投入
- 获得即时反馈：看见下一步成长点
- 结识同频伙伴：一起练习和成长
- 时间: 2026年5月10日 周日 19:30-21:30
- 地点: 上海市静安区 示例会议室
- 费用: 来宾35元 / 其他俱乐部会员25元 / 学生15元 / 角色免费
- 行动语: 扫码报名，一起开启表达之旅！
- 页脚: TOASTMASTERS 国际演讲俱乐部
Theme visual direction: 围绕故事表达、影响力和领导力建立视觉隐喻，整体应温暖、清晰、有现场分享感。
Theme visual keywords: 故事线、聚光灯、演讲台、听众互动、影响力涟漪
Typography: Chinese text must be readable, high-contrast, and professionally aligned. Use bold dark-blue title typography, smaller clean body text, consistent spacing, no chaotic text blocks.
Hard constraints: no extra people, no distorted face, no fake QR code, no dashed QR placeholder frame, no QR placeholder text, no watermark, no random unreadable text, no unrelated icons.

Composition: Closest to the provided reference poster. Light blue-white gradient, right-side full-height speaker, left-side large title, mid-lower guest intro, four benefit cards, bottom deep-blue event bar.
Mood: clean, bright, credible, inviting, high-end public training poster.
```

保存为：`outputs/2026-05-10-meeting-123/candidate-ai-clean-1.png`

## candidate-ai-clean-2 高级杂志感完整海报

```text
Use case: ads-marketing
Asset type: complete 1080x1920 vertical Chinese mobile poster for WeChat sharing
Primary request: Design a polished, complete Toastmasters event poster in Chinese. The poster must feel more like a finished premium training/event poster than a background template.
Reference direction: 清爽蓝白的线下培训活动海报，右侧主讲人肖像，左侧大标题，中下部嘉宾介绍和“你将收获”模块，底部深蓝信息栏，留白充足，专业可信。
Input image: Use the provided speaker portrait as the main person. Preserve recognizable facial structure, hairstyle, age, and professional business presence. Keep one person only.
Official brand/QR handling: You may create a polished Toastmasters-style top brand area and icon as part of the complete poster. Do not create any QR code. In the lower-left event bar, reserve one clean blank white square area for a real QR code overlay; do not draw a dashed frame, do not draw a fake QR, and do not write placeholder words such as “放置二维码” inside that blank square.
Top header layout: Put the Toastmasters-style icon on the top-left. Put “示例 Toastmasters 演讲俱乐部 / 第 123 次会议” directly to the right of that icon in the same compact header row or header area. Do not add a separate English brand slogan or generic Chinese tagline; the icon already communicates the Toastmasters brand. Do not repeat the club name and meeting number again above the main title.
Exact Chinese copy to include:
- 顶部品牌行: 示例 Toastmasters 演讲俱乐部 / 第 123 次会议
- 主标题: 把故事讲成影响力
- 副标题: A Toastmasters Evening of Voice and Leadership
- 分享嘉宾: 张三
- 嘉宾身份: 资深演讲教练 / 企业培训师
- 嘉宾介绍: 用真实故事建立信任，让表达成为领导力。
- 你将收获:
- 掌握表达结构：让内容更清晰
- 提升现场感染力：让听众更投入
- 获得即时反馈：看见下一步成长点
- 结识同频伙伴：一起练习和成长
- 时间: 2026年5月10日 周日 19:30-21:30
- 地点: 上海市静安区 示例会议室
- 费用: 来宾35元 / 其他俱乐部会员25元 / 学生15元 / 角色免费
- 行动语: 扫码报名，一起开启表达之旅！
- 页脚: TOASTMASTERS 国际演讲俱乐部
Theme visual direction: 围绕故事表达、影响力和领导力建立视觉隐喻，整体应温暖、清晰、有现场分享感。
Theme visual keywords: 故事线、聚光灯、演讲台、听众互动、影响力涟漪
Typography: Chinese text must be readable, high-contrast, and professionally aligned. Use bold dark-blue title typography, smaller clean body text, consistent spacing, no chaotic text blocks.
Hard constraints: no extra people, no distorted face, no fake QR code, no dashed QR placeholder frame, no QR placeholder text, no watermark, no random unreadable text, no unrelated icons.

Composition: More premium editorial and spacious. Keep a refined light background, strong portrait presence, large title, and elegant theme-related visual metaphors. Information hierarchy must remain very clear.
Mood: executive, premium, modern, polished, still readable on mobile.
```

保存为：`outputs/2026-05-10-meeting-123/candidate-ai-clean-2.png`

## candidate-ai-clean-3 强主题传播吸睛版

```text
Use case: ads-marketing
Asset type: complete 1080x1920 vertical Chinese mobile poster for WeChat sharing
Primary request: Design a polished, complete Toastmasters event poster in Chinese. The poster must feel more like a finished premium training/event poster than a background template.
Reference direction: 清爽蓝白的线下培训活动海报，右侧主讲人肖像，左侧大标题，中下部嘉宾介绍和“你将收获”模块，底部深蓝信息栏，留白充足，专业可信。
Input image: Use the provided speaker portrait as the main person. Preserve recognizable facial structure, hairstyle, age, and professional business presence. Keep one person only.
Official brand/QR handling: You may create a polished Toastmasters-style top brand area and icon as part of the complete poster. Do not create any QR code. In the lower-left event bar, reserve one clean blank white square area for a real QR code overlay; do not draw a dashed frame, do not draw a fake QR, and do not write placeholder words such as “放置二维码” inside that blank square.
Top header layout: Put the Toastmasters-style icon on the top-left. Put “示例 Toastmasters 演讲俱乐部 / 第 123 次会议” directly to the right of that icon in the same compact header row or header area. Do not add a separate English brand slogan or generic Chinese tagline; the icon already communicates the Toastmasters brand. Do not repeat the club name and meeting number again above the main title.
Exact Chinese copy to include:
- 顶部品牌行: 示例 Toastmasters 演讲俱乐部 / 第 123 次会议
- 主标题: 把故事讲成影响力
- 副标题: A Toastmasters Evening of Voice and Leadership
- 分享嘉宾: 张三
- 嘉宾身份: 资深演讲教练 / 企业培训师
- 嘉宾介绍: 用真实故事建立信任，让表达成为领导力。
- 你将收获:
- 掌握表达结构：让内容更清晰
- 提升现场感染力：让听众更投入
- 获得即时反馈：看见下一步成长点
- 结识同频伙伴：一起练习和成长
- 时间: 2026年5月10日 周日 19:30-21:30
- 地点: 上海市静安区 示例会议室
- 费用: 来宾35元 / 其他俱乐部会员25元 / 学生15元 / 角色免费
- 行动语: 扫码报名，一起开启表达之旅！
- 页脚: TOASTMASTERS 国际演讲俱乐部
Theme visual direction: 围绕故事表达、影响力和领导力建立视觉隐喻，整体应温暖、清晰、有现场分享感。
Theme visual keywords: 故事线、聚光灯、演讲台、听众互动、影响力涟漪
Typography: Chinese text must be readable, high-contrast, and professionally aligned. Use bold dark-blue title typography, smaller clean body text, consistent spacing, no chaotic text blocks.
Hard constraints: no extra people, no distorted face, no fake QR code, no dashed QR placeholder frame, no QR placeholder text, no watermark, no random unreadable text, no unrelated icons.

Composition: Stronger theme expression. Add tasteful visual elements from the configured theme keywords around the speaker, while preserving readable blocks for all event copy.
Mood: memorable, energetic, intelligent, premium, optimized for attracting attention in WeChat feeds.
```

保存为：`outputs/2026-05-10-meeting-123/candidate-ai-clean-3.png`
