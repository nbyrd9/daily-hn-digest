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

## Latest snapshot - [`2026-11-13.md`](./digests/2026-11-13.md)

_Captured 2026-11-13 20:08 UTC._

1. **[FM-1 Workbench](https://open.m-vave.com/fm1-workbench)**
   47 points by `simonebrunozzi` - [18 comments](https://news.ycombinator.com/item?id=50488325)

2. **[After 600 experiments, here's what I discovered about JEPA world models](https://haddyalchaer.com/jepa)**
   119 points by `halcdev` - [25 comments](https://news.ycombinator.com/item?id=50487185)

3. **[Reverse engineering my Coway air purifier to ditch the cloud](https://scottjg.com/posts/2026-11-11-reverse-engineering-my-coway-air-purifier-to-ditch-the-cloud/)**
   574 points by `scottjg` - [160 comments](https://news.ycombinator.com/item?id=50474959)

4. **[Models can now transmit viruses in weight-space](https://www.alphaxiv.org/abs/2611.weight-space-misfolding)**
   67 points by `mkglees` - [31 comments](https://news.ycombinator.com/item?id=50487762)

5. **[Doomsday: Friday, 13 November, A.D. 2026 (1960)](https://www.science.org/doi/10.1126/science.132.3436.1291)**
   386 points by `voxleone` - [271 comments](https://news.ycombinator.com/item?id=50482379)

6. **[Show HN: Isometric SF – A pixel-art map of the SF Bay Area](https://isometricsf.com/)**
   61 points by `juscha1` - [20 comments](https://news.ycombinator.com/item?id=50487228)

7. **[Ctrl+C, Ctrl+v, Ctrl+cve: Bypassing Android's Clipboard Read Security Measures](https://toninoble.com/post/ctrlc-ctrlv-ctrlcve)**
   24 points by `dethmasque` - [7 comments](https://news.ycombinator.com/item?id=50487605)

8. **[A technical vision for the Haskell ecosystem](https://discourse.haskell.org/t/a-technical-vision-for-the-haskell-ecosystem/15078)**
   137 points by `cosmic_quanta` - [58 comments](https://news.ycombinator.com/item?id=50484235)

9. **[Perplexity Decider v1.3: Training, eval, and use cases](https://www.perplexity.ai/hub/blog/perplexity-decider)**
   10 points by `gmays` - [0 comments](https://news.ycombinator.com/item?id=50488464)

10. **[AI unlocks Gödel's notebooks, said to contain hundreds of proved theorems](https://www.theguardian.com/science/2026/nov/13/kurt-godel-notebooks-ai-helps-unlock-hidden-discoveries-man-who-transformed-maths)**
   196 points by `bookofjoe` - [46 comments](https://news.ycombinator.com/item?id=50486748)
