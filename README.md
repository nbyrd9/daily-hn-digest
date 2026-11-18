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

## Latest snapshot - [`2026-11-18.md`](./digests/2026-11-18.md)

_Captured 2026-11-18 23:24 UTC._

1. **[Unauthenticated remote code execution in Nginx](https://www.wiz.io/blog/nginx-http2-rce-vulnerabilities)**
   1014 points by `speedping` - [467 comments](https://news.ycombinator.com/item?id=50547374)

2. **[Seven new models at scalable price-performance](https://microsoft.ai/news/microsoft-ignite-2026/)**
   396 points by `gmays` - [274 comments](https://news.ycombinator.com/item?id=50548021)

3. **[Inside Deutsche Bank](https://www.inside-db.com/)**
   504 points by `gyre007` - [181 comments](https://news.ycombinator.com/item?id=50547620)

4. **[DaisyRose-27B: 1,200-task RL took Qwen3.8 from 5.6% to 12% on Terminal-Bench 4.1](https://www.radixark.com/blog/daisyrose-27b)**
   102 points by `de_sty` - [26 comments](https://news.ycombinator.com/item?id=50551046)

5. **[AI agents ask better questions than KPMG accountants in audit trial](https://europeanbusinessmagazine.com/ai-agents-better-questions-kpmg/)**
   304 points by `Betelbuddy` - [141 comments](https://news.ycombinator.com/item?id=50547777)

6. **[DNS resolvers are the wrong place to fight piracy](https://techstackups.com/articles/quad9-leaves-france-dns-blocking/)**
   554 points by `ritzaco` - [204 comments](https://news.ycombinator.com/item?id=50545958)

7. **[Gemini 4 Neon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/)**
   299 points by `yigitdemirag` - [291 comments](https://news.ycombinator.com/item?id=50552424)

8. **[Cuttlefish on Mac: Android's Virtual Device Framework on Apple Silicon](https://engineering.fb.com/2026/11/13/android/cuttlefish-on-mac/)**
   22 points by `acossta` - [3 comments](https://news.ycombinator.com/item?id=50510385)

9. **[Advancing chip design with OpenAI models](https://openai.com/index/advancing-chip-design-with-our-models/)**
   138 points by `vighneshiyer` - [78 comments](https://news.ycombinator.com/item?id=50549493)

10. **[The Cambridge Dictionary has named ‘human’ as the Word of the Year 2026](https://www.cam.ac.uk/news/cambridge-dictionary-reveals-word-of-the-year-2026)**
   221 points by `DeepLogin` - [164 comments](https://news.ycombinator.com/item?id=50546914)
