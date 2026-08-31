#!/usr/bin/env python3
"""Build a daily digest of the top Hacker News stories.

Fetches the current top stories from the public Hacker News API, writes a
dated markdown file under digests/, and rewrites README.md so the newest
digest is always shown on the repo's front page.

No API keys or third-party packages required (standard library only).
"""

from __future__ import annotations

import json
import pathlib
import sys
import urllib.request
from datetime import datetime, timezone

API = "https://hacker-news.firebaseio.com/v0"
TOP_N = 10
ROOT = pathlib.Path(__file__).resolve().parent.parent
DIGESTS = ROOT / "digests"
README = ROOT / "README.md"

README_HEADER = """# Daily Hacker News Digest

A self-updating archive of the top {top_n} [Hacker News](https://news.ycombinator.com/)
stories, captured once a day by a scheduled GitHub Actions workflow. Each run
appends a dated file under [`digests/`](./digests) and refreshes the snapshot
below, so this repo doubles as a searchable record of what the tech community
was reading on any given day.

- **How it works:** [`.github/workflows/daily-digest.yml`](./.github/workflows/daily-digest.yml)
  runs [`scripts/build_digest.py`](./scripts/build_digest.py) on a cron schedule.
- **Data source:** the public [Hacker News API](https://github.com/HackerNews/API)
  (no authentication).
- **Browse the archive:** [`digests/`](./digests)

---

"""


def fetch_json(url: str):
    with urllib.request.urlopen(url, timeout=30) as resp:
        return json.load(resp)


def get_top_stories(n: int) -> list[dict]:
    ids = fetch_json(f"{API}/topstories.json")
    stories = []
    for story_id in ids:
        item = fetch_json(f"{API}/item/{story_id}.json")
        if not item or item.get("type") != "story" or item.get("dead") or item.get("deleted"):
            continue
        stories.append(item)
        if len(stories) == n:
            break
    return stories


def render_digest(stories: list[dict], captured: datetime) -> str:
    lines = [
        f"# Hacker News Top {len(stories)} - {captured:%Y-%m-%d}",
        "",
        f"_Captured {captured:%Y-%m-%d %H:%M UTC}._",
        "",
    ]
    for rank, s in enumerate(stories, start=1):
        title = s.get("title", "(untitled)")
        hn_url = f"https://news.ycombinator.com/item?id={s['id']}"
        target = s.get("url", hn_url)
        score = s.get("score", 0)
        comments = s.get("descendants", 0)
        by = s.get("by", "unknown")
        lines.append(f"{rank}. **[{title}]({target})**")
        lines.append(f"   {score} points by `{by}` - [{comments} comments]({hn_url})")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def update_readme(digest_body: str, digest_name: str) -> None:
    first_line = digest_body.splitlines()[0]
    snapshot = digest_body.replace(
        first_line,
        f"## Latest snapshot - [`{digest_name}`](./digests/{digest_name})",
        1,
    )
    README.write_text(README_HEADER.format(top_n=TOP_N) + snapshot, encoding="utf-8")


def main() -> int:
    captured = datetime.now(timezone.utc)
    stories = get_top_stories(TOP_N)
    if not stories:
        print("No stories fetched; aborting.", file=sys.stderr)
        return 1

    DIGESTS.mkdir(exist_ok=True)
    digest_name = f"{captured:%Y-%m-%d}.md"
    digest_body = render_digest(stories, captured)
    (DIGESTS / digest_name).write_text(digest_body, encoding="utf-8")
    update_readme(digest_body, digest_name)
    print(f"Wrote digests/{digest_name} with {len(stories)} stories.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
