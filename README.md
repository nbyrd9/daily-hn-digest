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

_Captured 2026-10-11 10:41 UTC._

1. **[IRCv3](https://ircv3.net/)**
   32 points by `basilikum` - [8 comments](https://news.ycombinator.com/item?id=50041540)

2. **[LineageOS 24.0](https://lineageos.org/Changelog-32/)**
   114 points by `timschumi` - [26 comments](https://news.ycombinator.com/item?id=50040276)

3. **[Build your own decision model](https://nishtahir.com/build-your-own-decision-model/)**
   316 points by `softwaredoug` - [72 comments](https://news.ycombinator.com/item?id=50037949)

4. **[2D Vehicles](https://patkerr.co.uk/2d-vehicles/)**
   489 points by `Michelangelo11` - [102 comments](https://news.ycombinator.com/item?id=49991852)

5. **[A city-building game in which the city would prefer you didn't](https://housing.over.pizza/)**
   355 points by `JumpCrisscross` - [120 comments](https://news.ycombinator.com/item?id=50036864)

6. **[The Lightbulb Computer](https://lightbulbcomputer.com/)**
   434 points by `oskarth` - [66 comments](https://news.ycombinator.com/item?id=50029487)

7. **[How big is a Git commit?](https://ratfactor.com/cards/git-commit-size)**
   38 points by `theanonymousone` - [17 comments](https://news.ycombinator.com/item?id=50017548)

8. **[European Alternatives](https://buy-european.net/en/alternatives)**
   69 points by `doener` - [36 comments](https://news.ycombinator.com/item?id=50039063)

9. **[Retrofitting language models to operate over bytes](https://www.nature.com/articles/s41586-026-11111-4)**
   70 points by `theanonymousone` - [7 comments](https://news.ycombinator.com/item?id=50001234)

10. **[PSPi 6 – Raspberry Pi in a PSP](https://github.com/othermod/PSPi-Version-6)**
   89 points by `therepanic` - [7 comments](https://news.ycombinator.com/item?id=50038623)
