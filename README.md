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

## Latest snapshot - [`2026-11-22.md`](./digests/2026-11-22.md)

_Captured 2026-11-22 09:06 UTC._

1. **[Toyota, Nissan, and Honda to standardize parts to lower costs](https://www.caranddriver.com/news/a74490092/toyota-nissan-honda-standardize-parts-lower-costs/)**
   417 points by `zdw` - [231 comments](https://news.ycombinator.com/item?id=50596133)

2. **[Pill to treat pancreatic cancer hailed as 'biggest breakthrough in decades'](https://www.theguardian.com/society/2026/nov/20/pill-pancreatic-cancer-breakthrough-daraxonrasib)**
   947 points by `rafaelc` - [209 comments](https://news.ycombinator.com/item?id=50582069)

3. **[Lean verification of the Riemann Hypothesis](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/)**
   1006 points by `g-b-r` - [830 comments](https://news.ycombinator.com/item?id=50589618)

4. **[Show HN: The Riemann Proof Handbook](https://github.com/tamnd/riemann-handbook)**
   36 points by `tamnd` - [9 comments](https://news.ycombinator.com/item?id=50596664)

5. **[Notes on the discrete Fourier transform (DFT)](https://eli.thegreenplace.net/2026/notes-on-the-discrete-fourier-transform-dft/)**
   18 points by `kouosi` - [4 comments](https://news.ycombinator.com/item?id=50596960)

6. **[Inkling-2-Mini in 5.4 GB Memory](https://github.com/ShinMegamiBoson/lookatmyquant)**
   450 points by `k__` - [112 comments](https://news.ycombinator.com/item?id=50591853)

7. **[Data Processing Incidents on Inference Providers](https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers/)**
   136 points by `sdko` - [53 comments](https://news.ycombinator.com/item?id=50595554)

8. **[Sandwich Simulator](https://stulle.app/)**
   202 points by `subdomain` - [69 comments](https://news.ycombinator.com/item?id=50594911)

9. **[If tiny 'primordial' black holes exist](https://phys.org/news/2026-11-tiny-primordial-black-holes.html)**
   25 points by `wglb` - [0 comments](https://news.ycombinator.com/item?id=50569846)

10. **[Detonating a pile of lead azide](https://www.science.org/content/blog-post/detonating-huge-pile-lead-azide-really)**
   600 points by `beginning_end` - [385 comments](https://news.ycombinator.com/item?id=50588982)
