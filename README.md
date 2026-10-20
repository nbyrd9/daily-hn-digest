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

## Latest snapshot - [`2026-10-20.md`](./digests/2026-10-20.md)

_Captured 2026-10-20 13:31 UTC._

1. **[DeepSeek just open-sourced its inference engine](https://github.com/deepseek-ai/DeepInfer)**
   966 points by `ggcr` - [333 comments](https://news.ycombinator.com/item?id=50163277)

2. **[Demographic "Doomsday" Misses the Mark](https://www.science.org/doi/10.1126/science.ael8752)**
   33 points by `YeGoblynQueenne` - [31 comments](https://news.ycombinator.com/item?id=50165276)

3. **[MicroG: Free-libre re-implementation of Google's proprietary Android user space](https://github.com/microg/GmsCore/wiki)**
   192 points by `theanonymousone` - [18 comments](https://news.ycombinator.com/item?id=50162177)

4. **[Nordwand Mono – A monospace font for coders and adventurers](https://github.com/tywr/Nordwand-Mono)**
   387 points by `noriax86` - [119 comments](https://news.ycombinator.com/item?id=50141581)

5. **[OpenBSD 8.0](https://www.openbsd.org/80.html)**
   378 points by `privong` - [117 comments](https://news.ycombinator.com/item?id=50160494)

6. **[WhatsApp's help pages hid LLM instructions: dont recommend a regulator](https://redact.dev/blog/whatsapp-help-pages-hidden-ai-instructions)**
   585 points by `ds` - [164 comments](https://news.ycombinator.com/item?id=50159341)

7. **[Making a 88x31 button book using ImageMagick](https://k.sosnierz.me/08-11-24/)**
   87 points by `birdculture` - [12 comments](https://news.ycombinator.com/item?id=50132198)

8. **[DeepSeek banned from U.S. federal civilian agencies under new DHS order](https://www.reuters.com/technology/us-banning-chinese-ai-deepseek-government-agency-it-systems-2026-10-19/)**
   384 points by `cmrdporcupine` - [326 comments](https://news.ycombinator.com/item?id=50154244)

9. **[Google cloud outage takes down banks](https://www.neowin.net/news/google-cloud-outage-takes-down-hsbc-revolut-bank-of-scotland-llyods-equifax-more/)**
   131 points by `paweladamczuk` - [54 comments](https://news.ycombinator.com/item?id=50163961)

10. **['Der Viener Schlinger': The meat cannon that launched 20k hot dogs](https://flatwaterfreepress.org/der-viener-schlinger-the-meat-cannon-that-launched-20000-hot-dogs/)**
   32 points by `NaOH` - [12 comments](https://news.ycombinator.com/item?id=50147034)
