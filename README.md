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

## Latest snapshot - [`2026-10-11.md`](./digests/2026-10-11.md)

_Captured 2026-10-11 21:19 UTC._

1. **[Total Annihilation, rebuilt for modern computers](https://nanolathe.gg)**
   225 points by `jttnr` - [92 comments](https://news.ycombinator.com/item?id=50045984)

2. **[Cartographers of North Korea](https://cartographers-nk.wonyoung.so/)**
   63 points by `edent` - [5 comments](https://news.ycombinator.com/item?id=50047091)

3. **[Chapter 1 of Ways of Seeing by John Berger](https://www.ways-of-seeing.com/ch1)**
   50 points by `rafael859` - [6 comments](https://news.ycombinator.com/item?id=50046241)

4. **[Artificial Insanity](https://richwhitehouse.com/index.php?postid=78)**
   30 points by `leglock` - [22 comments](https://news.ycombinator.com/item?id=50047071)

5. **[Be The Onion's Hero for Once](https://mailchi.mp/email.theonion.com/archivehunt)**
   130 points by `mooreds` - [8 comments](https://news.ycombinator.com/item?id=50047055)

6. **[Terence Tao: Math 2.0 [pdf]](https://teorth.github.io/tao-web/slides/math-2-0-caltech-2026.pdf)**
   255 points by `Anon84` - [309 comments](https://news.ycombinator.com/item?id=50043026)

7. **[NYC's "Click to Cancel" rule is now in effect](https://www.nyc.gov/main/click-to-cancel)**
   225 points by `gregsadetsky` - [91 comments](https://news.ycombinator.com/item?id=50045946)

8. **[I guess I'm using WebP now?](https://anderegg.ca/2026/10/08/i-guess-im-using-webp-now)**
   42 points by `Brajeshwar` - [30 comments](https://news.ycombinator.com/item?id=50021989)

9. **[The Unreasonable Effectiveness of Vex in NixOS](https://blog.kammel.dev/post/nixos_vex/)**
   19 points by `datosh` - [0 comments](https://news.ycombinator.com/item?id=50046864)

10. **[apsw: Another Python SQLite Wrapper](https://github.com/rogerbinns/apsw)**
   42 points by `tosh` - [12 comments](https://news.ycombinator.com/item?id=50045273)
