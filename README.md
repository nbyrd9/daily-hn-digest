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

## Latest snapshot - [`2026-10-03.md`](./digests/2026-10-03.md)

_Captured 2026-10-03 18:39 UTC._

1. **[ADHD, autism or complex trauma? [pdf]](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/30CC4826561366615BFAEC807CDE28A7/S0007125026108046a.pdf/adhd-autism-or-complex-trauma-the-complicated-nature-of-the-question.pdf)**
   27 points by `skeptical1884` - [0 comments](https://news.ycombinator.com/item?id=49946403)

2. **[FTL: A new operating system for clouds](https://ftl-os.org/)**
   88 points by `romac` - [39 comments](https://news.ycombinator.com/item?id=49944912)

3. **[Kolibri: A Sovereign Open-Weight Model](https://aleph-alpha.com/en/blog/kolibri-has-landed-a-sovereign-open-weight-model/)**
   290 points by `bastitx` - [222 comments](https://news.ycombinator.com/item?id=49942706)

4. **[Kolibri – Tech Report [pdf]](https://aleph-alpha.com/downloads/tech-report.pdf)**
   16 points by `yu3zhou4` - [0 comments](https://news.ycombinator.com/item?id=49946069)

5. **[Woking Electrical Control Room (2016)](http://www.darbiansphotography.com/woking-electrical-control-room-urbex)**
   95 points by `NaOH` - [15 comments](https://news.ycombinator.com/item?id=49938399)

6. **[Delta WiFi Survival Guide](https://dialta.adorellc.pro/)**
   5 points by `husky8` - [2 comments](https://news.ycombinator.com/item?id=49946482)

7. **[Hole Punch: Sling your spaceship around gravitational fields](https://notoriousbfg.com/hole-punch/)**
   5 points by `trwhite` - [0 comments](https://news.ycombinator.com/item?id=49946393)

8. **[C++ Insights – See your source code with the eyes of a Compiler](https://github.com/andreasfertig/cppinsights)**
   105 points by `rramadass` - [16 comments](https://news.ycombinator.com/item?id=49928361)

9. **[Body Awareness in Goffin's Cockatoos](https://www.nature.com/articles/s41598-026-57500-7)**
   24 points by `bryanrasmussen` - [3 comments](https://news.ycombinator.com/item?id=49913106)

10. **[Newgrounds.com – A community of games, music, and art](https://www.newgrounds.com/)**
   397 points by `azhenley` - [112 comments](https://news.ycombinator.com/item?id=49940394)
