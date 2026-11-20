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

## Latest snapshot - [`2026-11-20.md`](./digests/2026-11-20.md)

_Captured 2026-11-20 15:39 UTC._

1. **[Anthropic employee claims general proof of the Riemann Hypothesis [pdf]](https://alpo.ge/remark.pdf)**
   579 points by `iamronaldo` - [318 comments](https://news.ycombinator.com/item?id=50574968)

2. **[If you can't explain something in simple terms, you don't understand it (2017)](https://kottke.org/17/06/if-you-cant-explain-something-in-simple-terms-you-dont-understand-it)**
   307 points by `sammatilda` - [184 comments](https://news.ycombinator.com/item?id=50572355)

3. **[Frostbite: A new CPU architecture discovered, designed and verified by AI](https://architectlabs.com/blog/frostbite)**
   376 points by `shioyama` - [241 comments](https://news.ycombinator.com/item?id=50572503)

4. **[Show HN: I made an audio-to-MIDI model 60x more efficient](https://kobi.music/research/dettato)**
   76 points by `hidude562` - [15 comments](https://news.ycombinator.com/item?id=50526023)

5. **[Floppy3.5: A portable 3.5-inch floppy WiFi NAS](https://github.com/bigcrimping/floppy3.5)**
   65 points by `fortran77` - [15 comments](https://news.ycombinator.com/item?id=50560595)

6. **[Signal Is Serious About Protecting Your Privacy](https://signal.org/blog/protecting-your-privacy/)**
   137 points by `dotcoma` - [49 comments](https://news.ycombinator.com/item?id=50572348)

7. **[The Making of Oxygene](https://jeanmicheljarre.com/aaa/the-making-of-oxygene)**
   118 points by `hggh` - [42 comments](https://news.ycombinator.com/item?id=50572822)

8. **[Show HN: Fast deterministic natural language search for OpenStreetMap data](https://hippomaps.ch/?q=cafes+by+the+Limmat+100+m+from+the+lake+in+zurich#map=15.02/47.36708/8.54935)**
   76 points by `vihren` - [24 comments](https://news.ycombinator.com/item?id=50561199)

9. **[The G1 Garbage Collector](https://dev.java/learn/jvm/tool/garbage-collection/g1gc-overview/)**
   15 points by `ejboy` - [4 comments](https://news.ycombinator.com/item?id=50527444)

10. **[OpenSSL: Buffer overflow in EVP_EncodeBlock() (CVE-2026-121481, CVSS 9.8)](https://github.com/openssl/openssl/pull/33652)**
   327 points by `JacobHenner` - [276 comments](https://news.ycombinator.com/item?id=50569226)
