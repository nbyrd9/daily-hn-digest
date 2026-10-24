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

_Captured 2026-10-24 17:07 UTC._

1. **[Roku developer repositories moved from GitHub to GitLab](https://blog.roku.com/developer/gitlab-move)**
   73 points by `cxr` - [31 comments](https://news.ycombinator.com/item?id=50222622)

2. **[FreeDNS](https://freedns.afraid.org/)**
   110 points by `esher` - [23 comments](https://news.ycombinator.com/item?id=50222133)

3. **[The St. Helena 5 pence coin shows Jonathan, a roughly 190 year old tortoise](https://de.numista.com/9866)**
   13 points by `schleck8` - [0 comments](https://news.ycombinator.com/item?id=50222927)

4. **[Neural chip decodes interactions between brain regions](https://actu.epfl.ch/news/neural-chip-decodes-interactions-between-brain-r-2/)**
   26 points by `giuliomagnifico` - [3 comments](https://news.ycombinator.com/item?id=50222525)

5. **[OBS Studio 33](https://github.com/obsproject/obs-studio/releases/tag/33.0.0)**
   357 points by `pentagrama` - [122 comments](https://news.ycombinator.com/item?id=50218430)

6. **[Around a dozen banking apps began specifically permitting GrapheneOS](https://grapheneos.social/@GrapheneOS/117492375462459244)**
   492 points by `privacyishuman` - [169 comments](https://news.ycombinator.com/item?id=50217495)

7. **[Node2Shell evolves to HTTP2Shell, blast radius affects many HTTP libs and apps](https://www.aikido.dev/blog/python-packages-vulnerable-node2shell-brotli-cve-2026-111497)**
   167 points by `theanonymousone` - [82 comments](https://news.ycombinator.com/item?id=50219177)

8. **[TornadoVM 7 Enables GPU-Native Workloads from Java Applications](https://www.infoq.com/news/2026/10/tornadovm-7-gpu/)**
   55 points by `pjmlp` - [11 comments](https://news.ycombinator.com/item?id=50192975)

9. **[Kimi K3.1 Pro and K3.1 Pro Highspeed](https://www.kimi.ai/blog/kimi-k3-1-pro)**
   1023 points by `Jowsey` - [625 comments](https://news.ycombinator.com/item?id=50212065)

10. **[Physicists trap a single antimatter particle for a month](https://www.scientificamerican.com/article/physicists-trap-a-single-antimatter-particle-for-a-month/)**
   196 points by `mooreds` - [66 comments](https://news.ycombinator.com/item?id=50186450)
