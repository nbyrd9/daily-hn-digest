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

## Latest snapshot - [`2026-11-17.md`](./digests/2026-11-17.md)

_Captured 2026-11-17 00:14 UTC._

1. **[Carnegie Mellon is putting computer science courses on YouTube for free](https://www.cs.cmu.edu/learn/)**
   494 points by `pcompeau` - [85 comments](https://news.ycombinator.com/item?id=50522980)

2. **[BugMeNot has closed](https://www.bugmenot.com/)**
   239 points by `lode` - [118 comments](https://news.ycombinator.com/item?id=50523601)

3. **[Windows 11 Is Collecting Data on Which Coding Agents and Developer Tools You Use](https://xusheng.dev/posts/windows-coding-agent-telemetry/)**
   60 points by `cwaffles` - [29 comments](https://news.ycombinator.com/item?id=50524736)

4. **[How to Break into Security, Ptacek Edition (2012)](https://krebsonsecurity.com/2012/06/how-to-break-into-security-ptacek-edition/)**
   58 points by `ronfriedhaber` - [14 comments](https://news.ycombinator.com/item?id=50524225)

5. **[World's Largest Brands Infected With Malware Via Optimizely](https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/)**
   117 points by `martinald` - [19 comments](https://news.ycombinator.com/item?id=50523300)

6. **[OpenCode Browse](https://opencode.ai/product/browse)**
   75 points by `mfiguiere` - [36 comments](https://news.ycombinator.com/item?id=50523459)

7. **[Grazing sheep in fields with solar arrays](https://news.cornell.edu/stories/2026/10/sheep-grazing-solar-fields-offers-farmers-economic-ecological-gains)**
   197 points by `PaulHoule` - [194 comments](https://news.ycombinator.com/item?id=50520182)

8. **[Jiff 1.0: A datetime library for Rust](https://burntsushi.net/jiff/)**
   287 points by `burntsushi` - [68 comments](https://news.ycombinator.com/item?id=50519744)

9. **[Chemistry is Actually Geometry](https://chillphysicsenjoyer.substack.com/p/chemistry-is-actually-geometry)**
   70 points by `sebg` - [16 comments](https://news.ycombinator.com/item?id=50522643)

10. **[Frame – 31.5" color ePaper display](https://trmnl.com/blog/introducing-frame)**
   273 points by `geerlingguy` - [193 comments](https://news.ycombinator.com/item?id=50519354)
