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

## Latest snapshot - [`2026-10-17.md`](./digests/2026-10-17.md)

_Captured 2026-10-17 21:13 UTC._

1. **[Bleached corals thrive within days when touching healthy neighbour](https://www.nature.com/articles/d41586-026-03266-x)**
   166 points by `alkyon` - [23 comments](https://news.ycombinator.com/item?id=50126253)

2. **[Chrome and Edge are removing XSLT: what breaks and what does not](https://doctor-seo.net/en/blog/news/chrome-edge-removing-xslt/)**
   27 points by `croes` - [17 comments](https://news.ycombinator.com/item?id=50134617)

3. **[The Commodore 64 hardware simulator: break chips and pins, see the results](https://github.com/antirez/c64-hw-simulator)**
   92 points by `antirez` - [17 comments](https://news.ycombinator.com/item?id=50100366)

4. **[Furifont, a Japanese font that shows furigana](https://furifont.antfu.me/)**
   181 points by `plaguna` - [42 comments](https://news.ycombinator.com/item?id=50100994)

5. **[Dam removals are bringing fish back across the northeastern United States](https://www.smithsonianmag.com/science-nature/dam-removals-are-bringing-fish-back-across-the-northeastern-united-states-striking-down-one-tiny-barrier-at-a-time-180989679/)**
   77 points by `sohkamyung` - [17 comments](https://news.ycombinator.com/item?id=50126312)

6. **[Making chicken transparent using Dorito dust](https://chillphysicsenjoyer.substack.com/p/making-chicken-transparent-using)**
   215 points by `crescit_eundo` - [59 comments](https://news.ycombinator.com/item?id=50131213)

7. **[DeepSeek-v4.1-Flash-1017](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)**
   583 points by `theykk` - [519 comments](https://news.ycombinator.com/item?id=50129045)

8. **[Pele – Mermaid diagrams as themeable SVG](https://pele.run/)**
   101 points by `dchest` - [13 comments](https://news.ycombinator.com/item?id=50132193)

9. **[Microsoft and CMU Team Up to Train Early Career Software Engineers](https://www.cs.cmu.edu/news/2026/microsoft-cmu-praise)**
   22 points by `azhenley` - [17 comments](https://news.ycombinator.com/item?id=50133830)

10. **[Gold is now the top U.S. export](https://www.numismaticnews.net/gold-now-top-u-s-export)**
   124 points by `iamnothere` - [63 comments](https://news.ycombinator.com/item?id=50132870)
