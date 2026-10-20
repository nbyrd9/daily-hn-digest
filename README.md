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

## Latest snapshot - [`2026-10-20.md`](./digests/2026-10-20.md)

_Captured 2026-10-20 02:05 UTC._

1. **[Lula supporters protest against Meta to denounce its 'electoral interference'](https://efe.com/english/latest-news/2026-10-20/lula-supporters-protest-against-meta-to-denounce-its-electoral-interference/)**
   98 points by `jumpocelot` - [21 comments](https://news.ycombinator.com/item?id=50159993)

2. **[MiniMax M3.1 Flash](https://www.minimax.io/blog/minimax-m31f)**
   386 points by `jtg` - [166 comments](https://news.ycombinator.com/item?id=50154540)

3. **[I built a drone with only one motor [video]](https://www.youtube.com/watch?v=Ndftcft6XhU)**
   392 points by `hakonjdjohnsen` - [84 comments](https://news.ycombinator.com/item?id=50150089)

4. **[Wine ported to OpenBSD](https://marc.info/?l=openbsd-ports&m=179236125692175)**
   507 points by `iamnothere` - [168 comments](https://news.ycombinator.com/item?id=50152307)

5. **[OpenBSD 8.0 release will have inteldrm/radeondrm/amdgpu drivers from Linux 6.18](https://bsd.network/@brynet/117407035545900963)**
   92 points by `doener` - [14 comments](https://news.ycombinator.com/item?id=50158138)

6. **[Weball: Play Katamari on Websites](https://www.funwithcomputervision.com/weball/)**
   61 points by `croes` - [4 comments](https://news.ycombinator.com/item?id=50140584)

7. **[France's supermarket fridges were vulnerable online for months](https://ipinfo.io/blog/france-fridges-hack)**
   62 points by `emot` - [57 comments](https://news.ycombinator.com/item?id=50159616)

8. **[RuneScape Bench: MMOs for Agents [video]](https://www.youtube.com/watch?v=cNm4zyUtWj0)**
   158 points by `evakhoury` - [64 comments](https://news.ycombinator.com/item?id=50136126)

9. **[It's still ok to enjoy programming](https://chriskiehl.com/article/it-is-still-ok-to-enjoy-programming)**
   448 points by `goostavos` - [418 comments](https://news.ycombinator.com/item?id=50134472)

10. **[Android apps running native on macOS](https://github.com/kksimp/Mac.apk)**
   260 points by `flocked` - [137 comments](https://news.ycombinator.com/item?id=50154624)
