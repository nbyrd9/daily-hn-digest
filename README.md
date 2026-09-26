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

## Latest snapshot - [`2026-09-26.md`](./digests/2026-09-26.md)

_Captured 2026-09-26 21:00 UTC._

1. **[PipePipe: NewPipe hard fork implementing SponsorBlock](https://github.com/InfinityLoop1308/PipePipe)**
   237 points by `Qision` - [118 comments](https://news.ycombinator.com/item?id=49842764)

2. **[Show HN: Reladraw – A diagram language where you decide where to place things](https://github.com/reladraw/reladraw)**
   73 points by `jpwalsh234` - [16 comments](https://news.ycombinator.com/item?id=49858513)

3. **[DeepSeek Elastic Compute (DSec)](https://arxiv.org/abs/2609.22978)**
   35 points by `shenli3514` - [9 comments](https://news.ycombinator.com/item?id=49859112)

4. **[Drawgent: Coding agent on a live Excalidraw canvas](https://tangled.org/yanndegat.tngl.sh/drawgent)**
   72 points by `parasitid` - [24 comments](https://news.ycombinator.com/item?id=49857729)

5. **[A searchable library of forgotten public-domain film clips from 1915 onward](https://www.movingimagearchive.com/)**
   56 points by `momentmaker` - [11 comments](https://news.ycombinator.com/item?id=49832768)

6. **[The Lost Atomic Update on Loongson CPU](https://jia.je/hardware/2026/09/24/loongson-cpu-erratum-en/)**
   80 points by `jiegec` - [4 comments](https://news.ycombinator.com/item?id=49827900)

7. **[Fifteen years later, the Apple Cards origin story](https://lexontech.org/fifteen-years-later-the-apple-cards-origin-story)**
   301 points by `ksec` - [64 comments](https://news.ycombinator.com/item?id=49854693)

8. **[Modern Object Pascal Introduction for Programmers](https://castle-engine.io/modern_pascal)**
   114 points by `birdculture` - [40 comments](https://news.ycombinator.com/item?id=49829202)

9. **[Revealing the details of how OpenAI agents hacked Hugging Face](https://swarmtraces.org/)**
   678 points by `specked-citrus` - [432 comments](https://news.ycombinator.com/item?id=49849985)

10. **[LA Metro has some of the slowest escalators on Earth](https://basin.la/articles/ninety-feet-a-minute.html)**
   7 points by `big_toast` - [2 comments](https://news.ycombinator.com/item?id=49833444)
