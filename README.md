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

_Captured 2026-10-29 07:54 UTC._

1. **[Qwenputer: A functioning, deterministic RISC-V CPU inside Qwen3.5](https://divagr.com/blog/qwenputer)**
   357 points by `csmantle` - [80 comments](https://news.ycombinator.com/item?id=50282838)

2. **[Why is this fingerprinting script creating bioweapons?](https://nullpt.rs/fingerprinting-bioweapons)**
   1104 points by `hazebooth` - [219 comments](https://news.ycombinator.com/item?id=50276998)

3. **[We Won't "Just Hang Out"](https://borretti.me/article/we-wont-just-hang-out)**
   18 points by `barry-cotter` - [11 comments](https://news.ycombinator.com/item?id=50285154)

4. **[A new faster algorithm to compute 64-bit signed floor division](https://www.benjoffe.com/fast-floordiv)**
   41 points by `benjoffe` - [3 comments](https://news.ycombinator.com/item?id=50256409)

5. **[A Health Update](https://furbo.org/2026/10/28/a-health-update/)**
   220 points by `frizlab` - [35 comments](https://news.ycombinator.com/item?id=50280974)

6. **[GitLab Security Incident: Attempted Exploitation of CVE-2026-97229](https://alpinelinux.org/posts/GitLab-security-incident-CVE-2026-97229.html)**
   162 points by `sashk` - [68 comments](https://news.ycombinator.com/item?id=50282544)

7. **[StackOverflow now gets fewer than 1000 questions a month](https://data.stackexchange.com/stackoverflow/query/1926661#graph?t=1)**
   351 points by `babelfish` - [296 comments](https://news.ycombinator.com/item?id=50282454)

8. **[Claude Code regularly sends each background agent’s transcript to its model](https://gist.github.com/flamerix-ai/c3905705cc4205e5de3011fa2e74efce)**
   303 points by `NikZaal` - [92 comments](https://news.ycombinator.com/item?id=50284255)

9. **[OpenAI's agents talked to each other through the CPU Cache](https://the-decoder.com/openais-isolated-ai-agents-found-ways-to-talk-to-each-other-through-cpu-cache/)**
   83 points by `limbicsystem` - [26 comments](https://news.ycombinator.com/item?id=50251200)

10. **[CNC Stone Carving](https://carmelitegothic.com/cnc-stone-carving/)**
   457 points by `bschne` - [127 comments](https://news.ycombinator.com/item?id=50274409)
