# 生图提示词

把下面 3 条提示词分别交给 ChatGPT image2 / 生图工具生成完整中文海报。生成结果保存为 `candidate-ai-clean-1.png`、`candidate-ai-clean-2.png`、`candidate-ai-clean-3.png`。

注意：中文排版和顶部品牌区交给生图模型完成；二维码仍然在最后由脚本覆盖，避免二维码被 AI 仿制。

## candidate-ai-clean-1 清爽培训海报

```text
Use case: ads-marketing
Asset type: complete 1080x1920 vertical Chinese mobile poster for WeChat sharing
Primary request: Design a polished, complete Toastmasters event poster in Chinese. The poster must feel more like a finished premium training/event poster than a background template.
Content discipline: Use only the exact event text provided below. Do not add unprovided sections, benefits, course outcomes, guest biography, slogans, or explanatory copy.
Reference direction: 中文 Toastmasters 嘉宾分享海报，使用 Cindy Zhang 的照片作为主视觉，去掉原照片里的纯灰背景，保留人物干净专业的白色西装形象。必须尽量保持原始照片中的五官、脸型、发型、肤色、白色西装和姿态，不要重画成另一个人。不要出现副标题、“你将收获”模块、收益列表、课程要点列表或额外说明文案。嘉宾信息只出现一次：姓名和身份即可，不再重复嘉宾介绍。底部深蓝信息栏左侧保持一块安静的连续深蓝背景区域，不放文字、图标、外框或装饰面板，信息文字从右侧开始。整体温柔、清晰、专业，有一点神秘感但不要玄学化。
Input image: Use the provided speaker portrait as the main person with high photo fidelity. Preserve the original face, facial proportions, hairstyle, skin tone, expression, clothing, and body posture as closely as possible. Do not redraw or beautify the person into a different identity; only remove the original background and integrate the cut-out into the poster design. Keep one person only.
Official brand/QR handling: You may create a polished Toastmasters-style top brand area and icon as part of the complete poster. Do not create any QR code. Keep the lower-left part of the event bar as normal continuous deep-blue background texture. Leave that area visually quiet and free of text, icons, outlines, containers, labels, or decorative panels. Start the time, location, fee, and action text to the right of that quiet area.
Top header layout: Put the Toastmasters-style icon on the top-left. Put “上海活力中文演讲俱乐部 / 第875次会议” directly to the right of that icon in the same compact header row or header area. Do not add a separate English brand slogan or generic Chinese tagline; the icon already communicates the Toastmasters brand. Do not repeat the club name and meeting number again above the main title.
Exact Chinese copy to include:
- 顶部品牌行: 上海活力中文演讲俱乐部 / 第875次会议
- 主标题: 翻牌时刻：和你的拖延症聊聊天

- 分享嘉宾: Cindy Zhang
- 嘉宾身份: 双语潜意识卡牌带领师 / 个人成长教练

- 时间: 2026年6月7日 周日 14:00-17:00
- 地点: 乌鲁木齐南路66号梧桐院邻里汇3号楼2楼（地铁1号线衡山路站4号口步行400米）
- 费用: 来宾35元 / 其他俱乐部会员25元 / 学生15元 / 角色免费
- 行动语: 扫码报名，和拖延症好好聊聊！
- 页脚: TOASTMASTERS 国际演讲俱乐部
Theme visual direction: 围绕“翻牌时刻：和你的拖延症聊聊天”建立视觉隐喻：卡牌翻开、内在对话、时间沙漏、待办清单、行动按钮、轻柔光晕。画面要像一场个人成长工作坊，而不是硬核商业讲座。
Theme visual keywords: 潜意识卡牌、翻牌时刻、拖延症、内在对话、个人成长、行动启动
Typography: Chinese text must be readable, high-contrast, and professionally aligned. Use bold dark-blue title typography, smaller clean body text, consistent spacing, no chaotic text blocks.
Hard constraints: no extra people, no distorted face, no scannable code or code-like pattern, no watermark, no random unreadable text, no unrelated icons, no outlines or containers in the lower-left event bar.

Composition: Closest to the provided reference poster. Light blue-white gradient, right-side full-height speaker, left-side large title, mid-lower compact guest name-and-title block, open visual breathing room with theme-related cards and dialogue imagery, no benefit list, bottom deep-blue event bar.
Mood: clean, bright, credible, inviting, high-end public training poster.
```

保存为：`outputs/2026-06-07-meeting-875/candidate-ai-clean-1.png`

## candidate-ai-clean-2 高级杂志感完整海报

```text
Use case: ads-marketing
Asset type: complete 1080x1920 vertical Chinese mobile poster for WeChat sharing
Primary request: Design a polished, complete Toastmasters event poster in Chinese. The poster must feel more like a finished premium training/event poster than a background template.
Content discipline: Use only the exact event text provided below. Do not add unprovided sections, benefits, course outcomes, guest biography, slogans, or explanatory copy.
Reference direction: 中文 Toastmasters 嘉宾分享海报，使用 Cindy Zhang 的照片作为主视觉，去掉原照片里的纯灰背景，保留人物干净专业的白色西装形象。必须尽量保持原始照片中的五官、脸型、发型、肤色、白色西装和姿态，不要重画成另一个人。不要出现副标题、“你将收获”模块、收益列表、课程要点列表或额外说明文案。嘉宾信息只出现一次：姓名和身份即可，不再重复嘉宾介绍。底部深蓝信息栏左侧保持一块安静的连续深蓝背景区域，不放文字、图标、外框或装饰面板，信息文字从右侧开始。整体温柔、清晰、专业，有一点神秘感但不要玄学化。
Input image: Use the provided speaker portrait as the main person with high photo fidelity. Preserve the original face, facial proportions, hairstyle, skin tone, expression, clothing, and body posture as closely as possible. Do not redraw or beautify the person into a different identity; only remove the original background and integrate the cut-out into the poster design. Keep one person only.
Official brand/QR handling: You may create a polished Toastmasters-style top brand area and icon as part of the complete poster. Do not create any QR code. Keep the lower-left part of the event bar as normal continuous deep-blue background texture. Leave that area visually quiet and free of text, icons, outlines, containers, labels, or decorative panels. Start the time, location, fee, and action text to the right of that quiet area.
Top header layout: Put the Toastmasters-style icon on the top-left. Put “上海活力中文演讲俱乐部 / 第875次会议” directly to the right of that icon in the same compact header row or header area. Do not add a separate English brand slogan or generic Chinese tagline; the icon already communicates the Toastmasters brand. Do not repeat the club name and meeting number again above the main title.
Exact Chinese copy to include:
- 顶部品牌行: 上海活力中文演讲俱乐部 / 第875次会议
- 主标题: 翻牌时刻：和你的拖延症聊聊天

- 分享嘉宾: Cindy Zhang
- 嘉宾身份: 双语潜意识卡牌带领师 / 个人成长教练

- 时间: 2026年6月7日 周日 14:00-17:00
- 地点: 乌鲁木齐南路66号梧桐院邻里汇3号楼2楼（地铁1号线衡山路站4号口步行400米）
- 费用: 来宾35元 / 其他俱乐部会员25元 / 学生15元 / 角色免费
- 行动语: 扫码报名，和拖延症好好聊聊！
- 页脚: TOASTMASTERS 国际演讲俱乐部
Theme visual direction: 围绕“翻牌时刻：和你的拖延症聊聊天”建立视觉隐喻：卡牌翻开、内在对话、时间沙漏、待办清单、行动按钮、轻柔光晕。画面要像一场个人成长工作坊，而不是硬核商业讲座。
Theme visual keywords: 潜意识卡牌、翻牌时刻、拖延症、内在对话、个人成长、行动启动
Typography: Chinese text must be readable, high-contrast, and professionally aligned. Use bold dark-blue title typography, smaller clean body text, consistent spacing, no chaotic text blocks.
Hard constraints: no extra people, no distorted face, no scannable code or code-like pattern, no watermark, no random unreadable text, no unrelated icons, no outlines or containers in the lower-left event bar.

Composition: More premium editorial and spacious. Keep a refined light background, strong portrait presence, large title, and elegant theme-related visual metaphors. Information hierarchy must remain very clear.
Mood: executive, premium, modern, polished, still readable on mobile.
```

保存为：`outputs/2026-06-07-meeting-875/candidate-ai-clean-2.png`

## candidate-ai-clean-3 强主题传播吸睛版

```text
Use case: ads-marketing
Asset type: complete 1080x1920 vertical Chinese mobile poster for WeChat sharing
Primary request: Design a polished, complete Toastmasters event poster in Chinese. The poster must feel more like a finished premium training/event poster than a background template.
Content discipline: Use only the exact event text provided below. Do not add unprovided sections, benefits, course outcomes, guest biography, slogans, or explanatory copy.
Reference direction: 中文 Toastmasters 嘉宾分享海报，使用 Cindy Zhang 的照片作为主视觉，去掉原照片里的纯灰背景，保留人物干净专业的白色西装形象。必须尽量保持原始照片中的五官、脸型、发型、肤色、白色西装和姿态，不要重画成另一个人。不要出现副标题、“你将收获”模块、收益列表、课程要点列表或额外说明文案。嘉宾信息只出现一次：姓名和身份即可，不再重复嘉宾介绍。底部深蓝信息栏左侧保持一块安静的连续深蓝背景区域，不放文字、图标、外框或装饰面板，信息文字从右侧开始。整体温柔、清晰、专业，有一点神秘感但不要玄学化。
Input image: Use the provided speaker portrait as the main person with high photo fidelity. Preserve the original face, facial proportions, hairstyle, skin tone, expression, clothing, and body posture as closely as possible. Do not redraw or beautify the person into a different identity; only remove the original background and integrate the cut-out into the poster design. Keep one person only.
Official brand/QR handling: You may create a polished Toastmasters-style top brand area and icon as part of the complete poster. Do not create any QR code. Keep the lower-left part of the event bar as normal continuous deep-blue background texture. Leave that area visually quiet and free of text, icons, outlines, containers, labels, or decorative panels. Start the time, location, fee, and action text to the right of that quiet area.
Top header layout: Put the Toastmasters-style icon on the top-left. Put “上海活力中文演讲俱乐部 / 第875次会议” directly to the right of that icon in the same compact header row or header area. Do not add a separate English brand slogan or generic Chinese tagline; the icon already communicates the Toastmasters brand. Do not repeat the club name and meeting number again above the main title.
Exact Chinese copy to include:
- 顶部品牌行: 上海活力中文演讲俱乐部 / 第875次会议
- 主标题: 翻牌时刻：和你的拖延症聊聊天

- 分享嘉宾: Cindy Zhang
- 嘉宾身份: 双语潜意识卡牌带领师 / 个人成长教练

- 时间: 2026年6月7日 周日 14:00-17:00
- 地点: 乌鲁木齐南路66号梧桐院邻里汇3号楼2楼（地铁1号线衡山路站4号口步行400米）
- 费用: 来宾35元 / 其他俱乐部会员25元 / 学生15元 / 角色免费
- 行动语: 扫码报名，和拖延症好好聊聊！
- 页脚: TOASTMASTERS 国际演讲俱乐部
Theme visual direction: 围绕“翻牌时刻：和你的拖延症聊聊天”建立视觉隐喻：卡牌翻开、内在对话、时间沙漏、待办清单、行动按钮、轻柔光晕。画面要像一场个人成长工作坊，而不是硬核商业讲座。
Theme visual keywords: 潜意识卡牌、翻牌时刻、拖延症、内在对话、个人成长、行动启动
Typography: Chinese text must be readable, high-contrast, and professionally aligned. Use bold dark-blue title typography, smaller clean body text, consistent spacing, no chaotic text blocks.
Hard constraints: no extra people, no distorted face, no scannable code or code-like pattern, no watermark, no random unreadable text, no unrelated icons, no outlines or containers in the lower-left event bar.

Composition: Stronger theme expression. Add tasteful visual elements from the configured theme keywords around the speaker, while preserving readable blocks for all event copy.
Mood: memorable, energetic, intelligent, premium, optimized for attracting attention in WeChat feeds.
```

保存为：`outputs/2026-06-07-meeting-875/candidate-ai-clean-3.png`
