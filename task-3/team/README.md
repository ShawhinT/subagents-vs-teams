# AI Builder Academy — Landing Page

A FastHTML landing page for the AI Builder Academy course product.

## Requirements

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) package manager

## Setup

Dependencies are already declared in `pyproject.toml`. Install them with:

```bash
uv sync
```

## Running the App

```bash
uv run python main.py
```

The server starts on **http://localhost:5001** by default.

The app runs with `live=True`, so it will auto-reload on file changes during development.

## Project Structure

```
team/
├── main.py           # FastHTML app — all page sections and routing
├── static/
│   ├── style.css     # All custom styles (fonts, colors, layout, responsive)
│   └── instructor.jpg  # Instructor photo placeholder (replace with real photo)
├── pyproject.toml    # uv project config with python-fasthtml dependency
└── README.md         # This file
```

## Customization

- **Instructor photo**: Replace `static/instructor.jpg` with an actual photo. The image renders as a 160x160 circular crop. If the file is missing or fails to load, the page falls back to a gray circle via CSS/JS.
- **Kit form**: The waitlist embed uses `data-uid="fa5023cefd"`. To change the Kit form, update the `NotStr(...)` call in the `waitlist()` function in `main.py`.
- **Colors and fonts**: All design tokens are in `static/style.css` at the top of each section's comment block.

## Brand

- Primary: `#287ca7` (blue)
- Secondary: `#b70d0a` (red)
- Accent: `#8fc93b` (green)
- Background: `#000000` (black)
- Text: `#fafffd` (near-white)
- Headers: Manrope (Google Fonts)
- Body: Libre Franklin (Google Fonts)
