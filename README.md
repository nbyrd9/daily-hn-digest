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

## Latest snapshot - [`2026-11-06.md`](./digests/2026-11-06.md)

_Captured 2026-11-06 05:32 UTC._

1. **[Claude Code sends your email address to websites](https://github.com/anthropics/claude-code/issues/107757)**
   789 points by `motoroco` - [267 comments](https://news.ycombinator.com/item?id=50385272)

2. **[sshole](https://sshhole.com)**
   2485 points by `josemrb` - [610 comments](https://news.ycombinator.com/item?id=50378228)

3. **[MS Paint Remote Code Execution Vulnerability](https://www.cve.org/CVERecord?id=CVE-2026-83844)**
   412 points by `kuberwastaken` - [154 comments](https://news.ycombinator.com/item?id=50384233)

4. **[Pwn.college](https://pwn.college/)**
   46 points by `tripdout` - [4 comments](https://news.ycombinator.com/item?id=50387796)

5. **[Nvidia Kubernetes Engine (NVKE)](https://github.com/dsx-ai-factory/nvke)**
   34 points by `gkapur` - [11 comments](https://news.ycombinator.com/item?id=50387738)

6. **[Closed AI models dominate the price-performance frontier](https://village.dev/blog/closed-ai-models-now-dominate-the-price-performance-frontier/)**
   38 points by `kevin_hu` - [27 comments](https://news.ycombinator.com/item?id=50387546)

7. **[Inkling 2 Small](https://thinkingmachines.ai/news/inkling-2-small/)**
   133 points by `Philpax` - [53 comments](https://news.ycombinator.com/item?id=50386338)

8. **[The Hackintosh Reborn](https://www.naut.ca/blog/2026/11/05/the-hackintosh-reborn-with-ai/)**
   260 points by `rubatuga` - [129 comments](https://news.ycombinator.com/item?id=50383057)

9. **[Window Sweaters](https://github.com/saragordic/window-sweaters)**
   280 points by `nickswalker` - [92 comments](https://news.ycombinator.com/item?id=50381383)

10. **[Show HN: Firenook – Firebase emulators in Rust: 40× faster writes, 10× less RAM](https://firenook.dev/)**
   75 points by `sanjevirau` - [14 comments](https://news.ycombinator.com/item?id=50378643)
