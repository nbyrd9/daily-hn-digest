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

## Latest snapshot - [`2026-09-17.md`](./digests/2026-09-17.md)

_Captured 2026-09-17 15:17 UTC._

1. **[Fujitsu launches made-in-Japan next-generation CPU FUJITSU-MONAKA](https://global.fujitsu/en-global/pr/news/2026/09/14-02)**
   158 points by `my123` - [53 comments](https://news.ycombinator.com/item?id=49715813)

2. **[I Don't Like LLMs](https://martinfowler.com/articles/2026-dont-like-llms.html)**
   56 points by `TangerineDream` - [31 comments](https://news.ycombinator.com/item?id=49740834)

3. **[One Year of Sponsored Servo Development](https://servo.org/blog/2026/09/15/one-year-of-sponsorship/)**
   248 points by `AshleysBrain` - [110 comments](https://news.ycombinator.com/item?id=49737849)

4. **[I had Gemini train its own replacement for $9](https://www.petervijeh.com/projects/reddit-ner)**
   68 points by `p-s-v` - [22 comments](https://news.ycombinator.com/item?id=49740330)

5. **[Nvidia announces native GPU programming in Rust](https://developer.nvidia.com/blog/introducing-cuda-rust-two-tracks-for-writing-gpu-kernels/)**
   852 points by `nonmaskable` - [337 comments](https://news.ycombinator.com/item?id=49724881)

6. **[CCC invites all model citizens to 40C3](https://events.ccc.de/en/2026/09/12/40c3-model-citizens/)**
   161 points by `antonly` - [41 comments](https://news.ycombinator.com/item?id=49737787)

7. **[Show HN: I built a new version of my fun spatial 3D online meeting app](https://flat.social)**
   64 points by `pawelwentpawel` - [38 comments](https://news.ycombinator.com/item?id=49740047)

8. **[My temporary PHP fix from 2014 has nearly 20M installs. Today I'm deprecating it](https://jakeasmith.com/blog/http-build-url/)**
   235 points by `jakeasmith` - [60 comments](https://news.ycombinator.com/item?id=49718773)

9. **[Show HN: Share your AI Setup, Learn from others](https://mysetup.ai/)**
   18 points by `steveybrown` - [6 comments](https://news.ycombinator.com/item?id=49740105)

10. **[Training a 4B model to produce 81% faster query plans than Postgres](https://rohanbansal.com/qorl)**
   635 points by `polyphilz` - [128 comments](https://news.ycombinator.com/item?id=49731285)
