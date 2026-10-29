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

## Latest snapshot - [`2026-10-29.md`](./digests/2026-10-29.md)

_Captured 2026-10-29 15:18 UTC._

1. **[Mistral Large 4 (Le Chonk) is now Open Weight](https://mistral.ai/news/mistral-large-4-oss/)**
   293 points by `kuberwastaken` - [64 comments](https://news.ycombinator.com/item?id=50289418)

2. **[Gemini 4 Carbon is the new #1 on the Artificial Analysis Intelligence Index v5](https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1)**
   212 points by `theHocineSaad` - [161 comments](https://news.ycombinator.com/item?id=50288019)

3. **[Read the letter the FBI sent MLK to try to convince him to kill himself (2014)](https://www.vox.com/xpress/2014/11/12/7204453/martin-luther-king-fbi-letter)**
   233 points by `surprisetalk` - [134 comments](https://news.ycombinator.com/item?id=50288867)

4. **[DoorDash is acquiring Instacart for $17B](https://about.doordash.com/en-us/news/doordash-to-acquire-instacart)**
   33 points by `DeepLogin` - [15 comments](https://news.ycombinator.com/item?id=50289859)

5. **[Finland investigate Google over destruction of 250k trees](https://yle.fi/a/74-20254086)**
   17 points by `DeepLogin` - [4 comments](https://news.ycombinator.com/item?id=50290170)

6. **[Chained PHP2Shell Exploit Roots 25 Servers, Including US Government Servers](https://dreamgroup.com/blog/chained-php2shell-exploit-roots-25-servers)**
   96 points by `882542F3884314B` - [44 comments](https://news.ycombinator.com/item?id=50286987)

7. **[React.lazy, Suspense and the Hidden 300 ms Delay](https://tabwidgets.com/blog/react-lazy-suspense-delay)**
   8 points by `ctrlt` - [1 comments](https://news.ycombinator.com/item?id=50290042)

8. **[Qwenputer: A functioning, deterministic RISC-V CPU inside Qwen3.5](https://divagr.com/blog/qwenputer)**
   622 points by `csmantle` - [130 comments](https://news.ycombinator.com/item?id=50282838)

9. **[Zero click, silent, remote Android DoS](https://smsofdeath.com/)**
   230 points by `MarkBlah` - [124 comments](https://news.ycombinator.com/item?id=50285452)

10. **[Google determines the names for bodies of water in Google Earth (2008)](https://publicpolicy.googleblog.com/2008/04/how-google-determines-names-for-bodies.html)**
   130 points by `terminalbraid` - [101 comments](https://news.ycombinator.com/item?id=50287448)
