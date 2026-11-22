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

_Captured 2026-11-22 17:37 UTC._

1. **[Open Social Web Alliance](https://osw-alliance.net/en/)**
   109 points by `doener` - [95 comments](https://news.ycombinator.com/item?id=50600511)

2. **[Show HN: I built a game where you are an LLM's subagent](https://github.com/gulivan/worker755)**
   135 points by `ivantgam` - [34 comments](https://news.ycombinator.com/item?id=50599762)

3. **[Toyota, Nissan, and Honda to standardize parts to lower costs](https://www.caranddriver.com/news/a74490092/toyota-nissan-honda-standardize-parts-lower-costs/)**
   960 points by `zdw` - [568 comments](https://news.ycombinator.com/item?id=50596133)

4. **[Perplexity and Intelligence](https://openai.com/index/perplexity-and-intelligence/)**
   8 points by `acossta` - [3 comments](https://news.ycombinator.com/item?id=50601525)

5. **[Pill to treat pancreatic cancer hailed as 'biggest breakthrough in decades'](https://www.theguardian.com/society/2026/nov/20/pill-pancreatic-cancer-breakthrough-daraxonrasib)**
   1255 points by `rafaelc` - [272 comments](https://news.ycombinator.com/item?id=50582069)

6. **[A Better Vocabulary for Testing](https://alperenkeles.com/posts/vocab-for-testing/)**
   40 points by `alpaylan` - [12 comments](https://news.ycombinator.com/item?id=50594182)

7. **[I joined the NTP Pool, but not with my Stratum 1 Pi](https://www.jeffgeerling.com/blog/2026/i-joined-the-ntp-pool/)**
   19 points by `fortran77` - [0 comments](https://news.ycombinator.com/item?id=50600622)

8. **[Europe weakens chemical rules as science links them to 'lifestyle diseases'](https://www.lemonde.fr/en/opinion/article/2026/11/22/as-science-increasingly-shows-the-role-chemical-substances-play-in-lifestyle-diseases-europe-weakens-its-regulations_6786595_23.html)**
   66 points by `atmosx` - [33 comments](https://news.ycombinator.com/item?id=50600677)

9. **[Lean verification of the Riemann Hypothesis](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/)**
   1164 points by `g-b-r` - [964 comments](https://news.ycombinator.com/item?id=50589618)

10. **[The Where's Waldo of the 1500s](https://blog.alexbeals.com/posts/il-civetta)**
   35 points by `speckx` - [7 comments](https://news.ycombinator.com/item?id=50551397)
