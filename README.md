# Daily Hacker News Digest

A self-updating archive of the top 10 [Hacker News](https://news.ycombinator.com/)
stories. A scheduled GitHub Actions workflow captures the current standings
one to three times a day, at randomized times, rewriting the dated file for
the day under [`digests/`](./digests) and refreshing the snapshot below -- so
this repo doubles as a searchable record of what the tech community was
reading, and how the rankings shifted through the day.

- **How it works:** [`.github/workflows/daily-digest.yml`](./.github/workflows/daily-digest.yml)
  fires every 2 hours; [`scripts/scheduled_commit.py`](./scripts/scheduled_commit.py)
  uses a date-seeded RNG to pick 1-3 two-hour windows for the day, waits a
  random 0-85 minutes, then builds the digest via
  [`scripts/build_digest.py`](./scripts/build_digest.py), commits, and pushes.
- **Data source:** the public [Hacker News API](https://github.com/HackerNews/API)
  (no authentication).
- **Browse the archive:** [`digests/`](./digests)

---

## Latest snapshot - [`2026-09-01.md`](./digests/2026-09-01.md)

_Captured 2026-09-01 23:19 UTC._

1. **[Claude Fable 5.1 and Claude Mythos 5.1](https://www.anthropic.com/claude-fable-and-mythos-5-1)**
   817 points by `denysvitali` - [786 comments](https://news.ycombinator.com/item?id=49525378)

2. **[Hang on to Your Firefox](https://www.newsonaut.com/articles/hang-on-to-your-firefox)**
   135 points by `speckx` - [75 comments](https://news.ycombinator.com/item?id=49527748)

3. **[How accurate have Ed Zitron's AI skeptic predictions been?](https://danluu.com/zitron/)**
   303 points by `jatins` - [353 comments](https://news.ycombinator.com/item?id=49526069)

4. **[Show HN: Weedout – Safari extension that hides YouTube AI-labeled videos](https://masteranza.github.io/weedout/)**
   26 points by `masteranza` - [8 comments](https://news.ycombinator.com/item?id=49528895)

5. **[The ChatGPT/Codex app bundles a full copy of LibreOffice](https://simonwillison.net/2026/Sep/1/codex-libreoffice/)**
   191 points by `timpera` - [99 comments](https://news.ycombinator.com/item?id=49527396)

6. **[AnkiDroid: Google Play no longer allowing Open Collective donation link](https://github.com/ankidroid/Anki-Android/issues/21656)**
   808 points by `hexa555` - [236 comments](https://news.ycombinator.com/item?id=49520022)

7. **[Refurbishing a Tektronix TDS7104 Oscilloscope](https://tomverbeure.github.io/2026/08/23/Tektronix-TDS7104-Refurbishing.html)**
   64 points by `jwise0` - [31 comments](https://news.ycombinator.com/item?id=49527232)

8. **[Path to Astra: critical capabilities and frontier safeguards](https://openai.com/index/path-to-astra/)**
   65 points by `jithinraj` - [21 comments](https://news.ycombinator.com/item?id=49527595)

9. **[The creator of Jujutsu has joined ERSC](https://ersc.io/blog/martin-joins-ersc)**
   159 points by `steveklabnik` - [124 comments](https://news.ycombinator.com/item?id=49525297)

10. **[Introducing Ad Blocker for Firefox on iOS](https://blog.mozilla.org/en/firefox/ad-blocker-on-ios/)**
   263 points by `HieronymusBosch` - [95 comments](https://news.ycombinator.com/item?id=49521973)
