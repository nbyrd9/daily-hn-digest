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

_Captured 2026-10-27 09:58 UTC._

1. **[Three new discoveries in mathematics, computer science, and physics](https://openai.com/index/building-scientific-understanding-with-academic-communities/)**
   898 points by `jonluca` - [423 comments](https://news.ycombinator.com/item?id=50251344)

2. **[The Mythical Man-Month in the Age of AI](https://j11g.com/the-mythical-man-month-in-the-age-of-ai)**
   130 points by `ilreb` - [101 comments](https://news.ycombinator.com/item?id=50255298)

3. **[The Exponential Time Hypothesis Is False [pdf]](https://github.com/openai/math/blob/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/paper.pdf)**
   620 points by `vok` - [226 comments](https://news.ycombinator.com/item?id=50251661)

4. **[New 'Circadian' Subtype of Depression Affecting 1 in 4 Patients](https://www.sciencealert.com/researchers-identify-new-circadian-subtype-of-depression-affecting-1-in-4-patients)**
   51 points by `gmays` - [20 comments](https://news.ycombinator.com/item?id=50196212)

5. **[Sebastian Raschka's from-scratch video course on building reasoning models](https://magazine.sebastianraschka.com/p/building-reasoning-models)**
   705 points by `sgiannopoulos` - [97 comments](https://news.ycombinator.com/item?id=50245138)

6. **[Oldest GUI application that still runs on Windows 11](https://blog.enlyth.com/posts/oldest-windows-gui-app-win-11/)**
   422 points by `enlyth` - [240 comments](https://news.ycombinator.com/item?id=50248055)

7. **[Writing about pratt parsing so I remember it](https://www.unix.dog/~yosh/blog/2026-10-25_pratt-parsing.html)**
   27 points by `dverlaeckt80` - [1 comments](https://news.ycombinator.com/item?id=50255177)

8. **[I still teach OpenGL ES 3.0](https://eliasfarhan.ch/graphics/cpp/2026/01/27/why-i-teach-opengles.html)**
   60 points by `majorchord` - [38 comments](https://news.ycombinator.com/item?id=50253939)

9. **[Type Server Protocol](https://github.com/microsoft/pylance-release/blob/main/docs/tsp/type-server-protocol.md)**
   242 points by `adamnemecek` - [159 comments](https://news.ycombinator.com/item?id=50248371)

10. **[CSS-Tricks has a new owner](https://css-tricks.com/css-tricks-has-a-new-owner/)**
   478 points by `edent` - [105 comments](https://news.ycombinator.com/item?id=50245831)
