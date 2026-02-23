# YouTube Course Creator

A distraction-free course viewer for YouTube playlists, with progress tracking and per-lesson notes.

## Startup

```bash
uv run python main.py
```

Then open http://localhost:5001 in your browser.

## Features

- Paste any YouTube playlist URL to create a course page
- Sidebar with ordered lesson list and completion status
- YouTube embed player with no distractions
- Mark lessons complete/incomplete (persists across reloads)
- Per-lesson notes that auto-save on blur
- Playlist metadata cached in SQLite — repeat visits load instantly

## Stack

- **FastHTML** — server-rendered HTML with HTMX partial updates
- **yt-dlp** — playlist metadata extraction (no API key needed)
- **SQLite** (via fastlite) — local persistence for cache, completion state, and notes

## Data

All data is stored in `course.db` (SQLite) in the project directory.
