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

## Latest snapshot - [`2026-09-19.md`](./digests/2026-09-19.md)

_Captured 2026-09-19 14:48 UTC._

1. **[Laya the open source version of Jev](https://laya.convaiinnovations.com/)**
   313 points by `nandakishor_ml` - [62 comments](https://news.ycombinator.com/item?id=49765348)

2. **[What Zig felt like, coming from Rust](https://besok.github.io/posts/what-zig-felt-like-coming-from-rust/)**
   28 points by `ksec` - [8 comments](https://news.ycombinator.com/item?id=49766637)

3. **[Tin: full-text search for Postgres](https://planetscale.com/blog/introducing-tin)**
   19 points by `ksec` - [3 comments](https://news.ycombinator.com/item?id=49766611)

4. **[AI-generated posters don’t have to be horrible](https://john.hartnup.uk/2026/06/07/ai-event-posters.html)**
   556 points by `ereiamjh` - [343 comments](https://news.ycombinator.com/item?id=49764791)

5. **[Human brain is two separate organs, Stanford Medicine-led research finds](https://med.stanford.edu/news/all-news/2026/09/two-separate-brains.html)**
   422 points by `emigre` - [156 comments](https://news.ycombinator.com/item?id=49763697)

6. **[A graphical desktop for the ZX Spectrum](https://github.com/mindbox77/zxdesk)**
   15 points by `graemep` - [4 comments](https://news.ycombinator.com/item?id=49766676)

7. **[“The Secret Life of Circuits” is here](https://blog.coredump.cx/p/the-secret-life-of-circuits-is-here)**
   150 points by `surprisetalk` - [33 comments](https://news.ycombinator.com/item?id=49720143)

8. **[Android 17 is the first since 3.x to add new APIs without releasing to the AOSP](https://grapheneos.social/@GrapheneOS/117282080803799576)**
   934 points by `theanonymousone` - [513 comments](https://news.ycombinator.com/item?id=49758736)

9. **[Black Holes or Black Hole Stars? Astronomers Spar over 'Little Red Dots'](https://www.quantamagazine.org/black-holes-or-black-hole-stars-astronomers-spar-over-webb-telescopes-little-red-dots-20260914/)**
   15 points by `jandrewrogers` - [3 comments](https://news.ycombinator.com/item?id=49756121)

10. **[San Francisco Onion Futures Company](https://onionfutures.com/)**
   262 points by `z-mach9` - [91 comments](https://news.ycombinator.com/item?id=49763296)
