from fasthtml.common import *
from starlette.staticfiles import StaticFiles

app, rt = fast_app(
    hdrs=(
        Link(rel='preconnect', href='https://fonts.googleapis.com'),
        Link(rel='preconnect', href='https://fonts.gstatic.com', crossorigin=''),
        Link(rel='stylesheet', href='https://fonts.googleapis.com/css2?family=Manrope:wght@600;700;800&family=Libre+Franklin:wght@400;500&display=swap'),
        Link(rel='stylesheet', href='/static/style.css'),
    ),
    pico=False,
    live=True
)

app.mount('/static', StaticFiles(directory='static'), name='static')


def hero():
    return Section(
        Div(
            H1("Stop Being an AI User. Start Building AI Products."),
            P(
                "AI Builder Academy teaches engineers and technical professionals how to design, "
                "build, and ship real AI systems end-to-end — from foundations to deployment.",
                cls='hero-sub'
            ),
            A("Join the Waitlist", href="#waitlist", cls='btn-cta'),
            P("Self-paced · Project-based · Built for engineers", cls='hero-small'),
            cls='container'
        ),
        cls='hero'
    )


def social_proof():
    return Section(
        Div(
            P("Trusted by engineers at Google, Meta, AWS, Microsoft, Salesforce", cls='proof-label'),
            Div(
                Div(
                    Span("100K+", cls='proof-number'),
                    Span("learners", cls='proof-text'),
                    cls='proof-item'
                ),
                Div(
                    Span("4.8★", cls='proof-number'),
                    Span("avg rating", cls='proof-text'),
                    cls='proof-item'
                ),
                Div(
                    Span("135+", cls='proof-number'),
                    Span("student projects shipped", cls='proof-text'),
                    cls='proof-item'
                ),
                cls='proof-bar'
            ),
            cls='container'
        ),
        cls='social-proof'
    )


def problem():
    return Section(
        Div(
            H2("You know AI. You just haven't shipped it yet."),
            Ul(
                Li("You've read the papers, watched the tutorials, and played with ChatGPT — but you still can't point to a real AI system you've built."),
                Li("The gap between 'understanding AI' and 'shipping AI' isn't knowledge. It's structure, practice, and someone who's actually done it."),
                Li("AI Builder Academy bridges that gap — with a hands-on curriculum designed around real projects, not theory."),
                cls='problem-list'
            ),
            cls='container'
        ),
        cls='problem'
    )


def who_its_for():
    return Section(
        Div(
            H2("Built for the Builder in the Middle"),
            Div(
                Div(
                    H3("This is for you if..."),
                    Ul(
                        Li(Span("✓", cls='check'), " You're an engineer or technical professional"),
                        Li(Span("✓", cls='check'), " You use AI tools but haven't built AI systems"),
                        Li(Span("✓", cls='check'), " You want to increase your impact or shift into AI work"),
                        Li(Span("✓", cls='check'), " You prefer building over passive watching"),
                        cls='fit-list'
                    ),
                    cls='fit-col for-col'
                ),
                Div(
                    H3("This is NOT for you if..."),
                    Ul(
                        Li(Span("✗", cls='ex'), " You want a lecture series with no projects"),
                        Li(Span("✗", cls='ex'), " You're looking for a credential, not capability"),
                        Li(Span("✗", cls='ex'), " You need hand-holding through basic Python"),
                        Li(Span("✗", cls='ex'), " You're a complete programming beginner"),
                        cls='fit-list'
                    ),
                    cls='fit-col not-col'
                ),
                cls='fit-grid'
            ),
            cls='container'
        ),
        cls='who-its-for'
    )


def curriculum():
    modules = [
        ("LLM Foundations & Prompt Engineering",
         "Master how large language models work and how to get reliable outputs through systematic prompting."),
        ("Retrieval, RAG & Vector Search",
         "Build systems that ground AI in your data using embeddings, vector databases, and retrieval pipelines."),
        ("AI Agents & Tool Use (MCP/Workflows)",
         "Design autonomous agents that use tools, call APIs, and execute multi-step workflows."),
        ("Evaluating & Improving AI Systems",
         "Build evaluation frameworks to measure, debug, and systematically improve AI performance."),
        ("Designing AI Architectures",
         "Learn to architect production-grade AI systems: when to use RAG vs. fine-tuning vs. agents."),
        ("Building End-to-End AI Applications",
         "Integrate everything into a cohesive app — from data ingestion to user-facing output."),
        ("Deploying & Shipping AI Apps",
         "Package, deploy, and maintain AI apps in production environments."),
    ]

    module_items = [
        Div(
            Span(str(i + 1), cls='module-num'),
            Div(
                Strong(title),
                P(desc, cls='module-desc'),
                cls='module-content'
            ),
            cls='module-item'
        )
        for i, (title, desc) in enumerate(modules)
    ]

    capstone = Div(
        P(
            "Every student completes a capstone AI project they can demonstrate publicly. "
            "Real code. Real deployment. A portfolio artifact you own.",
        ),
        cls='capstone-box'
    )

    return Section(
        Div(
            H2("7 Modules. 1 Capstone. Real Skills."),
            P("A structured path from AI foundations to production deployment.", cls='section-sub'),
            Div(*module_items, cls='module-list'),
            capstone,
            cls='container'
        ),
        cls='curriculum'
    )


def instructor():
    return Section(
        Div(
            H2("Learn from Someone Who Still Ships Code"),
            Div(
                Div(
                    Img(
                        src='/static/instructor.jpg',
                        alt='Shaw Talebi',
                        cls='instructor-photo',
                        onerror="this.style.display='none';this.nextElementSibling.style.display='block';"
                    ),
                    Div(cls='instructor-photo-fallback'),
                    cls='instructor-photo-wrap'
                ),
                Div(
                    H3("Shaw Talebi, PhD"),
                    P(
                        "Shaw is an AI educator and builder with over 100,000 learners across YouTube and online courses. "
                        "A former data scientist at Toyota with nearly 8 years in applied AI, Shaw holds a PhD and continues "
                        "to build and deploy real AI products — including two SaaS products he launched himself."
                    ),
                    P(
                        "He founded AI Builders Bootcamp, a live cohort program that has helped engineers at Google, Meta, "
                        "AWS, Microsoft, and Salesforce build production-ready AI systems. His philosophy: one cannot teach "
                        "what one does not do."
                    ),
                    P(
                        "Known for plain-language explanations and first-principles thinking, Shaw makes complex AI "
                        "engineering approachable without dumbing it down."
                    ),
                    P(
                        Em("Featured in O'Reilly's "),
                        Em(Strong("Building LLMs for Production")),
                        Em(" · 4.8★ across 72 Maven reviews"),
                        cls='instructor-proof'
                    ),
                    cls='instructor-bio'
                ),
                cls='instructor-inner'
            ),
            cls='container'
        ),
        cls='instructor-section'
    )


def testimonials():
    cards = [
        ("Shaw met each person at their skill level and made the material engaging, accessible, and immediately valuable.",
         "Bootcamp Alumni"),
        ("The most practical AI curriculum I've found. You actually build things you can show people.",
         "Software Engineer"),
        ("Shaw explains concepts clearly, connects everything to real projects, and backs it all up with code. Exactly what I needed.",
         "Technical PM"),
    ]

    card_els = [
        Div(
            P(f'"{quote}"', cls='testimonial-quote'),
            P(f"— {author}", cls='testimonial-author'),
            cls='testimonial-card'
        )
        for quote, author in cards
    ]

    return Section(
        Div(
            H2("What Students Say"),
            Div(*card_els, cls='testimonial-grid'),
            cls='container'
        ),
        cls='testimonials'
    )


def waitlist():
    return Section(
        Div(
            H2(Strong("Be First In."), " The waitlist is open."),
            P(
                "AI Builder Academy is in development. Join the waitlist to get early access, "
                "launch pricing, and updates.",
                cls='waitlist-sub'
            ),
            NotStr('<script async data-uid="fa5023cefd" src="https://the-data-entrepreneurs.kit.com/fa5023cefd/index.js"></script>'),
            cls='waitlist-inner'
        ),
        id='waitlist',
        cls='waitlist-section'
    )


def footer():
    return Footer(
        Div(
            P(
                "© 2025 AI Builder Academy · Built by Shaw Talebi",
                cls='footer-copy'
            ),
            P(
                A("Privacy", href="#", cls='footer-link'),
                Span(" · "),
                A("Contact", href="#", cls='footer-link'),
                cls='footer-links'
            ),
            cls='container footer-inner'
        ),
        cls='site-footer'
    )


@rt('/')
def index():
    return (
        Title("AI Builder Academy — Stop Being an AI User. Start Building."),
        hero(),
        social_proof(),
        problem(),
        who_its_for(),
        curriculum(),
        instructor(),
        testimonials(),
        waitlist(),
        footer(),
    )


serve()
