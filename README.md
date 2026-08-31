# Daily Hacker News Digest

A self-updating archive of the top 10 [Hacker News](https://news.ycombinator.com/)
stories. A scheduled GitHub Actions workflow captures the current standings
one to three times a day, at randomized times, rewriting the dated file for
the day under [`digests/`](./digests) and refreshing the snapshot below -- so
this repo doubles as a searchable record of what the tech community was
reading, and how the rankings shifted through the day.

- **How it works:** [`.github/workflows/daily-digest.yml`](./.github/workflows/daily-digest.yml)
  fires every 2 hours; [`scripts/scheduled_commit.py`](./scripts/scheduled_commit.py)
  uses a date-seeded RNG to pick 1-3 two-hour windows for the day, waits a
  random 0-85 minutes, then builds the digest via
  [`scripts/build_digest.py`](./scripts/build_digest.py), commits, and pushes.
- **Data source:** the public [Hacker News API](https://github.com/HackerNews/API)
  (no authentication).
- **Browse the archive:** [`digests/`](./digests)

---

## Latest snapshot - [`2026-08-31.md`](./digests/2026-08-31.md)

_Captured 2026-08-31 01:17 UTC._

1. **[“I just chose words carefully”](https://unsung.aresluna.org/i-just-chose-words-carefully/)**
   236 points by `zdw` - [59 comments](https://news.ycombinator.com/item?id=49503601)

2. **[Creepy Crawlies](https://people.kernel.org/monsieuricon/creepy-crawlies)**
   915 points by `zdw` - [420 comments](https://news.ycombinator.com/item?id=49491791)

3. **[Haiku R1/beta6 has been released](https://www.haiku-os.org/news/2026-08-26_haiku_r1_beta6)**
   250 points by `metrofun` - [75 comments](https://news.ycombinator.com/item?id=49499867)

4. **[Cores in space: The core memory module from a 1980 Spacelab computer](https://www.righto.com/2026/08/spacelab-core-memory.html)**
   74 points by `pwg` - [12 comments](https://news.ycombinator.com/item?id=49502214)

5. **[Show HN: NFC Energy-Harvesting PCB Business Card with an MCU](https://wilsonharper.net/projects/businesscard/)**
   92 points by `WilsonHarper` - [9 comments](https://news.ycombinator.com/item?id=49478426)

6. **[Sort branches by last commit date](https://ryangreenberg.com/til/git-branches-by-commit-date/)**
   86 points by `speckx` - [27 comments](https://news.ycombinator.com/item?id=49435285)

7. **[Continuous Diffusion Language Models (CDLM's)](https://sander.ai/2026/08/24/continuous-dlms.html)**
   52 points by `peter_d_sherman` - [15 comments](https://news.ycombinator.com/item?id=49502611)

8. **[Commercially Available Bike Generators Are Not Sustainable (2011)](https://solar.lowtechmagazine.com/2011/05/bike-powered-electricity-generators-are-not-sustainable/)**
   22 points by `baud147258` - [13 comments](https://news.ycombinator.com/item?id=49450461)

9. **[Relm4 makes developing beautiful cross-platform applications idiomatic](https://relm4.org/)**
   11 points by `Bluestein` - [7 comments](https://news.ycombinator.com/item?id=49446705)

10. **[Why open source rocks – a new SM750 (Silicon Motion GPU) HDMI Driver](https://github.com/KodeMunkie/sm750hdmifb)**
   65 points by `SillyUsername` - [33 comments](https://news.ycombinator.com/item?id=49501611)
