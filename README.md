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

## Latest snapshot - [`2026-10-14.md`](./digests/2026-10-14.md)

_Captured 2026-10-14 15:17 UTC._

1. **[Iosevka is an open-source, sans-serif and slab-serif, monospace font](https://typeof.net/Iosevka/)**
   422 points by `otobrglez` - [157 comments](https://news.ycombinator.com/item?id=50084240)

2. **[Pg_vectorsearch: An index that is faster than pgvector's IVFFlat and HNSW](https://github.com/timescale/pg_vectorsearch)**
   94 points by `jascha_eng` - [33 comments](https://news.ycombinator.com/item?id=50086165)

3. **[ASML's strong orders ease fears AI spending boom is running out of steam](https://www.reuters.com/business/asml-forecasts-q4-sales-above-expectations-ai-chip-demand-2026-10-14/)**
   39 points by `tartoran` - [22 comments](https://news.ycombinator.com/item?id=50088430)

4. **[Passkeys Are Not a Trap](https://scotthelme.co.uk/passkeys-are-not-a-trap/)**
   3 points by `speckx` - [0 comments](https://news.ycombinator.com/item?id=50088935)

5. **[Amazon pushes up prices across the Internet](https://www.not-ship.com/how-amazon-pushes-up-prices-all-across-the-internet/)**
   361 points by `sighborg` - [342 comments](https://news.ycombinator.com/item?id=50084757)

6. **[TV4 postpones show after AI agent erases edited material](https://swedenherald.com/article/tv4-postpones-the-challenge-until-2027-after-technical-failure-erases-edited-footage)**
   79 points by `tobr` - [46 comments](https://news.ycombinator.com/item?id=50085323)

7. **[Pulsar at ESUG 2026 (new Smalltalk IDE)](https://blog.lorenzano.eu/pulsar-at-esug-2026/)**
   56 points by `mpweiher` - [9 comments](https://news.ycombinator.com/item?id=50085306)

8. **[The Gold-Bug: Edgar Allan Poe's story that taught me about cryptography (2024)](https://robotsinplainenglish.com/e/2024-01-21-gold-bug.html)**
   18 points by `ripe` - [0 comments](https://news.ycombinator.com/item?id=50055632)

9. **[Sound – Bartosz Ciechanowski (2022)](https://ciechanow.ski/sound/)**
   215 points by `dverlaeckt80` - [23 comments](https://news.ycombinator.com/item?id=50045147)

10. **[The Aaronson Oracle](https://aaronsonoracle.com/)**
   34 points by `routeroff` - [26 comments](https://news.ycombinator.com/item?id=50086484)
