# Brand Specification · leiping.dev 产品矩阵品牌资产规范

本文档为 `leiping.dev` 枢纽页面及四大核心产品的品牌资产核准清单与互链规范。

## 0. 枢纽站点定位 (Hub Site)
- **品牌名称**：雷平 · Perry Lei (Perry Studio / leiping.dev)
- **根域名**：`https://leiping.dev`
- **定位**：独立开发者、系统架构师的产品矩阵与技术发布中心
- **SEO 角色**：矩阵顶层根枢纽 (Canonical Root Hub)。为所有子域与独立品牌域名提供高权重、无损 dofollow 权威流动，并构建互通的实体拓扑结构。

---

## 1. 拾页 (Shiye)
- **官方域名**：`https://shiye.leiping.dev`
- **形态**：Web App (Next.js 14) + iOS App + Worker 流水线
- **品牌口号**：一页互动学习手账 · 家长为孩子生成的智能学习伴侣
- **核心定位**：将复杂课本章节与考点智能解析提炼为一张标准 A4 互动手账，支持免登录分享与孩子端无干扰作答。
- **品牌色彩**：
  - 主色（陶土红）：`#C4552D`
  - 强调金（纸面金）：`#E8A13C`
  - 纸面底色：`#FFF8EC`
- **视觉符号**：页签 / Bookmark（一页折角方形纸，内嵌短书签，末端 V 形缺口，方块轮廓始终闭合）。
- **Dofollow 锚点策略**：
  - 主链接：`https://shiye.leiping.dev` (文本: 拾页 · 互动学习手账)
  - 辅助锚点：课本知识点提炼、A4手账生成器、家长端控制台

---

## 2. WordHub
- **官方域名**：`https://wordhub.top`
- **形态**：Web (Next.js) + macOS 原生桌面端 (SwiftUI) + iOS + 浏览器扩展 (WXT)
- **品牌口号**：全面的英语与语言深度学习平台 · 词源与词汇网络
- **核心定位**：以词源学 (Etymology) 和 WordNet 认知网络为基石，结合语境记忆法与跨设备无缝同步，让深度英语研习者真正吃透词汇脉络。
- **品牌色彩**：
  - 主色（深邃蓝）：`#2563EB` / `#1D4ED8`
  - 辅色（认知绿）：`#10B981`
  - 背景：深石墨 `#0F172A` / 纯净学术白 `#F8FAFC`
- **视觉符号**：星系词汇互联网络徽标。
- **Dofollow 锚点策略**：
  - 主链接：`https://wordhub.top` (文本: WordHub · 词源与深度语言学习平台)
  - 辅助锚点：词源溯源词典 (Etymology Explorer)、WordNet 词网、macOS 词汇伴侣

---

## 3. TOTPBOX
- **官方域名**：`https://www.totpbox.com`
- **形态**：浏览器扩展 (Chrome / Edge / Firefox - WXT MV3) + Web 控制台
- **品牌口号**：Local-First 2FA Authenticator & Passkey Companion
- **核心定位**：本地优先、零知识架构的身份验证伴侣。全本地 AES-256-GCM 强加密，无主密码泄露风险，提供极速自动填充并平滑引导升级至现代 Passkeys。
- **品牌色彩**：
  - 主色（极客曜黑）：`#090D16` / `#0F172A`
  - 辅色（安全金）：`#F59E0B` / `#D97706`
  - 安全绿：`#10B981`
- **视觉符号**：盾牌与安全钥匙孔徽标。
- **Dofollow 锚点策略**：
  - 主链接：`https://www.totpbox.com` (文本: TOTPBOX · 本地加密双因素认证与 Passkey 助手)
  - 辅助锚点：Chrome 应用商店下载、零知识安全架构白皮书

---

## 4. CogniSphere
- **官方域名**：`https://cognisphere.leiping.dev`
- **形态**：浏览器扩展 (Chrome / Edge / Firefox - WXT React 19) + 官网
- **品牌口号**：Ask any page a question · 网页深度伴读与即时 AI 问答
- **核心定位**：常驻浏览器侧边栏的智能阅读辅助。划词即解、全页提炼研读，支持 BYOK (Gemini, Claude, OpenAI, DeepSeek, Ollama) 及 Chrome 内置端侧本地模型。
- **品牌色彩**：
  - 主色（电光蓝）：`#3266F1`
  - 辅色（智识紫）：`#6366F1`
  - 背景：冷钛灰 `#111827`
- **视觉符号**：认知星球微光徽标。
- **Dofollow 锚点策略**：
  - 主链接：`https://cognisphere.leiping.dev` (文本: CogniSphere · 智能网页伴读与 AI 问答)
  - 辅助锚点：Chrome Web Store 扩展直达、BYOK 多模型配置指南

---

## 5. Dofollow 互链矩阵规范 (Reciprocal Linking Policy)
1. **纯净标准语义**：所有外链严格采用 `<a href="..." target="_blank" rel="noopener">`，坚决不含 `nofollow`、`ugc` 或 `sponsored` 属性。
2. **上下文丰富性**：每个产品均配置清晰的富文本描述段落与结构化标签，使搜索引擎明确判断出同属开发者个人的产品矩阵（Software Applications Portfolio）。
3. **结构化数据加持**：页面头部内嵌 Schema.org 的 `WebSite` 与 `ItemList`（含每个子产品的 `SoftwareApplication` 实体），将矩阵拓扑关系语义化固化给 Google 与各类 AI 搜索引擎。
