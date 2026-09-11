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

## Latest snapshot - [`2026-09-11.md`](./digests/2026-09-11.md)

_Captured 2026-09-11 13:15 UTC._

1. **[The Waymo effect: how AI is quietly making research less collaborative](https://www.researchagenda.news/articles/the-waymo-effect.html)**
   139 points by `JohnHammersley` - [86 comments](https://news.ycombinator.com/item?id=49656496)

2. **[RTK reports token savings, but our cost benchmarks disagree](https://quesma.com/blog/does-rtk-make-ai-coding-cheaper/)**
   53 points by `michalwarda` - [26 comments](https://news.ycombinator.com/item?id=49656471)

3. **[Cherenkov Radiation - traveling faster than light](http://www.iaea.org/newscenter/news/what-is-cherenkov-radiation)**
   124 points by `andsoitis` - [71 comments](https://news.ycombinator.com/item?id=49655286)

4. **[So you want to use OpenRouter?](https://mmoustafa.com/blog/so-you-want-to-use-openrouter/)**
   277 points by `player85` - [62 comments](https://news.ycombinator.com/item?id=49621546)

5. **[Shopify is moving from React Native back to Swift and Kotlin](https://shopify.engineering/back-to-native)**
   1132 points by `fnthawar2` - [825 comments](https://news.ycombinator.com/item?id=49643982)

6. **[Ask HN: Can we please limit the AI news flood?](https://news.ycombinator.com/item?id=49657850)**
   15 points by `cromka` - [2 comments](https://news.ycombinator.com/item?id=49657850)

7. **[Show HN: Foldelight – the iPhone Duo folding effect the MacBook was owed](https://lufzle.dev/foldelight/)**
   7 points by `riffonio` - [2 comments](https://news.ycombinator.com/item?id=49656948)

8. **[Don't let anyone take away your big box of cables](https://blog.jim-nielsen.com/2026/hands-off-my-cables/)**
   613 points by `Brajeshwar` - [384 comments](https://news.ycombinator.com/item?id=49645393)

9. **[Claude is no longer available for minors](https://support.claude.com/en/articles/15171100-age-assurance-on-claude)**
   175 points by `Muhammad523` - [237 comments](https://news.ycombinator.com/item?id=49656225)

10. **[iPod Classic 6G in QEMU](https://www.reddit.com/r/emulation/s/VL4Au2HGxq)**
   52 points by `dmonterocrespo` - [7 comments](https://news.ycombinator.com/item?id=49611240)
