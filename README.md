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

## Latest snapshot - [`2026-09-17.md`](./digests/2026-09-17.md)

_Captured 2026-09-17 09:54 UTC._

1. **[One Year of Sponsored Servo Development](https://servo.org/blog/2026/09/15/one-year-of-sponsorship/)**
   60 points by `AshleysBrain` - [26 comments](https://news.ycombinator.com/item?id=49737849)

2. **[I didn't sign the Fields medallists' letter](https://gowers.wordpress.com/2026/09/17/why-i-didnt-sign-the-fields-medallists-letter/)**
   18 points by `simianwords` - [24 comments](https://news.ycombinator.com/item?id=49738091)

3. **[Nvidia announces native GPU programming in Rust](https://developer.nvidia.com/blog/introducing-cuda-rust-two-tracks-for-writing-gpu-kernels/)**
   685 points by `nonmaskable` - [268 comments](https://news.ycombinator.com/item?id=49724881)

4. **[Keys Not Included: recovering the signing keys for US driver's license barcodes](https://ryan.science/blog/keys-not-included)**
   167 points by `Ryan5453` - [64 comments](https://news.ycombinator.com/item?id=49735930)

5. **[The Relation Between Mathematics and Physics by Paul Dirac](https://www.damtp.cam.ac.uk/events/strings02/dirac/speach.html)**
   46 points by `rramadass` - [12 comments](https://news.ycombinator.com/item?id=49685835)

6. **[My temporary PHP fix from 2014 has nearly 20M installs. Today I'm deprecating it](https://jakeasmith.com/blog/http-build-url/)**
   104 points by `jakeasmith` - [17 comments](https://news.ycombinator.com/item?id=49718773)

7. **[Training a 4B model to produce 81% faster query plans than Postgres](https://rohanbansal.com/qorl)**
   550 points by `polyphilz` - [117 comments](https://news.ycombinator.com/item?id=49731285)

8. **[GLM Built Its Own Inference Infrastructure](https://z.ai/blog/glm-built-its-inference-infrastructure)**
   12 points by `whiteros_e` - [0 comments](https://news.ycombinator.com/item?id=49737922)

9. **[Lucasart's Afterlife](https://togameforlife.wordpress.com/2023/12/09/on-lucasarts-afterlife/)**
   18 points by `Bondi_Blue` - [10 comments](https://news.ycombinator.com/item?id=49719751)

10. **[Xiaomi Mimo 2.6 live post-training dashboard](https://mimo.xiaomi.com/rl/)**
   434 points by `krackers` - [111 comments](https://news.ycombinator.com/item?id=49732270)
