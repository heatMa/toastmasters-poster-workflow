# 生图提示词

把下面 3 条提示词分别交给 ChatGPT image2 / 生图工具生成完整中文海报。生成结果保存为 `candidate-ai-clean-1.png`、`candidate-ai-clean-2.png`、`candidate-ai-clean-3.png`。

注意：中文排版和顶部品牌区交给生图模型完成；二维码仍然在最后由脚本覆盖，避免二维码被 AI 仿制。

## candidate-ai-clean-1 清爽培训海报

```text
Use case: ads-marketing
Asset type: complete 1080x1920 vertical Chinese mobile poster for WeChat sharing
Primary request: Design a polished, complete Toastmasters event poster in Chinese. The poster must feel more like a finished premium training/event poster than a background template.
Content discipline: Use only the exact event text provided below. Do not add unprovided sections, benefits, course outcomes, guest biography, slogans, or explanatory copy.
Reference direction: 中文 Toastmasters 会议海报。主题围绕声音训练、公众表达、麦克风、声波、专业培训。使用嘉宾 Helen 的照片作为主视觉，明亮、专业、可信、适合微信传播。
Input image: Use the provided speaker portrait as the main person with high photo fidelity. Preserve the original face, facial proportions, hairstyle, skin tone, expression, clothing, and body posture as closely as possible. Do not redraw or beautify the person into a different identity; only remove the original background and integrate the cut-out into the poster design. Keep one person only.
Official brand/QR handling: You may create a polished Toastmasters-style top brand area and icon as part of the complete poster. Do not create any QR code. Keep the lower-left part of the event bar as normal continuous deep-blue background texture. Leave that area visually quiet and free of text, icons, outlines, containers, labels, or decorative panels. Start the time, location, fee, and action text to the right of that quiet area.
Top header layout: Put the Toastmasters-style icon on the top-left. Put “上海活力中文演讲俱乐部 / 第877次会议” directly to the right of that icon in the same compact header row or header area. Do not add a separate English brand slogan or generic Chinese tagline; the icon already communicates the Toastmasters brand. Do not repeat the club name and meeting number again above the main title.
Exact Chinese copy to include:
- 顶部品牌行: 上海活力中文演讲俱乐部 / 第877次会议
- 主标题: 解码好声音

- 分享嘉宾: Helen
- 嘉宾身份: 原省级电台主持人 / AACTP注册培训师 / 英国谢菲尔德大学硕士
- 嘉宾介绍: 《解码好声音》版权课程讲师
- 你将收获:
- 怎样算好声音？
- 为什么要有好声音？
- 怎样修炼好声音？
- 时间: 2026年6月28日 周日 14:00-17:00
- 地点: 乌鲁木齐南路66号梧桐院邻里汇3号楼2楼
- 费用: 来宾35元 / 其他俱乐部会员25元 / 学生15元 / 角色免费

- 页脚: TOASTMASTERS 国际演讲俱乐部
Theme visual direction: 围绕“解码好声音”建立视觉隐喻：麦克风、声波、音频频谱、表达训练、舞台沟通。
Theme visual keywords: 好声音、麦克风、声波、表达训练、公众演讲
Typography: Chinese text must be readable, high-contrast, and professionally aligned. Use bold dark-blue title typography, smaller clean body text, consistent spacing, no chaotic text blocks.
Hard constraints: no extra people, no distorted face, no scannable code or code-like pattern, no watermark, no random unreadable text, no unrelated icons, no outlines or containers in the lower-left event bar.

Composition: Closest to the provided reference poster. Light blue-white gradient, right-side full-height speaker, left-side large title, mid-lower structured guest intro, four benefit cards, bottom deep-blue event bar.
Mood: clean, bright, credible, inviting, high-end public training poster.
```

保存为：`outputs/2026-06-28-meeting-877/candidate-ai-clean-1.png`

## candidate-ai-clean-2 高级杂志感完整海报

```text
Use case: ads-marketing
Asset type: complete 1080x1920 vertical Chinese mobile poster for WeChat sharing
Primary request: Design a polished, complete Toastmasters event poster in Chinese. The poster must feel more like a finished premium training/event poster than a background template.
Content discipline: Use only the exact event text provided below. Do not add unprovided sections, benefits, course outcomes, guest biography, slogans, or explanatory copy.
Reference direction: 中文 Toastmasters 会议海报。主题围绕声音训练、公众表达、麦克风、声波、专业培训。使用嘉宾 Helen 的照片作为主视觉，明亮、专业、可信、适合微信传播。
Input image: Use the provided speaker portrait as the main person with high photo fidelity. Preserve the original face, facial proportions, hairstyle, skin tone, expression, clothing, and body posture as closely as possible. Do not redraw or beautify the person into a different identity; only remove the original background and integrate the cut-out into the poster design. Keep one person only.
Official brand/QR handling: You may create a polished Toastmasters-style top brand area and icon as part of the complete poster. Do not create any QR code. Keep the lower-left part of the event bar as normal continuous deep-blue background texture. Leave that area visually quiet and free of text, icons, outlines, containers, labels, or decorative panels. Start the time, location, fee, and action text to the right of that quiet area.
Top header layout: Put the Toastmasters-style icon on the top-left. Put “上海活力中文演讲俱乐部 / 第877次会议” directly to the right of that icon in the same compact header row or header area. Do not add a separate English brand slogan or generic Chinese tagline; the icon already communicates the Toastmasters brand. Do not repeat the club name and meeting number again above the main title.
Exact Chinese copy to include:
- 顶部品牌行: 上海活力中文演讲俱乐部 / 第877次会议
- 主标题: 解码好声音

- 分享嘉宾: Helen
- 嘉宾身份: 原省级电台主持人 / AACTP注册培训师 / 英国谢菲尔德大学硕士
- 嘉宾介绍: 《解码好声音》版权课程讲师
- 你将收获:
- 怎样算好声音？
- 为什么要有好声音？
- 怎样修炼好声音？
- 时间: 2026年6月28日 周日 14:00-17:00
- 地点: 乌鲁木齐南路66号梧桐院邻里汇3号楼2楼
- 费用: 来宾35元 / 其他俱乐部会员25元 / 学生15元 / 角色免费

- 页脚: TOASTMASTERS 国际演讲俱乐部
Theme visual direction: 围绕“解码好声音”建立视觉隐喻：麦克风、声波、音频频谱、表达训练、舞台沟通。
Theme visual keywords: 好声音、麦克风、声波、表达训练、公众演讲
Typography: Chinese text must be readable, high-contrast, and professionally aligned. Use bold dark-blue title typography, smaller clean body text, consistent spacing, no chaotic text blocks.
Hard constraints: no extra people, no distorted face, no scannable code or code-like pattern, no watermark, no random unreadable text, no unrelated icons, no outlines or containers in the lower-left event bar.

Composition: More premium editorial and spacious. Keep a refined light background, strong portrait presence, large title, and elegant theme-related visual metaphors. Information hierarchy must remain very clear.
Mood: executive, premium, modern, polished, still readable on mobile.
```

保存为：`outputs/2026-06-28-meeting-877/candidate-ai-clean-2.png`

## candidate-ai-clean-3 强主题传播吸睛版

```text
Use case: ads-marketing
Asset type: complete 1080x1920 vertical Chinese mobile poster for WeChat sharing
Primary request: Design a polished, complete Toastmasters event poster in Chinese. The poster must feel more like a finished premium training/event poster than a background template.
Content discipline: Use only the exact event text provided below. Do not add unprovided sections, benefits, course outcomes, guest biography, slogans, or explanatory copy.
Reference direction: 中文 Toastmasters 会议海报。主题围绕声音训练、公众表达、麦克风、声波、专业培训。使用嘉宾 Helen 的照片作为主视觉，明亮、专业、可信、适合微信传播。
Input image: Use the provided speaker portrait as the main person with high photo fidelity. Preserve the original face, facial proportions, hairstyle, skin tone, expression, clothing, and body posture as closely as possible. Do not redraw or beautify the person into a different identity; only remove the original background and integrate the cut-out into the poster design. Keep one person only.
Official brand/QR handling: You may create a polished Toastmasters-style top brand area and icon as part of the complete poster. Do not create any QR code. Keep the lower-left part of the event bar as normal continuous deep-blue background texture. Leave that area visually quiet and free of text, icons, outlines, containers, labels, or decorative panels. Start the time, location, fee, and action text to the right of that quiet area.
Top header layout: Put the Toastmasters-style icon on the top-left. Put “上海活力中文演讲俱乐部 / 第877次会议” directly to the right of that icon in the same compact header row or header area. Do not add a separate English brand slogan or generic Chinese tagline; the icon already communicates the Toastmasters brand. Do not repeat the club name and meeting number again above the main title.
Exact Chinese copy to include:
- 顶部品牌行: 上海活力中文演讲俱乐部 / 第877次会议
- 主标题: 解码好声音

- 分享嘉宾: Helen
- 嘉宾身份: 原省级电台主持人 / AACTP注册培训师 / 英国谢菲尔德大学硕士
- 嘉宾介绍: 《解码好声音》版权课程讲师
- 你将收获:
- 怎样算好声音？
- 为什么要有好声音？
- 怎样修炼好声音？
- 时间: 2026年6月28日 周日 14:00-17:00
- 地点: 乌鲁木齐南路66号梧桐院邻里汇3号楼2楼
- 费用: 来宾35元 / 其他俱乐部会员25元 / 学生15元 / 角色免费

- 页脚: TOASTMASTERS 国际演讲俱乐部
Theme visual direction: 围绕“解码好声音”建立视觉隐喻：麦克风、声波、音频频谱、表达训练、舞台沟通。
Theme visual keywords: 好声音、麦克风、声波、表达训练、公众演讲
Typography: Chinese text must be readable, high-contrast, and professionally aligned. Use bold dark-blue title typography, smaller clean body text, consistent spacing, no chaotic text blocks.
Hard constraints: no extra people, no distorted face, no scannable code or code-like pattern, no watermark, no random unreadable text, no unrelated icons, no outlines or containers in the lower-left event bar.

Composition: Stronger theme expression. Add tasteful visual elements from the configured theme keywords around the speaker, while preserving readable blocks for all event copy.
Mood: memorable, energetic, intelligent, premium, optimized for attracting attention in WeChat feeds.
```

保存为：`outputs/2026-06-28-meeting-877/candidate-ai-clean-3.png`
