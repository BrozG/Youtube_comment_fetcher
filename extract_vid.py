import re
from urllib.parse import urlparse, parse_qs

_PATTERNS = [
    re.compile(r"youtu\.be/([A-Za-z0-9_-]{11})"),
    re.compile(r"youtube\.com/shorts/([A-Za-z0-9_-]{11})"),
    re.compile(r"youtube\.com/embed/([A-Za-z0-9_-]{11})"),
]

def extract_video_id(url: str) -> str | None:
    """Return the 11‑char YouTube video ID or None."""
    p = urlparse(url)

    # Standard watch?v=ID URLs
    if p.path == "/watch":
        vid = parse_qs(p.query).get("v", [None])[0]
        if vid and len(vid) == 11:
            return vid

    # youtu.be / shorts / embed
    for rx in _PATTERNS:
        m = rx.search(url)
        if m:
            return m.group(1)

    return None