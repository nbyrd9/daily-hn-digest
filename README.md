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

## Latest snapshot - [`2026-10-12.md`](./digests/2026-10-12.md)

_Captured 2026-10-12 09:18 UTC._

1. **[Postgres isn't slow, your storage is](https://clickhouse.com/blog/posette-talk-recap-postgres-isnt-slow-your-storage-is)**
   66 points by `saisrirampur` - [36 comments](https://news.ycombinator.com/item?id=50052163)

2. **[Type-safe HTML templating in Zig](https://lalinsky.com/2026/10/11/type-safe-html-templating-in-zig.html)**
   111 points by `lukaslalinsky` - [46 comments](https://news.ycombinator.com/item?id=50051573)

3. **[Fable Took My Job](https://cendyne.dev/posts/2026-10-11-fable-took-my-jorb.html)**
   9 points by `jllyhill` - [0 comments](https://news.ycombinator.com/item?id=50053216)

4. **[Fingerprints are the new cookies](https://royfish.dev/fingerprints-are-the-new-cookies)**
   356 points by `royfish` - [172 comments](https://news.ycombinator.com/item?id=50048642)

5. **[Calculus with Julia](https://jverzani.github.io/CalculusWithJuliaNotes.jl/)**
   121 points by `subset` - [10 comments](https://news.ycombinator.com/item?id=50034206)

6. **[Total Annihilation, rebuilt for modern computers](https://nanolathe.gg)**
   497 points by `jttnr` - [198 comments](https://news.ycombinator.com/item?id=50045984)

7. **[Running the unmodified Linux amdgpu driver on an iPad](https://github.com/Geramy/LemonSeed-Studio)**
   17 points by `joshcsimmons` - [7 comments](https://news.ycombinator.com/item?id=50041573)

8. **[Zod 4.6.6 compromised by malware?](https://github.com/colinhacks/zod/commit/d821685ea6732436fcdf786a81d076958471e467)**
   113 points by `luggage_bazooka` - [28 comments](https://news.ycombinator.com/item?id=50052814)

9. **[Whatever became of holography? (2011)](https://www.americanscientist.org/article/whatever-became-of-holography)**
   128 points by `cainxinth` - [63 comments](https://news.ycombinator.com/item?id=50049411)

10. **[Cartographers of North Korea (2019)](https://cartographers-nk.wonyoung.so/)**
   257 points by `edent` - [46 comments](https://news.ycombinator.com/item?id=50047091)
