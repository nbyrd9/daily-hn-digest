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

## Latest snapshot - [`2026-09-17.md`](./digests/2026-09-17.md)

_Captured 2026-09-17 22:46 UTC._

1. **[Astra for Law](https://openai.com/index/astra-for-law/)**
   194 points by `vertigoruntime` - [197 comments](https://news.ycombinator.com/item?id=49745940)

2. **[Bend – A language that blocks AI mistakes via proof, on CPU and GPU](https://bend-lang.com/)**
   185 points by `nicolas-siplis` - [100 comments](https://news.ycombinator.com/item?id=49746163)

3. **[Bonsai 2 27B: Near-Lossless Compression in a 9x Smaller Footprint](https://prismml.com/news/bonsai-2-27b)**
   90 points by `JonSchneider` - [22 comments](https://news.ycombinator.com/item?id=49746618)

4. **[Hister: A private search engine for the pages you visit and the files you keep](https://github.com/asciimoo/hister)**
   387 points by `bookofjoe` - [120 comments](https://news.ycombinator.com/item?id=49743097)

5. **[Sex, AI, and the Apocalypse](https://www.iankduncan.com/personal/2026-09-16-sex-ai-and-the-apocalypse/)**
   47 points by `Anon84` - [14 comments](https://news.ycombinator.com/item?id=49746654)

6. **[Wax motor](https://en.wikipedia.org/wiki/Wax_motor)**
   162 points by `mhb` - [37 comments](https://news.ycombinator.com/item?id=49726007)

7. **[Fujitsu launches made-in-Japan next-generation CPU FUJITSU-MONAKA](https://global.fujitsu/en-global/pr/news/2026/09/14-02)**
   473 points by `my123` - [174 comments](https://news.ycombinator.com/item?id=49715813)

8. **[Flet 1.0 – Build cross-platform apps in Python](https://flet.dev/)**
   19 points by `absqueued` - [3 comments](https://news.ycombinator.com/item?id=49746290)

9. **[CrowdSec Source Code Leak](https://www.crowdsec.net/blog/crowdsec-statement-source-code-exposure)**
   118 points by `eccgecko` - [34 comments](https://news.ycombinator.com/item?id=49742355)

10. **[Everybody's Lost Their Minds](https://www.netmeister.org/blog/everybodys-lost-their-minds.html)**
   248 points by `ibobev` - [161 comments](https://news.ycombinator.com/item?id=49745570)
