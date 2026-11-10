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

## Latest snapshot - [`2026-11-10.md`](./digests/2026-11-10.md)

_Captured 2026-11-10 04:45 UTC._

1. **[Claude Fable 5.2 and Mythos 5.2](https://www.anthropic.com/claude-fable-and-mythos-5-2)**
   333 points by `lairv` - [676 comments](https://news.ycombinator.com/item?id=50429068)

2. **[USPS now offers official ZIP Code boundary polygons](https://postalpro.usps.com/zcb)**
   548 points by `munro` - [276 comments](https://news.ycombinator.com/item?id=50431058)

3. **[E-means: Outperforming k-means in one-tenth the epochs](https://e-means.github.io/)**
   314 points by `porridgeraisin` - [29 comments](https://news.ycombinator.com/item?id=50429734)

4. **[Payments Canada announces launch of Canada's Real-Time Rail (RTR) payment system](https://www.payments.ca/canada-launches-real-time-rail-bringing-247-payment-infrastructure-national-economy)**
   491 points by `ocd` - [274 comments](https://news.ycombinator.com/item?id=50427362)

5. **[Foldable Flight: The Best Paper Airplanes](https://www.foldableflight.com)**
   902 points by `vismit2000` - [144 comments](https://news.ycombinator.com/item?id=50424581)

6. **[Horible public key tricks](https://maurycyz.com/projects/badcert/)**
   73 points by `Curiositry` - [30 comments](https://news.ycombinator.com/item?id=50434264)

7. **[Locating the source of a mysterious beep](https://simonwillison.net/2026/Nov/9/mysterious-beeps/)**
   56 points by `bigwheels` - [30 comments](https://news.ycombinator.com/item?id=50434310)

8. **[How Many People Work from Home?](https://nicholasdecker.substack.com/p/how-many-people-work-from-home)**
   12 points by `surprisetalk` - [6 comments](https://news.ycombinator.com/item?id=50378118)

9. **[Exact – a new cross platform UI framework](https://github.com/expo/exact)**
   84 points by `vmg12` - [36 comments](https://news.ycombinator.com/item?id=50433541)

10. **[CoreWeave bond yield tops 16% as AI credit stress rises](https://www.cnbc.com/2026/11/06/coreweave-bond-yield-tops-16percent-as-ai-credit-stress-rises.html)**
   48 points by `lxm` - [16 comments](https://news.ycombinator.com/item?id=50435660)
