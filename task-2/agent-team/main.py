from fasthtml.common import *
from starlette.responses import RedirectResponse
import urllib.parse

try:
    from extractor import extract_playlist
except ImportError:
    def extract_playlist(url):
        raise RuntimeError("extractor.py not found")

app, rt, (playlists, Playlist), (videos, Video), (completions, Completion), (notes, Note) = fast_app(
    "data.db",
    playlist={"id": str, "url": str, "title": str, "pk": "id"},
    video={"id": int, "playlist_id": str, "video_id": str, "title": str, "thumbnail": str, "duration": int, "position": int, "pk": "id"},
    completion={"id": int, "playlist_id": str, "video_id": str, "completed": bool, "pk": "id"},
    note={"id": int, "playlist_id": str, "video_id": str, "content": str, "pk": "id"},
    hdrs=(Script(src="https://unpkg.com/htmx.org@1.9.12"),),
)


def fmt_duration(seconds: int) -> str:
    if not seconds:
        return "0:00"
    return f"{seconds // 60}:{seconds % 60:02d}"


def app_style() -> Style:
    return Style("""
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #f5f5f5; color: #333; }

        .home-container {
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        }
        .home-card {
            background: white;
            border-radius: 16px;
            padding: 48px 40px;
            width: 100%;
            max-width: 480px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            text-align: center;
        }
        .home-card h1 { font-size: 1.8rem; font-weight: 700; color: #1a1a2e; margin-bottom: 8px; }
        .home-card p { color: #666; margin-bottom: 28px; font-size: 0.95rem; line-height: 1.5; }
        .home-form { display: flex; flex-direction: column; gap: 12px; }
        .home-input {
            width: 100%; padding: 12px 16px;
            border: 2px solid #e0e0e0; border-radius: 8px;
            font-size: 1rem; outline: none; transition: border-color 0.2s;
        }
        .home-input:focus { border-color: #0f3460; }
        .home-btn {
            padding: 12px; background: #0f3460; color: white;
            border: none; border-radius: 8px; font-size: 1rem;
            font-weight: 600; cursor: pointer; transition: background 0.2s;
        }
        .home-btn:hover { background: #16213e; }
        .error-msg {
            margin-top: 16px; padding: 10px 14px;
            background: #fee2e2; border: 1px solid #fca5a5;
            border-radius: 6px; color: #b91c1c; font-size: 0.9rem;
        }

        .course-layout { display: flex; height: 100vh; overflow: hidden; }
        .sidebar {
            width: 280px; min-width: 280px;
            background: #1a1a2e; color: white;
            display: flex; flex-direction: column; overflow: hidden;
        }
        .sidebar-header {
            padding: 20px 16px;
            border-bottom: 1px solid rgba(255,255,255,0.1);
            background: #0f0f1a;
        }
        .sidebar-header h2 { font-size: 0.95rem; font-weight: 600; line-height: 1.4; color: #e0e0ff; }
        .lesson-count { font-size: 0.75rem; color: #8888aa; margin-top: 4px; }
        .lesson-list { flex: 1; overflow-y: auto; padding: 8px 0; }
        .lesson-list::-webkit-scrollbar { width: 4px; }
        .lesson-list::-webkit-scrollbar-track { background: #1a1a2e; }
        .lesson-list::-webkit-scrollbar-thumb { background: #444466; border-radius: 2px; }
        .lesson-item {
            display: flex; align-items: flex-start; gap: 10px;
            width: 100%; padding: 10px 14px;
            background: none; border: none; color: #cccce0;
            text-align: left; cursor: pointer; transition: background 0.15s;
            text-decoration: none;
        }
        .lesson-item:hover { background: rgba(255,255,255,0.08); }
        .lesson-item.active { background: rgba(15,52,96,0.6); color: white; }
        .lesson-item.completed { color: #8888aa; }
        .lesson-num { font-size: 0.7rem; color: #666688; min-width: 22px; padding-top: 2px; flex-shrink: 0; }
        .lesson-info { flex: 1; min-width: 0; }
        .lesson-title { font-size: 0.82rem; line-height: 1.35; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
        .lesson-item.completed .lesson-title { text-decoration: line-through; opacity: 0.7; }
        .lesson-duration { font-size: 0.7rem; color: #666688; margin-top: 2px; }
        .lesson-check { font-size: 0.85rem; color: #4ade80; min-width: 16px; padding-top: 2px; flex-shrink: 0; }

        .main-content { flex: 1; overflow-y: auto; background: white; }
        .lesson-area { max-width: 900px; margin: 0 auto; padding: 32px 40px; }
        .video-wrapper {
            width: 100%; aspect-ratio: 16 / 9;
            border-radius: 10px; overflow: hidden;
            background: #000; margin-bottom: 24px;
        }
        .video-wrapper iframe { width: 100%; height: 100%; border: none; }
        .lesson-header {
            display: flex; align-items: flex-start;
            justify-content: space-between; gap: 16px; margin-bottom: 24px;
        }
        .lesson-header h1 { font-size: 1.3rem; font-weight: 700; color: #1a1a2e; line-height: 1.4; }
        .complete-btn {
            padding: 8px 18px; border: 2px solid #0f3460;
            border-radius: 8px; background: white; color: #0f3460;
            font-size: 0.85rem; font-weight: 600; cursor: pointer;
            white-space: nowrap; transition: all 0.2s;
        }
        .complete-btn:hover { background: #0f3460; color: white; }
        .complete-btn.done { background: #4ade80; border-color: #22c55e; color: #14532d; }
        .complete-btn.done:hover { background: #f0fdf4; }
        .notes-section { margin-top: 8px; }
        .notes-section h3 { font-size: 0.95rem; font-weight: 600; color: #555; margin-bottom: 8px; }
        .notes-textarea {
            width: 100%; min-height: 150px; padding: 12px;
            border: 2px solid #e0e0e0; border-radius: 8px;
            font-size: 0.9rem; line-height: 1.5; resize: vertical;
            outline: none; font-family: inherit; transition: border-color 0.2s;
        }
        .notes-textarea:focus { border-color: #0f3460; }
        .notes-status { font-size: 0.78rem; color: #22c55e; height: 20px; margin-top: 4px; display: inline-block; }
    """)


def get_completion(playlist_id: str, video_id: str) -> bool:
    rows = completions(where=f"playlist_id='{playlist_id}' AND video_id='{video_id}'")
    return bool(rows and rows[0].completed)


def get_note_content(playlist_id: str, video_id: str) -> str:
    rows = notes(where=f"playlist_id='{playlist_id}' AND video_id='{video_id}'")
    return rows[0].content if rows else ""


def make_sidebar_item(v, playlist_id: str, active_video_id: str = None, oob: bool = False):
    is_completed = get_completion(playlist_id, v.video_id)
    is_active = v.video_id == active_video_id
    classes = "lesson-item"
    if is_active:
        classes += " active"
    if is_completed:
        classes += " completed"
    check = Span("✓", cls="lesson-check") if is_completed else Span("", cls="lesson-check")
    attrs = dict(
        cls=classes,
        hx_get=f"/course/{playlist_id}/lesson/{v.video_id}",
        hx_target="#lesson-area",
        hx_swap="innerHTML",
        hx_push_url="true",
        id=f"sidebar-item-{v.video_id}",
    )
    if oob:
        attrs["hx_swap_oob"] = "true"
    return A(
        Span(str(v.position + 1), cls="lesson-num"),
        Div(
            Span(v.title, cls="lesson-title"),
            Span(fmt_duration(v.duration), cls="lesson-duration"),
            cls="lesson-info"
        ),
        check,
        **attrs,
    )


def make_lesson_parts(playlist_id: str, video_id: str, video_title: str):
    is_done = get_completion(playlist_id, video_id)
    note_content = get_note_content(playlist_id, video_id)
    btn_cls = "complete-btn done" if is_done else "complete-btn"
    btn_text = "Mark Incomplete" if is_done else "Mark Complete"
    return (
        Div(
            Iframe(
                src=f"https://www.youtube-nocookie.com/embed/{video_id}",
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture",
                allowfullscreen=True,
            ),
            cls="video-wrapper"
        ),
        Div(
            H1(video_title),
            Button(
                btn_text,
                cls=btn_cls,
                id=f"complete-btn-{video_id}",
                hx_post=f"/course/{playlist_id}/lesson/{video_id}/complete",
                hx_swap="outerHTML",
                hx_target=f"#complete-btn-{video_id}",
            ),
            cls="lesson-header",
        ),
        Div(
            H3("Notes"),
            Textarea(
                note_content,
                cls="notes-textarea",
                name="content",
                placeholder="Add your notes for this lesson...",
                hx_post=f"/course/{playlist_id}/lesson/{video_id}/notes",
                hx_trigger="blur",
                hx_swap="outerHTML",
                hx_target="#notes-status",
            ),
            Span("", cls="notes-status", id="notes-status"),
            cls="notes-section"
        ),
    )


@rt('/')
def get(error: str = None):
    err_block = Div(error, cls="error-msg") if error else ""
    return (
        Title("YouTube Course Creator"),
        app_style(),
        Div(
            Div(
                H1("YouTube Course Creator"),
                P("Paste a YouTube playlist URL to turn it into a distraction-free course with progress tracking and notes."),
                Form(
                    Input(
                        type="text",
                        name="url",
                        placeholder="https://www.youtube.com/playlist?list=...",
                        cls="home-input",
                        required=True,
                        autofocus=True,
                    ),
                    Button("Load Course", type="submit", cls="home-btn"),
                    cls="home-form",
                    method="post",
                    action="/fetch",
                ),
                err_block,
                cls="home-card",
            ),
            cls="home-container",
        ),
    )


@rt('/fetch')
def post(url: str):
    url = url.strip()
    if not url:
        return RedirectResponse('/?error=Please+enter+a+playlist+URL', status_code=303)
    existing = playlists(where=f"url='{url}'")
    if existing:
        return RedirectResponse(f'/course/{existing[0].id}', status_code=303)
    try:
        data = extract_playlist(url)
    except Exception as e:
        return RedirectResponse(f'/?error={urllib.parse.quote(str(e))}', status_code=303)
    playlists.upsert(Playlist(id=data['playlist_id'], url=url, title=data['title']))
    for v in data['videos']:
        videos.insert(Video(
            playlist_id=data['playlist_id'],
            video_id=v['video_id'],
            title=v['title'],
            thumbnail=v['thumbnail'],
            duration=v['duration'],
            position=v['position'],
        ))
    return RedirectResponse(f'/course/{data["playlist_id"]}', status_code=303)


@rt('/course/{playlist_id}')
def get(playlist_id: str):
    playlist_rows = playlists(where=f"id='{playlist_id}'")
    if not playlist_rows:
        return RedirectResponse('/?error=Playlist+not+found', status_code=303)
    playlist = playlist_rows[0]
    vids = sorted(videos(where=f"playlist_id='{playlist_id}'"), key=lambda v: v.position)
    if not vids:
        return RedirectResponse('/?error=No+videos+found', status_code=303)
    first = vids[0]
    sidebar_items = [make_sidebar_item(v, playlist_id, active_video_id=first.video_id) for v in vids]
    lesson_parts = make_lesson_parts(playlist_id, first.video_id, first.title)
    return (
        Title(f"{playlist.title} - YouTube Course Creator"),
        app_style(),
        Div(
            Div(
                Div(H2(playlist.title), P(f"{len(vids)} lessons", cls="lesson-count"), cls="sidebar-header"),
                Div(*sidebar_items, cls="lesson-list", id="lesson-list"),
                cls="sidebar"
            ),
            Div(
                Div(*lesson_parts, cls="lesson-area", id="lesson-area"),
                cls="main-content",
            ),
            cls="course-layout"
        ),
    )


@rt('/course/{playlist_id}/lesson/{video_id}')
def get(playlist_id: str, video_id: str):
    vids = sorted(videos(where=f"playlist_id='{playlist_id}'"), key=lambda v: v.position)
    current = next((v for v in vids if v.video_id == video_id), None)
    if not current:
        return Div("Lesson not found.", cls="lesson-area")
    lesson_parts = make_lesson_parts(playlist_id, video_id, current.title)
    sidebar_oob = [make_sidebar_item(v, playlist_id, active_video_id=video_id, oob=True) for v in vids]
    return (*lesson_parts, *sidebar_oob)


@rt('/course/{playlist_id}/lesson/{video_id}/complete')
def post(playlist_id: str, video_id: str):
    current = get_completion(playlist_id, video_id)
    new_state = not current
    rows = completions(where=f"playlist_id='{playlist_id}' AND video_id='{video_id}'")
    if rows:
        c = rows[0]
        c.completed = new_state
        completions.upsert(c)
    else:
        completions.insert(Completion(playlist_id=playlist_id, video_id=video_id, completed=new_state))
    btn_cls = "complete-btn done" if new_state else "complete-btn"
    btn_text = "Mark Incomplete" if new_state else "Mark Complete"
    updated_btn = Button(
        btn_text,
        cls=btn_cls,
        id=f"complete-btn-{video_id}",
        hx_post=f"/course/{playlist_id}/lesson/{video_id}/complete",
        hx_swap="outerHTML",
        hx_target=f"#complete-btn-{video_id}",
    )
    vids = videos(where=f"playlist_id='{playlist_id}'")
    v = next((x for x in vids if x.video_id == video_id), None)
    if v:
        sidebar_update = make_sidebar_item(v, playlist_id, active_video_id=video_id, oob=True)
        return updated_btn, sidebar_update
    return updated_btn


@rt('/course/{playlist_id}/lesson/{video_id}/notes')
def post(playlist_id: str, video_id: str, content: str = ""):
    rows = notes(where=f"playlist_id='{playlist_id}' AND video_id='{video_id}'")
    if rows:
        n = rows[0]
        n.content = content
        notes.upsert(n)
    else:
        notes.insert(Note(playlist_id=playlist_id, video_id=video_id, content=content))
    return Span("Saved!", cls="notes-status", id="notes-status")


if __name__ == '__main__':
    serve()
