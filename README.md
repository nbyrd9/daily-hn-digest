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

## Latest snapshot - [`2026-10-31.md`](./digests/2026-10-31.md)

_Captured 2026-10-31 08:31 UTC._

1. **[My favourite PowerMac is a Nintendo Wii](https://virtuallyfun.com/2026/10/29/my-favourite-powermac-is-a-nintendo-wii/)**
   304 points by `DHowett` - [82 comments](https://news.ycombinator.com/item?id=50307190)

2. **[Cloudflare Turnstile solver library (no headless browser required)](https://github.com/chris124567/cfsolve)**
   185 points by `costco` - [54 comments](https://news.ycombinator.com/item?id=50277379)

3. **[Tell HN: Scribd Breached](https://news.ycombinator.com/item?id=50312756)**
   179 points by `x______________` - [71 comments](https://news.ycombinator.com/item?id=50312756)

4. **[The $6.3B Binance hack was pulled off in just 20 minutes](https://www.wired.com/story/the-dollar63-billion-binance-hack-was-pulled-off-in-just-20-minutes/)**
   435 points by `domhudson` - [290 comments](https://news.ycombinator.com/item?id=50303172)

5. **[Northflank Breached](https://status.northflank.com)**
   425 points by `js4ever` - [312 comments](https://news.ycombinator.com/item?id=50305025)

6. **[Breaking the open web won't stop the bad bots](https://www.techpolicy.press/breaking-the-open-web-wont-stop-the-bad-bots/)**
   254 points by `raybb` - [106 comments](https://news.ycombinator.com/item?id=50263837)

7. **[Show HN: Samosa – Linter for Math Derivations](https://samosa-math.vercel.app)**
   13 points by `Hussain04` - [1 comments](https://news.ycombinator.com/item?id=50258605)

8. **[Longitudinal Changes InWearable-Captured PhysiologyBefore Sudden Cardiac Death](https://www.jacc.org/doi/epdf/10.1016/j.jaccas.2026.110397)**
   27 points by `brandonb` - [11 comments](https://news.ycombinator.com/item?id=50274885)

9. **[Show HN: Marelleo, an open-source story box I built for my kids using ESP32](https://zebra.rodeo/en/blog/marelleo/)**
   4 points by `foOg` - [1 comments](https://news.ycombinator.com/item?id=50260753)

10. **[Show HN: A working Nintendo in ~1GB of Qwen weights](https://github.com/dbreunig/nesformer)**
   242 points by `dbreunig` - [121 comments](https://news.ycombinator.com/item?id=50306442)
