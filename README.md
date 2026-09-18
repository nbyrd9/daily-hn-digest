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

## Latest snapshot - [`2026-09-18.md`](./digests/2026-09-18.md)

_Captured 2026-09-18 20:49 UTC._

1. **[Korea raises data breach fines to 10% of revenue](https://www.koreajoongangdaily.com/business/korea-raises-data-breach-fines-to-10-of-revenue/12869899)**
   87 points by `throw7` - [20 comments](https://news.ycombinator.com/item?id=49759466)

2. **[Android 17 is the first since 3.x to add new APIs without releasing to the AOSP](https://grapheneos.social/@GrapheneOS/117282080803799576)**
   204 points by `theanonymousone` - [93 comments](https://news.ycombinator.com/item?id=49758736)

3. **[Cloudflare Quick Tunnels](https://try.cloudflare.com/)**
   431 points by `jcbhmr` - [192 comments](https://news.ycombinator.com/item?id=49754785)

4. **[Saving another 100TB of RAM with math (and Rust)](https://blog.cloudflare.com/saving-100-tb-of-ram-with-math/)**
   76 points by `f311a` - [10 comments](https://news.ycombinator.com/item?id=49758580)

5. **[Apple releases iPhone Duo simulator and Xcode 27.1 beta](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_1-release-notes)**
   66 points by `CameronBanga` - [31 comments](https://news.ycombinator.com/item?id=49758419)

6. **[Cache-to-Cache: Direct Semantic Communication Between Large Language Models](https://arxiv.org/abs/2510.03215)**
   35 points by `rochansinha` - [6 comments](https://news.ycombinator.com/item?id=49758615)

7. **[Photon-Emission-Guided Laser Fault Injection Enables RP2350 Secure Debug](https://donjon.ledger.com/blog/rp2350-secure-debug-laser-fault-injection/)**
   116 points by `synack` - [35 comments](https://news.ycombinator.com/item?id=49757050)

8. **[Show HN: Cactus Needle 3: 8-29MB automation models can match DeepSeek V4 Flash](https://cactuscompute.com/needle)**
   120 points by `HenryNdubuaku` - [59 comments](https://news.ycombinator.com/item?id=49748553)

9. **[OpenJev](https://openjev.com/)**
   487 points by `ilreb` - [233 comments](https://news.ycombinator.com/item?id=49752041)

10. **[The Implications of Linguistic Illegibility for LLM Security](https://arxiv.org/abs/2609.02852)**
   23 points by `tomjakubowski` - [10 comments](https://news.ycombinator.com/item?id=49758689)
