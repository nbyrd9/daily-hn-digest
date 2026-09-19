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

## Latest snapshot - [`2026-09-19.md`](./digests/2026-09-19.md)

_Captured 2026-09-19 19:55 UTC._

1. **[I built non-autoregressive decision models with RL a year ago](https://laya.convaiinnovations.com/)**
   829 points by `nandakishor_ml` - [204 comments](https://news.ycombinator.com/item?id=49765348)

2. **[AI-generated posters don’t have to be horrible](https://john.hartnup.uk/2026/06/07/ai-event-posters.html)**
   1055 points by `ereiamjh` - [597 comments](https://news.ycombinator.com/item?id=49764791)

3. **[Btrfs/ZFS/bcachefs under workloads classic benchmarks skip](https://bartosz.fenski.pl/modern-fs-benchmark/)**
   38 points by `farlight` - [26 comments](https://news.ycombinator.com/item?id=49768833)

4. **[Human brain is two separate organs, Stanford Medicine-led research finds](https://med.stanford.edu/news/all-news/2026/09/two-separate-brains.html)**
   572 points by `emigre` - [207 comments](https://news.ycombinator.com/item?id=49763697)

5. **[A graphical desktop for the ZX Spectrum](https://github.com/mindbox77/zxdesk)**
   116 points by `graemep` - [89 comments](https://news.ycombinator.com/item?id=49766676)

6. **[Tin: full-text search for Postgres](https://planetscale.com/blog/introducing-tin)**
   136 points by `ksec` - [61 comments](https://news.ycombinator.com/item?id=49766611)

7. **[Suzanne Ciani's Buchla Cookbook](https://echo.orpheusinstituut.be/article/suzannes-buchla-cookbook)**
   21 points by `stuart78` - [8 comments](https://news.ycombinator.com/item?id=49735010)

8. **[UFO Series Home Page: "UFO" TV Series from 1970](https://ufoseries.com/)**
   7 points by `DropDead` - [1 comments](https://news.ycombinator.com/item?id=49754194)

9. **[The Secret Life of Circuits](https://blog.coredump.cx/p/the-secret-life-of-circuits-is-here)**
   242 points by `surprisetalk` - [62 comments](https://news.ycombinator.com/item?id=49720143)

10. **[Show HN: CUA-S1 – A System One Model for Computer Use](https://github.com/trycua/cua)**
   15 points by `frabonacci` - [1 comments](https://news.ycombinator.com/item?id=49767564)
