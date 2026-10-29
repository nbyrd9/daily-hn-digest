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

## Latest snapshot - [`2026-10-29.md`](./digests/2026-10-29.md)

_Captured 2026-10-29 02:27 UTC._

1. **[Qwenputer: A functioning, deterministic RISC-V CPU inside Qwen3.5](https://divagr.com/blog/qwenputer)**
   99 points by `csmantle` - [22 comments](https://news.ycombinator.com/item?id=50282838)

2. **[Why is this fingerprinting script creating bioweapons?](https://nullpt.rs/fingerprinting-bioweapons)**
   887 points by `hazebooth` - [188 comments](https://news.ycombinator.com/item?id=50276998)

3. **[GitLab Security Incident: Attempted Exploitation of CVE-2026-97229](https://alpinelinux.org/posts/GitLab-security-incident-CVE-2026-97229.html)**
   82 points by `sashk` - [28 comments](https://news.ycombinator.com/item?id=50282544)

4. **[The first wired XR glasses powered by Android XR](https://blog.google/products-and-platforms/platforms/android/xreal-aura/)**
   38 points by `yincrash` - [29 comments](https://news.ycombinator.com/item?id=50282538)

5. **[A Health Update](https://furbo.org/2026/10/28/a-health-update/)**
   112 points by `frizlab` - [12 comments](https://news.ycombinator.com/item?id=50280974)

6. **[CNC Stone Carving](https://carmelitegothic.com/cnc-stone-carving/)**
   408 points by `bschne` - [118 comments](https://news.ycombinator.com/item?id=50274409)

7. **[Gemini 4 Carbon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/)**
   815 points by `acossta` - [679 comments](https://news.ycombinator.com/item?id=50276792)

8. **[Formlabs Studio 1 $699 Resin Printer](https://formlabs.com/products/form-studio-1-basic-founders-edition/)**
   126 points by `mhb` - [88 comments](https://news.ycombinator.com/item?id=50281044)

9. **[The Grid, a factory-scale robot in Massachusetts that builds PCBs on demand](https://www.circuithub.com/post/unveiling-the-grid)**
   434 points by `seddona` - [205 comments](https://news.ycombinator.com/item?id=50243060)

10. **[Start Doing Graph Theory](https://vertex.degree/)**
   589 points by `ibobev` - [129 comments](https://news.ycombinator.com/item?id=50208960)
