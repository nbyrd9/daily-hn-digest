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

## Latest snapshot - [`2026-10-18.md`](./digests/2026-10-18.md)

_Captured 2026-10-18 17:24 UTC._

1. **[macOS 15.8.2 Breaks OpenGL](https://developer.apple.com/forums/verify-human/verify.html?next=/forums/thread/850550)**
   165 points by `Audiophilip` - [117 comments](https://news.ycombinator.com/item?id=50141909)

2. **[RepRapMicron](https://github.com/VikOlliver/RepRapMicron/wiki)**
   194 points by `RobotToaster` - [27 comments](https://news.ycombinator.com/item?id=50141076)

3. **[Someone Behind the Software](https://karrisaarinen.com/posts/someone-behind-the-software/)**
   25 points by `tosh` - [5 comments](https://news.ycombinator.com/item?id=50142573)

4. **[Java sealed classes and exhaustive pattern matching](https://neilmadden.blog/2026/04/24/java-sealed-classes-and-exhaustive-pattern-matching/)**
   46 points by `hnisjafx40` - [12 comments](https://news.ycombinator.com/item?id=50141579)

5. **[DeepSeek search and fetch – $0.75 per 1000 successful requests](https://api-docs.deepseek.com/guides/search/)**
   425 points by `fagnerbrack` - [206 comments](https://news.ycombinator.com/item?id=50138531)

6. **[Legal experts warn Meta's new terms still grant broad scraping permissions](https://www.niemanlab.org/2026/10/legal-experts-warn-metas-new-terms-still-grant-broad-scraping-permissions-despite-language-changes/)**
   166 points by `DeepLogin` - [45 comments](https://news.ycombinator.com/item?id=50139692)

7. **[Sigsaly: Churchill's top secret hotline to the President](https://www.iwm.org.uk/history/iwm/cwr/telephone)**
   30 points by `stmw` - [0 comments](https://news.ycombinator.com/item?id=50096110)

8. **[Show HN: The Zelda timeline to catch up before the Ocarina of Time remake](https://legendofhyrule.com/)**
   86 points by `jsomau` - [35 comments](https://news.ycombinator.com/item?id=50140769)

9. **[The Intel 8087 chip: floating-point addition and subtraction](https://www.righto.com/2026/10/8087-addition-subtraction-microcode.html)**
   18 points by `pwg` - [3 comments](https://news.ycombinator.com/item?id=50142449)

10. **[Open MicroManipulator – A sub-micrometer 3D motion control plattform](https://github.com/0x23/MicroManipulatorStepper)**
   120 points by `_Microft` - [10 comments](https://news.ycombinator.com/item?id=50140001)
