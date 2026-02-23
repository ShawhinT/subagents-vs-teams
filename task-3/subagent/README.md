# AI Builder Academy — Landing Page

A FastHTML landing page for AI Builder Academy, a self-paced program teaching engineers to design, build, and ship real AI applications end to end.

## Startup

```bash
uv run python main.py
```

The server starts at **http://localhost:5001** by default.

## Stack

- **[uv](https://docs.astral.sh/uv/)** — project management
- **[FastHTML](https://fastht.ml/)** — Python web framework (HTMX-based)
- Custom CSS — dark theme, mobile-responsive, no CSS frameworks

## Structure

```
.
├── main.py          # App + all page components
├── pyproject.toml   # Dependencies (python-fasthtml)
├── static/          # Static asset directory
└── README.md
```

## Page Sections

1. Sticky navigation bar
2. Hero — headline, code visual, waitlist CTA
3. Stats bar — social proof numbers
4. Problem section — the AI user → builder gap
5. Benefits — what students will be able to do
6. Curriculum — 7 modules + capstone
7. Instructor — Shaw Talebi bio
8. Testimonials — student quotes
9. Waitlist — Kit (ConvertKit) embed
10. FAQ — native `<details>` accordion
11. Footer

## Brand

- **Colors**: `#287ca7` primary · `#b70d0a` secondary · `#8fc93b` accent · `#000` bg
- **Fonts**: Manrope (headers) · Libre Franklin (body) via Google Fonts
