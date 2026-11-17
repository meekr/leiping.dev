import os
import base64
import json
import asyncio
from playwright.async_api import async_playwright

BASE_DIR = '/Users/perrylei/repos/leiping.dev/design-demos'
os.makedirs(BASE_DIR, exist_ok=True)
SCREENSHOTS_DIR = os.path.join(BASE_DIR, 'screenshots')
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

# 1. Load brand assets
with open('/Users/perrylei/repos/Shiye/packages/ui/assets/brand/shiye-mark.svg') as f:
    shiye_svg = f.read().strip()

with open('/Users/perrylei/repos/CogniSphere/design/icon.svg') as f:
    cogni_svg = f.read().strip()

with open('/Users/perrylei/repos/TOTPBOX/apps/web/public/logo.png', 'rb') as f:
    totp_b64 = 'data:image/png;base64,' + base64.b64encode(f.read()).decode('utf-8')

with open('/Users/perrylei/repos/WordHub/apps/web/public/logo.png', 'rb') as f:
    wordhub_b64 = 'data:image/png;base64,' + base64.b64encode(f.read()).decode('utf-8')

# Common structured data JSON-LD (Schema.org)
schema_json = json.dumps({
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "Person",
            "@id": "https://leiping.dev/#creator",
            "name": "Perry Lei",
            "alternateName": "雷平",
            "url": "https://leiping.dev",
            "sameAs": [
                "https://github.com/perrylei"
            ],
            "jobTitle": "Independent Software Engineer & Product Architect"
        },
        {
            "@type": "WebSite",
            "@id": "https://leiping.dev/#website",
            "url": "https://leiping.dev",
            "name": "雷平的产品矩阵 · Perry Lei Studio",
            "description": "雷平 (Perry Lei) 的个人产品矩阵与工程主页。涵盖互动学习手账、词源语言研习、本地隐私安全与 AI 网页伴读。",
            "publisher": {"@id": "https://leiping.dev/#creator"}
        },
        {
            "@type": "ItemList",
            "@id": "https://leiping.dev/#products",
            "name": "Perry Lei Product Matrix",
            "itemListElement": [
                {
                    "@type": "SoftwareApplication",
                    "position": 1,
                    "name": "拾页 (Shiye)",
                    "url": "https://shiye.leiping.dev",
                    "applicationCategory": "EducationalApplication",
                    "operatingSystem": "Web, iOS",
                    "description": "家长为孩子生成的一页互动学习手账。课本考点智能解析与无干扰互动学习。"
                },
                {
                    "@type": "SoftwareApplication",
                    "position": 2,
                    "name": "WordHub",
                    "url": "https://wordhub.top",
                    "applicationCategory": "EducationalApplication",
                    "operatingSystem": "Web, macOS, iOS, Extension",
                    "description": "全面的英语与语言深度学习平台。以词源学 (Etymology) 和 WordNet 认知网络为基石。"
                },
                {
                    "@type": "SoftwareApplication",
                    "position": 3,
                    "name": "TOTPBOX",
                    "url": "https://www.totpbox.com",
                    "applicationCategory": "SecurityApplication",
                    "operatingSystem": "Chrome, Edge, Web",
                    "description": "Local-First 2FA 认证与 Passkey 助手。零知识架构、AES-256-GCM 本地加密保险库。"
                },
                {
                    "@type": "SoftwareApplication",
                    "position": 4,
                    "name": "CogniSphere",
                    "url": "https://cognisphere.leiping.dev",
                    "applicationCategory": "BrowserExtension",
                    "operatingSystem": "Chrome, Edge, Firefox, Web",
                    "description": "网页深度伴读与即时 AI 问答扩展。划词即解、全页研读，支持 BYOK 与端侧模型。"
                }
            ]
        }
    ]
}, ensure_ascii=False, indent=2)

# ==============================================================================
# DIRECTION 1: Editorial Swiss (经典出版物与工坊档案 · 浅色暖纸底 + 衬线大标题)
# ==============================================================================
html_dir1 = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>雷平 · Perry Lei — 软件矩阵与工坊档案</title>
  <meta name="description" content="雷平 (Perry Lei) 的个人产品矩阵与工程主页。涵盖拾页 (Shiye)、WordHub、TOTPBOX、CogniSphere，所有产品统一构建、独立演进。">
  <script type="application/ld+json">
{schema_json}
  </script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg: #f8f6f0;
      --card-bg: #ffffff;
      --border: #e3ded5;
      --border-dark: #222222;
      --text: #1a1a1a;
      --text-muted: #595550;
      --text-subtle: #6e675f;
      --accent: #b8441f;
      --font-display: 'Instrument Serif', Georgia, serif;
      --font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    }}
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    body {{
      background-color: var(--bg);
      color: var(--text);
      font-family: var(--font-sans);
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
      padding: 0 2rem 5rem;
    }}
    .sheet {{
      max-width: 980px;
      margin: 3rem auto 0;
      background: var(--card-bg);
      border: 1px solid var(--border);
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
      border-radius: 4px;
      padding: 4rem 4.5rem;
    }}
    header {{
      border-bottom: 2px solid var(--border-dark);
      padding-bottom: 2.5rem;
      margin-bottom: 3.5rem;
    }}
    .masthead-meta {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.9rem;
      letter-spacing: 0.05em;
      color: var(--text-muted);
      text-transform: uppercase;
      margin-bottom: 1.5rem;
      font-weight: 600;
    }}
    .masthead-title {{
      font-family: var(--font-display);
      font-size: 3.75rem;
      line-height: 1.08;
      font-weight: 400;
      color: #111;
      margin-bottom: 1.25rem;
      letter-spacing: -0.01em;
    }}
    .masthead-lead {{
      font-size: 1.15rem;
      color: var(--text-muted);
      max-width: 720px;
      line-height: 1.65;
    }}
    .matrix-catalog {{
      display: flex;
      flex-direction: column;
      gap: 2.5rem;
    }}
    .product-entry {{
      display: grid;
      grid-template-columns: 80px 1fr 200px;
      gap: 2rem;
      align-items: start;
      padding-bottom: 2.5rem;
      border-bottom: 1px solid var(--border);
    }}
    .product-entry:last-child {{
      border-bottom: none;
      padding-bottom: 0;
    }}
    .entry-mark {{
      width: 80px;
      height: 80px;
      border-radius: 8px;
      border: 1px solid var(--border);
      background: #faf8f5;
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
    }}
    .entry-mark svg,
    .entry-mark img {{
      width: 56px;
      height: 56px;
      object-fit: contain;
    }}
    .entry-body {{
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
    }}
    .entry-title {{
      font-family: var(--font-display);
      font-size: 2.2rem;
      font-weight: 400;
      color: #111;
      line-height: 1.2;
    }}
    .entry-desc {{
      font-size: 1rem;
      color: var(--text-muted);
      line-height: 1.6;
    }}
    .entry-meta-tags {{
      display: flex;
      gap: 0.75rem;
      flex-wrap: wrap;
      margin-top: 0.25rem;
    }}
    .meta-tag {{
      font-size: 0.875rem;
      color: var(--text-subtle);
      background: #f4efe8;
      padding: 0.25rem 0.65rem;
      border-radius: 3px;
      font-weight: 500;
    }}
    .entry-link-col {{
      display: flex;
      flex-direction: column;
      align-items: flex-end;
      gap: 0.75rem;
    }}
    .primary-link {{
      display: inline-block;
      font-size: 1rem;
      font-weight: 700;
      color: #111;
      text-decoration: underline;
      text-underline-offset: 4px;
      transition: color 0.15s;
    }}
    .primary-link:hover {{
      color: var(--accent);
    }}
    .canonical-badge {{
      font-size: 0.8125rem;
      color: #1a7f37;
      background: #eefbe8;
      padding: 0.25rem 0.6rem;
      border-radius: 3px;
      font-weight: 600;
      border: 1px solid #d4edd2;
    }}
    .synergy-box {{
      margin-top: 4rem;
      background: #faf8f5;
      border: 1px solid var(--border);
      border-radius: 4px;
      padding: 2.25rem;
    }}
    .synergy-title {{
      font-family: var(--font-display);
      font-size: 1.75rem;
      font-weight: 400;
      color: #111;
      margin-bottom: 0.5rem;
    }}
    .synergy-p {{
      font-size: 1rem;
      color: var(--text-muted);
      line-height: 1.6;
      margin-bottom: 1.5rem;
    }}
    .synergy-links {{
      display: flex;
      flex-wrap: wrap;
      gap: 1.5rem;
      font-size: 1rem;
    }}
    .synergy-links a {{
      color: #111;
      font-weight: 600;
      text-decoration: none;
      border-bottom: 1px solid #777;
      padding-bottom: 2px;
      transition: all 0.15s;
    }}
    .synergy-links a:hover {{
      color: var(--accent);
      border-bottom-color: var(--accent);
    }}
    footer {{
      margin-top: 3.5rem;
      padding-top: 2rem;
      border-top: 1px solid var(--border);
      display: flex;
      justify-content: space-between;
      color: var(--text-subtle);
      font-size: 0.9rem;
    }}
    @media (max-width: 820px) {{
      .sheet {{
        padding: 2.5rem 1.75rem;
        margin-top: 1.5rem;
      }}
      .masthead-title {{
        font-size: 2.5rem;
      }}
      .product-entry {{
        grid-template-columns: 1fr;
        gap: 1.25rem;
      }}
      .entry-link-col {{
        align-items: flex-start;
      }}
      footer {{
        flex-direction: column;
        gap: 0.75rem;
      }}
    }}
  </style>
</head>
<body>
  <div class="sheet">
    <header>
      <div class="masthead-meta">
        <div>Perry Lei Studio Archive</div>
        <div>Volume I · Issue 2026</div>
      </div>
      <h1 class="masthead-title">Crafting Tools for Thought & Privacy.</h1>
      <p class="masthead-lead">雷平 (Perry Lei) 的个人产品矩阵与工程主页。秉持工匠精神，打造解决真实问题的高完成度软件：涵盖一页互动学习手账、词源语言研习网络、本地零知识安全保险库与端侧智能伴读。本站作为枢纽，向全矩阵输出标准 Dofollow 互链。</p>
    </header>

    <main class="matrix-catalog">
      <!-- 拾页 Shiye -->
      <article class="product-entry">
        <div class="entry-mark" style="background: #fff8ec;">
          {shiye_svg}
        </div>
        <div class="entry-body">
          <h2 class="entry-title">拾页 · Shiye</h2>
          <p class="entry-desc">家长为孩子生成的一页互动学习手账。提炼教材考点与认知线索，一键排版 A4 纸张手账，免登录分享链接交付孩子端沉浸作答。</p>
          <div class="entry-meta-tags">
            <span class="meta-tag">Web App (Next.js 14)</span>
            <span class="meta-tag">iOS 客户端</span>
            <span class="meta-tag">BullMQ 异步流水线</span>
            <span class="meta-tag">PostgreSQL</span>
          </div>
        </div>
        <div class="entry-link-col">
          <a href="https://shiye.leiping.dev" class="primary-link" target="_blank" rel="noopener">shiye.leiping.dev ↗</a>
          <span class="canonical-badge">Dofollow Canonical</span>
        </div>
      </article>

      <!-- WordHub -->
      <article class="product-entry">
        <div class="entry-mark">
          <img src="{wordhub_b64}" alt="WordHub">
        </div>
        <div class="entry-body">
          <h2 class="entry-title">WordHub</h2>
          <p class="entry-desc">全面的英语与语言深度学习平台。以词源学 (Etymology) 和 WordNet 认知网络为基石，结合语境记忆法与跨设备无缝同步，让每一次查词都成为认知跃迁。</p>
          <div class="entry-meta-tags">
            <span class="meta-tag">macOS 原生 (SwiftUI)</span>
            <span class="meta-tag">iOS 移动端</span>
            <span class="meta-tag">Next.js Web 端</span>
            <span class="meta-tag">WordNet 3.1 词网</span>
          </div>
        </div>
        <div class="entry-link-col">
          <a href="https://wordhub.top" class="primary-link" target="_blank" rel="noopener">wordhub.top ↗</a>
          <span class="canonical-badge">Dofollow Canonical</span>
        </div>
      </article>

      <!-- TOTPBOX -->
      <article class="product-entry">
        <div class="entry-mark">
          <img src="{totp_b64}" alt="TOTPBOX">
        </div>
        <div class="entry-body">
          <h2 class="entry-title">TOTPBOX</h2>
          <p class="entry-desc">本地优先的双因素认证助手与 Passkey 伴侣。零知识架构，全本地 AES-256-GCM 强加密保险库，拒绝主密码上云泄露，极速自动填充并平滑升级通行密钥。</p>
          <div class="entry-meta-tags">
            <span class="meta-tag">Chrome & Edge MV3</span>
            <span class="meta-tag">Zero-Knowledge</span>
            <span class="meta-tag">AES-256-GCM 加密</span>
            <span class="meta-tag">WebAuthn 通行密钥</span>
          </div>
        </div>
        <div class="entry-link-col">
          <a href="https://www.totpbox.com" class="primary-link" target="_blank" rel="noopener">totpbox.com ↗</a>
          <span class="canonical-badge">Dofollow Canonical</span>
        </div>
      </article>

      <!-- CogniSphere -->
      <article class="product-entry">
        <div class="entry-mark" style="background: #111827;">
          {cogni_svg}
        </div>
        <div class="entry-body">
          <h2 class="entry-title">CogniSphere</h2>
          <p class="entry-desc">常驻浏览器侧边栏的智能阅读辅助。划词即解、全页提炼研读，支持 BYOK (Gemini, Claude, DeepSeek, Ollama) 及 Chrome 内置端侧本地大模型。</p>
          <div class="entry-meta-tags">
            <span class="meta-tag">React 19 & Tailwind v4</span>
            <span class="meta-tag">WXT 扩展框架</span>
            <span class="meta-tag">BYOK 多模型接入</span>
            <span class="meta-tag">Chrome Nano 端侧 AI</span>
          </div>
        </div>
        <div class="entry-link-col">
          <a href="https://cognisphere.leiping.dev" class="primary-link" target="_blank" rel="noopener">cognisphere.leiping.dev ↗</a>
          <span class="canonical-badge">Dofollow Canonical</span>
        </div>
      </article>
    </main>

    <section class="synergy-box">
      <h3 class="synergy-title">矩阵权威分发网络 (Cross-Product Synergy)</h3>
      <p class="synergy-p">本站作为雷平个人技术资产与软件矩阵的唯一根域名 (Canonical Hub)，向每个子产品永久注入权威 Dofollow 外部反向链接，助力新产品冷启动与长期 SEO 权重积累。</p>
      <div class="synergy-links">
        <a href="https://shiye.leiping.dev" target="_blank" rel="noopener">拾页 · 互动学习手账 ↗</a>
        <a href="https://wordhub.top" target="_blank" rel="noopener">WordHub · 词源与词汇网络 ↗</a>
        <a href="https://www.totpbox.com" target="_blank" rel="noopener">TOTPBOX · 2FA与通行密钥 ↗</a>
        <a href="https://cognisphere.leiping.dev" target="_blank" rel="noopener">CogniSphere · 网页AI伴读 ↗</a>
      </div>
    </section>

    <footer>
      <div>© 2026 Perry Lei (雷平). 保留所有权利.</div>
      <div>根域名: leiping.dev · 架构与产品工坊</div>
    </footer>
  </div>
</body>
</html>
"""

with open(os.path.join(BASE_DIR, 'direction-1-studio-index.html'), 'w') as f:
    f.write(html_dir1)

# ==============================================================================
# DIRECTION 2: Modern Dark Bento (独立创作者深色便当展厅 · Apple设计奖质感)
# ==============================================================================
html_dir2 = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Perry Studio · 雷平的产品工坊</title>
  <meta name="description" content="雷平的独立软件工坊与精选产品矩阵。探寻 AI 伴读、词源网络、安全隐私与启发式学习的精妙结合。">
  <script type="application/ld+json">
{schema_json}
  </script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700;12..96,800&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg: #090c10;
      --card-bg: rgba(22, 27, 34, 0.75);
      --border: rgba(255, 255, 255, 0.1);
      --border-hover: rgba(255, 255, 255, 0.28);
      --text: #f0f6fc;
      --text-muted: #9ba5b2;
      --shiye-accent: #c4552d;
      --wordhub-blue: #3b82f6;
      --totp-gold: #f59e0b;
      --cogni-indigo: #6366f1;
      --font-display: 'Bricolage Grotesque', sans-serif;
      --font-sans: 'Plus Jakarta Sans', -apple-system, sans-serif;
    }}
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    body {{
      background-color: var(--bg);
      background-image: 
        radial-gradient(circle at 15% 15%, rgba(59, 130, 246, 0.14) 0%, transparent 40%),
        radial-gradient(circle at 85% 75%, rgba(196, 85, 45, 0.12) 0%, transparent 45%);
      color: var(--text);
      font-family: var(--font-sans);
      padding: 0 1.5rem 5rem;
      min-height: 100vh;
      -webkit-font-smoothing: antialiased;
    }}
    .wrap {{
      max-width: 1080px;
      margin: 0 auto;
    }}
    .top-bar {{
      padding: 3rem 0 2rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid var(--border);
    }}
    .brand-mark {{
      font-weight: 800;
      font-size: 1.25rem;
      letter-spacing: -0.02em;
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }}
    .brand-avatar {{
      width: 36px;
      height: 36px;
      border-radius: 10px;
      background: linear-gradient(135deg, #3b82f6, #8b5cf6);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.95rem;
      font-weight: 700;
      color: #fff;
    }}
    .hero {{
      text-align: center;
      padding: 4.5rem 1rem 3.5rem;
      max-width: 820px;
      margin: 0 auto;
    }}
    .hero-badge {{
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      background: rgba(255,255,255,0.06);
      border: 1px solid rgba(255,255,255,0.15);
      padding: 0.4rem 1.15rem;
      border-radius: 9999px;
      font-size: 0.875rem;
      color: #cbd5e1;
      margin-bottom: 1.5rem;
      backdrop-filter: blur(8px);
    }}
    .hero h1 {{
      font-family: var(--font-display);
      font-size: 3.25rem;
      font-weight: 800;
      line-height: 1.15;
      letter-spacing: -0.03em;
      margin-bottom: 1.25rem;
      color: #ffffff;
    }}
    .hero p {{
      font-size: 1.2rem;
      color: var(--text-muted);
      line-height: 1.6;
    }}

    .bento-grid {{
      display: grid;
      grid-template-columns: repeat(12, 1fr);
      gap: 1.5rem;
      margin-top: 1rem;
    }}
    .bento-card {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 20px;
      padding: 2.25rem;
      backdrop-filter: blur(16px);
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      position: relative;
      overflow: hidden;
    }}
    .bento-card:hover {{
      border-color: var(--border-hover);
      transform: translateY(-4px);
      box-shadow: 0 20px 40px -15px rgba(0,0,0,0.6);
    }}
    .col-7 {{ grid-column: span 7; }}
    .col-5 {{ grid-column: span 5; }}
    .col-6 {{ grid-column: span 6; }}

    .card-glow {{
      position: absolute;
      top: 0;
      right: 0;
      width: 220px;
      height: 220px;
      border-radius: 50%;
      filter: blur(80px);
      pointer-events: none;
      opacity: 0.25;
    }}
    .bento-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 1.5rem;
    }}
    .bento-icon {{
      width: 60px;
      height: 60px;
      border-radius: 14px;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
      border: 1px solid rgba(255,255,255,0.15);
      box-shadow: 0 4px 12px rgba(0,0,0,0.25);
    }}
    .bento-icon svg, .bento-icon img {{
      width: 44px;
      height: 44px;
      object-fit: contain;
    }}
    .bento-link {{
      color: #fff;
      background: rgba(255,255,255,0.08);
      border: 1px solid rgba(255,255,255,0.15);
      width: 40px;
      height: 40px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      text-decoration: none;
      font-size: 1.1rem;
      transition: all 0.2s;
    }}
    .bento-link:hover {{
      background: #fff;
      color: #000;
      transform: scale(1.08);
    }}
    .bento-title-row {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
      margin-bottom: 0.5rem;
      flex-wrap: wrap;
    }}
    .bento-title {{
      font-family: var(--font-display);
      font-size: 1.75rem;
      font-weight: 700;
      color: #fff;
    }}
    .bento-badge {{
      font-size: 0.8125rem;
      padding: 0.25rem 0.65rem;
      border-radius: 9999px;
      font-weight: 600;
    }}
    .bento-desc {{
      color: var(--text-muted);
      font-size: 1.05rem;
      line-height: 1.6;
      margin-bottom: 1.75rem;
    }}
    .bento-preview {{
      background: rgba(0,0,0,0.35);
      border: 1px solid rgba(255,255,255,0.08);
      border-radius: 12px;
      padding: 1rem 1.25rem;
      font-size: 0.875rem;
      display: flex;
      align-items: center;
      gap: 0.75rem;
      margin-top: auto;
      flex-wrap: wrap;
    }}
    .synergy-banner {{
      margin-top: 2.5rem;
      background: linear-gradient(90deg, rgba(59,130,246,0.12), rgba(196,85,45,0.12));
      border: 1px solid rgba(255,255,255,0.12);
      border-radius: 20px;
      padding: 2.25rem 2.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 1.5rem;
    }}
    .synergy-text h3 {{
      font-family: var(--font-display);
      font-size: 1.4rem;
      font-weight: 700;
      margin-bottom: 0.35rem;
      color: #fff;
    }}
    .synergy-text p {{
      color: var(--text-muted);
      font-size: 1rem;
    }}
    .synergy-pills {{
      display: flex;
      gap: 0.75rem;
      flex-wrap: wrap;
    }}
    .synergy-pills a {{
      color: #fff;
      text-decoration: none;
      font-size: 0.95rem;
      font-weight: 600;
      padding: 0.6rem 1.15rem;
      background: rgba(255,255,255,0.08);
      border: 1px solid rgba(255,255,255,0.18);
      border-radius: 8px;
      transition: all 0.15s;
    }}
    .synergy-pills a:hover {{
      background: #fff;
      color: #090c10;
    }}
    footer {{
      margin-top: 5rem;
      text-align: center;
      color: var(--text-muted);
      font-size: 0.95rem;
      border-top: 1px solid var(--border);
      padding-top: 2.5rem;
    }}
    @media (max-width: 860px) {{
      .col-7, .col-5, .col-6 {{
        grid-column: span 12;
      }}
      .hero h1 {{
        font-size: 2.4rem;
      }}
    }}
  </style>
</head>
<body>
  <div class="wrap">
    <nav class="top-bar">
      <div class="brand-mark">
        <div class="brand-avatar">L</div>
        <span>雷平 · Perry Lei</span>
      </div>
      <div style="font-size: 0.95rem; color: var(--text-muted);">
        leiping.dev // Product Atelier
      </div>
    </nav>

    <header class="hero">
      <div class="hero-badge">
        <span>独立匠心矩阵 · 100% Dofollow 互通</span>
      </div>
      <h1>用工匠的精神，雕琢每一个数字工具。</h1>
      <p>从课本一页纸手账，到词源深度研习，再到本地加密保险库与智能网页伴读。每一款软件都解决真实的痛点，守护数字自主。</p>
    </header>

    <main class="bento-grid">
      <!-- 1. WordHub (Col-7 Big Card) -->
      <article class="bento-card col-7">
        <div class="card-glow" style="background: var(--wordhub-blue);"></div>
        <div>
          <div class="bento-header">
            <div class="bento-icon" style="background: #0f172a;">
              <img src="{wordhub_b64}" alt="WordHub">
            </div>
            <a href="https://wordhub.top" class="bento-link" target="_blank" rel="noopener" title="访问 WordHub (dofollow)">↗</a>
          </div>
          <div class="bento-title-row">
            <h2 class="bento-title">WordHub</h2>
            <span class="bento-badge" style="background: rgba(59,130,246,0.25); color: #93c5fd;">词源与全端词网</span>
          </div>
          <p class="bento-desc">全面的英语与语言深度学习平台。以词源学 (Etymology) 和 WordNet 认知网络为基石，结合语境记忆法与跨设备无缝同步，让每一次查词都成为一次认知跃升。</p>
        </div>
        <div class="bento-preview">
          <span style="color: #93c5fd; font-weight: 600;">WordNet 3.1 词网</span>
          <span style="color: var(--text-muted);">/</span>
          <span>macOS 原生客户端</span>
          <span style="color: var(--text-muted);">/</span>
          <span>iOS 移动伴读</span>
          <a href="https://wordhub.top" target="_blank" rel="noopener" style="color: #93c5fd; text-decoration: none; margin-left: auto; font-weight: 600;">wordhub.top ↗</a>
        </div>
      </article>

      <!-- 2. 拾页 Shiye (Col-5 Card) -->
      <article class="bento-card col-5">
        <div class="card-glow" style="background: var(--shiye-accent);"></div>
        <div>
          <div class="bento-header">
            <div class="bento-icon" style="background: #fff8ec;">
              {shiye_svg}
            </div>
            <a href="https://shiye.leiping.dev" class="bento-link" target="_blank" rel="noopener" title="访问 拾页 (dofollow)">↗</a>
          </div>
          <div class="bento-title-row">
            <h2 class="bento-title">拾页 Shiye</h2>
            <span class="bento-badge" style="background: rgba(196,85,45,0.25); color: #fdba74;">一页互动手账</span>
          </div>
          <p class="bento-desc">家长为孩子生成的一页互动学习手账。提炼课本核心考点，一键生成 A4 纸张排版手账，免登录链接交付孩子沉浸学习。</p>
        </div>
        <div class="bento-preview">
          <span style="color: #fdba74; font-weight: 600;">A4 手账生成器</span>
          <span style="color: var(--text-muted);">/</span>
          <span>孩子端免登录</span>
          <a href="https://shiye.leiping.dev" target="_blank" rel="noopener" style="color: #fdba74; text-decoration: none; margin-left: auto; font-weight: 600;">shiye.leiping.dev ↗</a>
        </div>
      </article>

      <!-- 3. TOTPBOX (Col-6 Card) -->
      <article class="bento-card col-6">
        <div class="card-glow" style="background: var(--totp-gold);"></div>
        <div>
          <div class="bento-header">
            <div class="bento-icon" style="background: #0f172a;">
              <img src="{totp_b64}" alt="TOTPBOX">
            </div>
            <a href="https://www.totpbox.com" class="bento-link" target="_blank" rel="noopener" title="访问 TOTPBOX (dofollow)">↗</a>
          </div>
          <div class="bento-title-row">
            <h2 class="bento-title">TOTPBOX</h2>
            <span class="bento-badge" style="background: rgba(245,158,11,0.25); color: #fde047;">本地零知识 2FA</span>
          </div>
          <p class="bento-desc">零知识架构的现代身份验证伴侣。全本地 AES-256-GCM 强加密，拒绝云端主密码泄露，自动填充验证码，平滑过渡至通行密钥 (Passkeys)。</p>
        </div>
        <div class="bento-preview">
          <span style="color: #fde047; font-weight: 600;">AES-256 本地保险库</span>
          <span style="color: var(--text-muted);">/</span>
          <span>Chrome MV3 扩展</span>
          <a href="https://www.totpbox.com" target="_blank" rel="noopener" style="color: #fde047; text-decoration: none; margin-left: auto; font-weight: 600;">totpbox.com ↗</a>
        </div>
      </article>

      <!-- 4. CogniSphere (Col-6 Card) -->
      <article class="bento-card col-6">
        <div class="card-glow" style="background: var(--cogni-indigo);"></div>
        <div>
          <div class="bento-header">
            <div class="bento-icon" style="background: #111827;">
              {cogni_svg}
            </div>
            <a href="https://cognisphere.leiping.dev" class="bento-link" target="_blank" rel="noopener" title="访问 CogniSphere (dofollow)">↗</a>
          </div>
          <div class="bento-title-row">
            <h2 class="bento-title">CogniSphere</h2>
            <span class="bento-badge" style="background: rgba(99,102,241,0.25); color: #c7d2fe;">网页伴读与 AI 问答</span>
          </div>
          <p class="bento-desc">常驻浏览器侧边栏的认知放大器。划词即解、全页提炼问答。自带密钥自由调用 Gemini、Claude、OpenAI、DeepSeek，或零成本运行端侧本地模型。</p>
        </div>
        <div class="bento-preview">
          <span style="color: #c7d2fe; font-weight: 600;">BYOK 自带 Key</span>
          <span style="color: var(--text-muted);">/</span>
          <span>Chrome 本地端侧大模型</span>
          <a href="https://cognisphere.leiping.dev" target="_blank" rel="noopener" style="color: #c7d2fe; text-decoration: none; margin-left: auto; font-weight: 600;">cognisphere.leiping.dev ↗</a>
        </div>
      </article>
    </main>

    <section class="synergy-banner">
      <div class="synergy-text">
        <h3>全域产品 Dofollow 互联网络</h3>
        <p>所有产品均由雷平独立架构与维护，彼此 dofollow 互链，构建高信誉软件矩阵网络。</p>
      </div>
      <div class="synergy-pills">
        <a href="https://shiye.leiping.dev" target="_blank" rel="noopener">拾页 Shiye ↗</a>
        <a href="https://wordhub.top" target="_blank" rel="noopener">WordHub ↗</a>
        <a href="https://www.totpbox.com" target="_blank" rel="noopener">TOTPBOX ↗</a>
        <a href="https://cognisphere.leiping.dev" target="_blank" rel="noopener">CogniSphere ↗</a>
      </div>
    </section>

    <footer>
      <p>© 2026 雷平 (Perry Lei). 雕琢于生活与代码之间 · leiping.dev 矩阵中枢</p>
    </footer>
  </div>
</body>
</html>
"""

with open(os.path.join(BASE_DIR, 'direction-2-digital-bento.html'), 'w') as f:
    f.write(html_dir2)

# ==============================================================================
# DIRECTION 3: Obsidian Cyber Terminal (先锋黑曜石终端 · Cyber-Luxe Console)
# ==============================================================================
html_dir3 = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>LEIPING.DEV // PERRY LEI SOFTWARE MATRIX</title>
  <meta name="description" content="Obsidian Matrix Console. Real-time index of Perry Lei's distributed product ecosystem: Shiye, WordHub, TOTPBOX, CogniSphere.">
  <script type="application/ld+json">
{schema_json}
  </script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg: #040608;
      --panel: #0a0e14;
      --border: #1a2332;
      --border-bright: #2d3b52;
      --neon-cyan: #00f0ff;
      --neon-green: #00ff9d;
      --neon-amber: #ffb800;
      --text: #f0f4f8;
      --text-dim: #9aa5b5;
      --font-mono: 'JetBrains Mono', monospace;
      --font-display: 'Space Grotesk', -apple-system, sans-serif;
    }}
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    body {{
      background-color: var(--bg);
      background-image: 
        linear-gradient(rgba(0, 240, 255, 0.04) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0, 240, 255, 0.04) 1px, transparent 1px);
      background-size: 32px 32px;
      color: var(--text);
      font-family: var(--font-mono);
      min-height: 100vh;
      padding: 2.5rem 1.5rem 5rem;
      -webkit-font-smoothing: antialiased;
    }}
    .terminal-window {{
      max-width: 1040px;
      margin: 0 auto;
      border: 1px solid var(--border);
      border-radius: 8px;
      background: rgba(10, 14, 20, 0.96);
      box-shadow: 0 0 50px rgba(0, 240, 255, 0.08);
      overflow: hidden;
    }}
    .window-header {{
      background: #080c10;
      border-bottom: 1px solid var(--border);
      padding: 0.9rem 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.875rem;
      color: var(--text-dim);
    }}
    .window-controls {{
      display: flex;
      gap: 0.5rem;
    }}
    .ctrl-dot {{
      width: 11px;
      height: 11px;
      border-radius: 50%;
      border: 1px solid rgba(255,255,255,0.15);
    }}
    .window-body {{
      padding: 3rem;
    }}
    .terminal-hero {{
      margin-bottom: 3rem;
      border-bottom: 1px solid var(--border);
      padding-bottom: 2.25rem;
    }}
    .prompt-line {{
      color: var(--neon-cyan);
      font-size: 0.95rem;
      margin-bottom: 0.85rem;
      display: flex;
      gap: 0.6rem;
    }}
    .hero-title {{
      font-family: var(--font-display);
      font-size: 2.75rem;
      font-weight: 700;
      color: #fff;
      letter-spacing: -0.02em;
      margin-bottom: 0.85rem;
    }}
    .hero-desc {{
      color: var(--text-dim);
      font-size: 1.05rem;
      line-height: 1.6;
      max-width: 740px;
    }}
    .telemetry-bar {{
      display: flex;
      gap: 1.75rem;
      margin-top: 1.5rem;
      font-size: 0.875rem;
      color: var(--neon-green);
      flex-wrap: wrap;
    }}
    .grid-2x2 {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 1.75rem;
    }}
    .pod-card {{
      background: #070a0e;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 2rem;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.2s ease;
      position: relative;
    }}
    .pod-card:hover {{
      border-color: var(--neon-cyan);
      box-shadow: 0 0 25px rgba(0, 240, 255, 0.15);
      transform: translateY(-2px);
    }}
    .pod-top {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 1.25rem;
    }}
    .pod-icon {{
      width: 56px;
      height: 56px;
      border-radius: 8px;
      background: #0f1622;
      border: 1px solid var(--border-bright);
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
    }}
    .pod-icon svg, .pod-icon img {{
      width: 40px;
      height: 40px;
      object-fit: contain;
    }}
    .pod-id {{
      font-size: 0.8125rem;
      color: var(--text-dim);
      background: rgba(255,255,255,0.06);
      padding: 0.25rem 0.6rem;
      border-radius: 4px;
    }}
    .pod-name {{
      font-family: var(--font-display);
      font-size: 1.5rem;
      font-weight: 700;
      color: #fff;
      margin-bottom: 0.35rem;
    }}
    .pod-url {{
      color: var(--neon-cyan);
      font-size: 0.95rem;
      text-decoration: none;
      display: inline-block;
      margin-bottom: 0.85rem;
      font-weight: 500;
    }}
    .pod-desc {{
      color: var(--text-dim);
      font-size: 0.95rem;
      line-height: 1.6;
      margin-bottom: 1.5rem;
    }}
    .pod-specs {{
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
      font-size: 0.875rem;
      color: var(--text-dim);
      border-top: 1px dashed var(--border);
      padding-top: 1.25rem;
      margin-bottom: 1.5rem;
    }}
    .spec-item {{
      display: flex;
      justify-content: space-between;
    }}
    .spec-val {{
      color: #fff;
    }}
    .pod-btn {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: transparent;
      border: 1px solid var(--border-bright);
      color: #fff;
      text-decoration: none;
      font-size: 0.95rem;
      font-weight: 600;
      padding: 0.75rem 1.25rem;
      border-radius: 4px;
      transition: all 0.15s;
    }}
    .pod-btn:hover {{
      background: var(--neon-cyan);
      color: #000;
      border-color: var(--neon-cyan);
    }}
    .topology-hud {{
      margin-top: 3.5rem;
      background: #05080c;
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 1.75rem;
    }}
    .hud-header {{
      display: flex;
      justify-content: space-between;
      font-size: 0.875rem;
      color: var(--neon-green);
      margin-bottom: 1.25rem;
      text-transform: uppercase;
      font-weight: 600;
    }}
    .node-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 1.25rem;
    }}
    .node-box {{
      border: 1px solid var(--border);
      padding: 1.15rem;
      border-radius: 4px;
      font-size: 0.875rem;
    }}
    .node-box a {{
      color: var(--neon-cyan);
      text-decoration: none;
      display: block;
      margin-top: 0.4rem;
      font-weight: 500;
    }}
    footer {{
      margin-top: 2.5rem;
      padding-top: 1.75rem;
      border-top: 1px solid var(--border);
      display: flex;
      justify-content: space-between;
      font-size: 0.875rem;
      color: var(--text-dim);
    }}
    @media (max-width: 820px) {{
      .grid-2x2, .node-grid {{
        grid-template-columns: 1fr;
      }}
      .window-body {{
        padding: 1.75rem;
      }}
      .hero-title {{
        font-size: 2rem;
      }}
    }}
  </style>
</head>
<body>
  <div class="terminal-window">
    <div class="window-header">
      <div class="window-controls">
        <span class="ctrl-dot" style="background: #ef4444;"></span>
        <span class="ctrl-dot" style="background: #f59e0b;"></span>
        <span class="ctrl-dot" style="background: #10b981;"></span>
      </div>
      <div>SYS_ROOT: leiping.dev // CLUSTER_ONLINE</div>
      <div>ENCRYPTION: TLS 1.3 // DOFOLLOW_MESH</div>
    </div>

    <div class="window-body">
      <div class="terminal-hero">
        <div class="prompt-line">
          <span>root@leiping.dev:~$</span>
          <span>matrix-cli list-all --dofollow-audit</span>
        </div>
        <h1 class="hero-title">PERRY LEI // SOFTWARE MATRIX</h1>
        <p class="hero-desc">雷平的去中心化产品与工程控制台。专注本地优先隐私、深度词源认知、一页纸学习交互与智能阅读伴侣。所有子产品通过权威 Dofollow 互链矩阵紧密协同。</p>
        <div class="telemetry-bar">
          <span>● MESH_STATUS: ACTIVE</span>
          <span>● TOTAL_NODES: 4</span>
          <span>● DOFOLLOW_REL: PASSING_RANK</span>
          <span>● GEO_TARGET: GLOBAL</span>
        </div>
      </div>

      <div class="grid-2x2">
        <!-- 01: 拾页 Shiye -->
        <article class="pod-card">
          <div>
            <div class="pod-top">
              <div class="pod-icon" style="background: #fff8ec;">
                {shiye_svg}
              </div>
              <span class="pod-id">[NODE_01]</span>
            </div>
            <h2 class="pod-name">拾页 · Shiye</h2>
            <a href="https://shiye.leiping.dev" class="pod-url" target="_blank" rel="noopener">shiye.leiping.dev ↗</a>
            <p class="pod-desc">家长为孩子生成的一页互动学习手账。课本考点智能解析、A4 单页排版、免登录即刻交付沉浸作答。</p>
          </div>
          <div>
            <div class="pod-specs">
              <div class="spec-item"><span>RUNTIME:</span><span class="spec-val">Next.js 14 / Turborepo</span></div>
              <div class="spec-item"><span>CLIENT:</span><span class="spec-val">Web + iOS App</span></div>
              <div class="spec-item"><span>PIPELINE:</span><span class="spec-val">BullMQ / Postgres</span></div>
            </div>
            <a href="https://shiye.leiping.dev" class="pod-btn" target="_blank" rel="noopener">
              <span>INITIALIZE POD</span>
              <span>→</span>
            </a>
          </div>
        </article>

        <!-- 02: WordHub -->
        <article class="pod-card">
          <div>
            <div class="pod-top">
              <div class="pod-icon">
                <img src="{wordhub_b64}" alt="WordHub">
              </div>
              <span class="pod-id">[NODE_02]</span>
            </div>
            <h2 class="pod-name">WordHub</h2>
            <a href="https://wordhub.top" class="pod-url" target="_blank" rel="noopener">wordhub.top ↗</a>
            <p class="pod-desc">全面的英语与语言深度学习平台。以词源学与 WordNet 认知网络为基石，结合语境记忆法与全端数据同步。</p>
          </div>
          <div>
            <div class="pod-specs">
              <div class="spec-item"><span>RUNTIME:</span><span class="spec-val">Next.js / FastAPI</span></div>
              <div class="spec-item"><span>NATIVE:</span><span class="spec-val">macOS (SwiftUI) / iOS</span></div>
              <div class="spec-item"><span>NETWORK:</span><span class="spec-val">WordNet 3.1 Graph</span></div>
            </div>
            <a href="https://wordhub.top" class="pod-btn" target="_blank" rel="noopener">
              <span>INITIALIZE POD</span>
              <span>→</span>
            </a>
          </div>
        </article>

        <!-- 03: TOTPBOX -->
        <article class="pod-card">
          <div>
            <div class="pod-top">
              <div class="pod-icon">
                <img src="{totp_b64}" alt="TOTPBOX">
              </div>
              <span class="pod-id">[NODE_03]</span>
            </div>
            <h2 class="pod-name">TOTPBOX</h2>
            <a href="https://www.totpbox.com" class="pod-url" target="_blank" rel="noopener">totpbox.com ↗</a>
            <p class="pod-desc">本地优先的双因素认证助手与通行密钥伴侣。零知识架构、全本地 AES-256-GCM 强加密保险库、极速自动填充。</p>
          </div>
          <div>
            <div class="pod-specs">
              <div class="spec-item"><span>SECURITY:</span><span class="spec-val">AES-256-GCM (Zero-Knowledge)</span></div>
              <div class="spec-item"><span>EXTENSION:</span><span class="spec-val">Chrome / Edge MV3 (WXT)</span></div>
              <div class="spec-item"><span>PROTOCOL:</span><span class="spec-val">RFC 6238 TOTP + WebAuthn</span></div>
            </div>
            <a href="https://www.totpbox.com" class="pod-btn" target="_blank" rel="noopener">
              <span>INITIALIZE POD</span>
              <span>→</span>
            </a>
          </div>
        </article>

        <!-- 04: CogniSphere -->
        <article class="pod-card">
          <div>
            <div class="pod-top">
              <div class="pod-icon" style="background: #111827;">
                {cogni_svg}
              </div>
              <span class="pod-id">[NODE_04]</span>
            </div>
            <h2 class="pod-name">CogniSphere</h2>
            <a href="https://cognisphere.leiping.dev" class="pod-url" target="_blank" rel="noopener">cognisphere.leiping.dev ↗</a>
            <p class="pod-desc">常驻浏览器侧边栏的智能阅读辅助。划词即解、全页提炼研读，支持 BYOK (Gemini, Claude, DeepSeek) 与端侧 AI。</p>
          </div>
          <div>
            <div class="pod-specs">
              <div class="spec-item"><span>STACK:</span><span class="spec-val">React 19 / WXT / Tailwind v4</span></div>
              <div class="spec-item"><span>MODELS:</span><span class="spec-val">BYOK (Multi-LLM) + Local Nano</span></div>
              <div class="spec-item"><span>TARGET:</span><span class="spec-val">Chrome / Edge / Firefox</span></div>
            </div>
            <a href="https://cognisphere.leiping.dev" class="pod-btn" target="_blank" rel="noopener">
              <span>INITIALIZE POD</span>
              <span>→</span>
            </a>
          </div>
        </article>
      </div>

      <div class="topology-hud">
        <div class="hud-header">
          <span>// DOFOLLOW LINK EQUALITY ARCHITECTURE</span>
          <span>100% CLEAN REL // ZERO NOFOLLOW</span>
        </div>
        <div class="node-grid">
          <div class="node-box">
            <div style="color: var(--text-dim);">HUB -> SHIYE</div>
            <a href="https://shiye.leiping.dev" target="_blank" rel="noopener">shiye.leiping.dev</a>
          </div>
          <div class="node-box">
            <div style="color: var(--text-dim);">HUB -> WORDHUB</div>
            <a href="https://wordhub.top" target="_blank" rel="noopener">wordhub.top</a>
          </div>
          <div class="node-box">
            <div style="color: var(--text-dim);">HUB -> TOTPBOX</div>
            <a href="https://www.totpbox.com" target="_blank" rel="noopener">totpbox.com</a>
          </div>
          <div class="node-box">
            <div style="color: var(--text-dim);">HUB -> COGNISPHERE</div>
            <a href="https://cognisphere.leiping.dev" target="_blank" rel="noopener">cognisphere.leiping.dev</a>
          </div>
        </div>
      </div>

      <footer>
        <div>PERRY LEI // ARCHITECT ID: 0xLEIPING</div>
        <div>HOST: leiping.dev // ALL SYSTEMS GREEN</div>
      </footer>
    </div>
  </div>
</body>
</html>
"""

with open(os.path.join(BASE_DIR, 'direction-3-cyber-terminal.html'), 'w') as f:
    f.write(html_dir3)

# ==============================================================================
# COMPARISON DASHBOARD (index.html in design-demos)
# ==============================================================================
index_html = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>leiping.dev 视觉方案三方向评审工作台 · Perry Lei</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background: #090b0e;
      color: #e6edf3;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      height: 100vh;
      display: flex;
      flex-direction: column;
      overflow: hidden;
    }
    .top-nav {
      background: #0f1217;
      border-bottom: 1px solid #1f2530;
      padding: 0.75rem 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      z-index: 10;
    }
    .logo-area {
      display: flex;
      align-items: center;
      gap: 1rem;
    }
    .logo-badge {
      font-weight: 700;
      font-size: 1rem;
      letter-spacing: -0.01em;
      color: #fff;
    }
    .tab-group {
      display: flex;
      gap: 0.5rem;
      background: #090b0e;
      padding: 0.25rem;
      border-radius: 8px;
      border: 1px solid #1f2530;
    }
    .tab-btn {
      background: transparent;
      border: none;
      color: #8b949e;
      padding: 0.45rem 1rem;
      font-size: 0.875rem;
      font-weight: 500;
      border-radius: 6px;
      cursor: pointer;
      transition: all 0.15s;
    }
    .tab-btn.active {
      background: #21262d;
      color: #fff;
      font-weight: 600;
      box-shadow: 0 1px 3px rgba(0,0,0,0.3);
    }
    .action-links {
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }
    .open-raw-btn {
      font-size: 0.8125rem;
      color: #38bdf8;
      text-decoration: none;
      border: 1px solid rgba(56, 189, 248, 0.3);
      padding: 0.35rem 0.75rem;
      border-radius: 6px;
      transition: background 0.15s;
    }
    .open-raw-btn:hover {
      background: rgba(56, 189, 248, 0.1);
    }
    .main-view {
      flex: 1;
      display: flex;
      position: relative;
    }
    iframe {
      width: 100%;
      height: 100%;
      border: none;
      background: #000;
    }
    .info-bar {
      background: #0f1217;
      border-top: 1px solid #1f2530;
      padding: 0.6rem 1.5rem;
      display: flex;
      justify-content: space-between;
      font-size: 0.8rem;
      color: #8b949e;
    }
    .info-bar strong {
      color: #fff;
    }
  </style>
</head>
<body>
  <div class="top-nav">
    <div class="logo-area">
      <div class="logo-badge">leiping.dev · 视觉三方向评审</div>
      <span style="font-size: 0.8125rem; color: #8b949e;">拾页 · WordHub · TOTPBOX · CogniSphere (Dofollow 互链)</span>
    </div>

    <div class="tab-group">
      <button class="tab-btn active" onclick="switchTab('direction-1-studio-index.html', this, '方向一：Editorial Swiss (经典出版物与工坊档案 · 浅色暖纸底+衬线体)')">
        方向一：经典出版档案 (浅)
      </button>
      <button class="tab-btn" onclick="switchTab('direction-2-digital-bento.html', this, '方向二：Digital Bento (独立创作者深色便当展厅 · Apple设计奖质感)')">
        方向二：独立工坊便当 (深)
      </button>
      <button class="tab-btn" onclick="switchTab('direction-3-cyber-terminal.html', this, '方向三：Obsidian Pulse (先锋黑曜石终端 · Cyber-Luxe控制台)')">
        方向三：黑曜石终端 (先锋)
      </button>
    </div>

    <div class="action-links">
      <a id="rawLink" href="direction-1-studio-index.html" target="_blank" class="open-raw-btn">在新标签页打开本版 ↗</a>
    </div>
  </div>

  <div class="main-view">
    <iframe id="previewFrame" src="direction-1-studio-index.html"></iframe>
  </div>

  <div class="info-bar">
    <div id="dirTitle"><strong>方向一：Editorial Swiss</strong> · 经典出版物与工坊档案 (浅色暖纸底 #f8f6f0 · 优雅衬线 · 人文与工匠气息)</div>
    <div>100% Dofollow · Schema.org JSON-LD · 移动端完全自适应</div>
  </div>

  <script>
    function switchTab(url, btn, desc) {
      document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      document.getElementById('previewFrame').src = url;
      document.getElementById('rawLink').href = url;
      document.getElementById('dirTitle').innerHTML = desc;
    }
  </script>
</body>
</html>
"""

with open(os.path.join(BASE_DIR, 'index.html'), 'w') as f:
    f.write(index_html)

print("Updated HTML Demos created successfully!")

# Take screenshots
async def take_screenshots():
    print("Launching Playwright to capture screenshots...")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={'width': 1440, 'height': 900})
        page = await context.new_page()

        demos = [
            ('direction-1-studio-index.html', 'dir1-studio-index.png'),
            ('direction-2-digital-bento.html', 'dir2-digital-bento.png'),
            ('direction-3-cyber-terminal.html', 'dir3-cyber-terminal.png')
        ]

        for html_file, shot_name in demos:
            file_url = f"file://{os.path.join(BASE_DIR, html_file)}"
            print(f"Capturing {html_file} -> {shot_name}...")
            await page.goto(file_url, wait_until='networkidle')
            await page.screenshot(
                path=os.path.join(SCREENSHOTS_DIR, shot_name),
                full_page=True
            )

        print("Capturing index.html overview...")
        await page.goto(f"file://{os.path.join(BASE_DIR, 'index.html')}", wait_until='networkidle')
        await page.screenshot(
            path=os.path.join(SCREENSHOTS_DIR, 'overview-workbench.png'),
            full_page=False
        )

        await browser.close()
    print("All screenshots updated!")

asyncio.run(take_screenshots())
