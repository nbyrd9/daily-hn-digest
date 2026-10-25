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

## Latest snapshot - [`2026-10-25.md`](./digests/2026-10-25.md)

_Captured 2026-10-25 20:39 UTC._

1. **[Dolly Parton's Imagination Library](https://imaginationlibrary.com/)**
   178 points by `jumploops` - [27 comments](https://news.ycombinator.com/item?id=50234474)

2. **[Eunice is almost here (William Gibson, Agency)](https://armincat.com/articles/eunice-is-almost-here)**
   17 points by `armcat` - [13 comments](https://news.ycombinator.com/item?id=50235316)

3. **[Why the Rich Are Getting Richer and the Poor Are Further Removed from Prosperity](https://lusopt2016.blogspot.com/2026/10/a-grande-divisao-porque-e-que-os-ricos.html)**
   10 points by `inandout` - [0 comments](https://news.ycombinator.com/item?id=50235433)

4. **[A 10-year-old CNN outperforms frontier LLMs for skin cancer diagnosis](https://lynchlab.net/llm-skin-cancer)**
   271 points by `sungam` - [131 comments](https://news.ycombinator.com/item?id=50233779)

5. **[I refuse to accept a censored Internet. Join Me at FOSDEM 27](https://talkweb.eu/openweb/4558/)**
   256 points by `Tomte` - [124 comments](https://news.ycombinator.com/item?id=50233929)

6. **[JetBrains Thinkrail](https://github.com/JetBrains/thinkrail)**
   85 points by `hmokiguess` - [39 comments](https://news.ycombinator.com/item?id=50233294)

7. **[Oregon Police Are Charging a Local News Outlet $2.5M for Records About One Cop](https://theintercept.com/2026/10/01/oregon-police-misconduct-public-records-cost-fee/)**
   210 points by `tdeck` - [51 comments](https://news.ycombinator.com/item?id=50234232)

8. **[Why I Am a Programmer](https://www.alfie.wtf/programming/why-i-am-a-programmer.html)**
   16 points by `jruohonen` - [5 comments](https://news.ycombinator.com/item?id=50235017)

9. **[VCF Southwest 2026, but Edited on Silicon Graphics for '90s TV [video]](https://www.youtube.com/watch?v=46wxttvq9qY)**
   33 points by `zdw` - [9 comments](https://news.ycombinator.com/item?id=50223435)

10. **[Gheist campaign plants secret-dumping workflows using stolen GitHub tokens](https://www.wiz.io/blog/gheist-attempted-scaled-abuse-of-stolen-github-tokens-stumbles)**
   8 points by `acossta` - [0 comments](https://news.ycombinator.com/item?id=50235010)
