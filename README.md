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

_Captured 2026-10-19 10:36 UTC._

1. **[Linux 7.3 Released](https://lwn.net/Articles/1101143/)**
   215 points by `cjd8` - [90 comments](https://news.ycombinator.com/item?id=50149392)

2. **[Hybrid Reasoning Agents: LLM agents that think in latent space, act through text](https://arxiv.org/abs/2610.18861)**
   402 points by `allinonai` - [196 comments](https://news.ycombinator.com/item?id=50145337)

3. **[How to Train Your Robot](https://www.construction-physics.com/p/how-to-train-your-robot)**
   42 points by `crescit_eundo` - [14 comments](https://news.ycombinator.com/item?id=50104874)

4. **[Rabbits were a medieval royal luxury in England until the Black Death](https://phys.org/news/2026-10-rabbits-medieval-royal-luxury-england.html)**
   89 points by `samizdis` - [84 comments](https://news.ycombinator.com/item?id=50131315)

5. **[William Gibson and the trademarking of cyberspace](https://colo.to/cyberspace.html)**
   190 points by `Eric_Gullichsen` - [70 comments](https://news.ycombinator.com/item?id=50146625)

6. **[There's never been a better time to go into math (by: 3blue1brown) [video]](https://www.youtube.com/watch?v=LKrwhjOI8Nc)**
   382 points by `mdp2021` - [455 comments](https://news.ycombinator.com/item?id=50136150)

7. **[Tmux and Claude Code: Sessions, Send-Keys, and the Ceiling](https://crystl.dev/guides/tmux-for-ai-agents/)**
   37 points by `ankitg12` - [19 comments](https://news.ycombinator.com/item?id=50148855)

8. **[If you don't run your own LLM proxy, how do you know whats going on?](https://jrdsgl.com/if-you-dont-run-your-own-llm-proxy-how-the-fuck-do-you-even-know-whats-going-on/)**
   173 points by `amrrs` - [119 comments](https://news.ycombinator.com/item?id=50145507)

9. **[Someone behind the software](https://karrisaarinen.com/posts/someone-behind-the-software/)**
   450 points by `tosh` - [167 comments](https://news.ycombinator.com/item?id=50142573)

10. **[Laptop Based on 6502 CPU](https://www.maddox.pro/?p=448)**
   135 points by `nanochess` - [56 comments](https://news.ycombinator.com/item?id=50111537)
