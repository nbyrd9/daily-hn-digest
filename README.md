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

## Latest snapshot - [`2026-09-29.md`](./digests/2026-09-29.md)

_Captured 2026-09-29 22:51 UTC._

1. **[U.S. postal inspectors shut down website selling counterfeit postage labels](https://postalemployeenetwork.com/news/2026/09/26/u-s-postal-inspectors-shut-down-website-selling-millions-of-counterfeit-postage-labels/)**
   122 points by `ilamont` - [61 comments](https://news.ycombinator.com/item?id=49899090)

2. **[GPT 6.1 Sol: Near-Astra intelligence for a fifth of the price](https://openai.com/index/introducing-gpt-6-1-sol/)**
   714 points by `crorella` - [642 comments](https://news.ycombinator.com/item?id=49896586)

3. **[PS5 Relapse Exploit](https://github.com/ntfargo/Relapse-Exploit)**
   197 points by `therepanic` - [101 comments](https://news.ycombinator.com/item?id=49895304)

4. **[How Delhi cut electricity loss from 50 to 5 percent](https://spectrum.ieee.org/delhi-electricity-loss)**
   405 points by `rbanffy` - [238 comments](https://news.ycombinator.com/item?id=49892245)

5. **[NAND-16: a computer built from 277,248 NAND gates](https://somethingbig.ai/computer)**
   91 points by `rossant` - [46 comments](https://news.ycombinator.com/item?id=49871018)

6. **[Show HN: Real-time Solar System with 526k asteroids and all tracked satellites](https://space.bl2.net/)**
   51 points by `wanick` - [21 comments](https://news.ycombinator.com/item?id=49898778)

7. **[America.gov](https://america.gov/)**
   224 points by `plesiv` - [185 comments](https://news.ycombinator.com/item?id=49893509)

8. **[A Privacy Analysis of Web and Mobile Conversational AI Agents [pdf]](https://jorgegarciaherrero.com/wp-content/interactivos/20260916-Prompt-like-a-butterfly-sting-like-a-tracker-(clean).pdf)**
   400 points by `damaru2` - [126 comments](https://news.ycombinator.com/item?id=49890226)

9. **[Show HN: TurboGPT: train 22KiB transformer in 13s](https://github.com/lostmsu/TurboGPT)**
   36 points by `lostmsu` - [5 comments](https://news.ycombinator.com/item?id=49898931)

10. **[Tcl/Tk 9.1](https://www.tcl-lang.org/software/tcltk/9.1.html)**
   225 points by `dmux` - [74 comments](https://news.ycombinator.com/item?id=49896712)
