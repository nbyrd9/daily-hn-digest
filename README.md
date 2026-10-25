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

## Latest snapshot - [`2026-10-25.md`](./digests/2026-10-25.md)

_Captured 2026-10-25 15:08 UTC._

1. **[Tool book of a Nuremberg knight from 1505](https://loeffelholz-codex.org/en/)**
   84 points by `edwardog` - [33 comments](https://news.ycombinator.com/item?id=50230917)

2. **[Show HN: Farol – a risk map of a pull request for the person who approves it](https://github.com/winnin/farol)**
   24 points by `ericholiveira` - [17 comments](https://news.ycombinator.com/item?id=50231349)

3. **[fheroes2: A recreation of Heroes of Might and Magic II game engine](https://github.com/ihhub/fheroes2)**
   97 points by `tosh` - [32 comments](https://news.ycombinator.com/item?id=50230384)

4. **[We should be more ambitious with the software we build](https://danluu.com/ambitious/)**
   564 points by `ltratt` - [524 comments](https://news.ycombinator.com/item?id=50225695)

5. **[R/open source bans all solo projects and projects using LLMs](https://www.reddit.com/r/opensource/comments/1xelcuf/your_tokens_arent_valuable_no_more_ai)**
   49 points by `schleck8` - [30 comments](https://news.ycombinator.com/item?id=50231722)

6. **[Cerebras Deploys Trillion-Parameter AI Models](https://www.cerebras.ai/blog/how-we-deploy-trillion-parameter-frontier-models-on-cerebras)**
   256 points by `gmays` - [85 comments](https://news.ycombinator.com/item?id=50227356)

7. **[How Japanese Dried Bonito Is Made](https://kottke.org/26/10/how-japanese-dried-bonito-is-made)**
   118 points by `bookofjoe` - [31 comments](https://news.ycombinator.com/item?id=50193936)

8. **[The Goose Programming Language](https://aardappel.github.io/goose/)**
   486 points by `bobbydigitales` - [297 comments](https://news.ycombinator.com/item?id=50224100)

9. **[Samsung running a TensorFlow lite model on 960x540 image to track you](https://twitter.com/mike64_t/status/2114150399406202896)**
   188 points by `mashally` - [121 comments](https://news.ycombinator.com/item?id=50230181)

10. **[US inequality is getting worse in ways you might not expect](https://theconversation.com/us-inequality-is-getting-worse-in-ways-you-might-not-expect-294075)**
   30 points by `JKCalhoun` - [27 comments](https://news.ycombinator.com/item?id=50231310)
