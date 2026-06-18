# 生图提示词

把下面 3 条提示词分别交给 ChatGPT image2 / 生图工具生成完整中文海报。生成结果保存为 `candidate-ai-clean-1.png`、`candidate-ai-clean-2.png`、`candidate-ai-clean-3.png`。

注意：中文排版和顶部品牌区交给生图模型完成；二维码仍然在最后由脚本覆盖，避免二维码被 AI 仿制。

## candidate-ai-clean-1 清爽培训海报

```text
Use case: ads-marketing
Asset type: complete 1080x1920 vertical Chinese mobile poster for WeChat sharing
Primary request: Design a polished, complete Toastmasters event poster in Chinese. The poster must feel more like a finished premium training/event poster than a background template.
Reference direction: 温暖治愈系的身心灵活动海报，右侧主讲人自然光肖像，左侧大标题，中下部嘉宾介绍和「你将收获」模块，底部深蓝信息栏，留白充足，专业可信。
Input image: Use the provided speaker portrait as the main person. Preserve recognizable facial structure, hairstyle, age, and professional business presence. Keep one person only.
Official brand/QR handling: You may create a polished Toastmasters-style top brand area and icon as part of the complete poster. Do not create any QR code. In the lower-left event bar, reserve one clean blank white square area for a real QR code overlay; do not draw a dashed frame, do not draw a fake QR, and do not write placeholder words such as “放置二维码” inside that blank square.
Top header layout: Put the Toastmasters-style icon on the top-left. Put “上海活力中文演讲俱乐部 / 第871次会议” directly to the right of that icon in the same compact header row or header area. Do not add a separate English brand slogan or generic Chinese tagline; the icon already communicates the Toastmasters brand. Do not repeat the club name and meeting number again above the main title.
Exact Chinese copy to include:
- 顶部品牌行: 上海活力中文演讲俱乐部 / 第871次会议
- 主标题: 人人都能做5分钟“解读师”
- 副标题: 唤醒直觉，连接内在智慧
- 分享嘉宾: 宋思甍
- 嘉宾身份: 心能觉醒身心灵平台创始人 / 正念疗愈师 / 超感解读师导师
- 嘉宾介绍: 心能觉醒身心灵平台创始人，正念疗愈师，企业正念教练，超感解读师导师，澳洲采光晶露调频师导师，星际玛雅13月亮历解读师。
- 你将收获:
- 掌握解读技巧：5分钟快速入门，连接内在智慧
- 提升直觉力：激活感知，看见更多可能性
- 正念减压：疗愈身心，回归当下平静
- 能量调频：探索身心灵奥秘，提升状态
- 时间: 2026年5月17日 周日 14:00-17:00
- 地点: 乌鲁木齐南路66号梧桐院邻里汇3号楼2楼（地铁1号线衡山路站4号口步行400米）
- 费用: 来宾35元 / 其他俱乐部会员25元 / 学生15元 / 角色免费
- 行动语: 扫码报名，开启你的解读之旅！
- 页脚: TOASTMASTERS 国际演讲俱乐部
Theme visual direction: 围绕「解读」与「正念」建立视觉隐喻：直觉、能量、水晶、星图、自然光。整体应温暖、柔和、有灵性但不玄乎。
Theme visual keywords: 水晶能量、星图罗盘、自然光晕、正念冥想、直觉之眼
Typography: Chinese text must be readable, high-contrast, and professionally aligned. Use bold dark-blue title typography, smaller clean body text, consistent spacing, no chaotic text blocks.
Hard constraints: no extra people, no distorted face, no fake QR code, no dashed QR placeholder frame, no QR placeholder text, no watermark, no random unreadable text, no unrelated icons.

Composition: Closest to the provided reference poster. Light blue-white gradient, right-side full-height speaker, left-side large title, mid-lower guest intro, four benefit cards, bottom deep-blue event bar.
Mood: clean, bright, credible, inviting, high-end public training poster.
```

保存为：`outputs/2026-05-17-meeting-871/candidate-ai-clean-1.png`

## candidate-ai-clean-2 高级杂志感完整海报

```text
Use case: ads-marketing
Asset type: complete 1080x1920 vertical Chinese mobile poster for WeChat sharing
Primary request: Design a polished, complete Toastmasters event poster in Chinese. The poster must feel more like a finished premium training/event poster than a background template.
Reference direction: 温暖治愈系的身心灵活动海报，右侧主讲人自然光肖像，左侧大标题，中下部嘉宾介绍和「你将收获」模块，底部深蓝信息栏，留白充足，专业可信。
Input image: Use the provided speaker portrait as the main person. Preserve recognizable facial structure, hairstyle, age, and professional business presence. Keep one person only.
Official brand/QR handling: You may create a polished Toastmasters-style top brand area and icon as part of the complete poster. Do not create any QR code. In the lower-left event bar, reserve one clean blank white square area for a real QR code overlay; do not draw a dashed frame, do not draw a fake QR, and do not write placeholder words such as “放置二维码” inside that blank square.
Top header layout: Put the Toastmasters-style icon on the top-left. Put “上海活力中文演讲俱乐部 / 第871次会议” directly to the right of that icon in the same compact header row or header area. Do not add a separate English brand slogan or generic Chinese tagline; the icon already communicates the Toastmasters brand. Do not repeat the club name and meeting number again above the main title.
Exact Chinese copy to include:
- 顶部品牌行: 上海活力中文演讲俱乐部 / 第871次会议
- 主标题: 人人都能做5分钟“解读师”
- 副标题: 唤醒直觉，连接内在智慧
- 分享嘉宾: 宋思甍
- 嘉宾身份: 心能觉醒身心灵平台创始人 / 正念疗愈师 / 超感解读师导师
- 嘉宾介绍: 心能觉醒身心灵平台创始人，正念疗愈师，企业正念教练，超感解读师导师，澳洲采光晶露调频师导师，星际玛雅13月亮历解读师。
- 你将收获:
- 掌握解读技巧：5分钟快速入门，连接内在智慧
- 提升直觉力：激活感知，看见更多可能性
- 正念减压：疗愈身心，回归当下平静
- 能量调频：探索身心灵奥秘，提升状态
- 时间: 2026年5月17日 周日 14:00-17:00
- 地点: 乌鲁木齐南路66号梧桐院邻里汇3号楼2楼（地铁1号线衡山路站4号口步行400米）
- 费用: 来宾35元 / 其他俱乐部会员25元 / 学生15元 / 角色免费
- 行动语: 扫码报名，开启你的解读之旅！
- 页脚: TOASTMASTERS 国际演讲俱乐部
Theme visual direction: 围绕「解读」与「正念」建立视觉隐喻：直觉、能量、水晶、星图、自然光。整体应温暖、柔和、有灵性但不玄乎。
Theme visual keywords: 水晶能量、星图罗盘、自然光晕、正念冥想、直觉之眼
Typography: Chinese text must be readable, high-contrast, and professionally aligned. Use bold dark-blue title typography, smaller clean body text, consistent spacing, no chaotic text blocks.
Hard constraints: no extra people, no distorted face, no fake QR code, no dashed QR placeholder frame, no QR placeholder text, no watermark, no random unreadable text, no unrelated icons.

Composition: More premium editorial and spacious. Keep a refined light background, strong portrait presence, large title, and elegant theme-related visual metaphors. Information hierarchy must remain very clear.
Mood: executive, premium, modern, polished, still readable on mobile.
```

保存为：`outputs/2026-05-17-meeting-871/candidate-ai-clean-2.png`

## candidate-ai-clean-3 强主题传播吸睛版

```text
Use case: ads-marketing
Asset type: complete 1080x1920 vertical Chinese mobile poster for WeChat sharing
Primary request: Design a polished, complete Toastmasters event poster in Chinese. The poster must feel more like a finished premium training/event poster than a background template.
Reference direction: 温暖治愈系的身心灵活动海报，右侧主讲人自然光肖像，左侧大标题，中下部嘉宾介绍和「你将收获」模块，底部深蓝信息栏，留白充足，专业可信。
Input image: Use the provided speaker portrait as the main person. Preserve recognizable facial structure, hairstyle, age, and professional business presence. Keep one person only.
Official brand/QR handling: You may create a polished Toastmasters-style top brand area and icon as part of the complete poster. Do not create any QR code. In the lower-left event bar, reserve one clean blank white square area for a real QR code overlay; do not draw a dashed frame, do not draw a fake QR, and do not write placeholder words such as “放置二维码” inside that blank square.
Top header layout: Put the Toastmasters-style icon on the top-left. Put “上海活力中文演讲俱乐部 / 第871次会议” directly to the right of that icon in the same compact header row or header area. Do not add a separate English brand slogan or generic Chinese tagline; the icon already communicates the Toastmasters brand. Do not repeat the club name and meeting number again above the main title.
Exact Chinese copy to include:
- 顶部品牌行: 上海活力中文演讲俱乐部 / 第871次会议
- 主标题: 人人都能做5分钟“解读师”
- 副标题: 唤醒直觉，连接内在智慧
- 分享嘉宾: 宋思甍
- 嘉宾身份: 心能觉醒身心灵平台创始人 / 正念疗愈师 / 超感解读师导师
- 嘉宾介绍: 心能觉醒身心灵平台创始人，正念疗愈师，企业正念教练，超感解读师导师，澳洲采光晶露调频师导师，星际玛雅13月亮历解读师。
- 你将收获:
- 掌握解读技巧：5分钟快速入门，连接内在智慧
- 提升直觉力：激活感知，看见更多可能性
- 正念减压：疗愈身心，回归当下平静
- 能量调频：探索身心灵奥秘，提升状态
- 时间: 2026年5月17日 周日 14:00-17:00
- 地点: 乌鲁木齐南路66号梧桐院邻里汇3号楼2楼（地铁1号线衡山路站4号口步行400米）
- 费用: 来宾35元 / 其他俱乐部会员25元 / 学生15元 / 角色免费
- 行动语: 扫码报名，开启你的解读之旅！
- 页脚: TOASTMASTERS 国际演讲俱乐部
Theme visual direction: 围绕「解读」与「正念」建立视觉隐喻：直觉、能量、水晶、星图、自然光。整体应温暖、柔和、有灵性但不玄乎。
Theme visual keywords: 水晶能量、星图罗盘、自然光晕、正念冥想、直觉之眼
Typography: Chinese text must be readable, high-contrast, and professionally aligned. Use bold dark-blue title typography, smaller clean body text, consistent spacing, no chaotic text blocks.
Hard constraints: no extra people, no distorted face, no fake QR code, no dashed QR placeholder frame, no QR placeholder text, no watermark, no random unreadable text, no unrelated icons.

Composition: Stronger theme expression. Add tasteful visual elements from the configured theme keywords around the speaker, while preserving readable blocks for all event copy.
Mood: memorable, energetic, intelligent, premium, optimized for attracting attention in WeChat feeds.
```

保存为：`outputs/2026-05-17-meeting-871/candidate-ai-clean-3.png`
