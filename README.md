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

_Captured 2026-11-17 06:50 UTC._

1. **[Carnegie Mellon is putting computer science courses on YouTube for free](https://www.cs.cmu.edu/learn/)**
   1202 points by `pcompeau` - [174 comments](https://news.ycombinator.com/item?id=50522980)

2. **[Windows 11 Is Collecting Data on Which Coding Agents and Developer Tools You Use](https://xusheng.dev/posts/windows-coding-agent-telemetry/)**
   468 points by `cwaffles` - [303 comments](https://news.ycombinator.com/item?id=50524736)

3. **[BugMeNot has closed](https://www.bugmenot.com/)**
   457 points by `lode` - [216 comments](https://news.ycombinator.com/item?id=50523601)

4. **[Optimizely compromised, served malware on Zoom, GitLab](https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/)**
   262 points by `kristjansson` - [103 comments](https://news.ycombinator.com/item?id=50524767)

5. **[If an App Asks for Full Disk Access or System and App Protection Override](https://support.apple.com/en-us/149699)**
   80 points by `jshier` - [48 comments](https://news.ycombinator.com/item?id=50526560)

6. **[Running coding agents without handing them my credentials](https://blog.antonio.cx/running-agents-with-lend)**
   91 points by `antoniomika` - [46 comments](https://news.ycombinator.com/item?id=50526152)

7. **[OpenCode Browse](https://opencode.ai/product/browse)**
   208 points by `mfiguiere` - [102 comments](https://news.ycombinator.com/item?id=50523459)

8. **[Why did modems have speakers? (2019)](https://retrocomputing.stackexchange.com/questions/11765)**
   40 points by `Skyfall106` - [20 comments](https://news.ycombinator.com/item?id=50510969)

9. **[Why 3dfx 1 cards had such a washed out color output?](https://twitter.com/id_aa_carmack/status/2122478083319992513)**
   79 points by `mfiguiere` - [10 comments](https://news.ycombinator.com/item?id=50525575)

10. **[Test/verification technique effectiveness with Astra](https://danluu.com/astra-testing/)**
   19 points by `luu` - [5 comments](https://news.ycombinator.com/item?id=50515035)
