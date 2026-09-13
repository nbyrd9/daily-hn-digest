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

## Latest snapshot - [`2026-09-13.md`](./digests/2026-09-13.md)

_Captured 2026-09-13 22:12 UTC._

1. **[Claude Fable 5.1 Solves the Cyphral Distich, a 370-year-old cipher](https://www.vals.ai/blogs/fable-solves-cyphral-distich)**
   109 points by `u1hcw9nx` - [24 comments](https://news.ycombinator.com/item?id=49688695)

2. **[Mark Zuckerberg: "Cambridge Analytica" (2017)](https://twitter.com/TechEmails/status/2099214399840059428)**
   187 points by `mfiguiere` - [70 comments](https://news.ycombinator.com/item?id=49688157)

3. **[Why is Google still serving dodgy ads?](https://www.atomic14.com/2026/09/13/why-is-google-still-serving-dodgy-ads)**
   416 points by `iamflimflam1` - [194 comments](https://news.ycombinator.com/item?id=49686445)

4. **[Julia 1.13 Highlights](https://julialang.org/blog/2026/09/julia-1.13-highlights/)**
   92 points by `eigenspace` - [6 comments](https://news.ycombinator.com/item?id=49642645)

5. **[Astra and Fable still hack on simple variants of alignment evals from 2025](https://www.lesswrong.com/posts/munJKF7iWMsWJLAH2/astra-and-fable-still-hack-on-simple-variants-of-alignment)**
   328 points by `Levitating` - [154 comments](https://news.ycombinator.com/item?id=49684393)

6. **[Flawed Routers Flood University of Wisconsin Internet Time Server (2003)](https://pages.cs.wisc.edu/~plonka/netgear-sntp/)**
   19 points by `walrus01` - [1 comments](https://news.ycombinator.com/item?id=49688391)

7. **[Data collected by cars and sold to third parties](https://www.theverge.com/column/994172/your-car-is-selling-your-data)**
   229 points by `bookofjoe` - [126 comments](https://news.ycombinator.com/item?id=49683953)

8. **[Global Shortage Has Led to Motor Oil Rationing at Costco](https://guessingheadlights.com/global-shortage-has-led-to-motor-oil-rationing-at-costco/)**
   170 points by `mikhael` - [126 comments](https://news.ycombinator.com/item?id=49686697)

9. **[JetKVM Mini](https://jetkvm.com/blog/introducing-jetkvm-mini)**
   493 points by `taubek` - [192 comments](https://news.ycombinator.com/item?id=49681152)

10. **[Bad Code Is Kudzu](https://vickiboykis.com/2026/09/01/bad-code-is-kudzu/)**
   14 points by `surprisetalk` - [3 comments](https://news.ycombinator.com/item?id=49643059)
