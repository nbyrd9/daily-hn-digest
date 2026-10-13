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

## Latest snapshot - [`2026-10-13.md`](./digests/2026-10-13.md)

_Captured 2026-10-13 10:04 UTC._

1. **[The baffling intelligence of a single cell (2024)](https://jsomers.net/e-coli-chemotaxis/)**
   282 points by `jsomers` - [59 comments](https://news.ycombinator.com/item?id=50041866)

2. **[Were Software Engineers blue-collar workers all along?](https://ptrbrynt.com/posts/were-we-blue-collar-workers-all-along)**
   62 points by `ilreb` - [71 comments](https://news.ycombinator.com/item?id=50068946)

3. **[GLM-Legal](https://z.ai/blog/glm-legal)**
   563 points by `ilreb` - [316 comments](https://news.ycombinator.com/item?id=50058507)

4. **[Intel D270 GPU AI Accelerator–Up to 480 GB LPDDR5X](https://www.intel.com/content/www/us/en/products/details/discrete-gpus/data-center-gpu/d-series.html)**
   209 points by `hurricanepootis` - [107 comments](https://news.ycombinator.com/item?id=50063365)

5. **[Hackers activate automatic defrosting in supermarket fridges across Europe](https://www.tomshardware.com/tech-industry/cyber-security/unprecedented-cyberattack-cripples-supermarket-fridges-across-europe-as-hackers-activate-automatic-defrosting-delivery-and-store-prices-also-impacted-by-incident)**
   700 points by `Zeekaas` - [820 comments](https://news.ycombinator.com/item?id=50055304)

6. **[A Modern Web App in C](https://prophitt.me/writing/a-modern-web-app-in-c)**
   565 points by `prophittcorey` - [238 comments](https://news.ycombinator.com/item?id=50058528)

7. **[Who is vfmaddrnd231pd?](https://purplesyringa.moe/blog/who-is-vfmaddrnd231pd/)**
   204 points by `pngmangi` - [20 comments](https://news.ycombinator.com/item?id=50063138)

8. **[Document Review with Unsiloed and TypeSafe Jev](https://www.unsiloed.ai/blog/document-review-unsiloed-typesafe-jev)**
   7 points by `ritzaco` - [1 comments](https://news.ycombinator.com/item?id=50068443)

9. **[DishwasherBench – Can Frontier Models Stack a Dishwasher?](https://github.com/composo-ai/DishwasherBench)**
   44 points by `mlukewizard` - [17 comments](https://news.ycombinator.com/item?id=50068437)

10. **[Janas: Run LLMs larger than RAM by streaming experts from SSD](https://github.com/prabanta-dev/janas)**
   142 points by `khalidkhair` - [46 comments](https://news.ycombinator.com/item?id=50063717)
