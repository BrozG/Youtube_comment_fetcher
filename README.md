# 📺 YouTube Comment Fetcher

> A Python tool that fetches the newest 1000 comments from any YouTube video using the YouTube Data API v3.

---

## ✨ Features

- 💬 Fetches up to **1000 comments** sorted newest first
- 🔑 Uses **YouTube Data API v3** via Google Cloud
- 🔒 Secure API key storage with `.env`
- 📄 Exports comments for analysis
- ⚡ Fast and lightweight — pure Python

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| YouTube Data API v3 | Fetching comments |
| Google Cloud Console | API key management |
| python-dotenv | Secure API key handling |

---

## 🚀 Getting Started

### Step 1 — Create a Google Cloud Project
1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Click top bar → **New Project**
3. Name it (e.g. `YouTube Comment Fetcher`) → click **Create**

### Step 2 — Enable YouTube Data API v3
1. Go to **APIs & Services → Library**
2. Search for **YouTube Data API v3**
3. Click it → click **Enable**

### Step 3 — Create API Credentials
1. Go to **APIs & Services → Credentials**
2. Click **+ Create Credentials → API key**
3. Copy the generated API key
4. *(Recommended)* Restrict the key to limit quota usage

### Step 4 — Set Up the Project
```bash
git clone https://github.com/BrozG/Youtube_comment_fetcher
cd Youtube_comment_fetcher
pip install -r requirements.txt
```

### Step 5 — Add Your API Key
Create a `.env` file in the root folder:
```bash
API_KEY="your_api_key_here"
```
> See `env_example` for the correct format

### Step 6 — Run It
```bash
python main.py
```

---

## 📁 Project Structure

```
Youtube_comment_fetcher/
├── main.py               # Entry point
├── fetch_comments.py     # YouTube API comment fetching logic
├── extract_vid.py        # Video ID extraction from URL
├── env_example           # Example .env format
├── .gitignore
└── README.md
```

---

## 💡 What I'd Improve Next

- 🌐 Turn it into a **browser extension** — paste URL and get comments instantly
- 📊 Add **sentiment analysis** on fetched comments
- 📈 Visualize comment trends over time
- 💾 Export to CSV or JSON

---

## ⚠️ Important

- Never commit your `.env` file — it's already in `.gitignore` ✅
- YouTube Data API v3 has a **daily quota limit** on free tier

---

## 👤 Author

**BrozG** — Full Stack & AI/ML Developer

[![GitHub](https://img.shields.io/badge/GitHub-BrozG-blue)](https://github.com/BrozG)

---

## 📄 License

MIT
