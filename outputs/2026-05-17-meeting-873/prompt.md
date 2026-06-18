# 生图提示词

把下面 3 条提示词分别交给 ChatGPT image2 / 生图工具生成完整中文海报。生成结果保存为 `candidate-ai-clean-1.png`、`candidate-ai-clean-2.png`、`candidate-ai-clean-3.png`。

注意：中文排版和顶部品牌区交给生图模型完成；二维码仍然在最后由脚本覆盖，避免二维码被 AI 仿制。

## candidate-ai-clean-1 清爽培训海报

```text
Use case: ads-marketing
Asset type: complete 1080x1920 vertical Chinese mobile poster for WeChat sharing
Primary request: Design a polished, complete Toastmasters event poster in Chinese. The poster must feel more like a finished premium training/event poster than a background template.
Reference direction: 专业职场分享海报，使用嘉宾照片抠出人物作为主视觉，去掉原照片里的会议室背景。左侧大标题，中部嘉宾身份，底部深蓝信息栏，右下方预留干净白色二维码方块，整体简洁、可信、有商务质感。
Input image: Use the provided speaker portrait as the main person. Preserve recognizable facial structure, hairstyle, age, and professional business presence. Keep one person only.
Official brand/QR handling: You may create a polished Toastmasters-style top brand area and icon as part of the complete poster. Do not create any QR code. In the lower-left event bar, reserve one clean blank white square area for a real QR code overlay; do not draw a dashed frame, do not draw a fake QR, and do not write placeholder words such as “放置二维码” inside that blank square.
Top header layout: Put the Toastmasters-style icon on the top-left. Put “Lighthouse俱乐部 / 第873次会议” directly to the right of that icon in the same compact header row or header area. Do not add a separate English brand slogan or generic Chinese tagline; the icon already communicates the Toastmasters brand. Do not repeat the club name and meeting number again above the main title.
Exact Chinese copy to include:
- 顶部品牌行: Lighthouse俱乐部 / 第873次会议
- 主标题: 职场中的关键时刻
- 副标题: 看见转折点，把握下一步
- 分享嘉宾: Eric赵
- 嘉宾身份: 会计师事务所合伙人
- 嘉宾介绍: Lighthouse俱乐部，会计师事务所合伙人。
- 你将收获:
- 识别关键时刻：看清职场转折点
- 提升判断力：在压力中做选择
- 关键沟通：把观点表达清楚
- 稳住下一步：把经验变成行动
- 时间: 2026年5月17日 周日 14:00-17:00
- 地点: 乌鲁木齐南路66号梧桐院邻里汇3号楼2楼（地铁1号线衡山路站4号口步行400米）
- 费用: 来宾35元 / 其他俱乐部会员25元 / 学生15元 / 角色免费
- 行动语: 扫码报名，把握职场关键时刻！
- 页脚: TOASTMASTERS 国际演讲俱乐部
Theme visual direction: 围绕“职场中的关键时刻”建立视觉隐喻：会议桌、决策节点、时间刻度、路径选择、聚光灯与稳健表达。避免泛科技炫光，保持成熟商务、清晰有力。
Theme visual keywords: 职场关键时刻、决策节点、会议表达、职业转折、路径选择、商务聚光灯
Typography: Chinese text must be readable, high-contrast, and professionally aligned. Use bold dark-blue title typography, smaller clean body text, consistent spacing, no chaotic text blocks.
Hard constraints: no extra people, no distorted face, no fake QR code, no dashed QR placeholder frame, no QR placeholder text, no watermark, no random unreadable text, no unrelated icons.

Composition: Closest to the provided reference poster. Light blue-white gradient, right-side full-height speaker, left-side large title, mid-lower guest intro, four benefit cards, bottom deep-blue event bar.
Mood: clean, bright, credible, inviting, high-end public training poster.
```

保存为：`outputs/2026-05-17-meeting-873/candidate-ai-clean-1.png`

## candidate-ai-clean-2 高级杂志感完整海报

```text
Use case: ads-marketing
Asset type: complete 1080x1920 vertical Chinese mobile poster for WeChat sharing
Primary request: Design a polished, complete Toastmasters event poster in Chinese. The poster must feel more like a finished premium training/event poster than a background template.
Reference direction: 专业职场分享海报，使用嘉宾照片抠出人物作为主视觉，去掉原照片里的会议室背景。左侧大标题，中部嘉宾身份，底部深蓝信息栏，右下方预留干净白色二维码方块，整体简洁、可信、有商务质感。
Input image: Use the provided speaker portrait as the main person. Preserve recognizable facial structure, hairstyle, age, and professional business presence. Keep one person only.
Official brand/QR handling: You may create a polished Toastmasters-style top brand area and icon as part of the complete poster. Do not create any QR code. In the lower-left event bar, reserve one clean blank white square area for a real QR code overlay; do not draw a dashed frame, do not draw a fake QR, and do not write placeholder words such as “放置二维码” inside that blank square.
Top header layout: Put the Toastmasters-style icon on the top-left. Put “Lighthouse俱乐部 / 第873次会议” directly to the right of that icon in the same compact header row or header area. Do not add a separate English brand slogan or generic Chinese tagline; the icon already communicates the Toastmasters brand. Do not repeat the club name and meeting number again above the main title.
Exact Chinese copy to include:
- 顶部品牌行: Lighthouse俱乐部 / 第873次会议
- 主标题: 职场中的关键时刻
- 副标题: 看见转折点，把握下一步
- 分享嘉宾: Eric赵
- 嘉宾身份: 会计师事务所合伙人
- 嘉宾介绍: Lighthouse俱乐部，会计师事务所合伙人。
- 你将收获:
- 识别关键时刻：看清职场转折点
- 提升判断力：在压力中做选择
- 关键沟通：把观点表达清楚
- 稳住下一步：把经验变成行动
- 时间: 2026年5月17日 周日 14:00-17:00
- 地点: 乌鲁木齐南路66号梧桐院邻里汇3号楼2楼（地铁1号线衡山路站4号口步行400米）
- 费用: 来宾35元 / 其他俱乐部会员25元 / 学生15元 / 角色免费
- 行动语: 扫码报名，把握职场关键时刻！
- 页脚: TOASTMASTERS 国际演讲俱乐部
Theme visual direction: 围绕“职场中的关键时刻”建立视觉隐喻：会议桌、决策节点、时间刻度、路径选择、聚光灯与稳健表达。避免泛科技炫光，保持成熟商务、清晰有力。
Theme visual keywords: 职场关键时刻、决策节点、会议表达、职业转折、路径选择、商务聚光灯
Typography: Chinese text must be readable, high-contrast, and professionally aligned. Use bold dark-blue title typography, smaller clean body text, consistent spacing, no chaotic text blocks.
Hard constraints: no extra people, no distorted face, no fake QR code, no dashed QR placeholder frame, no QR placeholder text, no watermark, no random unreadable text, no unrelated icons.

Composition: More premium editorial and spacious. Keep a refined light background, strong portrait presence, large title, and elegant theme-related visual metaphors. Information hierarchy must remain very clear.
Mood: executive, premium, modern, polished, still readable on mobile.
```

保存为：`outputs/2026-05-17-meeting-873/candidate-ai-clean-2.png`

## candidate-ai-clean-3 强主题传播吸睛版

```text
Use case: ads-marketing
Asset type: complete 1080x1920 vertical Chinese mobile poster for WeChat sharing
Primary request: Design a polished, complete Toastmasters event poster in Chinese. The poster must feel more like a finished premium training/event poster than a background template.
Reference direction: 专业职场分享海报，使用嘉宾照片抠出人物作为主视觉，去掉原照片里的会议室背景。左侧大标题，中部嘉宾身份，底部深蓝信息栏，右下方预留干净白色二维码方块，整体简洁、可信、有商务质感。
Input image: Use the provided speaker portrait as the main person. Preserve recognizable facial structure, hairstyle, age, and professional business presence. Keep one person only.
Official brand/QR handling: You may create a polished Toastmasters-style top brand area and icon as part of the complete poster. Do not create any QR code. In the lower-left event bar, reserve one clean blank white square area for a real QR code overlay; do not draw a dashed frame, do not draw a fake QR, and do not write placeholder words such as “放置二维码” inside that blank square.
Top header layout: Put the Toastmasters-style icon on the top-left. Put “Lighthouse俱乐部 / 第873次会议” directly to the right of that icon in the same compact header row or header area. Do not add a separate English brand slogan or generic Chinese tagline; the icon already communicates the Toastmasters brand. Do not repeat the club name and meeting number again above the main title.
Exact Chinese copy to include:
- 顶部品牌行: Lighthouse俱乐部 / 第873次会议
- 主标题: 职场中的关键时刻
- 副标题: 看见转折点，把握下一步
- 分享嘉宾: Eric赵
- 嘉宾身份: 会计师事务所合伙人
- 嘉宾介绍: Lighthouse俱乐部，会计师事务所合伙人。
- 你将收获:
- 识别关键时刻：看清职场转折点
- 提升判断力：在压力中做选择
- 关键沟通：把观点表达清楚
- 稳住下一步：把经验变成行动
- 时间: 2026年5月17日 周日 14:00-17:00
- 地点: 乌鲁木齐南路66号梧桐院邻里汇3号楼2楼（地铁1号线衡山路站4号口步行400米）
- 费用: 来宾35元 / 其他俱乐部会员25元 / 学生15元 / 角色免费
- 行动语: 扫码报名，把握职场关键时刻！
- 页脚: TOASTMASTERS 国际演讲俱乐部
Theme visual direction: 围绕“职场中的关键时刻”建立视觉隐喻：会议桌、决策节点、时间刻度、路径选择、聚光灯与稳健表达。避免泛科技炫光，保持成熟商务、清晰有力。
Theme visual keywords: 职场关键时刻、决策节点、会议表达、职业转折、路径选择、商务聚光灯
Typography: Chinese text must be readable, high-contrast, and professionally aligned. Use bold dark-blue title typography, smaller clean body text, consistent spacing, no chaotic text blocks.
Hard constraints: no extra people, no distorted face, no fake QR code, no dashed QR placeholder frame, no QR placeholder text, no watermark, no random unreadable text, no unrelated icons.

Composition: Stronger theme expression. Add tasteful visual elements from the configured theme keywords around the speaker, while preserving readable blocks for all event copy.
Mood: memorable, energetic, intelligent, premium, optimized for attracting attention in WeChat feeds.
```

保存为：`outputs/2026-05-17-meeting-873/candidate-ai-clean-3.png`
