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

## Latest snapshot - [`2026-10-19.md`](./digests/2026-10-19.md)

_Captured 2026-10-19 03:09 UTC._

1. **[Hybrid Reasoning Agents: LLM agents that think in latent space, act through text](https://arxiv.org/abs/2610.18861)**
   245 points by `allinonai` - [150 comments](https://news.ycombinator.com/item?id=50145337)

2. **[William Gibson and the trademarking of cyberspace](https://colo.to/cyberspace.html)**
   85 points by `Eric_Gullichsen` - [8 comments](https://news.ycombinator.com/item?id=50146625)

3. **[There's never been a better time to go into math (by: 3blue1brown) [video]](https://www.youtube.com/watch?v=LKrwhjOI8Nc)**
   210 points by `mdp2021` - [202 comments](https://news.ycombinator.com/item?id=50136150)

4. **[Laptop Based on 6502 CPU](https://www.maddox.pro/?p=448)**
   51 points by `nanochess` - [19 comments](https://news.ycombinator.com/item?id=50111537)

5. **[If you don't run your own LLM proxy, how do you know whats going on?](https://jrdsgl.com/if-you-dont-run-your-own-llm-proxy-how-the-fuck-do-you-even-know-whats-going-on/)**
   55 points by `amrrs` - [43 comments](https://news.ycombinator.com/item?id=50145507)

6. **[Someone behind the software](https://karrisaarinen.com/posts/someone-behind-the-software/)**
   338 points by `tosh` - [139 comments](https://news.ycombinator.com/item?id=50142573)

7. **[Starcraft: Ashfall](https://starcraft-shooter-2026.pages.dev/)**
   16 points by `debo_` - [8 comments](https://news.ycombinator.com/item?id=50147233)

8. **[RepRapMicron](https://github.com/VikOlliver/RepRapMicron/wiki)**
   341 points by `RobotToaster` - [55 comments](https://news.ycombinator.com/item?id=50141076)

9. **[Free Pascal compiler now supports dynamic packages](https://www.getlazarus.org/dynamic/)**
   117 points by `sysrpl` - [24 comments](https://news.ycombinator.com/item?id=50144066)

10. **[Dogs seem to agree with humans that 'bouba' is round and 'kiki' is spiky](https://www.sciencealert.com/dogs-seem-to-agree-with-humans-that-bouba-is-round-and-kiki-is-spiky)**
   146 points by `gmays` - [87 comments](https://news.ycombinator.com/item?id=50136979)
