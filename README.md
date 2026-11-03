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

## Latest snapshot - [`2026-11-03.md`](./digests/2026-11-03.md)

_Captured 2026-11-03 18:16 UTC._

1. **[Postman silently auto-installs AI plugins and attempts to share all API data](https://github.com/postmanlabs/postman-app-support/issues/14370)**
   224 points by `sidgarimella` - [61 comments](https://news.ycombinator.com/item?id=50354960)

2. **[Jailbreaking my car's navigation system just so I can change the time](https://blog.nns.ee/2026/11/02/renault-hack/)**
   289 points by `xx_ns` - [96 comments](https://news.ycombinator.com/item?id=50339288)

3. **[Qwen 3.8 27B on my laptop can interpret model weights, too](https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/)**
   48 points by `theanonymousone` - [5 comments](https://news.ycombinator.com/item?id=50355251)

4. **[Mac at Any Scale](https://namespace.so/blog/mac-at-any-scale)**
   155 points by `anner_` - [68 comments](https://news.ycombinator.com/item?id=50352758)

5. **[Fujifilm to boost tape production 5x as AI fuels archiving demand](https://arstechnica.com/gadgets/2026/10/fujifilm-to-boost-tape-production-5x-as-ai-fuels-archiving-demand/)**
   222 points by `bookofjoe` - [83 comments](https://news.ycombinator.com/item?id=50336918)

6. **[Schools that block Google’s A.I. will lose student access to its search engine](https://www.nytimes.com/2026/11/03/us/google-search-schools-restrict-ai.html)**
   248 points by `ceejayoz` - [190 comments](https://news.ycombinator.com/item?id=50353192)

7. **[OpenAI seems to be silently re-enabling model training on Codex chats](https://news.ycombinator.com/item?id=50352757)**
   185 points by `user052919` - [62 comments](https://news.ycombinator.com/item?id=50352757)

8. **[USDB: Scaling Storage for Next-Generation Recommender Systems at ByteDance](https://arxiv.org/abs/2611.02618)**
   18 points by `1equalsequals1` - [1 comments](https://news.ycombinator.com/item?id=50354250)

9. **[Bear turns 10, and it still feels like day one](https://blog.bear.app/2026/11/bear-turns-10-and-it-still-feels-like-day-one/)**
   55 points by `psxuaw` - [27 comments](https://news.ycombinator.com/item?id=50353383)

10. **[The 'Astra can read and write weights to improve Qwen' post is misleading](https://honnibal.dev/blog/astra-read-write-misleading)**
   717 points by `syllogism` - [166 comments](https://news.ycombinator.com/item?id=50351111)
