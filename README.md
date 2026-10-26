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

## Latest snapshot - [`2026-10-26.md`](./digests/2026-10-26.md)

_Captured 2026-10-26 22:53 UTC._

1. **[Working with academic communities to build scientific understanding](https://openai.com/index/building-scientific-understanding-with-academic-communities/)**
   158 points by `jonluca` - [39 comments](https://news.ycombinator.com/item?id=50251344)

2. **[CorridorKey 2.0](https://corridorkey.com/)**
   91 points by `ravenical` - [21 comments](https://news.ycombinator.com/item?id=50251127)

3. **[Type Server Protocol](https://github.com/microsoft/pylance-release/blob/main/docs/tsp/type-server-protocol.md)**
   168 points by `adamnemecek` - [125 comments](https://news.ycombinator.com/item?id=50248371)

4. **[Sebastian Raschka's from-scratch video course on building reasoning models](https://magazine.sebastianraschka.com/p/building-reasoning-models)**
   502 points by `sgiannopoulos` - [76 comments](https://news.ycombinator.com/item?id=50245138)

5. **[CSS-Tricks has a new owner](https://css-tricks.com/css-tricks-has-a-new-owner/)**
   342 points by `edent` - [79 comments](https://news.ycombinator.com/item?id=50245831)

6. **[Cross-request KV cache exposure in the GLM-5.3 Workers AI model (155 responses)](https://blog.cloudflare.com/kv-cache-exposure-remediation/)**
   8 points by `wondersky` - [1 comments](https://news.ycombinator.com/item?id=50252159)

7. **[Oldest GUI application that still runs on Windows 11](https://blog.enlyth.com/posts/oldest-windows-gui-app-win-11/)**
   221 points by `enlyth` - [130 comments](https://news.ycombinator.com/item?id=50248055)

8. **[A Printer Printing onto Paper](https://twitter.com/macrofying/status/2112904628509528219)**
   8 points by `MrBuddyCasino` - [0 comments](https://news.ycombinator.com/item?id=50204697)

9. **[Nietzschian Debugger](https://github.com/DilawarShafiq/nietzschian-debugger)**
   111 points by `dilawargopang` - [37 comments](https://news.ycombinator.com/item?id=50247493)

10. **[GPT-6.1 Terra](https://openai.com/index/introducing-gpt-6-1-terra/)**
   444 points by `meetpateltech` - [283 comments](https://news.ycombinator.com/item?id=50248124)
