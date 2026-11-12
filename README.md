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

## Latest snapshot - [`2026-11-12.md`](./digests/2026-11-12.md)

_Captured 2026-11-12 01:06 UTC._

1. **[Nvidia is preparing to oust Jensen Huang](https://www.wsj.com/business/nvidia-is-preparing-to-oust-nvidia-ceo-jensen-huang-30f421ad)**
   425 points by `jbredeche` - [626 comments](https://news.ycombinator.com/item?id=50459703)

2. **[93% of Paint Splatters Are Valid Perl Programs (2019)](https://www.mcmillen.dev/sigbovik/)**
   104 points by `zenincognito` - [19 comments](https://news.ycombinator.com/item?id=50459745)

3. **[AWS emulator](https://github.com/aws/aws-emulator)**
   646 points by `super_linear` - [212 comments](https://news.ycombinator.com/item?id=50456631)

4. **[Tim Peters has died](https://discuss.python.org/t/in-memoriam-tim-peters-1952-2026/110028)**
   831 points by `ayhanfuat` - [93 comments](https://news.ycombinator.com/item?id=50450488)

5. **[United Airlines bans AI agents from booking flights on behalf of travelers](https://www.cbsnews.com/news/united-airlines-bans-ai-agents-booking-flights/)**
   329 points by `herpderperator` - [313 comments](https://news.ycombinator.com/item?id=50458900)

6. **[Lock Your GitHub Actions](https://hugovk.dev/blog/2026/lock-github-actions/)**
   102 points by `gslin` - [19 comments](https://news.ycombinator.com/item?id=50459485)

7. **[A false smoke alarm almost drowned Jane Street's only NYC datacenter](https://michael.bacarella.com/2026/11/10/false-smoke-alarm-jane-street-datacenter/)**
   402 points by `mbac32768` - [199 comments](https://news.ycombinator.com/item?id=50455394)

8. **[Gemini Decisions API](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/)**
   248 points by `iamdelirium` - [79 comments](https://news.ycombinator.com/item?id=50456791)

9. **[Emacs in the Age of Magic](https://commandlinesystems.com/magic.txt)**
   140 points by `ggcr` - [49 comments](https://news.ycombinator.com/item?id=50458208)

10. **[A general purpose Apple Silicon layer for x86-64 PCs](https://github.com/tylertms/Stela)**
   34 points by `iceboundrock` - [10 comments](https://news.ycombinator.com/item?id=50460154)
