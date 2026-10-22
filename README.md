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

## Latest snapshot - [`2026-10-22.md`](./digests/2026-10-22.md)

_Captured 2026-10-22 09:15 UTC._

1. **[CVE-2026-111943: Compromised Intermediate Certificate Authority](https://nvd.nist.gov/vuln/detail/cve-2026-111943)**
   14 points by `keks24` - [1 comments](https://news.ycombinator.com/item?id=50192900)

2. **[WorldTUI: I trained a 360M model to pretend to be a terminal](https://simedw.com/2026/10/21/world-model-terminal/)**
   171 points by `alphax314` - [54 comments](https://news.ycombinator.com/item?id=50190363)

3. **[The recently proposed o(n log n) integer multiplication algorithm [pdf]](https://web.maths.unsw.edu.au/~davidharvey/research/subnlogn.pdf)**
   193 points by `craigcitro` - [129 comments](https://news.ycombinator.com/item?id=50190455)

4. **[Security Disclosure](https://blog.railway.com/p/security-disclosure-wednesday-october-21st)**
   451 points by `passenger` - [260 comments](https://news.ycombinator.com/item?id=50188228)

5. **[Show HN: The fastest browser for AI agents to run browser automation](https://ego-lite.apposters.com)**
   8 points by `ehurynovich` - [0 comments](https://news.ycombinator.com/item?id=50192585)

6. **[OpenAI CLI](https://github.com/openai/openai-cli)**
   110 points by `armcat` - [66 comments](https://news.ycombinator.com/item?id=50191507)

7. **[Claude Duet](https://claude.com/product/claude-duet)**
   363 points by `kuberwastaken` - [335 comments](https://news.ycombinator.com/item?id=50186037)

8. **[Compromised LiteLLM 1.107.0 on PyPI Installs a Credential Stealer and Backdoor](https://safedep.io/litellm-pypi-compromise-credential-stealer-backdoor/)**
   508 points by `abhisek` - [168 comments](https://news.ycombinator.com/item?id=50181114)

9. **[Rust Style Guide](https://google.github.io/styleguide/rustguide.html)**
   297 points by `kaycebasques` - [180 comments](https://news.ycombinator.com/item?id=50186010)

10. **[GitLab critical patch release](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-5-1-released/)**
   345 points by `artooro` - [80 comments](https://news.ycombinator.com/item?id=50185869)
