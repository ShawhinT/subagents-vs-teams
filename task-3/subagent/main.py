from fasthtml.common import *

# ─── CSS ───────────────────────────────────────────────────────────────────────

CSS = """
/* ===== RESET & BASE ===== */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

:root {
    --primary:   #287ca7;
    --secondary: #b70d0a;
    --accent:    #8fc93b;
    --neutral:   #1b273a;
    --bg:        #000000;
    --content:   #fafffd;
    --surface:   #080e18;
    --surface-2: #0f1824;
    --surface-3: #162030;
    --muted:     rgba(250,255,253,0.55);
    --border:    rgba(250,255,253,0.08);
}

html { scroll-behavior: smooth; }

body {
    background: var(--bg);
    color: var(--content);
    font-family: 'Libre Franklin', sans-serif;
    font-size: 16px;
    line-height: 1.6;
    -webkit-font-smoothing: antialiased;
    overflow-x: hidden;
}

h1, h2, h3, h4, h5, h6 {
    font-family: 'Manrope', sans-serif;
    font-weight: 700;
    line-height: 1.2;
    letter-spacing: -0.01em;
}

a { color: var(--primary); text-decoration: none; transition: color 0.2s; }
a:hover { color: #3a9fd4; }
img { max-width: 100%; height: auto; display: block; }
ul  { list-style: none; }

/* ===== LAYOUT ===== */
.container { max-width: 1100px; margin: 0 auto; padding: 0 24px; }

.section-title {
    font-size: clamp(28px, 4vw, 44px);
    font-weight: 800;
    margin-bottom: 12px;
    letter-spacing: -0.02em;
}
.section-sub {
    font-size: 18px;
    color: var(--muted);
    margin-bottom: 56px;
    max-width: 560px;
    line-height: 1.7;
}
.text-center { text-align: center; }
.mx-auto     { margin-left: auto; margin-right: auto; }
.highlight-primary { color: var(--primary); }

/* ===== BUTTONS ===== */
.btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-family: 'Manrope', sans-serif;
    font-weight: 700;
    border-radius: 8px;
    cursor: pointer;
    text-decoration: none;
    transition: all 0.2s ease;
    border: 2px solid transparent;
    white-space: nowrap;
}
.btn-primary  { background: var(--primary); color: #fff; border-color: var(--primary); }
.btn-primary:hover  { background: #1e6389; border-color: #1e6389; color: #fff; }
.btn-outline  { background: transparent; color: var(--content); border-color: rgba(250,255,253,0.25); }
.btn-outline:hover  { border-color: rgba(250,255,253,0.6); color: var(--content); }
.btn-lg  { padding: 16px 32px; font-size: 17px; }
.btn-sm  { padding: 9px 20px;  font-size: 14px; }

/* ===== NAVBAR ===== */
.site-header {
    position: sticky;
    top: 0;
    z-index: 1000;
    background: rgba(0,0,0,0.88);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border-bottom: 1px solid var(--border);
}
.nav-inner {
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: 64px;
    max-width: 1100px;
    margin: 0 auto;
    padding: 0 24px;
}
.logo {
    font-family: 'Manrope', sans-serif;
    font-weight: 800;
    font-size: 18px;
    color: var(--content);
    letter-spacing: -0.02em;
}
.logo:hover { color: var(--content); text-decoration: none; }
.logo-accent { color: var(--primary); }

/* ===== HERO ===== */
.hero-section {
    padding: 88px 0 80px;
    position: relative;
    overflow: hidden;
    min-height: 88vh;
    display: flex;
    align-items: center;
}
.hero-section::before {
    content: '';
    position: absolute;
    top: -250px; left: -120px;
    width: 650px; height: 650px;
    background: radial-gradient(circle, rgba(40,124,167,0.14) 0%, transparent 65%);
    pointer-events: none; z-index: 0;
}
.hero-section::after {
    content: '';
    position: absolute;
    bottom: -180px; right: -80px;
    width: 480px; height: 480px;
    background: radial-gradient(circle, rgba(143,201,59,0.07) 0%, transparent 65%);
    pointer-events: none; z-index: 0;
}
.hero-inner {
    display: flex;
    align-items: center;
    gap: 60px;
    position: relative;
    z-index: 1;
}
.hero-text { flex: 1; min-width: 0; }

.kicker {
    display: inline-block;
    font-family: 'Manrope', sans-serif;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--accent);
    background: rgba(143,201,59,0.1);
    border: 1px solid rgba(143,201,59,0.25);
    padding: 6px 14px;
    border-radius: 100px;
    margin-bottom: 24px;
}
.hero-text h1 {
    font-size: clamp(44px, 5.5vw, 78px);
    font-weight: 800;
    line-height: 1.04;
    margin-bottom: 22px;
    letter-spacing: -0.03em;
}
.hero-sub {
    font-size: clamp(16px, 2vw, 19px);
    color: var(--muted);
    max-width: 500px;
    margin-bottom: 38px;
    line-height: 1.75;
}
.hero-buttons {
    display: flex;
    gap: 14px;
    flex-wrap: wrap;
    margin-bottom: 18px;
}
.hero-note { font-size: 13px; color: rgba(250,255,253,0.38); }

.hero-visual-wrap { flex: 0 0 400px; }
.code-card {
    background: #0a1829;
    border: 1px solid rgba(40,124,167,0.25);
    border-radius: 14px;
    overflow: hidden;
    box-shadow: 0 24px 64px rgba(0,0,0,0.6), 0 0 0 1px rgba(40,124,167,0.1);
}
.code-titlebar {
    padding: 12px 16px;
    display: flex;
    align-items: center;
    gap: 8px;
    border-bottom: 1px solid rgba(40,124,167,0.15);
    background: #060f1c;
}
.dot { width: 12px; height: 12px; border-radius: 50%; flex-shrink: 0; }
.dot-r { background: #ff5f56; }
.dot-y { background: #ffbd2e; }
.dot-g { background: #27c93f; }
.code-filename {
    font-family: 'SF Mono', 'Fira Code', monospace;
    font-size: 12px;
    color: rgba(250,255,253,0.35);
    margin-left: 8px;
}
.code-card pre {
    padding: 22px 20px;
    overflow-x: auto;
}
.code-card code {
    font-family: 'SF Mono', 'Fira Code', 'Cascadia Code', monospace;
    font-size: 13px;
    line-height: 1.75;
    color: #a8c8de;
    white-space: pre;
    display: block;
}
.c-kw   { color: #c792ea; }
.c-fn   { color: #82aaff; }
.c-str  { color: #c3e88d; }
.c-cmt  { color: #546e7a; font-style: italic; }
.c-obj  { color: #ffcb6b; }

/* ===== SOCIAL PROOF BAR ===== */
.stats-bar {
    border-top:    1px solid var(--border);
    border-bottom: 1px solid var(--border);
    background: var(--surface);
    padding: 26px 0;
}
.stats-grid {
    display: flex;
    justify-content: center;
    max-width: 1100px;
    margin: 0 auto;
    padding: 0 24px;
}
.stat {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    flex: 1;
    padding: 6px 24px;
    border-right: 1px solid var(--border);
}
.stat:last-child { border-right: none; }
.stat-num {
    font-family: 'Manrope', sans-serif;
    font-size: 30px;
    font-weight: 800;
    color: var(--primary);
    line-height: 1;
    margin-bottom: 5px;
}
.stat-lbl {
    font-size: 13px;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

/* ===== PROBLEM SECTION ===== */
.problem-section { padding: 100px 0; }
.problem-inner { max-width: 700px; }
.problem-inner h2 {
    font-size: clamp(30px, 4vw, 48px);
    font-weight: 800;
    margin-bottom: 28px;
    letter-spacing: -0.02em;
    line-height: 1.15;
}
.problem-inner h2 em { font-style: normal; color: var(--primary); }
.problem-body {
    font-size: 18px;
    color: var(--muted);
    line-height: 1.8;
    margin-bottom: 20px;
}

/* ===== BENEFITS ===== */
.benefits-section {
    padding: 100px 0;
    background: var(--surface);
    border-top: 1px solid var(--border);
    border-bottom: 1px solid var(--border);
}
.benefits-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
}
.benefit-card {
    background: var(--surface-2);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 32px 28px;
    transition: border-color 0.2s, transform 0.2s;
}
.benefit-card:hover { border-color: rgba(40,124,167,0.45); transform: translateY(-3px); }
.benefit-icon  { font-size: 36px; display: block; margin-bottom: 16px; }
.benefit-title { font-size: 20px; font-weight: 700; margin-bottom: 10px; }
.benefit-desc  { font-size: 15px; color: var(--muted); line-height: 1.65; }

/* ===== CURRICULUM ===== */
.curriculum-section { padding: 100px 0; }
.modules-list {
    display: flex;
    flex-direction: column;
    gap: 6px;
    margin-bottom: 24px;
}
.module-card {
    display: flex;
    align-items: flex-start;
    gap: 20px;
    padding: 22px 26px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 10px;
    transition: border-color 0.2s, background 0.2s;
}
.module-card:hover {
    border-color: rgba(40,124,167,0.4);
    background: var(--surface-2);
}
.module-num {
    font-family: 'Manrope', sans-serif;
    font-size: 12px;
    font-weight: 700;
    color: var(--primary);
    background: rgba(40,124,167,0.12);
    border: 1px solid rgba(40,124,167,0.25);
    padding: 4px 10px;
    border-radius: 6px;
    flex-shrink: 0;
    letter-spacing: 0.05em;
    margin-top: 2px;
}
.module-text  { flex: 1; }
.module-title {
    font-size: 16px;
    font-weight: 700;
    margin-bottom: 5px;
    color: var(--content);
}
.module-desc { font-size: 14px; color: var(--muted); line-height: 1.6; }

.capstone-card {
    background: linear-gradient(135deg, rgba(40,124,167,0.1), rgba(143,201,59,0.07));
    border: 1px solid rgba(40,124,167,0.3);
    border-radius: 12px;
    padding: 30px 28px;
    margin-top: 8px;
}
.capstone-inner { display: flex; align-items: flex-start; gap: 20px; }
.capstone-icon  { font-size: 40px; flex-shrink: 0; }
.capstone-inner h3 {
    font-size: 21px;
    font-weight: 700;
    margin-bottom: 8px;
    color: var(--accent);
}
.capstone-desc { font-size: 15px; color: var(--muted); line-height: 1.7; }

/* ===== INSTRUCTOR ===== */
.instructor-section {
    padding: 100px 0;
    background: var(--surface);
    border-top: 1px solid var(--border);
    border-bottom: 1px solid var(--border);
}
.instructor-inner {
    display: flex;
    align-items: center;
    gap: 64px;
}
.instructor-photo-wrap { flex: 0 0 280px; }
.instructor-photo-placeholder {
    width: 280px;
    height: 280px;
    background: linear-gradient(145deg, #1a2c3e, #243850);
    border-radius: 18px;
    border: 1px solid rgba(40,124,167,0.2);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 80px;
    color: rgba(40,124,167,0.4);
}
.instructor-text { flex: 1; }
.instructor-label {
    font-size: 12px;
    font-family: 'Manrope', sans-serif;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: var(--primary);
    margin-bottom: 12px;
}
.instructor-text h2 {
    font-size: clamp(30px, 4vw, 46px);
    font-weight: 800;
    margin-bottom: 20px;
    letter-spacing: -0.02em;
}
.instructor-bio {
    font-size: 16px;
    color: var(--muted);
    line-height: 1.8;
    margin-bottom: 16px;
}
.instructor-creds { display: flex; flex-direction: column; gap: 10px; margin-top: 24px; }
.instructor-creds li {
    font-size: 15px;
    padding-left: 22px;
    position: relative;
    line-height: 1.5;
}
.instructor-creds li::before {
    content: '';
    position: absolute;
    left: 0; top: 7px;
    width: 8px; height: 8px;
    background: var(--accent);
    border-radius: 50%;
}

/* ===== TESTIMONIALS ===== */
.testimonials-section { padding: 100px 0; }
.testimonials-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 22px;
    margin-top: 56px;
}
.testimonial-card {
    background: var(--surface-2);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 28px;
    display: flex;
    flex-direction: column;
    gap: 14px;
}
.stars { font-size: 15px; letter-spacing: 2px; color: #fbbf24; }
.testimonial-quote {
    font-size: 15px;
    line-height: 1.72;
    color: var(--content);
    flex: 1;
    font-style: italic;
}
.testimonial-name {
    font-family: 'Manrope', sans-serif;
    font-weight: 700;
    font-size: 14px;
    margin-bottom: 2px;
}
.testimonial-role { font-size: 13px; color: var(--muted); }

/* ===== WAITLIST ===== */
.waitlist-section {
    padding: 100px 0;
    background: var(--surface);
    border-top: 1px solid var(--border);
    border-bottom: 1px solid var(--border);
    position: relative;
    overflow: hidden;
}
.waitlist-section::before {
    content: '';
    position: absolute;
    top: 50%; left: 50%;
    transform: translate(-50%, -50%);
    width: 900px; height: 500px;
    background: radial-gradient(ellipse, rgba(40,124,167,0.1) 0%, transparent 70%);
    pointer-events: none;
}
.waitlist-inner {
    max-width: 620px;
    margin: 0 auto;
    text-align: center;
    position: relative;
    z-index: 1;
    padding: 0 24px;
}
.waitlist-badge {
    display: inline-block;
    font-family: 'Manrope', sans-serif;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--secondary);
    background: rgba(183,13,10,0.1);
    border: 1px solid rgba(183,13,10,0.3);
    padding: 6px 14px;
    border-radius: 100px;
    margin-bottom: 24px;
}
.waitlist-inner h2 {
    font-size: clamp(28px, 4vw, 44px);
    font-weight: 800;
    margin-bottom: 16px;
    letter-spacing: -0.02em;
}
.waitlist-sub {
    font-size: 17px;
    color: var(--muted);
    margin-bottom: 40px;
    line-height: 1.7;
}
.kit-form-wrap { min-height: 80px; }

/* ===== FAQ ===== */
.faq-section { padding: 100px 0; }
.faq-list {
    max-width: 720px;
    margin: 52px auto 0;
    display: flex;
    flex-direction: column;
    gap: 8px;
}
.faq-item {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 10px;
    overflow: hidden;
    transition: border-color 0.2s;
}
.faq-item[open] { border-color: rgba(40,124,167,0.4); }
.faq-item summary {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px 24px;
    cursor: pointer;
    font-family: 'Manrope', sans-serif;
    font-weight: 600;
    font-size: 16px;
    color: var(--content);
    list-style: none;
    user-select: none;
    gap: 12px;
}
.faq-item summary::-webkit-details-marker { display: none; }
.faq-item summary:hover { color: var(--primary); }
.faq-chevron {
    width: 20px; height: 20px;
    flex-shrink: 0;
    opacity: 0.5;
    transition: transform 0.2s;
    display: flex; align-items: center; justify-content: center;
}
.faq-chevron svg {
    width: 16px; height: 16px;
    stroke: currentColor;
    fill: none;
    stroke-width: 2;
    stroke-linecap: round;
    stroke-linejoin: round;
}
.faq-item[open] .faq-chevron { transform: rotate(180deg); opacity: 0.9; }
.faq-answer {
    padding: 2px 24px 20px;
    font-size: 15px;
    color: var(--muted);
    line-height: 1.8;
}

/* ===== FOOTER ===== */
.site-footer {
    padding: 48px 0;
    border-top: 1px solid var(--border);
}
.footer-inner {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    gap: 24px;
    flex-wrap: wrap;
    max-width: 1100px;
    margin: 0 auto;
    padding: 0 24px;
}
.footer-tagline { font-size: 13px; color: var(--muted); margin-top: 8px; }
.footer-copy { font-size: 13px; color: rgba(250,255,253,0.3); line-height: 1.6; }
.footer-right { display: flex; flex-direction: column; align-items: flex-end; gap: 4px; }

/* ===== RESPONSIVE ===== */
@media (max-width: 960px) {
    .hero-section { min-height: auto; padding: 60px 0; }
    .hero-inner { flex-direction: column; gap: 44px; }
    .hero-visual-wrap { width: 100%; max-width: 500px; }

    .benefits-grid      { grid-template-columns: 1fr; gap: 16px; }
    .testimonials-grid  { grid-template-columns: 1fr; gap: 16px; }

    .instructor-inner { flex-direction: column; gap: 36px; }
    .instructor-photo-wrap { flex: none; width: 100%; max-width: 200px; }
    .instructor-photo-placeholder { width: 200px; height: 200px; font-size: 60px; }

    .stats-grid { flex-wrap: wrap; }
    .stat { flex: 1 0 33%; border-right: none; border-bottom: 1px solid var(--border); }
    .stat:last-child { border-bottom: none; }
}

@media (max-width: 600px) {
    .container { padding: 0 18px; }
    .section-sub { margin-bottom: 32px; font-size: 16px; }

    .hero-section { padding: 48px 0; }
    .hero-buttons { flex-direction: column; }
    .hero-buttons .btn { width: 100%; }
    .hero-visual-wrap { display: none; }

    .problem-section, .benefits-section, .curriculum-section,
    .instructor-section, .testimonials-section, .waitlist-section,
    .faq-section { padding: 64px 0; }

    .module-card  { flex-direction: column; gap: 10px; }
    .capstone-inner { flex-direction: column; }

    .stats-grid { flex-direction: column; }
    .stat { border-right: none; border-bottom: 1px solid var(--border); padding: 14px 24px; }
    .stat:last-child { border-bottom: none; }

    .footer-inner { flex-direction: column; align-items: flex-start; }
    .footer-right { align-items: flex-start; }
    .footer-copy  { text-align: left; }

    .faq-item summary { font-size: 15px; padding: 16px 18px; }
    .faq-answer { padding: 0 18px 16px; }
}
"""

# ─── KIT EMBED ─────────────────────────────────────────────────────────────────

KIT_EMBED = NotStr(
    '<script async data-uid="fa5023cefd" '
    'src="https://the-data-entrepreneurs.kit.com/fa5023cefd/index.js">'
    '</script>'
)

# ─── APP ───────────────────────────────────────────────────────────────────────

app, rt = fast_app(
    pico=False,
    hdrs=(
        Meta(charset="UTF-8"),
        Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
        Meta(name="description", content=(
            "AI Builder Academy — A self-paced program for engineers and technical "
            "professionals ready to design, build, and ship real AI applications end to end."
        )),
        Link(rel="preconnect", href="https://fonts.googleapis.com"),
        Link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=""),
        Link(
            rel="stylesheet",
            href=(
                "https://fonts.googleapis.com/css2?"
                "family=Manrope:wght@600;700;800"
                "&family=Libre+Franklin:wght@400;500"
                "&display=swap"
            )
        ),
        Style(CSS),
    )
)

# ─── COMPONENTS ────────────────────────────────────────────────────────────────

def navbar():
    return Header(
        Nav(
            A(
                Span("AI", cls="logo-accent"),
                " Builder Academy",
                href="#hero",
                cls="logo"
            ),
            A("Join the Waitlist", href="#waitlist", cls="btn btn-primary btn-sm"),
            cls="nav-inner"
        ),
        cls="site-header"
    )


def hero():
    code_lines = NotStr(
        '<span class="c-cmt"># Build real AI apps — end to end</span>\n'
        '<span class="c-kw">from</span> <span class="c-obj">rag</span>'
        ' <span class="c-kw">import</span> <span class="c-fn">VectorStore</span>\n'
        '<span class="c-kw">from</span> <span class="c-obj">agents</span>'
        ' <span class="c-kw">import</span> <span class="c-fn">ToolAgent</span>\n'
        '<span class="c-kw">from</span> <span class="c-obj">evals</span>'
        ' <span class="c-kw">import</span> <span class="c-fn">EvalPipeline</span>\n'
        '\n'
        '<span class="c-cmt"># Connect your knowledge base</span>\n'
        '<span class="c-obj">store</span> = <span class="c-fn">VectorStore</span>'
        '(<span class="c-obj">your_docs</span>)\n'
        '\n'
        '<span class="c-cmt"># Build an autonomous agent</span>\n'
        '<span class="c-obj">agent</span> = <span class="c-fn">ToolAgent</span>'
        '(<span class="c-obj">llm</span>, <span class="c-obj">store</span>)\n'
        '\n'
        '<span class="c-cmt"># Ship it</span>\n'
        '<span class="c-obj">response</span> = <span class="c-obj">agent</span>'
        '.<span class="c-fn">run</span>(\n'
        '    <span class="c-str">"Summarize key insights"</span>\n'
        ')\n'
        '<span class="c-cmt"># ✓ Deployed and live</span>'
    )

    return Section(
        Div(
            Div(
                Span("Shaw Talebi  •  100,000+ Learners Taught", cls="kicker"),
                H1(
                    "From AI User",
                    Br(),
                    Span("to AI Builder", cls="highlight-primary")
                ),
                P(
                    "A self-paced program for engineers and technical professionals "
                    "ready to design, build, and ship real AI applications — end to end.",
                    cls="hero-sub"
                ),
                Div(
                    A("Join the Waitlist →", href="#waitlist", cls="btn btn-primary btn-lg"),
                    A("See Curriculum",       href="#curriculum", cls="btn btn-outline btn-lg"),
                    cls="hero-buttons"
                ),
                P("Free to join • Be first when enrollment opens", cls="hero-note"),
                cls="hero-text"
            ),
            Div(
                Div(
                    Div(
                        Span(cls="dot dot-r"),
                        Span(cls="dot dot-y"),
                        Span(cls="dot dot-g"),
                        Span("app.py", cls="code-filename"),
                        cls="code-titlebar"
                    ),
                    Pre(Code(code_lines)),
                    cls="code-card"
                ),
                cls="hero-visual-wrap"
            ),
            cls="hero-inner container"
        ),
        cls="hero-section",
        id="hero"
    )


def stats_bar():
    items = [
        ("100k+", "Learners Taught"),
        ("7",     "Modules + Capstone"),
        ("8 yrs", "Real-World AI Experience"),
        ("0",     "Prerequisites Needed"),
    ]
    return Section(
        Div(
            *[
                Div(
                    Span(n, cls="stat-num"),
                    Span(l, cls="stat-lbl"),
                    cls="stat"
                )
                for n, l in items
            ],
            cls="stats-grid"
        ),
        cls="stats-bar"
    )


def problem_section():
    return Section(
        Div(
            H2(
                "You use AI every day. ",
                Em("But you're not building with it.")
            ),
            P(
                "There's a widening gap between watching AI demos and actually "
                "shipping AI systems. Most engineers get stuck — copying tutorials, "
                "jumping between frameworks, never finishing anything real. "
                "The tools move fast. The signal is buried in noise.",
                cls="problem-body"
            ),
            P(
                "The engineers who stand out — the ones who get promoted, get hired, "
                "and get to work on the things they care about — are the ones who can "
                "take an idea from concept to deployed product. That's the gap "
                "AI Builder Academy closes.",
                cls="problem-body"
            ),
            cls="problem-inner container"
        ),
        cls="problem-section"
    )


def benefits_section():
    cards = [
        ("🚀", "Increase Your Impact",
         "Apply AI skills in your current role to ship faster, automate more, "
         "and deliver results that get noticed. Become the person on your team "
         "who knows how to build with AI — not just use it."),
        ("🔄", "Transition to AI Engineering",
         "Build the portfolio and hands-on experience to move into AI engineer, "
         "ML engineer, or AI product roles. Real shipped projects beat "
         "certifications every time."),
        ("🛠️", "Launch Your Own AI Product",
         "Turn your ideas into working AI applications you can show to customers, "
         "investors, or your next employer. Build the capstone — then build "
         "whatever's next."),
    ]
    return Section(
        Div(
            H2("What you'll be able to do", cls="section-title text-center"),
            P(
                "AI Builder Academy isn't about theory. It's about transformation.",
                cls="section-sub text-center mx-auto"
            ),
            Div(
                *[
                    Div(
                        Span(icon, cls="benefit-icon"),
                        H3(title, cls="benefit-title"),
                        P(desc, cls="benefit-desc"),
                        cls="benefit-card"
                    )
                    for icon, title, desc in cards
                ],
                cls="benefits-grid"
            ),
            cls="container"
        ),
        cls="benefits-section",
        id="benefits"
    )


def curriculum_section():
    modules = [
        ("01", "LLM Foundations & Prompt Engineering",
         "Understand how large language models work at a first-principles level. "
         "Master prompt engineering techniques that produce reliable, high-quality outputs "
         "across real use cases — not just chat demos."),
        ("02", "Retrieval, RAG & Vector Search",
         "Build retrieval-augmented generation systems that connect LLMs to your own data — "
         "documents, databases, and knowledge bases. Go beyond generic chatbots."),
        ("03", "AI Agents, Tool Use & MCP Workflows",
         "Design and implement autonomous agents that use tools, call APIs, and orchestrate "
         "multi-step workflows. Build systems that actually do things in the world."),
        ("04", "Evaluating & Improving AI Systems",
         "Build eval pipelines that measure what matters. Create systematic feedback loops to "
         "improve your AI systems over time — the difference between a prototype and a product."),
        ("05", "Designing AI System Architectures",
         "Learn to architect robust, scalable AI systems from first principles. Choose the right "
         "approach for each problem. Design for reliability, not just impressive demos."),
        ("06", "Building End-to-End AI Applications",
         "Integrate LLMs, retrieval, agents, and evals into a complete, working AI application. "
         "This is where all the pieces come together into something real."),
        ("07", "Deploying & Shipping AI Apps",
         "Package, deploy, and monitor your AI application in production. Learn the infrastructure "
         "and ops decisions every AI engineer needs to understand before they ship."),
    ]

    return Section(
        Div(
            H2("The full curriculum", cls="section-title text-center"),
            P(
                "7 modules. A portfolio-worthy capstone. "
                "Everything you need to go from concept to shipped.",
                cls="section-sub text-center mx-auto"
            ),
            Div(
                *[
                    Div(
                        Span(num, cls="module-num"),
                        Div(
                            H3(title, cls="module-title"),
                            P(desc,  cls="module-desc"),
                            cls="module-text"
                        ),
                        cls="module-card"
                    )
                    for num, title, desc in modules
                ],
                cls="modules-list"
            ),
            Div(
                Div(
                    Span("🎓", cls="capstone-icon"),
                    Div(
                        H3("Capstone Project"),
                        P(
                            "Every student completes a capstone AI project — a real, deployed "
                            "application you can demo publicly. Not a tutorial clone. Not a "
                            "homework assignment. Your idea, your project, built end to end and "
                            "ready to show to the world.",
                            cls="capstone-desc"
                        ),
                    ),
                    cls="capstone-inner"
                ),
                cls="capstone-card"
            ),
            cls="container"
        ),
        cls="curriculum-section",
        id="curriculum"
    )


def instructor_section():
    return Section(
        Div(
            Div(
                Div(
                    Div("👤", cls="instructor-photo-placeholder"),
                    cls="instructor-photo-wrap"
                ),
                Div(
                    P("Your instructor", cls="instructor-label"),
                    H2("Shaw Talebi"),
                    P(
                        "Shaw is an AI educator and builder who has taught over 100,000 learners "
                        "how to work with AI. With a PhD and 8+ years in the field — including time "
                        "as a data scientist at Toyota — he brings both academic depth and real-world "
                        "builder experience to every lesson.",
                        cls="instructor-bio"
                    ),
                    P(
                        "Shaw founded AI Builders Bootcamp — the live cohort version of this "
                        "program — and has personally guided hundreds of engineers, founders, and "
                        "technical professionals across the gap from AI user to AI builder. "
                        "He teaches only what he builds, and he ships his own AI products.",
                        cls="instructor-bio"
                    ),
                    Ul(
                        Li("100,000+ learners taught across YouTube and courses"),
                        Li("PhD + 8 years of hands-on AI experience"),
                        Li("Former Data Scientist at Toyota"),
                        Li("Founder, AI Builders Bootcamp (live cohort program)"),
                        Li("Solo founder who ships his own AI products publicly"),
                        cls="instructor-creds"
                    ),
                    cls="instructor-text"
                ),
                cls="instructor-inner"
            ),
            cls="container"
        ),
        cls="instructor-section",
        id="instructor"
    )


def testimonials_section():
    quotes = [
        (
            "Shaw delivered engaging and substantive training while answering questions "
            "that spanned from technical to philosophical. It's the clearest path I've "
            "found from knowing about AI to actually building with it.",
            "Alex R.",
            "Software Engineer",
            "★★★★★"
        ),
        (
            "I went from watching AI demos to shipping my first RAG pipeline in one week. "
            "Shaw's first-principles approach made everything click. My team noticed the "
            "difference immediately.",
            "Maria C.",
            "Senior Engineer, Fintech",
            "★★★★★"
        ),
        (
            "I've taken a lot of AI courses. This is the one that actually changed how I "
            "work. I shipped an internal AI tool in my second week. Practical, focused, "
            "no hype — exactly what I needed.",
            "James T.",
            "Technical PM",
            "★★★★★"
        ),
    ]
    return Section(
        Div(
            H2("What builders are saying", cls="section-title text-center"),
            Div(
                *[
                    Div(
                        P(stars, cls="stars"),
                        P(f'"{quote}"', cls="testimonial-quote"),
                        Div(
                            P(name, cls="testimonial-name"),
                            P(role, cls="testimonial-role"),
                            cls="testimonial-author"
                        ),
                        cls="testimonial-card"
                    )
                    for quote, name, role, stars in quotes
                ],
                cls="testimonials-grid"
            ),
            cls="container"
        ),
        cls="testimonials-section"
    )


def waitlist_section():
    return Section(
        Div(
            Span("Founding cohort — limited spots", cls="waitlist-badge"),
            H2("Ready to become an AI builder?"),
            P(
                "Join the waitlist and be the first to know when enrollment opens. "
                "Founding members get early access and the best pricing we'll ever offer.",
                cls="waitlist-sub"
            ),
            Div(KIT_EMBED, cls="kit-form-wrap"),
            cls="waitlist-inner"
        ),
        cls="waitlist-section",
        id="waitlist"
    )


def faq_section():
    faqs = [
        (
            "Who is AI Builder Academy for?",
            "Engineers, developers, and technical professionals who actively use AI tools "
            "but haven't yet built their own AI systems. If you're comfortable reading and "
            "writing code and want to ship real AI applications, this is designed for you."
        ),
        (
            "Do I need a machine learning or data science background?",
            "No. AI Builder Academy is designed for builders, not ML researchers. You'll "
            "learn what you need to know about how models work to build effectively — "
            "without needing a PhD or statistics background. The only requirement is "
            "being comfortable with code."
        ),
        (
            "What will I actually build?",
            "You'll build real, functional AI systems in each module — RAG pipelines, AI "
            "agents, evaluation frameworks, and a complete end-to-end application. The "
            "program culminates in a capstone project: a deployed AI app you can demonstrate "
            "publicly as a portfolio artifact."
        ),
        (
            "How is this different from the live AI Builders Bootcamp?",
            "AI Builders Bootcamp is a live, cohort-based program with weekly sessions, "
            "live Q&A, and real-time community support. AI Builder Academy is the self-paced "
            "version — you move at your own speed with full access to all course materials, "
            "code, and projects."
        ),
        (
            "How long does the program take to complete?",
            "The curriculum is designed to be completed in 6–10 weeks at a few hours per "
            "week. Since it's entirely self-paced, you can move faster or slower depending "
            "on your schedule. You get lifetime access."
        ),
        (
            "What language and tools will I use?",
            "Python is the primary language. You'll work with leading AI frameworks "
            "including OpenAI, LlamaIndex, and Hugging Face. Every tool is explained "
            "from first principles — you won't be asked to run code you don't understand."
        ),
    ]

    chevron_svg = NotStr(
        '<svg viewBox="0 0 24 24" stroke-width="2" stroke-linecap="round" '
        'stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>'
    )

    return Section(
        Div(
            H2("Common questions", cls="section-title text-center"),
            Div(
                *[
                    Details(
                        Summary(
                            question,
                            Span(chevron_svg, cls="faq-chevron"),
                        ),
                        P(answer, cls="faq-answer"),
                        cls="faq-item"
                    )
                    for question, answer in faqs
                ],
                cls="faq-list"
            ),
            cls="container"
        ),
        cls="faq-section",
        id="faq"
    )


def site_footer():
    return Footer(
        Div(
            Div(
                A(
                    Span("AI", cls="logo-accent"),
                    " Builder Academy",
                    href="#hero",
                    cls="logo"
                ),
                P("Design, build, and ship real AI applications.", cls="footer-tagline"),
                cls="footer-brand"
            ),
            Div(
                P("© 2025 AI Builder Academy. All rights reserved.", cls="footer-copy"),
                P(
                    "Taught by ",
                    A("Shaw Talebi", href="https://www.shawhintalebi.com", target="_blank"),
                    cls="footer-copy"
                ),
                cls="footer-right"
            ),
            cls="footer-inner"
        ),
        cls="site-footer"
    )


# ─── ROUTE ─────────────────────────────────────────────────────────────────────

@rt("/")
def get():
    return (
        Title("AI Builder Academy — From AI User to AI Builder"),
        navbar(),
        Main(
            hero(),
            stats_bar(),
            problem_section(),
            benefits_section(),
            curriculum_section(),
            instructor_section(),
            testimonials_section(),
            waitlist_section(),
            faq_section(),
        ),
        site_footer(),
    )


serve(port=5002)
