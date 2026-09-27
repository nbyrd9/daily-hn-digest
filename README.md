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

## Latest snapshot - [`2026-09-27.md`](./digests/2026-09-27.md)

_Captured 2026-09-27 19:14 UTC._

1. **[Ember-1](https://fireworks.ai/blog/ember-1)**
   117 points by `gmays` - [52 comments](https://news.ycombinator.com/item?id=49868830)

2. **[In an $80 motel room, a discovery to shed light on the origins of life](https://www.nytimes.com/2026/09/26/science/motel-science-discovery.html)**
   138 points by `danso` - [53 comments](https://news.ycombinator.com/item?id=49866951)

3. **[Writing Efficient C++ Code (2013)](https://asawicki.info/articles/writing_efficient_cpp_code.php)**
   109 points by `ibobev` - [47 comments](https://news.ycombinator.com/item?id=49849409)

4. **[Replacing the old battery on rechargeable bike lights](https://jvns.ca/blog/2026/09/27/replacing-the-old-battery-on-rechargeable-bike-lights/)**
   100 points by `surprisetalk` - [49 comments](https://news.ycombinator.com/item?id=49866515)

5. **[Show HN: TinyAIArena watch AI agents battle it out](https://tinyaiarena.com/)**
   57 points by `hp6` - [31 comments](https://news.ycombinator.com/item?id=49867775)

6. **[The Normalization of Inexplicable Failures](https://www.ihatethefuture.com/2026/09/the-normalization-of-inexplicable.html)**
   186 points by `pxx` - [65 comments](https://news.ycombinator.com/item?id=49867486)

7. **[SNL Weekend Update: Anthropic CEO Dario Amodei on A.I.'S Threat to Humanity [video]](https://www.youtube.com/watch?v=-Nvne3LzBls)**
   132 points by `CharlesW` - [37 comments](https://news.ycombinator.com/item?id=49868831)

8. **[Oral history of John Chowning, inventor of FM synthesis [video]](https://www.youtube.com/watch?v=e1Xn3030IvM)**
   4 points by `Rochus` - [0 comments](https://news.ycombinator.com/item?id=49869142)

9. **[On caring for user data: NeoVim caused Vim undo files to be deleted](https://unsung.aresluna.org/they-had-no-concept-of-a-duty-of-care-to-their-users/)**
   292 points by `jandeboevrie` - [255 comments](https://news.ycombinator.com/item?id=49867067)

10. **[Fragment of oldest known peace treaty found in Turkey](https://www.livescience.com/archaeology/ancient-egyptians/we-have-found-traces-of-peace-thousands-of-years-old-fragment-of-worlds-oldest-known-peace-treaty-found-in-turkey)**
   20 points by `gmays` - [3 comments](https://news.ycombinator.com/item?id=49866988)
