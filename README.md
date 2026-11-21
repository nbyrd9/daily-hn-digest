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

## Latest snapshot - [`2026-11-21.md`](./digests/2026-11-21.md)

_Captured 2026-11-21 21:17 UTC._

1. **[Inkling-2-Mini in 5.4 GB Memory](https://github.com/ShinMegamiBoson/lookatmyquant)**
   234 points by `k__` - [50 comments](https://news.ycombinator.com/item?id=50591853)

2. **[Pill to treat pancreatic cancer hailed as 'biggest breakthrough in decades'](https://www.theguardian.com/society/2026/nov/20/pill-pancreatic-cancer-breakthrough-daraxonrasib)**
   138 points by `rafaelc` - [42 comments](https://news.ycombinator.com/item?id=50582069)

3. **[Lean verification of the Riemann Hypothesis](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/)**
   640 points by `g-b-r` - [506 comments](https://news.ycombinator.com/item?id=50589618)

4. **[Detonating a pile of lead azide](https://www.science.org/content/blog-post/detonating-huge-pile-lead-azide-really)**
   434 points by `beginning_end` - [290 comments](https://news.ycombinator.com/item?id=50588982)

5. **[Brazil's tax authority open-sources its tax calculator on GitHub under MIT](https://www.gov.br/receitafederal/pt-br/assuntos/noticias/2026/novembro/receita-federal-publica-primeiro-codigo-fonte-aberto-no-github-e-amplia-transparencia-da-reforma-tributaria)**
   614 points by `dvaplima` - [200 comments](https://news.ycombinator.com/item?id=50532613)

6. **[PostgreSQL Extensions in Go](https://jespino.github.io/gopgext/)**
   85 points by `valyala` - [9 comments](https://news.ycombinator.com/item?id=50591260)

7. **[My monitor was cutting my download speed by 75%](https://blog.tymscar.com/posts/studiodisplayethernet/)**
   385 points by `soheilpro` - [197 comments](https://news.ycombinator.com/item?id=50587875)

8. **[Getting the mind to steer the body to steer you](https://notnottalmud.substack.com/p/getting-the-mind-to-steer-the-body)**
   23 points by `jger15` - [9 comments](https://news.ycombinator.com/item?id=50583028)

9. **[Hurried Announcement: Alessandro Masullo GRH](https://math216.wordpress.com/2026/11/20/hurried-announcement-alessandro-masullo-grh/)**
   2354 points by `jasondavies` - [1137 comments](https://news.ycombinator.com/item?id=50579568)

10. **[Tropical Rainforests Species may be surprisingly young](https://phys.org/news/2026-11-species-tropical-rainforests-young-emergence.html)**
   20 points by `PaulHoule` - [10 comments](https://news.ycombinator.com/item?id=50532417)
