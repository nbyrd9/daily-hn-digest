#!/usr/bin/env python3
"""Decide whether this run should publish a digest, and if so, do it.

GitHub Actions cron cannot randomize either its firing time or how often it
fires, so this script layers a per-day plan on top of a fixed
every-2-hours trigger:

  * a deterministic RNG seeded from today's UTC date picks a commit count
    between 1 and 3, then that many distinct 2-hour windows -- every run
    of the day computes the same plan
  * a run whose window is not in today's plan exits without committing
  * a run whose window IS in the plan waits a random 0-85 minutes (so the
    push lands at an unpredictable minute), rebuilds the digest, commits,
    and pushes

A manual `workflow_dispatch` run always publishes immediately, ignoring
the plan (handy for testing).
"""

from __future__ import annotations

import os
import random
import subprocess
import sys
import time
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_digest import (  # noqa: E402
    DIGESTS,
    TOP_N,
    get_top_stories,
    render_digest,
    update_readme,
)

WINDOW_HOURS = list(range(0, 24, 2))  # 0,2,...,22 -- matches cron "0 */2 * * *"
MAX_JITTER_SECONDS = 85 * 60
EVENT_NAME = os.environ.get("GITHUB_EVENT_NAME", "")
IN_CI = os.environ.get("GITHUB_ACTIONS") == "true"
MANUAL = EVENT_NAME == "workflow_dispatch"


def sh(*args: str, check: bool = True) -> str:
    return subprocess.run(
        args, check=check, capture_output=True, text=True
    ).stdout.strip()


def todays_plan(day: str) -> list[int]:
    rng = random.Random(f"hn-digest::{day}")
    count = rng.randint(1, 3)
    return sorted(rng.sample(WINDOW_HOURS, count))


def current_window(now: datetime) -> int:
    return (now.hour // 2) * 2


def already_committed_this_window(day: str, window: int) -> bool:
    subjects = sh(
        "git", "log", f"--since={day}T00:00:00Z", "--pretty=%s", check=False
    )
    return f"[w{window:02d}]" in subjects


def publish(now: datetime, window: int) -> int:
    stories = get_top_stories(TOP_N)
    if not stories:
        print("No stories fetched; aborting without commit.", file=sys.stderr)
        return 1

    DIGESTS.mkdir(exist_ok=True)
    name = f"{now:%Y-%m-%d}.md"
    body = render_digest(stories, now)
    (DIGESTS / name).write_text(body, encoding="utf-8")
    update_readme(body, name)

    if not IN_CI:
        print(f"[local] wrote digests/{name}; skipping git commit/push.")
        return 0

    sh("git", "config", "user.name", "github-actions[bot]")
    sh(
        "git", "config", "user.email",
        "41898282+github-actions[bot]@users.noreply.github.com",
    )
    sh("git", "add", "-A")
    if not sh("git", "status", "--porcelain"):
        print("Digest unchanged since last run; nothing to commit.")
        return 0

    tag = "" if MANUAL else f" [w{window:02d}]"
    msg = f"chore: Hacker News digest {now:%Y-%m-%d %H:%M UTC}{tag}"
    sh("git", "commit", "-m", msg)

    for attempt in range(1, 5):
        sh("git", "pull", "--rebase", "--autostash", "origin", "main", check=False)
        push = subprocess.run(
            ["git", "push", "origin", "HEAD:main"],
            capture_output=True, text=True,
        )
        if push.returncode == 0:
            print(f"Pushed: {msg}")
            return 0
        print(f"push attempt {attempt} failed: {push.stderr.strip()}", file=sys.stderr)
        time.sleep(5)
    return 1


def main() -> int:
    now = datetime.now(timezone.utc)
    day = f"{now:%Y-%m-%d}"

    if MANUAL:
        print("Manual dispatch: publishing immediately.")
        return publish(now, current_window(now))

    window = current_window(now)
    plan = todays_plan(day)
    print(f"{day} plan: commit windows {plan} (UTC hours); this run is window {window:02d}.")

    if window not in plan:
        print("Window not in today's plan; exiting without commit.")
        return 0
    if already_committed_this_window(day, window):
        print("Window already produced a commit today; exiting.")
        return 0

    jitter = random.randint(0, MAX_JITTER_SECONDS)
    print(f"Sleeping {jitter // 60}m{jitter % 60:02d}s before publishing (time randomization).")
    time.sleep(jitter)

    return publish(datetime.now(timezone.utc), window)


if __name__ == "__main__":
    raise SystemExit(main())
