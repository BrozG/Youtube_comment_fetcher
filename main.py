import sys
import pandas as pd
from extract_vid import extract_video_id
from fetch_comments import fetch_top_comments

def get_url_from_user() -> str:
    return input("🎥  Paste a YouTube link: ").strip()

def main():
    # 1) Grab the link (CLI arg or prompt)
    url=sys.argv[1] if len(sys.argv)==2 else get_url_from_user()

    #2) Convert to video ID 
    video_id=extract_video_id(url)
    if not video_id:
        sys.exit("❌  Could not find a valid video ID in that link.")
    print(f"▶  Fetching up to 1000 toplevel comments for video: {video_id} …")
    # 3) Fetch comments (no replies)
    comments = fetch_top_comments(video_id, limit=1_000)
    if not comments:
        sys.exit("⚠️  No comments returned (video may have comments disabled).")
    # 4) Save to CSV
    df = pd.DataFrame(comments, columns=["Author", "Comment"])
    df.to_csv(f"comments/youtube_comments_{video_id}.csv", index=False)
    print(f"✅  Saved {len(df)} comments to youtube_comments.csv")


if __name__ == "__main__":
    main()