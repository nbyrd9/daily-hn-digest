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

## Latest snapshot - [`2026-09-25.md`](./digests/2026-09-25.md)

_Captured 2026-09-25 15:46 UTC._

1. **[Platform-Independent SIMD in Go](https://go.dev/blog/simd-experiment)**
   155 points by `yurivish` - [43 comments](https://news.ycombinator.com/item?id=49843269)

2. **[Classified Estimates Show the NSA Is Paying Billions to Test AI Models](https://www.washingtonsun.com/technology/classified-estimates-nsa-paying-billions-to-test-ai-models)**
   11 points by `rdmuser` - [4 comments](https://news.ycombinator.com/item?id=49845952)

3. **[Git-bug: Distributed, offline-first bug tracker embedded in Git](https://github.com/git-bug/git-bug)**
   141 points by `alentred` - [31 comments](https://news.ycombinator.com/item?id=49843174)

4. **[Allow Carriers on Planes](https://www.jefftk.com/p/allow-carriers-on-planes)**
   107 points by `surprisetalk` - [101 comments](https://news.ycombinator.com/item?id=49844786)

5. **[First Principles Thinking](https://sunilsadasivan.com/writing/first-principles-thinking/)**
   38 points by `sunils34` - [5 comments](https://news.ycombinator.com/item?id=49844736)

6. **[Pentium II at 600Mhz with Voodoo 3 Emulated on 86Box with M6 Mac Mini](https://nyaa.sh/reviews/mac-mini-m6-emulation)**
   171 points by `hugh4life` - [74 comments](https://news.ycombinator.com/item?id=49841285)

7. **[Ink and Switch Interactive Homepage](https://www.inkandswitch.com/)**
   122 points by `iFreilicht` - [17 comments](https://news.ycombinator.com/item?id=49842270)

8. **[Dutch governments builds alternative for Microsoft based on NixOS](https://www.dawo.community/en/)**
   740 points by `fjfaase` - [416 comments](https://news.ycombinator.com/item?id=49841563)

9. **[F-Droid 2.0](https://f-droid.org/2026/09/24/f-droid-2.0-a-new-chapter-for-android-freedom.html)**
   1358 points by `daveoc64` - [394 comments](https://news.ycombinator.com/item?id=49831968)

10. **[Boards of Casio](https://www.ambionix.com/blog/boards-of-casio/)**
   58 points by `fidotron` - [17 comments](https://news.ycombinator.com/item?id=49842084)
