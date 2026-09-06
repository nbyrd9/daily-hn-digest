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

## Latest snapshot - [`2026-09-06.md`](./digests/2026-09-06.md)

_Captured 2026-09-06 22:50 UTC._

1. **[GrapheneOS Overhauled Default Apps and Secure Clipboard](https://grapheneos.social/@GrapheneOS/117225539756835649)**
   103 points by `Cider9986` - [31 comments](https://news.ycombinator.com/item?id=49590512)

2. **[Show HN: Mador – Make any DOM reactive with a tiny 80-line Proxy state tuple](https://github.com/marsbos/mador)**
   44 points by `bosmarcel` - [17 comments](https://news.ycombinator.com/item?id=49590738)

3. **[Your intellectual fly is open (2025)](https://bcantrill.dtrace.org/2025/12/05/your-intellectual-fly-is-open/)**
   460 points by `cyb0rg0` - [294 comments](https://news.ycombinator.com/item?id=49585644)

4. **[It took a year to ship WebAssembly in Anubis](https://anubis.techaro.lol/blog/2026/anubis-wasm/)**
   93 points by `xena` - [57 comments](https://news.ycombinator.com/item?id=49590611)

5. **[Isar Aerospace reaches orbit and deploys payloads on second flight](https://isaraerospace.com/press/history-for-european-spaceflight-isar-aerospace-reaches-orbit-and-deploys-payloads-on-second-flight)**
   530 points by `mpweiher` - [172 comments](https://news.ycombinator.com/item?id=49584083)

6. **[Black Hole of Los Alamos Seller of surplus nuclear research materials (2011)](https://www.atlasobscura.com/places/black-hole-of-los-alamos)**
   24 points by `Bluestein` - [6 comments](https://news.ycombinator.com/item?id=49540637)

7. **[NetBSD 9.5 released and EOL for NetBSD-9](https://blog.netbsd.org/tnf/entry/netbsd_9_5_released_and)**
   97 points by `jaypatelani` - [4 comments](https://news.ycombinator.com/item?id=49587636)

8. **[Babylonian Lamb Stew with Beets (1750–1730 BCE)](https://babylonian-collection.yale.edu/about/babylonian-cooking)**
   72 points by `yubblegum` - [28 comments](https://news.ycombinator.com/item?id=49554622)

9. **[Show HN: VODForge – a free local desktop UI for YouTube video/playlist downloads](https://getvodforge.com/)**
   27 points by `coopernusbaum` - [5 comments](https://news.ycombinator.com/item?id=49590354)

10. **[Harnessing the Universal Geometry of Embeddings](https://arxiv.org/abs/2505.12540)**
   15 points by `ur-whale` - [2 comments](https://news.ycombinator.com/item?id=49590595)
