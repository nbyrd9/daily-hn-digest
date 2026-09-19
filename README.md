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

## Latest snapshot - [`2026-09-19.md`](./digests/2026-09-19.md)

_Captured 2026-09-19 17:26 UTC._

1. **[Laya the open source version of Jev](https://laya.convaiinnovations.com/)**
   600 points by `nandakishor_ml` - [145 comments](https://news.ycombinator.com/item?id=49765348)

2. **[A graphical desktop for the ZX Spectrum](https://github.com/mindbox77/zxdesk)**
   82 points by `graemep` - [58 comments](https://news.ycombinator.com/item?id=49766676)

3. **[AI-generated posters don’t have to be horrible](https://john.hartnup.uk/2026/06/07/ai-event-posters.html)**
   801 points by `ereiamjh` - [481 comments](https://news.ycombinator.com/item?id=49764791)

4. **[Human brain is two separate organs, Stanford Medicine-led research finds](https://med.stanford.edu/news/all-news/2026/09/two-separate-brains.html)**
   506 points by `emigre` - [186 comments](https://news.ycombinator.com/item?id=49763697)

5. **[Tin: full-text search for Postgres](https://planetscale.com/blog/introducing-tin)**
   93 points by `ksec` - [45 comments](https://news.ycombinator.com/item?id=49766611)

6. **[Asking Authors About Their Own Papers](https://medium.com/@TmlrOrg/asking-authors-about-their-own-papers-3d2e04e5dee0)**
   77 points by `stefanpie` - [40 comments](https://news.ycombinator.com/item?id=49734467)

7. **[“The Secret Life of Circuits” is here](https://blog.coredump.cx/p/the-secret-life-of-circuits-is-here)**
   202 points by `surprisetalk` - [54 comments](https://news.ycombinator.com/item?id=49720143)

8. **[Black Holes or Black Hole Stars? Astronomers Spar over 'Little Red Dots'](https://www.quantamagazine.org/black-holes-or-black-hole-stars-astronomers-spar-over-webb-telescopes-little-red-dots-20260914/)**
   53 points by `jandrewrogers` - [17 comments](https://news.ycombinator.com/item?id=49756121)

9. **[Android 17 is the first since 3.x to add new APIs without releasing to the AOSP](https://grapheneos.social/@GrapheneOS/117282080803799576)**
   992 points by `theanonymousone` - [555 comments](https://news.ycombinator.com/item?id=49758736)

10. **[GPT-6 Astra Solves a WWI German Radio Cipher](https://www.prinzai.com/p/gpt-6-astra-solves-a-wwi-german-radio)**
   264 points by `nsoonhui` - [135 comments](https://news.ycombinator.com/item?id=49763987)
