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

## Latest snapshot - [`2026-10-12.md`](./digests/2026-10-12.md)

_Captured 2026-10-12 20:07 UTC._

1. **[Codex CLI installs a persistent, self-updating background daemon by default](https://github.com/openai/codex/issues/48195)**
   223 points by `whimblepop` - [132 comments](https://news.ycombinator.com/item?id=50060694)

2. **[GLM-Legal](https://z.ai/blog/glm-legal)**
   299 points by `ilreb` - [164 comments](https://news.ycombinator.com/item?id=50058507)

3. **[A Modern Web App in C](https://prophitt.me/writing/a-modern-web-app-in-c)**
   223 points by `prophittcorey` - [87 comments](https://news.ycombinator.com/item?id=50058528)

4. **[AI models may be capable of self-replicating without access to a datacenter](https://www.anthropic.com/research/self-replicating-ai)**
   31 points by `artninja1988` - [21 comments](https://news.ycombinator.com/item?id=50061603)

5. **[AI coding agents generate more code, but not more software](https://arstechnica.com/ai/2026/10/ai-coding-agents-generate-more-code-but-not-more-software/)**
   175 points by `gumby` - [138 comments](https://news.ycombinator.com/item?id=50059523)

6. **[Launch HN: Agent37 (YC F26) – Low-cost agent sandboxes for running agents](https://news.ycombinator.com/item?id=50059096)**
   58 points by `vishnukool` - [42 comments](https://news.ycombinator.com/item?id=50059096)

7. **[Hackers activate automatic defrosting accross European supermarket fridges](https://www.tomshardware.com/tech-industry/cyber-security/unprecedented-cyberattack-cripples-supermarket-fridges-across-europe-as-hackers-activate-automatic-defrosting-delivery-and-store-prices-also-impacted-by-incident)**
   216 points by `Zeekaas` - [373 comments](https://news.ycombinator.com/item?id=50055304)

8. **[Turn a WiFi 7 Router into a 320Msps Software Defined Radio Receiver](https://github.com/h0m3us3r/w1700k-sdr)**
   160 points by `djfergus` - [47 comments](https://news.ycombinator.com/item?id=50055593)

9. **[Citroen revives the 2CV for an electric age](https://www.bbc.com/news/articles/c620r33plgppo)**
   193 points by `scrlk` - [216 comments](https://news.ycombinator.com/item?id=50055220)

10. **[Muse Wonder](https://research.meta.ai/blog/muse-wonder)**
   375 points by `meetpateltech` - [174 comments](https://news.ycombinator.com/item?id=50059115)
