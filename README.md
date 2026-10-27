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

## Latest snapshot - [`2026-10-27.md`](./digests/2026-10-27.md)

_Captured 2026-10-27 21:02 UTC._

1. **[Genie 4](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/)**
   532 points by `acossta` - [319 comments](https://news.ycombinator.com/item?id=50261319)

2. **[Ghostty 1.4.0](https://ghostty.org/docs/install/release-notes/1-4-0)**
   459 points by `deaux` - [137 comments](https://news.ycombinator.com/item?id=50261998)

3. **[Tailscale SSH: Investigation and remediation update](https://tailscale.com/ssh-investigation-update)**
   68 points by `figmert` - [18 comments](https://news.ycombinator.com/item?id=50264857)

4. **[Survival LLM: AI assistant and emergency library that runs on your own computer](https://www.brangus.io/survival-llm)**
   48 points by `Luc` - [28 comments](https://news.ycombinator.com/item?id=50264853)

5. **[New 14‑inch MacBook Pro with M6](https://www.apple.com/in/newsroom/2026/10/apple-introduces-the-new-14-inch-macbook-pro-with-m6/)**
   183 points by `beex` - [197 comments](https://news.ycombinator.com/item?id=50261352)

6. **[Classification of Finite Simple Groups Formalized in Lean](https://cfsg.axiommath.ai/)**
   123 points by `pfdietz` - [28 comments](https://news.ycombinator.com/item?id=50261647)

7. **[New iMac with M6](https://www.apple.com/imac/)**
   255 points by `notfried` - [310 comments](https://news.ycombinator.com/item?id=50258538)

8. **[Python's experimental JIT to be removed](https://lwn.net/SubscriberLink/1102102/0c00e4d550f25f8c/)**
   384 points by `f311a` - [203 comments](https://news.ycombinator.com/item?id=50257419)

9. **[Wikipedia's Cleanup of AI-Generated Content](https://spectrum.ieee.org/wikipedia-wikiproject-ai-writing-cleanup)**
   388 points by `rbanffy` - [179 comments](https://news.ycombinator.com/item?id=50257326)

10. **[An examination of lost firefly species of the US and Canada](https://journaloflostspecies.org/index.php/jls/article/view/37/33)**
   24 points by `bryanrasmussen` - [0 comments](https://news.ycombinator.com/item?id=50224079)
