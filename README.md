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

## Latest snapshot - [`2026-11-27.md`](./digests/2026-11-27.md)

_Captured 2026-11-27 17:09 UTC._

1. **[Show HN: bouncemarket – a live prediction market game for a bouncing ball](https://bouncemarket.minhanhday.com/)**
   167 points by `mday404` - [45 comments](https://news.ycombinator.com/item?id=50667726)

2. **[Credit card skimming scripts using WebRTC found on popular shopping sites](https://www.infohawk.com/news/2026-11-27-black-friday-webrtc-skimmer)**
   67 points by `scanr` - [23 comments](https://news.ycombinator.com/item?id=50668145)

3. **[First images of the impact of DART asteroid deflection experiment](https://arstechnica.com/space/2026/11/europes-hera-mission-returns-to-the-chaotic-scene-of-a-cosmic-smashup/)**
   103 points by `Bender` - [28 comments](https://news.ycombinator.com/item?id=50657392)

4. **[False Computer-Checked Proofs](https://cr.yp.to/proofs/falseccp.html)**
   40 points by `_tk_` - [17 comments](https://news.ycombinator.com/item?id=50667989)

5. **[Kimi for Science: More scientific ideas, made possible](https://www.kimi.ai/news/kimi-for-science-program)**
   139 points by `theanonymousone` - [97 comments](https://news.ycombinator.com/item?id=50665920)

6. **[The group chat where your AI talks behind your back](https://construct22.com/)**
   545 points by `utiiiD` - [241 comments](https://news.ycombinator.com/item?id=50663595)

7. **[A Deterministic Subexponential-Time Algorithm for the Discrete Logarithm Problem [pdf]](https://eprint.iacr.org/2026/3020.pdf)**
   170 points by `yuvadam` - [76 comments](https://news.ycombinator.com/item?id=50665968)

8. **[AI made self-hosting fun again](https://janlukas.blog/posts/ai-self-hosting)**
   958 points by `jlelse` - [458 comments](https://news.ycombinator.com/item?id=50660180)

9. **[US Air Force's cloud computing platform hacked](https://news.sky.com/story/us-air-forces-cloud-computing-platform-hacked-13617163)**
   180 points by `freakynit` - [99 comments](https://news.ycombinator.com/item?id=50666375)

10. **[Making a 3D fantasy map like a 16th-Century atlas](https://www.spritefusion.com/blog/making-a-fantasy-map-like-a-16th-century-atlas)**
   15 points by `HugoDz` - [1 comments](https://news.ycombinator.com/item?id=50667062)
