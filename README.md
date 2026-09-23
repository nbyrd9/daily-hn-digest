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

## Latest snapshot - [`2026-09-23.md`](./digests/2026-09-23.md)

_Captured 2026-09-23 14:54 UTC._

1. **[Claude Code reads AGENTS.md only when telemetry is on](https://blog.szypowi.cz/p/claude-code-reads-agents.md-only-when-telemetry-is-on/)**
   289 points by `pszypowicz` - [131 comments](https://news.ycombinator.com/item?id=49814947)

2. **[I Don't Want the Details](https://michaelheap.com/i-dont-want-the-details/)**
   100 points by `mooreds` - [68 comments](https://news.ycombinator.com/item?id=49815466)

3. **[Stripe built its internal AI platform](https://stripe.dev/blog/meet-stripes-knowledge-ai-platform)**
   21 points by `ltononro` - [10 comments](https://news.ycombinator.com/item?id=49815982)

4. **[Jev in 25 Lines of Python](https://www.nobodywho.ai/posts/jev-in-25-lines/)**
   412 points by `bashbjorn` - [132 comments](https://news.ycombinator.com/item?id=49812769)

5. **[Z80 REPL](https://abagames.github.io/z80-repl/index.html)**
   78 points by `adunk` - [10 comments](https://news.ycombinator.com/item?id=49814236)

6. **[GPT-6 Sol and Luna](https://openai.com/index/introducing-gpt-6-sol-and-luna/)**
   1648 points by `OfficialTurkey` - [793 comments](https://news.ycombinator.com/item?id=49805509)

7. **[Claude Opus 5.5](https://www.anthropic.com/claude-opus-5-5)**
   1662 points by `km144` - [1014 comments](https://news.ycombinator.com/item?id=49803892)

8. **[Jev in practice: typed decisions, scoped authority](https://tenuo.ai/blog/jev-scoped-authority)**
   11 points by `niyikiza` - [3 comments](https://news.ycombinator.com/item?id=49816487)

9. **[Tokens Too Cheap to Meter](https://jyn.dev/tokens-too-cheap-to-meter/)**
   62 points by `teoruiz` - [37 comments](https://news.ycombinator.com/item?id=49813482)

10. **[The GitHub wiki is an anti-pattern](https://michaelheap.com/github-wiki-is-an-antipattern/)**
   71 points by `ibobev` - [46 comments](https://news.ycombinator.com/item?id=49815484)
