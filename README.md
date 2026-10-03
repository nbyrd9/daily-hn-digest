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

## Latest snapshot - [`2026-10-03.md`](./digests/2026-10-03.md)

_Captured 2026-10-03 21:07 UTC._

1. **[Hole Punch: Sling your spaceship around gravitational fields](https://notoriousbfg.com/hole-punch/)**
   111 points by `trwhite` - [34 comments](https://news.ycombinator.com/item?id=49946393)

2. **[We want you to build the next Git platform on Cloudflare](https://blog.cloudflare.com/next-git-platform-on-cloudflare/)**
   32 points by `geoffbp` - [23 comments](https://news.ycombinator.com/item?id=49947051)

3. **[Kolibri – Tech Report [pdf]](https://aleph-alpha.com/downloads/tech-report.pdf)**
   102 points by `yu3zhou4` - [4 comments](https://news.ycombinator.com/item?id=49946069)

4. **[Celebrating the 100th birthday of the kidney donated to him as a teenager](https://www.whec.com/top-news/webster-man-celebrating-the-100th-birthday-of-the-kidney-his-mom-donated-to-him-as-a-teenager/)**
   73 points by `gscott` - [14 comments](https://news.ycombinator.com/item?id=49923873)

5. **[Getting the most out of Opus 5.5 in Claude and Claude Code](https://claude.dev/blog/getting-the-most-out-of-opus-5-5/)**
   45 points by `saikatsg` - [6 comments](https://news.ycombinator.com/item?id=49946567)

6. **[Show HN: Pi pod – Run your pi coding agent in sandboxes on your own server](https://pipod.dev/)**
   45 points by `edverma2` - [22 comments](https://news.ycombinator.com/item?id=49937304)

7. **[Kolibri: A Sovereign Open-Weight Model](https://aleph-alpha.com/en/blog/kolibri-has-landed-a-sovereign-open-weight-model/)**
   407 points by `bastitx` - [260 comments](https://news.ycombinator.com/item?id=49942706)

8. **[FTL: A new operating system for clouds](https://ftl-os.org/)**
   124 points by `romac` - [50 comments](https://news.ycombinator.com/item?id=49944912)

9. **[Vx – One Language, Every Chip](https://vxlang.org/)**
   36 points by `elffjs` - [20 comments](https://news.ycombinator.com/item?id=49946076)

10. **[RSS Feed Best Practices (2022)](https://kevincox.ca/2022/05/06/rss-feed-best-practices/)**
   15 points by `KomoD` - [0 comments](https://news.ycombinator.com/item?id=49946845)
