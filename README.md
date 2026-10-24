# Daily Hacker News Digest

A self-updating archive of the top 10 [Hacker News](https://news.ycombinator.com/)
stories. A scheduled GitHub Actions workflow captures the current standings
two to seven times a day, at randomized times, rewriting the dated file for
the day under [`digests/`](./digests) and refreshing the snapshot below -- so
this repo doubles as a searchable record of what the tech community was
reading, and how the rankings shifted through the day.

- **How it works:** [`.github/workflows/daily-digest.yml`](./.github/workflows/daily-digest.yml)
  fires every 2 hours; [`scripts/scheduled_commit.py`](./scripts/scheduled_commit.py)
  uses a date-seeded RNG to pick 2-7 two-hour windows for the day, waits a
  random 0-85 minutes, then builds the digest via
  [`scripts/build_digest.py`](./scripts/build_digest.py), commits, and pushes.
- **Data source:** the public [Hacker News API](https://github.com/HackerNews/API)
  (no authentication).
- **Browse the archive:** [`digests/`](./digests)

---

## Latest snapshot - [`2026-10-24.md`](./digests/2026-10-24.md)

_Captured 2026-10-24 14:05 UTC._

1. **[I Don't Understand Quantum Physics (2018)](https://www.southampton.ac.uk/~doug/quantum_physics/index.html)**
   146 points by `rramadass` - [95 comments](https://news.ycombinator.com/item?id=50219666)

2. **[OBS Studio 33](https://github.com/obsproject/obs-studio/releases/tag/33.0.0)**
   267 points by `pentagrama` - [79 comments](https://news.ycombinator.com/item?id=50218430)

3. **[Elon Musk Just Gave Europe a Reason to Replace American Technology](https://steveblank.com/2026/10/24/europe-gets-a-wake-up-call/)**
   162 points by `sblank` - [115 comments](https://news.ycombinator.com/item?id=50220913)

4. **[Around a dozen banking apps began specifically permitting GrapheneOS](https://grapheneos.social/@GrapheneOS/117492375462459244)**
   305 points by `privacyishuman` - [79 comments](https://news.ycombinator.com/item?id=50217495)

5. **[Kimi K3.1 Pro and K3.1 Pro Highspeed](https://www.kimi.ai/blog/kimi-k3-1-pro)**
   977 points by `Jowsey` - [584 comments](https://news.ycombinator.com/item?id=50212065)

6. **[Physicists trap a single antimatter particle for a month](https://www.scientificamerican.com/article/physicists-trap-a-single-antimatter-particle-for-a-month/)**
   126 points by `mooreds` - [49 comments](https://news.ycombinator.com/item?id=50186450)

7. **[Node2Shell evolves to HTTP2Shell, blast radius affects many HTTP libs and apps](https://www.aikido.dev/blog/python-packages-vulnerable-node2shell-brotli-cve-2026-111497)**
   83 points by `theanonymousone` - [38 comments](https://news.ycombinator.com/item?id=50219177)

8. **[Today, we hacked what we'd set out to hack: the iPhone](https://blog.calif.io/p/iphone)**
   962 points by `pavel_lishin` - [619 comments](https://news.ycombinator.com/item?id=50211474)

9. **[Appreciating the beauty of all your body's scars and scratches](https://1000awesomethings.com/2026/10/08/576-appreciating-the-beauty-of-all-your-bodys-scars-and-scratches-4/)**
   31 points by `surprisetalk` - [22 comments](https://news.ycombinator.com/item?id=50181106)

10. **[Twelve years of distributed SQLite](https://philipotoole.com/twelve-years-of-distributed-sqlite/)**
   265 points by `otoolep` - [41 comments](https://news.ycombinator.com/item?id=50217500)
