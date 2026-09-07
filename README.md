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

## Latest snapshot - [`2026-09-07.md`](./digests/2026-09-07.md)

_Captured 2026-09-07 14:47 UTC._

1. **[De-Brainrot Vacations](https://devz.cl/posts/i-spent-my-vacations-de-brainrotting/)**
   190 points by `DanielVZ` - [71 comments](https://news.ycombinator.com/item?id=49597907)

2. **[bzip3](https://github.com/iczelia/bzip3)**
   55 points by `tosh` - [13 comments](https://news.ycombinator.com/item?id=49598291)

3. **[Keep Our Servers Running](https://blog.archive.org/2026/09/01/keep-our-servers-running-your-recurring-donation-goes-3x-this-september/)**
   702 points by `sonicrocketman` - [173 comments](https://news.ycombinator.com/item?id=49593563)

4. **[Splash-free urinals (2025)](https://academic.oup.com/pnasnexus/article/4/4/pgaf087/8098745?login=false)**
   106 points by `u1hcw9nx` - [48 comments](https://news.ycombinator.com/item?id=49597895)

5. **[Caltech Mathathon – first hackathon ever devoted to research level mathematics](https://mathathonchallenge.com/index.html)**
   95 points by `astroanax` - [21 comments](https://news.ycombinator.com/item?id=49596055)

6. **[Live map of public transport in Belgium](https://openbaarvervoerbelgie.be/)**
   112 points by `coinfused` - [49 comments](https://news.ycombinator.com/item?id=49595865)

7. **[Smartphone makers don't bother to comply with EU repairability requirements](https://www.theregister.com/personal-tech/2026/09/07/smartphone-makers-dont-bother-to-comply-with-eu-repairability-requirements/5294532)**
   131 points by `mdp2021` - [55 comments](https://news.ycombinator.com/item?id=49597189)

8. **[Speculative Decoding in vLLM on AMD GPUs](https://vllm.ai/blog/2026-08-23-speculative-decoding-amd-gpus)**
   66 points by `ankitg12` - [18 comments](https://news.ycombinator.com/item?id=49596054)

9. **[Impedance Matching (2017)](https://www.edge.org/response-detail/27238)**
   47 points by `muti` - [16 comments](https://news.ycombinator.com/item?id=49596274)

10. **[LG smart TVs caught logging audio with screen off and snooping on local devices](https://www.notebookcheck.net/LG-smart-TVs-caught-logging-audio-with-screen-off-and-snooping-on-local-devices.1391214.0.html)**
   596 points by `chris_overseas` - [305 comments](https://news.ycombinator.com/item?id=49594878)
