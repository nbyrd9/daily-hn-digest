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

## Latest snapshot - [`2026-10-26.md`](./digests/2026-10-26.md)

_Captured 2026-10-26 02:19 UTC._

1. **[Dolly Parton's Imagination Library](https://imaginationlibrary.com/)**
   395 points by `jumploops` - [68 comments](https://news.ycombinator.com/item?id=50234474)

2. **[F-Zero X on Nintendo 3DS](https://hypnotize.works/gdx-3ds/postmortem/index.html)**
   47 points by `bpierre` - [28 comments](https://news.ycombinator.com/item?id=50237078)

3. **[Overgrown, when plants invade your abandoned tabs](https://charliegerard.dev/blog/overgrown-extension/)**
   146 points by `speckx` - [39 comments](https://news.ycombinator.com/item?id=50197108)

4. **[Attention Is Not What You Need (2025)](https://arxiv.org/abs/2512.19428)**
   26 points by `westurner` - [9 comments](https://news.ycombinator.com/item?id=50237224)

5. **[Why I Am a Programmer](https://www.alfie.wtf/programming/why-i-am-a-programmer.html)**
   143 points by `jruohonen` - [52 comments](https://news.ycombinator.com/item?id=50235017)

6. **[What goes into making an animated film?](https://www.disneyanimation.com/process/)**
   96 points by `embedding-shape` - [35 comments](https://news.ycombinator.com/item?id=50235738)

7. **[The State of Context Engineering](https://www.dbreunig.com/2026/10/24/the-state-of-context-engineering.html)**
   85 points by `pchristensen` - [24 comments](https://news.ycombinator.com/item?id=50235780)

8. **[A 10-year-old CNN outperforms frontier LLMs for skin cancer diagnosis](https://lynchlab.net/llm-skin-cancer)**
   446 points by `sungam` - [212 comments](https://news.ycombinator.com/item?id=50233779)

9. **[OpenAI and Anthropic cut their LLM prices by up to 80% within a few months. Why?](https://minimaxir.com/2026/10/cheap-llms/)**
   160 points by `minimaxir` - [186 comments](https://news.ycombinator.com/item?id=50236102)

10. **[Where the Romans Fought (interactive map)](https://iosiflazaridis.github.io/battles-of-the-romans/)**
   53 points by `endorphine` - [20 comments](https://news.ycombinator.com/item?id=50234879)
