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

## Latest snapshot - [`2026-11-06.md`](./digests/2026-11-06.md)

_Captured 2026-11-06 13:42 UTC._

1. **[Dutch 'idealist' bank ASN blocks non-Google Android, including GrapheneOS](https://github.com/PrivSec-dev/banking-apps-compat-report/issues/105)**
   299 points by `microtonal` - [188 comments](https://news.ycombinator.com/item?id=50390124)

2. **[Blender's UI and Runtime: Much Faster Than GPUI](https://github.com/ppmpreetham/BUI)**
   363 points by `ppmpreetham` - [150 comments](https://news.ycombinator.com/item?id=50389333)

3. **[Claude Code sends your email address to websites](https://github.com/anthropics/claude-code/issues/107757)**
   1298 points by `motoroco` - [409 comments](https://news.ycombinator.com/item?id=50385272)

4. **[We've built an open-source feature flag server for 11 years](https://github.com/Unleash/unleash)**
   33 points by `ivarconr` - [14 comments](https://news.ycombinator.com/item?id=50391145)

5. **[Living beyond the limits of survival: wood ants trapped in a gigantic pitfall (2016)](https://jhr.pensoft.net/articles.php?id=9096)**
   71 points by `hitekker` - [24 comments](https://news.ycombinator.com/item?id=50390525)

6. **[sshole](https://sshhole.com)**
   2790 points by `josemrb` - [677 comments](https://news.ycombinator.com/item?id=50378228)

7. **[Kugelblitz – Mac-Native Google Earth Alternative](https://apps.metaebene.me/en/kugelblitz)**
   134 points by `luoc` - [42 comments](https://news.ycombinator.com/item?id=50389370)

8. **[Tesla winds down Cybertruck production after years of poor sales in few markets](https://www.msn.com/en-us/technology/tech-companies/tesla-to-wind-down-cybertruck-production-after-years-of-poor-sales-in-few-markets/ar-AA2gSZGv)**
   80 points by `PLenz` - [49 comments](https://news.ycombinator.com/item?id=50391456)

9. **[MS Paint Remote Code Execution Vulnerability](https://www.cve.org/CVERecord?id=CVE-2026-83844)**
   600 points by `kuberwastaken` - [222 comments](https://news.ycombinator.com/item?id=50384233)

10. **[From Linux to Wikipedia: How Volunteers Build the Internet](https://thereader.mitpress.mit.edu/from-linux-to-wikipedia-how-volunteers-build-the-internet/)**
   160 points by `jonbaer` - [54 comments](https://news.ycombinator.com/item?id=50388122)
