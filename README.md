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

## Latest snapshot - [`2026-10-28.md`](./digests/2026-10-28.md)

_Captured 2026-10-28 08:15 UTC._

1. **[Git for the US Code](https://lexifina.com/blog/git-for-the-us-code)**
   223 points by `alansaber` - [112 comments](https://news.ycombinator.com/item?id=50268380)

2. **[Genie 4](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/)**
   860 points by `acossta` - [503 comments](https://news.ycombinator.com/item?id=50261319)

3. **[Ghostty 1.4](https://ghostty.org/docs/install/release-notes/1-4-0)**
   976 points by `deaux` - [299 comments](https://news.ycombinator.com/item?id=50261998)

4. **[Ink droplets in motion snag top prize in Nikon Small World contest](https://arstechnica.com/science/2026/10/meet-the-2026-winner-of-nikons-small-world-photomicrography-contest/)**
   197 points by `_Microft` - [30 comments](https://news.ycombinator.com/item?id=50234796)

5. **[Survival LLM: AI assistant and emergency library that runs on your own computer](https://www.brangus.io/survival-llm)**
   322 points by `Luc` - [135 comments](https://news.ycombinator.com/item?id=50264853)

6. **[MacOS Extensions Pack for the Apple Network Server v1.0](http://oldvcr.blogspot.com/2026/10/macos-extensions-pack-for-apple-network.html)**
   23 points by `classichasclass` - [0 comments](https://news.ycombinator.com/item?id=50227400)

7. **[Tailscale SSH: Investigation and remediation update](https://tailscale.com/ssh-investigation-update)**
   268 points by `figmert` - [139 comments](https://news.ycombinator.com/item?id=50264857)

8. **[Early progress on accelerating drug development with Claude](https://www.anthropic.com/research/early-progress-drug-development)**
   215 points by `dataking` - [189 comments](https://news.ycombinator.com/item?id=50265609)

9. **[SS United States to be sunk as largest artificial reef](https://divemagazine.com/scuba-diving-news/ss-united-states-to-be-sunk-as-worlds-largest-artificial-reef-in-november)**
   133 points by `geox` - [95 comments](https://news.ycombinator.com/item?id=50239214)

10. **[Raspberry Pi Zero 3W and Pi 4 Model A spotted in device trees](https://bret.dk/raspberry-pi-zero-3-w-pi-4-model-a/)**
   151 points by `sthlmb` - [79 comments](https://news.ycombinator.com/item?id=50265594)
