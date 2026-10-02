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

## Latest snapshot - [`2026-10-02.md`](./digests/2026-10-02.md)

_Captured 2026-10-02 20:35 UTC._

1. **[Apple Pass Designer](https://developer.apple.com/pass-designer/)**
   151 points by `soheilpro` - [91 comments](https://news.ycombinator.com/item?id=49937276)

2. **[Court agrees with EFF: Utah's VPN law demands a technical impossibility](https://www.eff.org/deeplinks/2026/10/court-agrees-eff-utahs-vpn-law-demands-technical-impossibility)**
   338 points by `hn_acker` - [143 comments](https://news.ycombinator.com/item?id=49927754)

3. **[Updates to Full Disk Access in macOS](https://developer.apple.com/news/?id=p6zjojqw)**
   43 points by `notfirstpost` - [23 comments](https://news.ycombinator.com/item?id=49937631)

4. **[With most information hidden, the game Stratego had stumped AI until now](https://arstechnica.com/science/2026/10/ai-finally-beat-the-best-stratego-player-in-history-and-did-it-on-a-budget/)**
   87 points by `PaulHoule` - [25 comments](https://news.ycombinator.com/item?id=49933740)

5. **[A 12-year sequence of telescope images of a star and four planets orbiting](https://bsky.app/profile/theplanetaryguy.com/post/3mwucf5ert22f)**
   69 points by `mariuz` - [14 comments](https://news.ycombinator.com/item?id=49932147)

6. **[Greg Kroah-Hartman – Security in the LLM Age [video]](https://www.youtube.com/watch?v=NnV_cWeoo5Q)**
   91 points by `usernomdeguerre` - [14 comments](https://news.ycombinator.com/item?id=49929391)

7. **[Show HN: Made an open-source Lego AI generator](https://github.com/anteloc/ldraw-nova)**
   22 points by `antelocnova` - [6 comments](https://news.ycombinator.com/item?id=49937916)

8. **[Loss of cell identity drives human aging: Two new papers](https://erictopol.substack.com/p/loss-of-cell-identity-drives-human)**
   87 points by `bookofjoe` - [17 comments](https://news.ycombinator.com/item?id=49926411)

9. **[From the creator of Redis; run LLM locally with ds4](https://dwarfstar.sh/)**
   44 points by `fibo` - [4 comments](https://news.ycombinator.com/item?id=49936575)

10. **[Mike Tomlin spent 12 years building a Minecraft city](https://www.nytimes.com/athletic/7648198/2026/10/01/mike-tomlin-minecraft-nfl-coach/)**
   94 points by `CoryOndrejka` - [22 comments](https://news.ycombinator.com/item?id=49925184)
