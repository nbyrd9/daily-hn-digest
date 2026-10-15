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

## Latest snapshot - [`2026-10-15.md`](./digests/2026-10-15.md)

_Captured 2026-10-15 23:33 UTC._

1. **[Muse Spark Open](https://research.meta.ai/blog/muse-spark-open)**
   561 points by `bigwheels` - [320 comments](https://news.ycombinator.com/item?id=50107379)

2. **[What I Self-Host](https://viceconsole.fyi/blog/2026/10/10/what-i-self-host/)**
   170 points by `BrunoBernardino` - [90 comments](https://news.ycombinator.com/item?id=50109715)

3. **[Neural networks are clean](https://already-clean.goodfire.com/)**
   454 points by `themgt` - [170 comments](https://news.ycombinator.com/item?id=50105647)

4. **[Someone on Torrent Sites Kept Fucking with My Sonarr](https://thereallo.dev/blog/someone-on-torrent-sites-kept-fucking-with-my-sonarr-setup)**
   171 points by `speckx` - [65 comments](https://news.ycombinator.com/item?id=50108872)

5. **[Wayland desktop for Linux with skeuomorphic design](https://github.com/fyzugx/DEsk)**
   468 points by `FinalDestiny` - [184 comments](https://news.ycombinator.com/item?id=50103338)

6. **[Jev meets the Trolley Problem](https://zachlandes.com/trolley-problem/)**
   252 points by `zlandes86` - [115 comments](https://news.ycombinator.com/item?id=50106023)

7. **[AdFection: Targeted ads turned into a pipeline for zero-click mercenary spyware](https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/)**
   357 points by `jcomp` - [525 comments](https://news.ycombinator.com/item?id=50101813)

8. **[Krea 3 – An image model built for editing at scale](https://www.krea.ai/krea-3)**
   227 points by `dvrp` - [76 comments](https://news.ycombinator.com/item?id=50105648)

9. **[Major ICQ security hole (1998)](https://opennet.ru/base/maillist/169.txt.html)**
   14 points by `sysoleg` - [3 comments](https://news.ycombinator.com/item?id=50069439)

10. **[Celebrating 70 Years of Fortran](https://fortran-lang.org/news/2026/09-15-Fortran-birthday/)**
   200 points by `rbanffy` - [92 comments](https://news.ycombinator.com/item?id=50104726)
