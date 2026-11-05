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

## Latest snapshot - [`2026-11-05.md`](./digests/2026-11-05.md)

_Captured 2026-11-05 23:38 UTC._

1. **[Search for everyone](https://kagi.com/changelog#11820)**
   397 points by `elashri` - [204 comments](https://news.ycombinator.com/item?id=50383740)

2. **[Claude Code sends your email address to websites](https://github.com/anthropics/claude-code/issues/107757)**
   201 points by `motoroco` - [51 comments](https://news.ycombinator.com/item?id=50385272)

3. **[MS Paint Remote Code Execution Vulnerability](https://www.cve.org/CVERecord?id=CVE-2026-83844)**
   233 points by `kuberwastaken` - [62 comments](https://news.ycombinator.com/item?id=50384233)

4. **[sshole](https://sshhole.com)**
   2215 points by `josemrb` - [556 comments](https://news.ycombinator.com/item?id=50378228)

5. **[Alpine Linux Security Advisory: OpenSSH-server password authentication bypass](https://alpinelinux.org/posts/2026-11-05-openssh-password-authentication-bypass/)**
   549 points by `pantalaimon` - [110 comments](https://news.ycombinator.com/item?id=50379704)

6. **[The Hackintosh Reborn](https://www.naut.ca/blog/2026/11/05/the-hackintosh-reborn-with-ai/)**
   160 points by `rubatuga` - [72 comments](https://news.ycombinator.com/item?id=50383057)

7. **[Tencent Launches Hy4, One of the Leading Open-Source AI Models](https://www.tencent.com/tencent-launches-hy4-joining-the-ranks-of-the-worlds-leading-open-source-ai-models/)**
   64 points by `gmays` - [1 comments](https://news.ycombinator.com/item?id=50383963)

8. **[Window Sweaters](https://github.com/saragordic/window-sweaters)**
   215 points by `nickswalker` - [76 comments](https://news.ycombinator.com/item?id=50381383)

9. **[Goodbye from Salon](https://www.salon.com/2026/11/05/goodbye-from-salon/)**
   337 points by `mkeeter` - [118 comments](https://news.ycombinator.com/item?id=50383739)

10. **[The Cost of Blogging](https://onlinegoddess.net/2026/11/the-cost-of-blogging/)**
   40 points by `speckx` - [33 comments](https://news.ycombinator.com/item?id=50383877)
