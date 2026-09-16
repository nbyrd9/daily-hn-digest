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

## Latest snapshot - [`2026-09-16.md`](./digests/2026-09-16.md)

_Captured 2026-09-16 03:21 UTC._

1. **[Introducing System One Models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev)**
   878 points by `albelfio` - [281 comments](https://news.ycombinator.com/item?id=49717558)

2. **[Show HN: An e-ink frame that hears birds and draws them as 1800s illustrations](https://github.com/arnegiacomo/fugleramme)**
   1370 points by `arnemunthekaas` - [183 comments](https://news.ycombinator.com/item?id=49711544)

3. **[Negativland, Culture Jamming, and the Art of Making Something New](https://blog.archive.org/2026/09/11/negativland-culture-jamming-and-the-art-of-making-something-new/)**
   14 points by `bananaboy` - [4 comments](https://news.ycombinator.com/item?id=49721548)

4. **[An update on Wayback Machine access](https://blog.archive.org/2026/09/15/an-update-on-wayback-machine-access/)**
   421 points by `ChrisArchitect` - [222 comments](https://news.ycombinator.com/item?id=49716176)

5. **[Gemini 3.8 Live and 3.8 Live Extended Thinking](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/)**
   331 points by `leumon` - [203 comments](https://news.ycombinator.com/item?id=49715947)

6. **[German Rheinmetall open-sources its Battlesuite connected weapon system protcol](https://rheinmetall.github.io/onboardapi-documentation/9.10.0/index.html)**
   147 points by `summarity` - [44 comments](https://news.ycombinator.com/item?id=49718928)

7. **[Apple Reference Image: A New Approach for Verified Photography](https://security.apple.com/blog/apple-reference-image/)**
   19 points by `imwally` - [8 comments](https://news.ycombinator.com/item?id=49721322)

8. **[Stay discoverable in search while disallowing AI training](https://blog.cloudflare.com/accountable-mixed-use-ai-crawlers/)**
   24 points by `djfergus` - [12 comments](https://news.ycombinator.com/item?id=49721435)

9. **[Recreating Voodoo Graphics and a Late-1990s Gaming PC on an FPGA](https://nand2mario.github.io/posts/2026/zsst-voodoo/)**
   53 points by `zdw` - [10 comments](https://news.ycombinator.com/item?id=49719938)

10. **[We got admin access to Baseten's production GitHub in 25 minutes](https://www.strix.ai/blog/baseten-harbor-github-pat-takeover)**
   241 points by `bearsyankees` - [130 comments](https://news.ycombinator.com/item?id=49716476)
