# 生图提示词

把下面 3 条提示词分别交给 ChatGPT image2 / 生图工具生成完整中文海报。生成结果保存为 `candidate-ai-clean-1.png`、`candidate-ai-clean-2.png`、`candidate-ai-clean-3.png`。

注意：中文排版和顶部品牌区交给生图模型完成；二维码仍然在最后由脚本覆盖，避免二维码被 AI 仿制。

## candidate-ai-clean-1 清爽培训海报

```text
Use case: ads-marketing
Asset type: complete 1080x1920 vertical Chinese mobile poster for WeChat sharing
Primary request: Design a polished, complete Toastmasters event poster in Chinese. The poster must feel more like a finished premium training/event poster than a background template.
Content discipline: Use only the exact event text provided below. Do not add unprovided sections, benefits, course outcomes, guest biography, slogans, or explanatory copy.
Reference direction: 中文 Toastmasters 会议海报。本期没有嘉宾分享，但这只是制作约束，不要把“本次没有嘉宾分享”或类似说明文字显示在海报上。不出现嘉宾照片、嘉宾介绍、分享嘉宾模块、单人主讲人模块、“你将收获”模块、收益列表或额外说明文案。海报主题只围绕“官员换届选举”。底部深蓝信息栏左侧保持一块安静的连续深蓝背景区域，不放文字、图标、外框或装饰面板，信息文字从右侧开始。整体正式、清晰、庄重、有组织感。
Input image: Do not use a speaker portrait or single featured guest. Build the main visual from the configured event theme and visual keywords only.
Official brand/QR handling: You may create a polished Toastmasters-style top brand area and icon as part of the complete poster. Do not create any QR code. Keep the lower-left part of the event bar as normal continuous deep-blue background texture. Leave that area visually quiet and free of text, icons, outlines, containers, labels, or decorative panels. Start the time, location, fee, and action text to the right of that quiet area.
Top header layout: Put the Toastmasters-style icon on the top-left. Put “上海活力中文演讲俱乐部 / 第876次会议” directly to the right of that icon in the same compact header row or header area. Do not add a separate English brand slogan or generic Chinese tagline; the icon already communicates the Toastmasters brand. Do not repeat the club name and meeting number again above the main title.
Exact Chinese copy to include:
- 顶部品牌行: 上海活力中文演讲俱乐部 / 第876次会议
- 主标题: 官员换届选举



- 时间: 2026年6月14日 周日 14:00-17:00
- 地点: 乌鲁木齐南路66号梧桐院邻里汇3号楼2楼（地铁1号线衡山路站4号口步行400米）
- 费用: 来宾35元 / 其他俱乐部会员25元 / 学生15元 / 角色免费

- 页脚: TOASTMASTERS 国际演讲俱乐部
Theme visual direction: 围绕“官员换届选举”建立视觉隐喻：会议投票、选票、讲台、俱乐部治理、交接、秩序、责任。不要添加未提供的活动说明或候选人信息。
Theme visual keywords: 官员换届选举、投票、选票、讲台、俱乐部治理、交接
Typography: Chinese text must be readable, high-contrast, and professionally aligned. Use bold dark-blue title typography, smaller clean body text, consistent spacing, no chaotic text blocks.
Hard constraints: no extra people, no distorted face, no scannable code or code-like pattern, no watermark, no random unreadable text, no unrelated icons, no outlines or containers in the lower-left event bar.

Composition: Clean event-program poster. Light blue-white main area, large left-side title, central visual metaphor for this event theme, structured event format block, bottom deep-blue event bar.
Mood: clean, bright, credible, inviting, high-end public training poster.
```

保存为：`outputs/2026-06-14-meeting-876/candidate-ai-clean-1.png`

## candidate-ai-clean-2 高级杂志感完整海报

```text
Use case: ads-marketing
Asset type: complete 1080x1920 vertical Chinese mobile poster for WeChat sharing
Primary request: Design a polished, complete Toastmasters event poster in Chinese. The poster must feel more like a finished premium training/event poster than a background template.
Content discipline: Use only the exact event text provided below. Do not add unprovided sections, benefits, course outcomes, guest biography, slogans, or explanatory copy.
Reference direction: 中文 Toastmasters 会议海报。本期没有嘉宾分享，但这只是制作约束，不要把“本次没有嘉宾分享”或类似说明文字显示在海报上。不出现嘉宾照片、嘉宾介绍、分享嘉宾模块、单人主讲人模块、“你将收获”模块、收益列表或额外说明文案。海报主题只围绕“官员换届选举”。底部深蓝信息栏左侧保持一块安静的连续深蓝背景区域，不放文字、图标、外框或装饰面板，信息文字从右侧开始。整体正式、清晰、庄重、有组织感。
Input image: Do not use a speaker portrait or single featured guest. Build the main visual from the configured event theme and visual keywords only.
Official brand/QR handling: You may create a polished Toastmasters-style top brand area and icon as part of the complete poster. Do not create any QR code. Keep the lower-left part of the event bar as normal continuous deep-blue background texture. Leave that area visually quiet and free of text, icons, outlines, containers, labels, or decorative panels. Start the time, location, fee, and action text to the right of that quiet area.
Top header layout: Put the Toastmasters-style icon on the top-left. Put “上海活力中文演讲俱乐部 / 第876次会议” directly to the right of that icon in the same compact header row or header area. Do not add a separate English brand slogan or generic Chinese tagline; the icon already communicates the Toastmasters brand. Do not repeat the club name and meeting number again above the main title.
Exact Chinese copy to include:
- 顶部品牌行: 上海活力中文演讲俱乐部 / 第876次会议
- 主标题: 官员换届选举



- 时间: 2026年6月14日 周日 14:00-17:00
- 地点: 乌鲁木齐南路66号梧桐院邻里汇3号楼2楼（地铁1号线衡山路站4号口步行400米）
- 费用: 来宾35元 / 其他俱乐部会员25元 / 学生15元 / 角色免费

- 页脚: TOASTMASTERS 国际演讲俱乐部
Theme visual direction: 围绕“官员换届选举”建立视觉隐喻：会议投票、选票、讲台、俱乐部治理、交接、秩序、责任。不要添加未提供的活动说明或候选人信息。
Theme visual keywords: 官员换届选举、投票、选票、讲台、俱乐部治理、交接
Typography: Chinese text must be readable, high-contrast, and professionally aligned. Use bold dark-blue title typography, smaller clean body text, consistent spacing, no chaotic text blocks.
Hard constraints: no extra people, no distorted face, no scannable code or code-like pattern, no watermark, no random unreadable text, no unrelated icons, no outlines or containers in the lower-left event bar.

Composition: More premium editorial and spacious. Keep a refined light background, strong event-theme visual presence, large title, and elegant theme-related visual metaphors. Information hierarchy must remain very clear.
Mood: executive, premium, modern, polished, still readable on mobile.
```

保存为：`outputs/2026-06-14-meeting-876/candidate-ai-clean-2.png`

## candidate-ai-clean-3 强主题传播吸睛版

```text
Use case: ads-marketing
Asset type: complete 1080x1920 vertical Chinese mobile poster for WeChat sharing
Primary request: Design a polished, complete Toastmasters event poster in Chinese. The poster must feel more like a finished premium training/event poster than a background template.
Content discipline: Use only the exact event text provided below. Do not add unprovided sections, benefits, course outcomes, guest biography, slogans, or explanatory copy.
Reference direction: 中文 Toastmasters 会议海报。本期没有嘉宾分享，但这只是制作约束，不要把“本次没有嘉宾分享”或类似说明文字显示在海报上。不出现嘉宾照片、嘉宾介绍、分享嘉宾模块、单人主讲人模块、“你将收获”模块、收益列表或额外说明文案。海报主题只围绕“官员换届选举”。底部深蓝信息栏左侧保持一块安静的连续深蓝背景区域，不放文字、图标、外框或装饰面板，信息文字从右侧开始。整体正式、清晰、庄重、有组织感。
Input image: Do not use a speaker portrait or single featured guest. Build the main visual from the configured event theme and visual keywords only.
Official brand/QR handling: You may create a polished Toastmasters-style top brand area and icon as part of the complete poster. Do not create any QR code. Keep the lower-left part of the event bar as normal continuous deep-blue background texture. Leave that area visually quiet and free of text, icons, outlines, containers, labels, or decorative panels. Start the time, location, fee, and action text to the right of that quiet area.
Top header layout: Put the Toastmasters-style icon on the top-left. Put “上海活力中文演讲俱乐部 / 第876次会议” directly to the right of that icon in the same compact header row or header area. Do not add a separate English brand slogan or generic Chinese tagline; the icon already communicates the Toastmasters brand. Do not repeat the club name and meeting number again above the main title.
Exact Chinese copy to include:
- 顶部品牌行: 上海活力中文演讲俱乐部 / 第876次会议
- 主标题: 官员换届选举



- 时间: 2026年6月14日 周日 14:00-17:00
- 地点: 乌鲁木齐南路66号梧桐院邻里汇3号楼2楼（地铁1号线衡山路站4号口步行400米）
- 费用: 来宾35元 / 其他俱乐部会员25元 / 学生15元 / 角色免费

- 页脚: TOASTMASTERS 国际演讲俱乐部
Theme visual direction: 围绕“官员换届选举”建立视觉隐喻：会议投票、选票、讲台、俱乐部治理、交接、秩序、责任。不要添加未提供的活动说明或候选人信息。
Theme visual keywords: 官员换届选举、投票、选票、讲台、俱乐部治理、交接
Typography: Chinese text must be readable, high-contrast, and professionally aligned. Use bold dark-blue title typography, smaller clean body text, consistent spacing, no chaotic text blocks.
Hard constraints: no extra people, no distorted face, no scannable code or code-like pattern, no watermark, no random unreadable text, no unrelated icons, no outlines or containers in the lower-left event bar.

Composition: Stronger theme expression. Add tasteful visual elements from the configured theme keywords around the title and program blocks, while preserving readable blocks for all event copy.
Mood: memorable, energetic, intelligent, premium, optimized for attracting attention in WeChat feeds.
```

保存为：`outputs/2026-06-14-meeting-876/candidate-ai-clean-3.png`
