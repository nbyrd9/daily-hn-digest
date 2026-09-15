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

## Latest snapshot - [`2026-09-15.md`](./digests/2026-09-15.md)

_Captured 2026-09-15 21:22 UTC._

1. **[Introducing System One Models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev)**
   343 points by `albelfio` - [133 comments](https://news.ycombinator.com/item?id=49717558)

2. **[Show HN: An e-ink frame that hears birds and draws them as 1800s illustrations](https://github.com/arnegiacomo/fugleramme)**
   1105 points by `arnemunthekaas` - [152 comments](https://news.ycombinator.com/item?id=49711544)

3. **[An Update on Wayback Machine Access](https://blog.archive.org/2026/09/15/an-update-on-wayback-machine-access/)**
   249 points by `ChrisArchitect` - [125 comments](https://news.ycombinator.com/item?id=49716176)

4. **[Gemini 3.8 Live and 3.8 Live Extended Thinking](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/)**
   178 points by `leumon` - [116 comments](https://news.ycombinator.com/item?id=49715947)

5. **[We got admin access to Baseten's production GitHub in 25 minutes](https://www.strix.ai/blog/baseten-harbor-github-pat-takeover)**
   150 points by `bearsyankees` - [60 comments](https://news.ycombinator.com/item?id=49716476)

6. **[Jean-Pierre Serre is 100 years old today](https://mathshistory.st-andrews.ac.uk/Biographies/Serre/)**
   17 points by `jzox` - [0 comments](https://news.ycombinator.com/item?id=49718822)

7. **[WangNet – 1.8 MB, zero-dependency Numberwang adjudication in 11 languages](https://github.com/GraafHenk/numberwang)**
   52 points by `Liogra123` - [17 comments](https://news.ycombinator.com/item?id=49717605)

8. **[Chopping up books when they're physically too big](https://attainablefelicity.mattkirkland.com/20260915/cut-up-your-books.html)**
   59 points by `matt_kirkland` - [50 comments](https://news.ycombinator.com/item?id=49716953)

9. **[Building a Linux GPU Driver for the M4 Mac Mini in One Month](https://codyho.dev/blog/gpu-driver/)**
   28 points by `ADevWithAnIdea` - [1 comments](https://news.ycombinator.com/item?id=49717638)

10. **[Show HN: Capsule – Single-file web apps that save their data into SQLite](https://withcapsule.app/)**
   242 points by `bashtian` - [110 comments](https://news.ycombinator.com/item?id=49712278)
