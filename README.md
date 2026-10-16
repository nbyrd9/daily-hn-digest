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

## Latest snapshot - [`2026-10-16.md`](./digests/2026-10-16.md)

_Captured 2026-10-16 14:58 UTC._

1. **[Hello Toronto – Waymo Is En Route](https://waymo.com/blog/2026/10/waymo-in-toronto/)**
   18 points by `ChrisArchitect` - [11 comments](https://news.ycombinator.com/item?id=50118981)

2. **[I Love Software Rendering](https://www.jamesfmackenzie.com/2026/10/13/i-love-software-rendering/)**
   126 points by `speckx` - [87 comments](https://news.ycombinator.com/item?id=50117746)

3. **[Gyroscopes Got So Small [video]](https://www.youtube.com/watch?v=0Zc_6xB5W3Y)**
   26 points by `surprisetalk` - [2 comments](https://news.ycombinator.com/item?id=50104965)

4. **[Is Liquid Metal Killing Our PCs? Scientific Analysis and a 2-Year Test [video]](https://www.youtube.com/watch?v=eF6bMSjPepM)**
   19 points by `zdw` - [4 comments](https://news.ycombinator.com/item?id=50111752)

5. **[Redesigning Source Control at Anthropic](https://simonwillison.net/2026/Oct/13/redesigning-source-control-at-anthropic/)**
   7 points by `hn9zmdcaou` - [2 comments](https://news.ycombinator.com/item?id=50118863)

6. **[Show HN: Gemini 4 Argon plays StarCraft](https://starskirmish.com/bench/v0-2/)**
   9 points by `__cayenne__` - [0 comments](https://news.ycombinator.com/item?id=50118688)

7. **[Yet another way to invoke functions without parentheses](https://blog.ikaes.de/yet-another-way-to-invoke-functions-without-parentheses/)**
   182 points by `aragonite` - [70 comments](https://news.ycombinator.com/item?id=50077225)

8. **[Big Fish: Exploiting a 37-Year-Old Kernel Bug in OpenBSD](https://calif.io/research/big-fish)**
   7 points by `rs_rs_rs_rs_rs` - [0 comments](https://news.ycombinator.com/item?id=50118977)

9. **[Woman who rescued injured crow keeps getting 'thank-you gifts' from birds [video]](https://www.youtube.com/watch?v=sjNpfz4UzqU)**
   622 points by `johnnyApplePRNG` - [203 comments](https://news.ycombinator.com/item?id=50065859)

10. **[The Economic Complexity of the Western Roman Empire](https://www.michelecoscia.com/?p=2613)**
   100 points by `mikk14` - [16 comments](https://news.ycombinator.com/item?id=50084790)
