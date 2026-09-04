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

## Latest snapshot - [`2026-09-04.md`](./digests/2026-09-04.md)

_Captured 2026-09-04 15:30 UTC._

1. **[Google AI Mode shows same products 21.6% more expensive than traditional search](https://productrise.app/blog/google-ai-mode-prefers-more-expensive-products)**
   163 points by `DeepLogin` - [25 comments](https://news.ycombinator.com/item?id=49563386)

2. **[Discovery of a new OpenAI agent message board](https://collusion.wiki/)**
   602 points by `moultano` - [416 comments](https://news.ycombinator.com/item?id=49563355)

3. **[Solving the Jane Street Reverse Engineering Challenge](https://jestoph.com/2026/09/04/jane-street-challenge.html)**
   220 points by `anitil` - [58 comments](https://news.ycombinator.com/item?id=49562657)

4. **[GPT-6 Astra](https://openai.com/index/gpt-6-astra/)**
   1996 points by `kibae` - [1825 comments](https://news.ycombinator.com/item?id=49554643)

5. **[Ok, but Does It Scale?](https://spacetimedb.com/blog/how-does-spacetime-scale)**
   55 points by `theanonymousone` - [26 comments](https://news.ycombinator.com/item?id=49563772)

6. **[.name Termination](https://neil.fraser.name/news/2026/09/03/)**
   2046 points by `pavel_lishin` - [499 comments](https://news.ycombinator.com/item?id=49550772)

7. **[The Two Abstractions of System Design: Hide or Reduce](http://muratbuffalo.blogspot.com/2026/05/the-two-abstractions-of-system-design.html)**
   31 points by `ubolonton_` - [2 comments](https://news.ycombinator.com/item?id=49534936)

8. **[Elevator of the Year Winner Modernization of the Metropolis Trust Building](https://www.starelevator.com/projects/star-elevator-modernization-of-the-metropolis-trust-building)**
   70 points by `palashawas` - [24 comments](https://news.ycombinator.com/item?id=49516312)

9. **[GMails custom domain "send as" discontinues January 2027](https://support.google.com/mail/answer/22370?hl=en)**
   20 points by `sva_` - [16 comments](https://news.ycombinator.com/item?id=49565693)

10. **[Qwen 3.8 27B available on Cerebras at 1500 tokens/s](https://inference-docs.cerebras.ai/models/overview)**
   629 points by `altertable` - [208 comments](https://news.ycombinator.com/item?id=49554520)
