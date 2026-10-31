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

_Captured 2026-10-31 15:04 UTC._

1. **[Molly(Signal fork) has not been updated since 3 months and is vulnerable](https://piefed.world/post/1503394)**
   125 points by `DeepLogin` - [78 comments](https://news.ycombinator.com/item?id=50314666)

2. **[Prospero: A new coding harness for a more civilized age](https://nullprogram.com/blog/2026/10/31/)**
   70 points by `fovc` - [38 comments](https://news.ycombinator.com/item?id=50315226)

3. **[We Took over ChatGPT Accounts](https://www.parameter.ai/labs/we-found-a-gap-at-openai)**
   135 points by `armcat` - [59 comments](https://news.ycombinator.com/item?id=50314699)

4. **[Switch Lowering in GCC](https://xoranth.net/gcc-switch/)**
   119 points by `signa11` - [22 comments](https://news.ycombinator.com/item?id=50314085)

5. **[Simple circuits can create complex behaviors](https://aatishb.com/myriad/lets-build-a-brain/)**
   46 points by `aatish` - [4 comments](https://news.ycombinator.com/item?id=50261253)

6. **[Serbia just elected the world's brainiest parliament](https://www.science.org/content/article/serbia-just-elected-world-s-brainiest-parliament)**
   511 points by `input_sh` - [306 comments](https://news.ycombinator.com/item?id=50314654)

7. **[Digital minimalism](https://vitalik.eth.limo/general/2026/10/31/digital_minimalism.html)**
   144 points by `wilbertliu` - [111 comments](https://news.ycombinator.com/item?id=50313661)

8. **[Show HN: Marelleo, an open-source story box I built for my kids using ESP32](https://zebra.rodeo/en/blog/marelleo/)**
   126 points by `foOg` - [36 comments](https://news.ycombinator.com/item?id=50260753)

9. **[AI, Lean, and the Future of Formal Verification, with Lean Creator Leo de Moura](https://thedataexchange.media/leo-de-moura-lean-aws/)**
   106 points by `datascientist` - [25 comments](https://news.ycombinator.com/item?id=50290652)

10. **[Hunting 'Zombie Accounts' in Active Directory](https://www.fabian.fyi/2026/10/zombie-hunt.html)**
   8 points by `optimiz` - [1 comments](https://news.ycombinator.com/item?id=50296700)
