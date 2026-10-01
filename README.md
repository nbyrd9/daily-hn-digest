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

## Latest snapshot - [`2026-10-01.md`](./digests/2026-10-01.md)

_Captured 2026-10-01 21:00 UTC._

1. **[Pi 1.0](https://earendil.com/posts/pi-1-0/)**
   305 points by `sergiotapia` - [109 comments](https://news.ycombinator.com/item?id=49926069)

2. **[Clef: Open-source decision models, and new RL fine-tuning platform](https://blog.cloudflare.com/clef-decision-models/)**
   334 points by `jasondavies` - [134 comments](https://news.ycombinator.com/item?id=49923692)

3. **[Car Is a Smartphone on Wheels. Here's Who's Listening](https://automatictransmission.khoury.northeastern.edu/index.html)**
   21 points by `rafaelc` - [8 comments](https://news.ycombinator.com/item?id=49926628)

4. **[Oxygen-deprived underwater zones may not be "dead zones" but clue to early life](https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2026AV002570)**
   39 points by `gumby` - [1 comments](https://news.ycombinator.com/item?id=49925742)

5. **[RIP, vector database](https://turbopuffer.com/blog/rip-vector-database)**
   224 points by `razin` - [60 comments](https://news.ycombinator.com/item?id=49923466)

6. **[Pi Durable](https://earendil.com/posts/pi-durable/)**
   43 points by `paulsmith` - [1 comments](https://news.ycombinator.com/item?id=49925969)

7. **[StreetComplete on iOS is now in public beta](https://github.com/streetcomplete/StreetComplete/issues/5421)**
   472 points by `Snowly` - [109 comments](https://news.ycombinator.com/item?id=49920160)

8. **[Bez: Generating a browser engine from specs and tests](https://tangled.org/burrito.space/bez)**
   62 points by `nerdypepper` - [17 comments](https://news.ycombinator.com/item?id=49925036)

9. **[ArXiv's Updated Rate Limit Policy](https://blog.arxiv.org/2026/10/01/updated-rate-limit-policy/)**
   11 points by `50kIters` - [1 comments](https://news.ycombinator.com/item?id=49926512)

10. **[Ask HN: Who is hiring? (October 2026)](https://news.ycombinator.com/item?id=49922569)**
   114 points by `whoishiring` - [111 comments](https://news.ycombinator.com/item?id=49922569)
