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

## Latest snapshot - [`2026-10-15.md`](./digests/2026-10-15.md)

_Captured 2026-10-15 20:38 UTC._

1. **[Muse Spark Open](https://research.meta.ai/blog/muse-spark-open)**
   412 points by `bigwheels` - [256 comments](https://news.ycombinator.com/item?id=50107379)

2. **[Neural networks are clean](https://already-clean.goodfire.com/)**
   336 points by `themgt` - [106 comments](https://news.ycombinator.com/item?id=50105647)

3. **[E Ink Kaleido 4](https://www.eink.com/news/detail/EInk-Launches-Latest-Version-of-Color-ePaper-Platform-E-Ink-Kaleido-4)**
   61 points by `Perroboc` - [23 comments](https://news.ycombinator.com/item?id=50108229)

4. **[Wayland desktop for Linux with skeuomorphic design](https://github.com/fyzugx/DEsk)**
   411 points by `FinalDestiny` - [168 comments](https://news.ycombinator.com/item?id=50103338)

5. **[Krea 3 – An image model built for editing at scale](https://www.krea.ai/krea-3)**
   185 points by `dvrp` - [68 comments](https://news.ycombinator.com/item?id=50105648)

6. **[AdFection: Targeted ads turned into a pipeline for zero-click mercenary spyware](https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/)**
   290 points by `jcomp` - [454 comments](https://news.ycombinator.com/item?id=50101813)

7. **[Why I Wrote PGP (1991, revised 1999)](https://philzimmermann.com/EN/essays/WhyIWrotePGP.html)**
   54 points by `GaryBluto` - [12 comments](https://news.ycombinator.com/item?id=50084674)

8. **[Celebrating 70 Years of Fortran](https://fortran-lang.org/news/2026/09-15-Fortran-birthday/)**
   171 points by `rbanffy` - [70 comments](https://news.ycombinator.com/item?id=50104726)

9. **[Jev meets the Trolley Problem](https://zachlandes.com/trolley-problem/)**
   143 points by `zlandes86` - [66 comments](https://news.ycombinator.com/item?id=50106023)

10. **[Delta’s Biscoff cookies were supposed to be temporary](https://www.seriouseats.com/biscoff-history-12168161)**
   117 points by `mhb` - [109 comments](https://news.ycombinator.com/item?id=50080155)
