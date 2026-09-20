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

## Latest snapshot - [`2026-09-20.md`](./digests/2026-09-20.md)

_Captured 2026-09-20 22:22 UTC._

1. **[Samsung is expected to more than double output of its HBM4 and HBM4E DRAM](https://en.sedaily.com/finance/2026/09/20/samsung-to-double-hbm4-output-next-year-sources-say)**
   250 points by `giuliomagnifico` - [176 comments](https://news.ycombinator.com/item?id=49778029)

2. **[ChatGPT now knows what you do on other websites via ad collector](https://www.buchodi.com/chatgpt-now-knows-what-you-do-on-other-websites-via-ad-collector/)**
   483 points by `lmbbuchodi` - [271 comments](https://news.ycombinator.com/item?id=49776729)

3. **[Qwen Image 2.1](https://qwen.ai/blog?id=qwen-image-2.1)**
   426 points by `jmillikin` - [145 comments](https://news.ycombinator.com/item?id=49775499)

4. **[Pirate Face Rescues LLM Models from Deletion](https://pirateface.co/)**
   373 points by `skepticalgenius` - [120 comments](https://news.ycombinator.com/item?id=49776699)

5. **[Nobody pays for FOSS, we can force them to](https://seldo.com/posts/nobody-pays-for-open-source-we-can-force-them-to/)**
   46 points by `Muhammad523` - [22 comments](https://news.ycombinator.com/item?id=49780064)

6. **[Apple iPhone 18 Pro Camera test](https://www.dxomark.com/apple-iphone-18-pro-camera-test/)**
   78 points by `luu` - [90 comments](https://news.ycombinator.com/item?id=49771218)

7. **[The Effect of CRTs on Pixel Art](https://datagubbe.se/crt/)**
   30 points by `tobr` - [10 comments](https://news.ycombinator.com/item?id=49768336)

8. **[Singapore’s National Library Board offers micropayments to build reading habits](https://www.gadgetreview.com/singapore-is-paying-people-to-put-down-their-phones-and-read-books)**
   154 points by `geox` - [64 comments](https://news.ycombinator.com/item?id=49776717)

9. **[A Necessary History of the Oddest Letter: W](https://lithub.com/a-necessary-history-of-the-oddest-letter-w/)**
   74 points by `NaOH` - [43 comments](https://news.ycombinator.com/item?id=49778195)

10. **[Nipple tattooist 'frustrated' by online censorship](https://www.bbc.com/news/articles/cx2z7ejn891o)**
   11 points by `harry_nutsachs` - [6 comments](https://news.ycombinator.com/item?id=49780466)
