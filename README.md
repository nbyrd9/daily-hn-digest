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

## Latest snapshot - [`2026-10-17.md`](./digests/2026-10-17.md)

_Captured 2026-10-17 13:43 UTC._

1. **[DeepSeek: DeepSeek v4.1 Flash 1017](https://openrouter.ai/deepseek/deepseek-v4.1-flash-1017)**
   351 points by `theanonymousone` - [140 comments](https://news.ycombinator.com/item?id=50129121)

2. **[Ultramarine 1 Flash](https://www.paperinstruments.com/ultramarine)**
   288 points by `i_rush_carriers` - [95 comments](https://news.ycombinator.com/item?id=50106747)

3. **[Tesla Roadster](https://www.tesla.com/roadster)**
   1506 points by `shekhar101` - [2709 comments](https://news.ycombinator.com/item?id=50112657)

4. **[Show HN: Llmspeed – feel how fast a local LLM runs before you buy the hardware](https://llmspeed.dev/)**
   137 points by `albinstman` - [47 comments](https://news.ycombinator.com/item?id=50127979)

5. **[DeepSeek-v4.1-Flash-1017](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)**
   272 points by `theykk` - [106 comments](https://news.ycombinator.com/item?id=50129045)

6. **[Llama.cpp on a jailbroken PS5: run any GGUF model natively on the console](https://github.com/cobanov/PS5LM)**
   314 points by `Anon84` - [76 comments](https://news.ycombinator.com/item?id=50122431)

7. **[You could have invented transformers from memory](https://alexwang.ai/posts/associative-memory/)**
   351 points by `speckx` - [80 comments](https://news.ycombinator.com/item?id=50122878)

8. **[Recipes Are Moving from Maven Central to the Code Genome Project](https://docs.openrewrite.org/reference/latest-versions-of-every-openrewrite-module)**
   23 points by `javahippie` - [5 comments](https://news.ycombinator.com/item?id=50104783)

9. **[Intuitive concurrent programming in any language](https://www.lf-lang.org/)**
   77 points by `mpweiher` - [16 comments](https://news.ycombinator.com/item?id=50103255)

10. **[Claude reveals ECDSA curve origins](https://www.anthropic.com/research/ecdsa-curve-origins)**
   925 points by `ahlCVA` - [339 comments](https://news.ycombinator.com/item?id=50122800)
