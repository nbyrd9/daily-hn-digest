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

## Latest snapshot - [`2026-10-13.md`](./digests/2026-10-13.md)

_Captured 2026-10-13 18:16 UTC._

1. **[Gemini 4 Argon](https://deepmind.google/models/gemini/)**
   471 points by `737max` - [356 comments](https://news.ycombinator.com/item?id=50073879)

2. **[Apple HomeView](https://www.apple.com/apple-homeview/)**
   478 points by `etothet` - [588 comments](https://news.ycombinator.com/item?id=50071017)

3. **[Cyberattack halts construction of tunnel between Denmark and Germany](https://ua.news/en/world/kiberataka-zupinila-budivnitstvo-tuneliu-mizh-daniieiu-ta-nimechchinoiu-rmf24)**
   72 points by `paaloeye` - [24 comments](https://news.ycombinator.com/item?id=50074289)

4. **[Thunderbird for iOS](https://blog.thunderbird.net/2026/10/thunderbird-for-ios-a-first-look-at-the-native-iphone-email-app-in-development/)**
   163 points by `mjorgers` - [59 comments](https://news.ycombinator.com/item?id=50072913)

5. **[11 year old unsoundness bugs found in Rust borrow checker](https://github.com/rust-lang/rust/issues/164250)**
   561 points by `formerly_proven` - [326 comments](https://news.ycombinator.com/item?id=50069499)

6. **[Gemini 4 Argon for Robotics](https://developers.googleblog.com/gemini-4-argon-for-robotics/)**
   38 points by `xnx` - [8 comments](https://news.ycombinator.com/item?id=50074869)

7. **[Firefox Enterprise](https://www.firefox.com/en-US/enterprise/)**
   418 points by `recvonline` - [173 comments](https://news.ycombinator.com/item?id=50070302)

8. **[Redesigning source control at Anthropic](https://www.anthropic.com/engineering/redesigning-source-control)**
   107 points by `Philpax` - [78 comments](https://news.ycombinator.com/item?id=50073633)

9. **[I posted to HN, and then my website was flooded with AI bot traffic](https://www.sammystraus.com/#i-posted-to-hn-and-then-my-website-was-flooded-with-ai-bot-traffic)**
   112 points by `sammy0910` - [70 comments](https://news.ycombinator.com/item?id=50073221)

10. **[We turned EmbeddingGemma 2 into a speech-to-text model](https://eg2.haku.sh/)**
   316 points by `amrrs` - [78 comments](https://news.ycombinator.com/item?id=50069971)
