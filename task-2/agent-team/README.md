# YouTube Course Creator

Turn any YouTube playlist into a clean, distraction-free course with progress tracking and per-lesson notes.

## Setup & Run

```bash
uv run python main.py
```

Then open http://localhost:5001 in your browser.

## Usage

1. Paste a YouTube playlist URL on the home page
2. Click "Load Course" to fetch the playlist (cached after first load)
3. Click any lesson in the sidebar to load it
4. Mark lessons complete with the button below the video
5. Write notes in the textarea — they auto-save when you click away

## Tech Stack

- FastHTML + HTMX for the UI
- yt-dlp for playlist metadata extraction
- SQLite for persistence (playlists, completion state, notes)
- uv for project management
