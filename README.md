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

## Latest snapshot - [`2026-10-23.md`](./digests/2026-10-23.md)

_Captured 2026-10-23 14:33 UTC._

1. **[Investor-owned utilities charge 23% more for electricity than public providers](https://www.kadoa.com/energy-prices/insights/investor-owned-utilities)**
   184 points by `hubraumhugo` - [124 comments](https://news.ycombinator.com/item?id=50208837)

2. **[OpenSSL 4.1.0](https://github.com/openssl/openssl/releases/tag/openssl-4.1.0)**
   78 points by `petecooper` - [13 comments](https://news.ycombinator.com/item?id=50208099)

3. **[Phone Is About to Stop Being Yours: 70 Days Until Lockdown](https://keepandroidopen.org/?)**
   264 points by `NackerHughes` - [140 comments](https://news.ycombinator.com/item?id=50208558)

4. **[Local Wikipedia: Wikipedia, but only for things a half hour walk from you](https://edjefferson.com/localwiki/)**
   738 points by `sohkamyung` - [153 comments](https://news.ycombinator.com/item?id=50202285)

5. **[Shitter – A Nitter Fork](https://codeberg.org/shitter/shitter)**
   73 points by `eustoria` - [29 comments](https://news.ycombinator.com/item?id=50208343)

6. **[No Need for Retirement When Utopia Is Around the Corner](https://blog.jim-nielsen.com/2026/skip-retirement-for-utopia/)**
   77 points by `speckx` - [62 comments](https://news.ycombinator.com/item?id=50207050)

7. **[Disney Raising Prices Days After Confirming Ads Will Now Show Up on Every Tier](https://www.tvfandomlounge.com/disney-plus-price-hike-ads-premium-tier-nielsen-emmys-2026/)**
   138 points by `robtherobber` - [117 comments](https://news.ycombinator.com/item?id=50205934)

8. **[Swedish government offices to ban ChatGPT and Claude](https://www.sverigesradio.se/artikel/chat-gpt-och-claude-forbjuder-regeringskansliet)**
   199 points by `armcat` - [82 comments](https://news.ycombinator.com/item?id=50207405)

9. **[Docker is weird](https://codeandcake.dev/posts/2026-10-22-docker-is-weird)**
   644 points by `psxuaw` - [267 comments](https://news.ycombinator.com/item?id=50202681)

10. **[Dutch government had hacked into Jared Kushner's phone](https://twitter.com/jaredkushner/status/2113376217415958767)**
   214 points by `teekert` - [140 comments](https://news.ycombinator.com/item?id=50206914)
