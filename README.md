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

_Captured 2026-10-20 23:57 UTC._

1. **[SimCity, but with Permits](https://permit.petercai.com/)**
   477 points by `pcai` - [256 comments](https://news.ycombinator.com/item?id=50170593)

2. **[Feds suspect ransom negotiator ran ShinyHunters extortion site](https://krebsonsecurity.com/2026/10/feds-suspect-ransom-negotiator-ran-shinyhunters-extortion-site/)**
   48 points by `Bender` - [10 comments](https://news.ycombinator.com/item?id=50173487)

3. **[DeepInfer: High-performance inference framework for DeepSeek models](https://github.com/deepseek-ai/DeepInfer)**
   2097 points by `ggcr` - [818 comments](https://news.ycombinator.com/item?id=50163277)

4. **[Voxtral 3](https://mistral.ai/news/voxtral-3/)**
   488 points by `ilreb` - [133 comments](https://news.ycombinator.com/item?id=50168396)

5. **[What shall I teach my son?](https://stevekrouse.com/ends)**
   218 points by `Curiositry` - [288 comments](https://news.ycombinator.com/item?id=50169707)

6. **[Google open-sources TorchTPU, a native PyTorch back end for TPUs](https://github.com/google-pytorch/torch_tpu)**
   241 points by `ilreb` - [57 comments](https://news.ycombinator.com/item?id=50169053)

7. **[The Other Epidemic: Trying to get off benzodiazepines](https://www.thebeliever.net/the-other-epidemic/)**
   18 points by `gaplong` - [6 comments](https://news.ycombinator.com/item?id=50173891)

8. **[SlopCodeBench 10/2026 – Opus 5.5, Astra wins overall, xhigh considered harmful](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/benchmarking-new-models-on-slop-code-bench.md)**
   140 points by `dhorthy` - [63 comments](https://news.ycombinator.com/item?id=50108717)

9. **[Academics have a duty to defend open knowledge systems like Wikipedia](https://blogs.lse.ac.uk/impactofsocialsciences/2026/10/19/academics-have-a-duty-to-defend-open-knowledge-systems-like-wikipedia/)**
   80 points by `jruohonen` - [33 comments](https://news.ycombinator.com/item?id=50170917)

10. **[Apple broke an essential presentation feature of iPads](https://teddysvoronos.com/2026-10-19-apple-broke-an-essential-presentation-feature-of-ipads/)**
   471 points by `evanb` - [245 comments](https://news.ycombinator.com/item?id=50165208)
