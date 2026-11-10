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

## Latest snapshot - [`2026-11-10.md`](./digests/2026-11-10.md)

_Captured 2026-11-10 19:43 UTC._

1. **[.name Grandfathered](https://neil.fraser.name/news/2026/11/10/)**
   397 points by `p4bl0` - [68 comments](https://news.ycombinator.com/item?id=50442736)

2. **[Smart home devices should work without the internet](https://docodethatmatters.com/home-automation-overnight-success/)**
   322 points by `skittleson` - [134 comments](https://news.ycombinator.com/item?id=50441707)

3. **[Synaptics patent claims stop work on DisplayLink drivers](https://lwn.net/SubscriberLink/1102549/acbc92e00cee3a3f/)**
   94 points by `speckx` - [44 comments](https://news.ycombinator.com/item?id=50443824)

4. **[Val Town is winding down](https://blog.val.town/winding-down)**
   136 points by `tosh` - [35 comments](https://news.ycombinator.com/item?id=50443427)

5. **[Starlink Mini 2](https://starlink.com/mini-2)**
   92 points by `robertjfclarke` - [68 comments](https://news.ycombinator.com/item?id=50444129)

6. **[AlphaProof Code](https://deepmind.google/blog/introducing-alphaproof-code/)**
   496 points by `ilreb` - [162 comments](https://news.ycombinator.com/item?id=50439193)

7. **[AMD's Zen 6 Family: Feeding the Beast](https://chipsandcheese.com/p/amds-zen-6-family-feeding-the-beast)**
   88 points by `pixelpoet` - [33 comments](https://news.ycombinator.com/item?id=50443090)

8. **[Show HN: Get your coding agent off ~2019 JavaScript, onto modern web primitives](https://github.com/GoogleChrome/modern-web-guidance)**
   67 points by `paulirish` - [27 comments](https://news.ycombinator.com/item?id=50443812)

9. **[Blender 5.3 released with Gaussian Splat support](https://www.blender.org/download/releases/5-3/)**
   303 points by `amlib` - [43 comments](https://news.ycombinator.com/item?id=50442426)

10. **[Ableton Live 13](https://www.ableton.com/en/live/)**
   197 points by `phaser` - [234 comments](https://news.ycombinator.com/item?id=50439695)
