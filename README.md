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

## Latest snapshot - [`2026-11-09.md`](./digests/2026-11-09.md)

_Captured 2026-11-09 02:00 UTC._

1. **[KetchUp – Open-source SketchUp alternative built with Rust and WebGPU](https://ketchup3d.github.io/app/)**
   199 points by `dcoulmbe` - [48 comments](https://news.ycombinator.com/item?id=50418176)

2. **[Unlocking any car from X brand in most of the world](https://shubs.io/unlocking-any-car-from-x-brand-in-most-of-the-world/)**
   53 points by `infosecau` - [21 comments](https://news.ycombinator.com/item?id=50419215)

3. **[Herb Sutter: When a language's creator and its owners strongly disagree [pdf]](https://isocpp.org/files/papers/P4454R0.pdf)**
   62 points by `acossta` - [40 comments](https://news.ycombinator.com/item?id=50418818)

4. **[Chimera Vocal Synth](https://chimera-vocal-synth.vercel.app/)**
   87 points by `nmstoker` - [14 comments](https://news.ycombinator.com/item?id=50418182)

5. **[Dux: Free, open-source Wayland desktop shell with file manager and theming](https://duxlabs.dev/)**
   199 points by `indigodaddy` - [61 comments](https://news.ycombinator.com/item?id=50416053)

6. **[Ask HN: What are you working on? (November 2026)](https://news.ycombinator.com/item?id=50417407)**
   127 points by `david927` - [466 comments](https://news.ycombinator.com/item?id=50417407)

7. **[Declarative Dragging](https://declarative-dragging.github.io/)**
   353 points by `smusamashah` - [42 comments](https://news.ycombinator.com/item?id=50368481)

8. **[Outlook.com Is Quietly Rejecting Email from Domains Without DMARC](https://mailroute.net/blog/outlook-rejecting-email-without-dmarc)**
   246 points by `xmddmx` - [188 comments](https://news.ycombinator.com/item?id=50416158)

9. **[Goldman Sachs is pulling Claude Code from its bankers and traders](https://www.thestateofai.com/news/goldman-sachs-claude-code-traders-bankers)**
   605 points by `TheWiggles` - [359 comments](https://news.ycombinator.com/item?id=50415628)

10. **[The Web Is More Than Enough, by Paul Ford](https://ftrain.com/aboard-the-web-is-more-than-enough)**
   76 points by `edward` - [38 comments](https://news.ycombinator.com/item?id=50416456)
