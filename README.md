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

## Latest snapshot - [`2026-11-19.md`](./digests/2026-11-19.md)

_Captured 2026-11-19 15:52 UTC._

1. **[How the European Commission rolled out Matrix to more than 40k staff](https://element.io/blog/how-the-european-commission-rolled-out-matrix-to-more-than-40-000-staff/)**
   431 points by `liotier` - [216 comments](https://news.ycombinator.com/item?id=50558533)

2. **[Everything you need to survive and rebuild society](https://lastbook.org/)**
   34 points by `tejohnso` - [13 comments](https://news.ycombinator.com/item?id=50560822)

3. **[Garage Door Spam](https://blog.harrison.page/garage-door-spam/)**
   358 points by `harrisonpage` - [144 comments](https://news.ycombinator.com/item?id=50519231)

4. **[Making 8-page foldable zines from a single A4 sheet in the browser](https://krthr.co/paper-folds-and-whats-new-in-fanzines-app/)**
   80 points by `krthr` - [23 comments](https://news.ycombinator.com/item?id=50559719)

5. **[Show HN: Foolscap – a writing app that reads your book and never writes for you](https://foolscap.works/)**
   68 points by `atugard` - [34 comments](https://news.ycombinator.com/item?id=50559749)

6. **[Nintendo takes Picofly firmware down from GitHub [video]](https://www.youtube.com/watch?v=-TLCGUpoD6c)**
   135 points by `cowlevel` - [37 comments](https://news.ycombinator.com/item?id=50547048)

7. **[Someone reported java4shell bug in September 2026](https://github.com/openjdk/jdk/pull/32781)**
   104 points by `notmine1337` - [27 comments](https://news.ycombinator.com/item?id=50558906)

8. **[Cooling buildings is overtaking heating them as an energy need, IEA says](https://maccus.fr/en/cooling-overtaking-heating/)**
   13 points by `robtherobber` - [2 comments](https://news.ycombinator.com/item?id=50560955)

9. **[Ruby2ßhell: Pre-authentication RCE on stock Rails](https://verialabs.com/ruby2shell/)**
   280 points by `jdns` - [111 comments](https://news.ycombinator.com/item?id=50556287)

10. **[OpenAI still has a WebRTC Problem](https://moq.dev/blog/webrtc-is-still-the-problem/)**
   45 points by `surprisetalk` - [12 comments](https://news.ycombinator.com/item?id=50560461)
