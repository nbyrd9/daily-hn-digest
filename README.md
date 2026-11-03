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

## Latest snapshot - [`2026-11-03.md`](./digests/2026-11-03.md)

_Captured 2026-11-03 09:06 UTC._

1. **[Astra can read and write weights to improve Qwen](https://rikiyat.github.io/blog/weight-space-programming/)**
   2541 points by `dbreunig` - [784 comments](https://news.ycombinator.com/item?id=50341174)

2. **[Nvidia – open-source auto-ontology](https://github.com/NVIDIA/auto-ontology)**
   37 points by `campervans` - [4 comments](https://news.ycombinator.com/item?id=50348962)

3. **[Show HN: Hacker Times, a New York Times-inspired version of Hacker News](https://hackertimes.ca/)**
   238 points by `polpenn` - [74 comments](https://news.ycombinator.com/item?id=50346981)

4. **[DiscImageStudio: burn visible artwork onto CDs, DVDs and Blu-ray discs](https://github.com/JiaFeiMiao-K-Cat/DiscImageStudio)**
   180 points by `bpierre` - [45 comments](https://news.ycombinator.com/item?id=50346849)

5. **[European RISC-V Industrial Computing Initiative](https://erici.eu)**
   92 points by `ymz5` - [44 comments](https://news.ycombinator.com/item?id=50334523)

6. **[Show HN: Subvocal – Talk to your computer without making noise](https://news.ycombinator.com/item?id=50340088)**
   679 points by `aarushyadav` - [336 comments](https://news.ycombinator.com/item?id=50340088)

7. **[Resisting Cognitive Surrender](https://knlb.dev/essays/surrender)**
   150 points by `knlb` - [62 comments](https://news.ycombinator.com/item?id=50323123)

8. **[Toit v2.0.0](https://toit.io/blog/toit-v2-0-0/)**
   40 points by `floitsch` - [15 comments](https://news.ycombinator.com/item?id=50321605)

9. **[Efficient algorithms, the Exponential Time Hypothesis, and losing the plot](https://www.argmin.net/p/galactus-the-devourer)**
   33 points by `sebg` - [14 comments](https://news.ycombinator.com/item?id=50320904)

10. **[US boy names that became girl names and vice versa](https://namedaisy.com/blog/boy-names-that-became-girl-names)**
   393 points by `xoobdev` - [370 comments](https://news.ycombinator.com/item?id=50339397)
