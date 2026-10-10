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

## Latest snapshot - [`2026-10-10.md`](./digests/2026-10-10.md)

_Captured 2026-10-10 23:41 UTC._

1. **[Build your own decision model](https://nishtahir.com/build-your-own-decision-model/)**
   21 points by `softwaredoug` - [2 comments](https://news.ycombinator.com/item?id=50037949)

2. **[2D Vehicles](https://patkerr.co.uk/2d-vehicles/)**
   322 points by `Michelangelo11` - [77 comments](https://news.ycombinator.com/item?id=49991852)

3. **[A city-building game in which the city would prefer you didn't](https://housing.over.pizza/)**
   114 points by `JumpCrisscross` - [42 comments](https://news.ycombinator.com/item?id=50036864)

4. **[Nix wrote half of my debugger](https://fzakaria.com/2026/10/07/nix-wrote-half-of-my-debugger)**
   100 points by `ingve` - [12 comments](https://news.ycombinator.com/item?id=50017247)

5. **[Why DuckDB 2.0 is faster](https://motherduck.com/blog/why-duckdb-20-is-faster/)**
   119 points by `tosh` - [39 comments](https://news.ycombinator.com/item?id=50035530)

6. **[The Lightbulb Computer](https://lightbulbcomputer.com/)**
   170 points by `oskarth` - [38 comments](https://news.ycombinator.com/item?id=50029487)

7. **[Knuth reward check](https://www.thomas-huehn.com/knuth-reward-check/)**
   129 points by `Curiositry` - [48 comments](https://news.ycombinator.com/item?id=50034081)

8. **[Talorys – A self-hosted personal AI agent on Cloudflare's free tier](https://github.com/rociiu/talorys)**
   230 points by `rociiu` - [118 comments](https://news.ycombinator.com/item?id=50031614)

9. **[Five months treating bugs like patients and coding agents like a medical team](https://www.cockroachlabs.com/blog/experiment-running-hospital-code/)**
   24 points by `rafiss` - [6 comments](https://news.ycombinator.com/item?id=50021899)

10. **[Mxc: Microsoft Execution Containers version 1.0.0](https://blogs.windows.com/windowsdeveloper/2026/10/07/microsoft-execution-containers-policy-driven-containment-for-ai-agents/)**
   149 points by `smokel` - [32 comments](https://news.ycombinator.com/item?id=50016956)
