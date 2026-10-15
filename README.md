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

## Latest snapshot - [`2026-10-15.md`](./digests/2026-10-15.md)

_Captured 2026-10-15 09:56 UTC._

1. **[Things to know when you get cancer](https://jjmaxwell4.com/writing/things-to-know-when-you-get-cancer/)**
   1366 points by `jjmaxwell4` - [339 comments](https://news.ycombinator.com/item?id=50093568)

2. **[Wanted to download an ISO, ended up writing a kernel exploit](https://blog.dfb.sh/blog/eap770-root-for-two-zeros/)**
   84 points by `0xdeafbeef` - [31 comments](https://news.ycombinator.com/item?id=50070625)

3. **[Creating a Garmin "MCP"](https://jackantico.io/garmin-mcp)**
   39 points by `ricotico060` - [37 comments](https://news.ycombinator.com/item?id=50081045)

4. **[OpenCode 2.0](https://anoma.ly/notes/opencode-2-0/)**
   614 points by `gmays` - [242 comments](https://news.ycombinator.com/item?id=50094994)

5. **[Tiny Little Office](https://tinylittleoffice.com/)**
   438 points by `donohoe` - [70 comments](https://news.ycombinator.com/item?id=50096142)

6. **[The cost of getting a job today](https://weli.dev/blog/the-cost-of-getting-a-job-today/)**
   7 points by `weli` - [0 comments](https://news.ycombinator.com/item?id=50101149)

7. **[Show HN: Indigene – Native plants for where you stand](https://indigene.app/)**
   26 points by `olivierlacan` - [5 comments](https://news.ycombinator.com/item?id=50064470)

8. **[LFM2.5-24B-A2B: Built for fast on-device agents](https://www.liquid.ai/blog/lfm2-5-24b-a2b)**
   212 points by `gmays` - [45 comments](https://news.ycombinator.com/item?id=50097369)

9. **[Do dentists know what they're doing?](https://mapwriting.substack.com/p/dentists)**
   700 points by `doitLP` - [507 comments](https://news.ycombinator.com/item?id=50050553)

10. **[The First Social Network: In rural Argentina residents send messages w AM radio](https://www.newyorker.com/magazine/2026/10/19/the-first-social-network)**
   15 points by `bookofjoe` - [3 comments](https://news.ycombinator.com/item?id=50079701)
