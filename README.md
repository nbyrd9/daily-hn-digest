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

## Latest snapshot - [`2026-11-05.md`](./digests/2026-11-05.md)

_Captured 2026-11-05 01:44 UTC._

1. **[Residential proxies detected on White House network](https://layer3intel.com/blog/residential-proxies-white-house-network)**
   636 points by `Rasbora` - [208 comments](https://news.ycombinator.com/item?id=50371246)

2. **[Images 2.6](https://openai.com/index/introducing-images-2-6/)**
   86 points by `davidbarker` - [72 comments](https://news.ycombinator.com/item?id=50372945)

3. **[A thousand fewer paths to root](https://openai.com/index/a-thousand-fewer-paths-to-root/)**
   82 points by `dangelosaurus` - [54 comments](https://news.ycombinator.com/item?id=50372929)

4. **[Starfall – Affordable, routine access to microgravity](https://www.spacex.com/starfall)**
   53 points by `gmays` - [21 comments](https://news.ycombinator.com/item?id=50373308)

5. **[AI is forcing us to pay off 40 years of technical debt](https://spectrum.ieee.org/ai-in-cybersecurity-php2shell-vulnerability)**
   1063 points by `pseudolus` - [633 comments](https://news.ycombinator.com/item?id=50364336)

6. **[Ripple-65B Preview: U.S. Open-Weight SOTA on Agentic Coding](https://www.ricursive.com/ripple)**
   220 points by `Philpax` - [78 comments](https://news.ycombinator.com/item?id=50369925)

7. **[Insects don't swarm at LED lights](https://www.birdsoutsidemywindow.org/2026/11/03/insects-dont-swarm-at-led-lights/)**
   164 points by `speckx` - [93 comments](https://news.ycombinator.com/item?id=50370610)

8. **[Kimi K3.1 Pro model weights are out](https://huggingface.co/moonshotai/Kimi-K3.1-Pro)**
   372 points by `abrarthought` - [101 comments](https://news.ycombinator.com/item?id=50366999)

9. **[Hacking the Xbox 360 Hypervisor Part 3: Bad Update Improvements](https://icode4.coffee/?p=1746)**
   61 points by `muricula` - [2 comments](https://news.ycombinator.com/item?id=50372164)

10. **[A new Go API for JSON](https://go.dev/blog/jsonv2)**
   228 points by `olexsmir` - [95 comments](https://news.ycombinator.com/item?id=50369106)
