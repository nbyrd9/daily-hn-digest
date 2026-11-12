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

## Latest snapshot - [`2026-11-12.md`](./digests/2026-11-12.md)

_Captured 2026-11-12 22:06 UTC._

1. **[Jensen Huang resigns](https://apnews.com/article/nvidia-megaspeed-china-singapore-huang-5403f152a601cf82ce939f1d24fffa0f)**
   2509 points by `lldb` - [2432 comments](https://news.ycombinator.com/item?id=50467087)

2. **[Rust 1.100](https://blog.rust-lang.org/2026/11/12/Rust-1.100.0/)**
   182 points by `mbStavola` - [103 comments](https://news.ycombinator.com/item?id=50472038)

3. **[Gemini 4 Hydrogen and Orchestrator](https://antigravity.google/blog/gemini-4-hydrogen-in-google-antigravity/)**
   181 points by `jonbaer` - [38 comments](https://news.ycombinator.com/item?id=50472260)

4. **[Dwarf planet candidate appears which takes roughly 280 years to orbit our sun](https://www.smithsonianmag.com/smart-news/astronomers-found-a-mysterious-object-orbiting-far-beyond-pluto-it-could-be-a-new-dwarf-planet-hidden-in-our-solar-system-180989857/)**
   123 points by `cybermango` - [54 comments](https://news.ycombinator.com/item?id=50472490)

5. **[Foundation Models Framework (macOS)](https://developer.apple.com/foundation-models-framework/)**
   30 points by `kermatt` - [4 comments](https://news.ycombinator.com/item?id=50474361)

6. **[Show HN: My $300 embroidery machine needed a subscription, so I built my own app](https://github.com/simpsoka/zigzag)**
   203 points by `simpsoka` - [83 comments](https://news.ycombinator.com/item?id=50470488)

7. **[Service degradation on Microsoft 365](https://status.cloud.microsoft/)**
   302 points by `dkpk` - [315 comments](https://news.ycombinator.com/item?id=50471731)

8. **[Anthropic IPO](https://ipo.anthropic.com/us/)**
   738 points by `josephljohnston` - [747 comments](https://news.ycombinator.com/item?id=50465829)

9. **[22-Year-Old PostgreSQL Bug Turned into Remote Code Execution](https://mehmetince.net/part-3-6-how-i-ended-up-turning-a-22-year-old-postgresql-type-confusion-primitive-into-rce-cve-2026-6460/)**
   85 points by `ozirus` - [10 comments](https://news.ycombinator.com/item?id=50471761)

10. **[I'm making LLMs work on small and old devices](https://github.com/hyperionaidev/smolmaxxing/)**
   230 points by `mrashad74` - [84 comments](https://news.ycombinator.com/item?id=50468888)
