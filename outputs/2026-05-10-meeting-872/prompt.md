# 生图提示词

把下面 3 条提示词分别交给 ChatGPT image2 / 生图工具生成完整中文海报。生成结果保存为 `candidate-ai-clean-1.png`、`candidate-ai-clean-2.png`、`candidate-ai-clean-3.png`。

注意：中文排版和顶部品牌区交给生图模型完成；二维码仍然在最后由脚本覆盖，避免二维码被 AI 仿制。

## candidate-ai-clean-1 清爽培训海报

```text
Use case: ads-marketing
Asset type: complete 1080x1920 vertical Chinese mobile poster for WeChat sharing
Primary request: Design a polished, complete Toastmasters event poster in Chinese. The poster must feel more like a finished premium training/event poster than a background template.
Reference direction: 清爽蓝白科技培训海报，右侧主讲人肖像，左侧大标题，结构化嘉宾介绍，“你将收获”四项收益，底部深蓝信息栏，图标精致，间距充足，高级但清晰。
Input image: Use the provided speaker portrait as the main person. Preserve recognizable facial structure, hairstyle, age, and professional business presence. Keep one person only.
Official brand/QR handling: You may create a polished Toastmasters-style top brand area and icon as part of the complete poster. Do not create any QR code. In the lower-left event bar, reserve one clean blank white square area for a real QR code overlay; do not draw a dashed frame, do not draw a fake QR, and do not write placeholder words such as “放置二维码” inside that blank square.
Top header layout: Put the Toastmasters-style icon on the top-left. Put “上海活力中文演讲俱乐部 / 第872次会议” directly to the right of that icon in the same compact header row or header area. Do not add a separate English brand slogan or generic Chinese tagline; the icon already communicates the Toastmasters brand. Do not repeat the club name and meeting number again above the main title.
Exact Chinese copy to include:
- 顶部品牌行: 上海活力中文演讲俱乐部 / 第872次会议
- 主标题: AI赋能演讲
- 副标题: 用智能工具放大表达、故事与影响力
- 分享嘉宾: 胡鹏飞
- 嘉宾身份: LMI全方位领导力教练顾问
- 嘉宾介绍: 10+马龄、活力中文前主席、国学头马创始官员；2026年度O2小区中英文演讲比赛双冠王。
- 你将收获:
- 掌握AI工具：高效生成演讲内容与PPT
- 提升演讲力：逻辑更清晰，表达更有力
- 激发创造力：拓展思维边界，让演讲更出彩
- 拥抱未来：与AI同行，成为更好的演讲者
- 时间: 2026年5月10日 周日 14:00-17:00
- 地点: 乌鲁木齐南路66号梧桐院邻里汇3号楼2楼（地铁1号线衡山路站4号口步行400米）
- 费用: 来宾35元 / 其他俱乐部会员25元 / 学生15元 / 角色免费
- 行动语: 扫码报名，一起开启表达之旅！
- 页脚: TOASTMASTERS 国际演讲俱乐部
Theme visual direction: 让设计强关联“AI赋能演讲”：AI 视觉应服务于公众演讲、沟通表达、内容生成和影响力提升，不要变成泛科幻背景。
Theme visual keywords: AI大脑线稿、电路线条、聊天气泡、麦克风、智能演示文稿、增长图表
Typography: Chinese text must be readable, high-contrast, and professionally aligned. Use bold dark-blue title typography, smaller clean body text, consistent spacing, no chaotic text blocks.
Hard constraints: no extra people, no distorted face, no fake QR code, no dashed QR placeholder frame, no QR placeholder text, no watermark, no random unreadable text, no unrelated icons.

Composition: Closest to the provided reference poster. Light blue-white gradient, right-side full-height speaker, left-side large title, mid-lower guest intro, four benefit cards, bottom deep-blue event bar.
Mood: clean, bright, credible, inviting, high-end public training poster.
```

保存为：`outputs/2026-05-10-meeting-872/candidate-ai-clean-1.png`

## candidate-ai-clean-2 高级杂志感完整海报

```text
Use case: ads-marketing
Asset type: complete 1080x1920 vertical Chinese mobile poster for WeChat sharing
Primary request: Design a polished, complete Toastmasters event poster in Chinese. The poster must feel more like a finished premium training/event poster than a background template.
Reference direction: 清爽蓝白科技培训海报，右侧主讲人肖像，左侧大标题，结构化嘉宾介绍，“你将收获”四项收益，底部深蓝信息栏，图标精致，间距充足，高级但清晰。
Input image: Use the provided speaker portrait as the main person. Preserve recognizable facial structure, hairstyle, age, and professional business presence. Keep one person only.
Official brand/QR handling: You may create a polished Toastmasters-style top brand area and icon as part of the complete poster. Do not create any QR code. In the lower-left event bar, reserve one clean blank white square area for a real QR code overlay; do not draw a dashed frame, do not draw a fake QR, and do not write placeholder words such as “放置二维码” inside that blank square.
Top header layout: Put the Toastmasters-style icon on the top-left. Put “上海活力中文演讲俱乐部 / 第872次会议” directly to the right of that icon in the same compact header row or header area. Do not add a separate English brand slogan or generic Chinese tagline; the icon already communicates the Toastmasters brand. Do not repeat the club name and meeting number again above the main title.
Exact Chinese copy to include:
- 顶部品牌行: 上海活力中文演讲俱乐部 / 第872次会议
- 主标题: AI赋能演讲
- 副标题: 用智能工具放大表达、故事与影响力
- 分享嘉宾: 胡鹏飞
- 嘉宾身份: LMI全方位领导力教练顾问
- 嘉宾介绍: 10+马龄、活力中文前主席、国学头马创始官员；2026年度O2小区中英文演讲比赛双冠王。
- 你将收获:
- 掌握AI工具：高效生成演讲内容与PPT
- 提升演讲力：逻辑更清晰，表达更有力
- 激发创造力：拓展思维边界，让演讲更出彩
- 拥抱未来：与AI同行，成为更好的演讲者
- 时间: 2026年5月10日 周日 14:00-17:00
- 地点: 乌鲁木齐南路66号梧桐院邻里汇3号楼2楼（地铁1号线衡山路站4号口步行400米）
- 费用: 来宾35元 / 其他俱乐部会员25元 / 学生15元 / 角色免费
- 行动语: 扫码报名，一起开启表达之旅！
- 页脚: TOASTMASTERS 国际演讲俱乐部
Theme visual direction: 让设计强关联“AI赋能演讲”：AI 视觉应服务于公众演讲、沟通表达、内容生成和影响力提升，不要变成泛科幻背景。
Theme visual keywords: AI大脑线稿、电路线条、聊天气泡、麦克风、智能演示文稿、增长图表
Typography: Chinese text must be readable, high-contrast, and professionally aligned. Use bold dark-blue title typography, smaller clean body text, consistent spacing, no chaotic text blocks.
Hard constraints: no extra people, no distorted face, no fake QR code, no dashed QR placeholder frame, no QR placeholder text, no watermark, no random unreadable text, no unrelated icons.

Composition: More premium editorial and spacious. Keep a refined light background, strong portrait presence, large title, and elegant theme-related visual metaphors. Information hierarchy must remain very clear.
Mood: executive, premium, modern, polished, still readable on mobile.
```

保存为：`outputs/2026-05-10-meeting-872/candidate-ai-clean-2.png`

## candidate-ai-clean-3 强主题传播吸睛版

```text
Use case: ads-marketing
Asset type: complete 1080x1920 vertical Chinese mobile poster for WeChat sharing
Primary request: Design a polished, complete Toastmasters event poster in Chinese. The poster must feel more like a finished premium training/event poster than a background template.
Reference direction: 清爽蓝白科技培训海报，右侧主讲人肖像，左侧大标题，结构化嘉宾介绍，“你将收获”四项收益，底部深蓝信息栏，图标精致，间距充足，高级但清晰。
Input image: Use the provided speaker portrait as the main person. Preserve recognizable facial structure, hairstyle, age, and professional business presence. Keep one person only.
Official brand/QR handling: You may create a polished Toastmasters-style top brand area and icon as part of the complete poster. Do not create any QR code. In the lower-left event bar, reserve one clean blank white square area for a real QR code overlay; do not draw a dashed frame, do not draw a fake QR, and do not write placeholder words such as “放置二维码” inside that blank square.
Top header layout: Put the Toastmasters-style icon on the top-left. Put “上海活力中文演讲俱乐部 / 第872次会议” directly to the right of that icon in the same compact header row or header area. Do not add a separate English brand slogan or generic Chinese tagline; the icon already communicates the Toastmasters brand. Do not repeat the club name and meeting number again above the main title.
Exact Chinese copy to include:
- 顶部品牌行: 上海活力中文演讲俱乐部 / 第872次会议
- 主标题: AI赋能演讲
- 副标题: 用智能工具放大表达、故事与影响力
- 分享嘉宾: 胡鹏飞
- 嘉宾身份: LMI全方位领导力教练顾问
- 嘉宾介绍: 10+马龄、活力中文前主席、国学头马创始官员；2026年度O2小区中英文演讲比赛双冠王。
- 你将收获:
- 掌握AI工具：高效生成演讲内容与PPT
- 提升演讲力：逻辑更清晰，表达更有力
- 激发创造力：拓展思维边界，让演讲更出彩
- 拥抱未来：与AI同行，成为更好的演讲者
- 时间: 2026年5月10日 周日 14:00-17:00
- 地点: 乌鲁木齐南路66号梧桐院邻里汇3号楼2楼（地铁1号线衡山路站4号口步行400米）
- 费用: 来宾35元 / 其他俱乐部会员25元 / 学生15元 / 角色免费
- 行动语: 扫码报名，一起开启表达之旅！
- 页脚: TOASTMASTERS 国际演讲俱乐部
Theme visual direction: 让设计强关联“AI赋能演讲”：AI 视觉应服务于公众演讲、沟通表达、内容生成和影响力提升，不要变成泛科幻背景。
Theme visual keywords: AI大脑线稿、电路线条、聊天气泡、麦克风、智能演示文稿、增长图表
Typography: Chinese text must be readable, high-contrast, and professionally aligned. Use bold dark-blue title typography, smaller clean body text, consistent spacing, no chaotic text blocks.
Hard constraints: no extra people, no distorted face, no fake QR code, no dashed QR placeholder frame, no QR placeholder text, no watermark, no random unreadable text, no unrelated icons.

Composition: Stronger theme expression. Add tasteful visual elements from the configured theme keywords around the speaker, while preserving readable blocks for all event copy.
Mood: memorable, energetic, intelligent, premium, optimized for attracting attention in WeChat feeds.
```

保存为：`outputs/2026-05-10-meeting-872/candidate-ai-clean-3.png`
