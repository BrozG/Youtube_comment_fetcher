import os
from typing import List, Dict

import requests
from dotenv import load_dotenv

# ── 1. read your API key ─────────────────────────────────────────
load_dotenv()
_API_KEY = os.getenv("API_KEY")
if not _API_KEY:
    raise RuntimeError("API_KEY missing in .env")

# ── 2. constants ────────────────────────────────────────────────
_BASE_URL      = "https://www.googleapis.com/youtube/v3/commentThreads"
_MAX_PER_PAGE  = 100     # enforced by YouTube
_DEFAULT_LIMIT = 1_000   # stop after this many comments

# ── 3. helper to call one page ──────────────────────────────────
def _call_api(video_id: str, page_token: str | None = None) -> Dict:
    params = {
        "part": "snippet",
        "videoId": video_id,
        "maxResults": _MAX_PER_PAGE,
        "textFormat": "plainText",
        "key": _API_KEY,
    }
    if page_token:
        params["pageToken"] = page_token

    resp = requests.get(_BASE_URL, params=params, timeout=20)
    resp.raise_for_status()
    return resp.json()

# ── 4. public function ──────────────────────────────────────────
def fetch_top_comments(
    video_id: str, limit: int = _DEFAULT_LIMIT
) -> List[Dict[str, str]]:
    """
    Stream through pages until `limit` comments are collected or no pages left.
    """
    comments: List[Dict[str, str]] = []
    next_token: str | None = None

    while len(comments) < limit:
        # 4a) fetch one page (100 or fewer comments)
        data = _call_api(video_id, next_token)

        # 4b) extract each top‑level comment
        for item in data.get("items", []):
            s = item["snippet"]["topLevelComment"]["snippet"]
            comments.append(
                {"Author": s["authorDisplayName"], "Comment": s["textDisplay"]}
            )
            if len(comments) >= limit:
                break

        # 4c) update next_token; if None, we reached the last page
        next_token = data.get("nextPageToken")
        if not next_token:
            break

    return comments

