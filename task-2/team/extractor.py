import yt_dlp


def extract_playlist(url: str) -> dict:
    """
    Extract playlist metadata using yt-dlp (no video download).

    Returns:
    {
        "playlist_id": str,
        "title": str,
        "videos": [
            {
                "video_id": str,
                "title": str,
                "thumbnail": str,  # URL of best thumbnail
                "duration": int,   # seconds (0 if unavailable)
                "position": int,   # 0-indexed position in playlist
            }
        ]
    }
    Raises ValueError if URL is invalid or playlist is empty.
    """
    ydl_opts = {
        "extract_flat": True,
        "quiet": True,
        "no_warnings": True,
        "ignoreerrors": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

    if not info:
        raise ValueError(f"Could not extract playlist info from URL: {url}")

    playlist_id = info.get("id") or url
    title = info.get("title") or "Untitled Playlist"

    entries = info.get("entries") or []
    videos = []
    position = 0

    for entry in entries:
        if not entry:
            continue
        video_id = entry.get("id") or entry.get("url", "")
        # Skip if no valid video id
        if not video_id or "/" in video_id:
            continue

        entry_title = entry.get("title") or f"Lesson {position + 1}"

        # Thumbnail: try thumbnails list first, then construct standard URL
        thumbnails = entry.get("thumbnails") or []
        if thumbnails:
            thumbnail = thumbnails[-1].get("url") or f"https://img.youtube.com/vi/{video_id}/mqdefault.jpg"
        else:
            thumbnail = f"https://img.youtube.com/vi/{video_id}/mqdefault.jpg"

        duration = entry.get("duration") or 0
        try:
            duration = int(duration)
        except (TypeError, ValueError):
            duration = 0

        videos.append({
            "video_id": video_id,
            "title": entry_title,
            "thumbnail": thumbnail,
            "duration": duration,
            "position": position,
        })
        position += 1

    if not videos:
        raise ValueError(f"No videos found in playlist: {url}")

    return {
        "playlist_id": playlist_id,
        "title": title,
        "videos": videos,
    }
