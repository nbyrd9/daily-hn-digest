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

## Latest snapshot - [`2026-09-27.md`](./digests/2026-09-27.md)

_Captured 2026-09-27 08:23 UTC._

1. **[Does Georgism work? Five years later](https://www.astralcodexten.com/p/does-georgism-work-five-years-later)**
   308 points by `silveraxe93` - [217 comments](https://news.ycombinator.com/item?id=49844657)

2. **[Go Concurrency Distilled](https://antonz.org/go-concurrency-distilled/)**
   200 points by `chmaynard` - [62 comments](https://news.ycombinator.com/item?id=49856988)

3. **[Flip Fluid on Flip Dots](https://mitxela.com/projects/flipflip)**
   46 points by `blutack` - [6 comments](https://news.ycombinator.com/item?id=49854219)

4. **[OpenAI Feared "Optics" of what might appear on Hacker News](https://authorsguild.org/news/ag-v-openai-top-execs-knew-mass-book-piracy-was-illegal/)**
   25 points by `papergirl` - [2 comments](https://news.ycombinator.com/item?id=49863864)

5. **[PipePipe: NewPipe hard fork implementing SponsorBlock](https://github.com/InfinityLoop1308/PipePipe)**
   403 points by `Qision` - [219 comments](https://news.ycombinator.com/item?id=49842764)

6. **[Improving site performance by shipping more CSS](https://github.blog/engineering/architecture-optimization/improving-site-performance-by-shipping-more-css/)**
   34 points by `torutofu` - [15 comments](https://news.ycombinator.com/item?id=49856193)

7. **[DeepSeek Elastic Compute (DSec)](https://arxiv.org/abs/2609.22978)**
   237 points by `shenli3514` - [79 comments](https://news.ycombinator.com/item?id=49859112)

8. **[Show HN: Reladraw – A diagram language where you decide where to place things](https://github.com/reladraw/reladraw)**
   288 points by `jpwalsh234` - [80 comments](https://news.ycombinator.com/item?id=49858513)

9. **[What is the size of Yemen? (2024)](https://theborys.substack.com/p/what-is-the-size-of-yemen)**
   147 points by `kspacewalk2` - [30 comments](https://news.ycombinator.com/item?id=49862809)

10. **[A searchable library of forgotten public-domain film clips from 1915 onward](https://www.movingimagearchive.com/)**
   161 points by `momentmaker` - [26 comments](https://news.ycombinator.com/item?id=49832768)
