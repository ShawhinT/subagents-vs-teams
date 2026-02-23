from fasthtml.common import *
from fastlite import database
import yt_dlp
import json
import time

# ─── Database ────────────────────────────────────────────────────────────────

db = database("course.db")

db.execute("""
    CREATE TABLE IF NOT EXISTS playlists (
        playlist_id TEXT PRIMARY KEY,
        url         TEXT NOT NULL,
        title       TEXT NOT NULL,
        videos_json TEXT NOT NULL,
        created_at  REAL
    )
""")

db.execute("""
    CREATE TABLE IF NOT EXISTS progress (
        playlist_id TEXT NOT NULL,
        video_id    TEXT NOT NULL,
        completed   INTEGER DEFAULT 0,
        notes       TEXT DEFAULT '',
        PRIMARY KEY (playlist_id, video_id)
    )
""")

# ─── Helpers ─────────────────────────────────────────────────────────────────

def fmt_dur(secs):
    if not secs:
        return ""
    m, s = divmod(int(secs), 60)
    h, m = divmod(m, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def get_prog(playlist_id, video_id):
    row = db.execute(
        "SELECT completed, notes FROM progress WHERE playlist_id=? AND video_id=?",
        (playlist_id, video_id),
    ).fetchone()
    return {"completed": bool(row[0]), "notes": row[1] or ""} if row else {"completed": False, "notes": ""}


def upsert_completed(playlist_id, video_id, completed):
    db.execute(
        "INSERT OR IGNORE INTO progress (playlist_id, video_id, completed, notes) VALUES (?,?,0,'')",
        (playlist_id, video_id),
    )
    db.execute(
        "UPDATE progress SET completed=? WHERE playlist_id=? AND video_id=?",
        (int(completed), playlist_id, video_id),
    )


def upsert_notes(playlist_id, video_id, notes):
    db.execute(
        "INSERT OR IGNORE INTO progress (playlist_id, video_id, completed, notes) VALUES (?,?,0,'')",
        (playlist_id, video_id),
    )
    db.execute(
        "UPDATE progress SET notes=? WHERE playlist_id=? AND video_id=?",
        (notes, playlist_id, video_id),
    )


# ─── CSS ─────────────────────────────────────────────────────────────────────

CSS = """
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
       background: #0f0f0f; color: #e0e0e0; }

/* ── Home ── */
.home { display:flex; flex-direction:column; align-items:center; justify-content:center;
        min-height:100vh; gap:1.25rem; padding:2rem; }
.home h1 { font-size:2rem; font-weight:700; color:#fff; letter-spacing:-0.02em; }
.home p  { color:#888; font-size:0.9375rem; }
.home form { display:flex; gap:0.5rem; width:100%; max-width:640px; }
.home form input { flex:1; padding:0.75rem 1rem; border-radius:8px; border:1px solid #333;
                   background:#1a1a1a; color:#fff; font-size:0.9375rem; outline:none; }
.home form input:focus { border-color:#555; }
.home form button { padding:0.75rem 1.25rem; border-radius:8px; border:none; background:#e00;
                    color:#fff; font-size:0.9375rem; font-weight:600; cursor:pointer; }
.home form button:hover { background:#c00; }
.err { color:#f87171; font-size:0.875rem; }

/* ── Course layout ── */
.course-layout { display:flex; height:100vh; overflow:hidden; }

/* ── Sidebar ── */
.sidebar { width:300px; min-width:300px; background:#161616; border-right:1px solid #252525;
           overflow-y:auto; display:flex; flex-direction:column; }
.sb-header { padding:1rem; border-bottom:1px solid #252525; }
.sb-label  { font-size:0.6875rem; font-weight:700; color:#555; text-transform:uppercase;
             letter-spacing:0.08em; margin-bottom:0.4rem; }
.sb-title  { font-size:0.9rem; color:#ddd; line-height:1.4; }
.prog-bar  { margin-top:0.75rem; height:3px; background:#2a2a2a; border-radius:2px; }
.prog-fill { height:100%; background:#22c55e; border-radius:2px; }
.prog-text { font-size:0.7rem; color:#555; margin-top:0.35rem; }

.lesson-list { list-style:none; padding:0.375rem; }
.lesson-item { margin-bottom:2px; }
.l-btn { display:flex; align-items:flex-start; gap:0.625rem; padding:0.625rem 0.75rem;
          width:100%; text-align:left; background:none; border:none; color:#ccc;
          cursor:pointer; border-radius:6px; transition:background 0.1s; }
.l-btn:hover  { background:#222; }
.l-btn.active { background:#282828; }
.l-btn.done .l-title { text-decoration:line-through; color:#555; }
.l-num  { font-size:0.6875rem; color:#444; min-width:1.25rem; margin-top:1px; flex-shrink:0; }
.l-info { flex:1; min-width:0; }
.l-title { font-size:0.8125rem; line-height:1.4; word-break:break-word; }
.l-dur   { font-size:0.6875rem; color:#555; margin-top:0.2rem; }
.l-check { color:#22c55e; flex-shrink:0; margin-top:1px; font-size:0.875rem; }

/* ── Main area ── */
.main-area  { flex:1; overflow-y:auto; min-width:0; }
.main-inner { max-width:900px; margin:0 auto; padding:1.5rem 2rem 4rem; }
.vid-wrap   { width:100%; aspect-ratio:16/9; background:#000; border-radius:12px;
              overflow:hidden; margin-bottom:1.5rem; }
.vid-wrap iframe { width:100%; height:100%; border:none; display:block; }

.lesson-hdr { display:flex; align-items:flex-start; justify-content:space-between;
              gap:1rem; margin-bottom:1.5rem; }
.lesson-hdr h2 { font-size:1.0625rem; color:#fff; line-height:1.4; }
.toggle-btn { flex-shrink:0; padding:0.4375rem 0.875rem; border-radius:6px;
              border:1px solid #333; background:#1c1c1c; color:#bbb;
              font-size:0.8125rem; font-weight:500; cursor:pointer; white-space:nowrap; }
.toggle-btn:hover { border-color:#555; color:#fff; }
.toggle-btn.done  { border-color:#166534; background:#14532d; color:#4ade80; }
.toggle-btn.done:hover { background:#15803d; }

.notes-label { font-size:0.6875rem; font-weight:700; color:#555; text-transform:uppercase;
               letter-spacing:0.08em; margin-bottom:0.5rem; }
.notes-ta { width:100%; min-height:180px; padding:0.75rem; border-radius:8px;
            border:1px solid #252525; background:#111; color:#ddd; font-size:0.875rem;
            font-family:inherit; resize:vertical; outline:none; }
.notes-ta:focus { border-color:#444; }
"""

# ─── UI components ────────────────────────────────────────────────────────────

def sidebar_item(video, idx, playlist_id, current_video_id):
    vid_id = video["id"]
    prog = get_prog(playlist_id, vid_id)
    is_done = prog["completed"]

    btn_cls = "l-btn"
    if vid_id == current_video_id:
        btn_cls += " active"
    if is_done:
        btn_cls += " done"

    return Li(
        Button(
            Span(str(idx + 1), cls="l-num"),
            Div(
                Span(video["title"], cls="l-title"),
                Span(fmt_dur(video.get("duration")), cls="l-dur") if video.get("duration") else "",
                cls="l-info",
            ),
            Span("✓", cls="l-check") if is_done else "",
            cls=btn_cls,
            hx_get=f"/lesson/{playlist_id}/{vid_id}",
            hx_target="#main-area",
            hx_swap="innerHTML",
        ),
        id=f"lesson-{vid_id}",
        cls="lesson-item",
    )


def render_sidebar(playlist_id, title, videos, current_video_id, oob=False):
    done = sum(1 for v in videos if get_prog(playlist_id, v["id"])["completed"])
    total = len(videos)
    pct = int(done / total * 100) if total else 0

    extra = {"hx_swap_oob": "true"} if oob else {}

    return Div(
        Div(
            Div("Course", cls="sb-label"),
            Div(title, cls="sb-title"),
            Div(Div(style=f"width:{pct}%", cls="prog-fill"), cls="prog-bar"),
            Div(f"{done}/{total} completed", cls="prog-text"),
            cls="sb-header",
        ),
        Ul(
            *[sidebar_item(v, i, playlist_id, current_video_id) for i, v in enumerate(videos)],
            cls="lesson-list",
        ),
        id="sidebar",
        cls="sidebar",
        **extra,
    )


def render_lesson(playlist_id, video, prog):
    vid_id = video["id"]
    is_done = prog["completed"]

    return Div(
        Div(
            Iframe(
                src=f"https://www.youtube.com/embed/{vid_id}",
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture",
                allowfullscreen=True,
            ),
            cls="vid-wrap",
        ),
        Div(
            H2(video["title"]),
            Button(
                "✓ Completed" if is_done else "Mark complete",
                id="toggle-btn",
                cls="toggle-btn done" if is_done else "toggle-btn",
                hx_post=f"/toggle/{playlist_id}/{vid_id}",
                hx_vals=f'{{"current_video_id": "{vid_id}"}}',
                hx_target="#toggle-btn",
                hx_swap="outerHTML",
            ),
            cls="lesson-hdr",
        ),
        Div(
            P("Notes", cls="notes-label"),
            Textarea(
                prog["notes"],
                id="notes-ta",
                name="notes",
                cls="notes-ta",
                placeholder="Take notes on this lesson…",
                hx_post=f"/notes/{playlist_id}/{vid_id}",
                hx_trigger="blur",
                hx_swap="none",
            ),
            cls="notes-section",
        ),
        cls="main-inner",
    )


# ─── App ─────────────────────────────────────────────────────────────────────

app, rt = fast_app(pico=False, hdrs=[Style(CSS)])


@rt("/")
def get():
    return (
        Title("YouTube Course Creator"),
        Div(
            H1("YouTube Course Creator"),
            P("Paste a YouTube playlist URL to create a distraction-free course page."),
            Form(
                Input(
                    name="url",
                    type="text",
                    placeholder="https://www.youtube.com/playlist?list=…",
                    autofocus=True,
                ),
                Button("Create Course", type="submit"),
                action="/fetch",
                method="post",
            ),
            cls="home",
        ),
    )


@rt("/fetch", methods=["POST"])
async def post_fetch(url: str):
    url = url.strip()

    # Cache hit — redirect immediately without calling yt-dlp
    row = db.execute("SELECT playlist_id FROM playlists WHERE url=?", (url,)).fetchone()
    if row:
        return RedirectResponse(f"/course/{row[0]}", status_code=303)

    # Fetch playlist metadata via yt-dlp (no API key required)
    ydl_opts = {"quiet": True, "extract_flat": "in_playlist", "skip_download": True}
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
    except Exception as exc:
        return (
            Title("YouTube Course Creator"),
            Div(
                H1("YouTube Course Creator"),
                P("Paste a YouTube playlist URL to create a distraction-free course page."),
                Form(
                    Input(name="url", type="text", value=url,
                          placeholder="https://www.youtube.com/playlist?list=…"),
                    Button("Create Course", type="submit"),
                    action="/fetch", method="post",
                ),
                P(f"Could not fetch playlist: {exc}", cls="err"),
                cls="home",
            ),
        )

    playlist_id = info["id"]
    title = info.get("title", "Untitled Playlist")
    entries = info.get("entries") or []

    videos = []
    for e in entries:
        if not e:
            continue
        thumbs = e.get("thumbnails") or []
        thumbnail = thumbs[-1]["url"] if thumbs else ""
        videos.append({
            "id": e["id"],
            "title": e.get("title", "Untitled"),
            "duration": e.get("duration"),
            "thumbnail": thumbnail,
        })

    db.execute(
        "INSERT OR REPLACE INTO playlists (playlist_id, url, title, videos_json, created_at)"
        " VALUES (?,?,?,?,?)",
        (playlist_id, url, title, json.dumps(videos), time.time()),
    )

    return RedirectResponse(f"/course/{playlist_id}", status_code=303)


@rt("/course/{playlist_id}")
def get_course(playlist_id: str):
    row = db.execute(
        "SELECT title, videos_json FROM playlists WHERE playlist_id=?", (playlist_id,)
    ).fetchone()
    if not row:
        return RedirectResponse("/", status_code=303)

    title, videos_json = row
    videos = json.loads(videos_json)
    if not videos:
        return (Title(title), Div("No videos in this playlist.", style="padding:2rem;color:#888;"))

    first = videos[0]
    prog = get_prog(playlist_id, first["id"])

    return (
        Title(title),
        Div(
            render_sidebar(playlist_id, title, videos, first["id"]),
            Div(render_lesson(playlist_id, first, prog), cls="main-area", id="main-area"),
            cls="course-layout",
        ),
    )


@rt("/lesson/{playlist_id}/{video_id}")
def get_lesson(playlist_id: str, video_id: str):
    row = db.execute(
        "SELECT title, videos_json FROM playlists WHERE playlist_id=?", (playlist_id,)
    ).fetchone()
    if not row:
        return Div("Playlist not found.", style="padding:2rem;color:#888;")

    title, videos_json = row
    videos = json.loads(videos_json)
    video = next((v for v in videos if v["id"] == video_id), None)
    if not video:
        return Div("Lesson not found.", style="padding:2rem;color:#888;")

    prog = get_prog(playlist_id, video_id)

    # Main area content + out-of-band sidebar swap (updates current-lesson highlight)
    return (
        render_lesson(playlist_id, video, prog),
        render_sidebar(playlist_id, title, videos, video_id, oob=True),
    )


@rt("/toggle/{playlist_id}/{video_id}", methods=["POST"])
def post_toggle(playlist_id: str, video_id: str, current_video_id: str = ""):
    prog = get_prog(playlist_id, video_id)
    new_done = not prog["completed"]
    upsert_completed(playlist_id, video_id, new_done)

    cv = current_video_id or video_id

    row = db.execute(
        "SELECT title, videos_json FROM playlists WHERE playlist_id=?", (playlist_id,)
    ).fetchone()
    title, videos_json = row
    videos = json.loads(videos_json)

    # Return updated toggle button (in-place swap) + updated sidebar (OOB)
    new_btn = Button(
        "✓ Completed" if new_done else "Mark complete",
        id="toggle-btn",
        cls="toggle-btn done" if new_done else "toggle-btn",
        hx_post=f"/toggle/{playlist_id}/{video_id}",
        hx_vals=f'{{"current_video_id": "{cv}"}}',
        hx_target="#toggle-btn",
        hx_swap="outerHTML",
    )

    return new_btn, render_sidebar(playlist_id, title, videos, cv, oob=True)


@rt("/notes/{playlist_id}/{video_id}", methods=["POST"])
async def post_notes(req, playlist_id: str, video_id: str):
    form = await req.form()
    notes = form.get("notes", "")
    upsert_notes(playlist_id, video_id, notes)
    return ""  # silent save — no UI update needed


serve()
