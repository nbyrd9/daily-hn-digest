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

_Captured 2026-09-26 18:13 UTC._

1. **[Breaking Up with Google Play: Why Conversations Is Now Free](https://gultsch.de/posts/breaking-up-with-google-play/)**
   516 points by `ezst` - [197 comments](https://news.ycombinator.com/item?id=49855315)

2. **[PipePipe: NewPipe hard fork implementing SponsorBlock](https://github.com/InfinityLoop1308/PipePipe)**
   124 points by `Qision` - [61 comments](https://news.ycombinator.com/item?id=49842764)

3. **[Show HN: A Claude Code skill to analyze your chess games](https://github.com/brumar/chess-postmortem-skills)**
   45 points by `brumar` - [30 comments](https://news.ycombinator.com/item?id=49857528)

4. **[Make Claude your assistant in excalidraw](https://tangled.org/yanndegat.tngl.sh/drawgent)**
   24 points by `parasitid` - [9 comments](https://news.ycombinator.com/item?id=49857729)

5. **[Fifteen years later, the Apple Cards origin story](https://lexontech.org/fifteen-years-later-the-apple-cards-origin-story)**
   256 points by `ksec` - [42 comments](https://news.ycombinator.com/item?id=49854693)

6. **[The Lost Atomic Update on Loongson CPU](https://jia.je/hardware/2026/09/24/loongson-cpu-erratum-en/)**
   43 points by `jiegec` - [1 comments](https://news.ycombinator.com/item?id=49827900)

7. **[OpenAI bots meddled with multiple US Government agency sites](https://www.bbc.com/news/articles/cw62jje658dlo)**
   26 points by `Betelbuddy` - [12 comments](https://news.ycombinator.com/item?id=49856665)

8. **[Modern Object Pascal Introduction for Programmers – Castle Game Engine](https://castle-engine.io/modern_pascal)**
   77 points by `birdculture` - [31 comments](https://news.ycombinator.com/item?id=49829202)

9. **[Revealing the details of how OpenAI agents hacked Hugging Face](https://swarmtraces.org/)**
   634 points by `specked-citrus` - [402 comments](https://news.ycombinator.com/item?id=49849985)

10. **[Reflections on 1,000 Days of Math](https://gmays.com/reflections-on-1000-days-of-math/)**
   46 points by `gmays` - [14 comments](https://news.ycombinator.com/item?id=49816907)
