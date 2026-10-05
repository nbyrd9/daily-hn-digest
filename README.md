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

## Latest snapshot - [`2026-10-05.md`](./digests/2026-10-05.md)

_Captured 2026-10-05 23:50 UTC._

1. **[ChatGPT is adding real cartoonists' signatures to fake New Yorker cartoons](https://www.niemanlab.org/2026/10/chatgpt-is-adding-real-cartoonists-signatures-to-fake-new-yorker-cartoons/)**
   38 points by `rdmuser` - [3 comments](https://news.ycombinator.com/item?id=49971846)

2. **[Beam: Reflection's 501B open-weight model](https://reflection.ai/blog/introducing-beam)**
   269 points by `Philpax` - [72 comments](https://news.ycombinator.com/item?id=49969183)

3. **[Find the flattest route between any two points in SF](https://flattensf.com/)**
   76 points by `ishan0102` - [20 comments](https://news.ycombinator.com/item?id=49971230)

4. **[Example.com Just Launched the Biggest Redesign in Decades](https://www.debugbear.com/blog/example-dot-com-redesign-history)**
   29 points by `jgx0` - [19 comments](https://news.ycombinator.com/item?id=49971921)

5. **[Dust: Pretraining Transformers Without Backpropagation](https://qlabs.sh/research/dust)**
   73 points by `E-Reverance` - [5 comments](https://news.ycombinator.com/item?id=49970871)

6. **[Opus 5.5 agents discover two room-temperature magnetic semiconductor candidates](https://www.vals.ai/blogs/room-temperature-magnetic-semiconductors)**
   173 points by `outlier99` - [131 comments](https://news.ycombinator.com/item?id=49970667)

7. **[Ephemeral Testing](https://lemire.me/blog/2026/10/05/ephemeral-testing/)**
   8 points by `ibobev` - [0 comments](https://news.ycombinator.com/item?id=49972008)

8. **[Using Blu-ray M-Disk as backup of last resort](https://smyck.net/2026/10/03/holocron-the-backup-of-last-resort/)**
   41 points by `hukl` - [38 comments](https://news.ycombinator.com/item?id=49951693)

9. **[Worth Building](https://armstr.ng/writing/worth-building)**
   17 points by `colinarms` - [4 comments](https://news.ycombinator.com/item?id=49971952)

10. **[Web Search API](https://developers.cloudflare.com/changelog/post/2026-10-02-introducing-web-search-api/)**
   472 points by `tosh` - [214 comments](https://news.ycombinator.com/item?id=49963171)
