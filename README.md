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

## Latest snapshot - [`2026-11-01.md`](./digests/2026-11-01.md)

_Captured 2026-11-01 22:24 UTC._

1. **[Show HN: HackerBooks – HackerTube, but for books mentioned on HN](https://hackerbooks.org)**
   694 points by `roansh` - [157 comments](https://news.ycombinator.com/item?id=50326821)

2. **[HackerTube: YouTube built from videos recommended by HN](https://karpathy.bearblog.dev/hacker-tube/)**
   2124 points by `karpathy` - [519 comments](https://news.ycombinator.com/item?id=50319510)

3. **[Nibnib: Image compression with extreme decompression speed](https://github.com/raphlinus/nibnib)**
   46 points by `raphlinus` - [5 comments](https://news.ycombinator.com/item?id=50299811)

4. **[Tips for more effective fuzz testing with AFL++](https://nullprogram.com/blog/2025/02/05/)**
   42 points by `luu` - [4 comments](https://news.ycombinator.com/item?id=50271106)

5. **[New 3D thermal invisibility cloak makes objects disappear from infrared cameras](https://www.sciencedaily.com/releases/2026/10/261025073051.htm)**
   13 points by `stevenalowe` - [5 comments](https://news.ycombinator.com/item?id=50299427)

6. **[Mathematics has changed. Let's act like it](https://terrytao.wordpress.com/2026/11/01/mathematics-has-changed-lets-act-like-it/)**
   155 points by `smilelamp` - [178 comments](https://news.ycombinator.com/item?id=50328251)

7. **[Copper – A minimal low-level programming language with OOP and generics](https://tibleiz.net/copper/)**
   104 points by `bogdanoff_2` - [58 comments](https://news.ycombinator.com/item?id=50308754)

8. **[Ask HN: Which TV do you recommend for privacy?](https://news.ycombinator.com/item?id=50328896)**
   32 points by `LecroJS` - [75 comments](https://news.ycombinator.com/item?id=50328896)

9. **[An Italian farmer found some unknown seeds in his attic and planted them](https://www.smithsonianmag.com/science-nature/italian-farmer-found-unknown-seeds-attic-with-nothing-lose-planted-them-result-biblical-180989644/)**
   735 points by `ecares` - [194 comments](https://news.ycombinator.com/item?id=50320963)

10. **[Show HN: OmniDiff – Opensource, super fast, content aware Git difftool, in Rust](https://github.com/ivankovic/omnidiff)**
   109 points by `FabCH` - [34 comments](https://news.ycombinator.com/item?id=50325253)
