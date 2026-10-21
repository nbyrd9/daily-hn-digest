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

## Latest snapshot - [`2026-10-21.md`](./digests/2026-10-21.md)

_Captured 2026-10-21 09:35 UTC._

1. **[The Future of CSS](https://www.joshwcomeau.com/css/interop-2027/)**
   364 points by `soheilpro` - [141 comments](https://news.ycombinator.com/item?id=50175070)

2. **[Eight Bits of Trust; eMudhra's CA keys cracked in milliseconds](https://scotthelme.co.uk/eight-bits-of-trust-emudhras-ca-keys-cracked-in-milliseconds/)**
   8 points by `hkc` - [0 comments](https://news.ycombinator.com/item?id=50177916)

3. **[The 1.5°C goal of the Paris Agreement is no longer viable](https://unric.org/en/unep-emissions-gap-report-2026-1-5-degree-overshoot/)**
   8 points by `velo_aprx` - [0 comments](https://news.ycombinator.com/item?id=50177911)

4. **[Show HN: SimCity, but with Permits](https://permit.petercai.com/)**
   792 points by `pcai` - [374 comments](https://news.ycombinator.com/item?id=50170593)

5. **[Upcoming critical PHP security release (CVE-2026-109618 / -109619)](https://news-web.php.net/php.announce/509)**
   797 points by `xd` - [314 comments](https://news.ycombinator.com/item?id=50172041)

6. **[Muse exposes users' personal and business secrets when they share conversations](https://arstechnica.com/security/2026/10/meta-muse-exposes-users-personal-and-business-secrets-when-they-share-conversations/)**
   171 points by `gumby` - [66 comments](https://news.ycombinator.com/item?id=50174687)

7. **[The Decoherence Trap](https://maevyn.codes/decoherence)**
   35 points by `cassianoleal` - [6 comments](https://news.ycombinator.com/item?id=50149861)

8. **[Voxtral 3](https://mistral.ai/news/voxtral-3/)**
   667 points by `ilreb` - [166 comments](https://news.ycombinator.com/item?id=50168396)

9. **[eMudhra intermediate CA compromise](https://emudhra.we-have-a-problem.com/)**
   938 points by `galadran` - [394 comments](https://news.ycombinator.com/item?id=50166579)

10. **[Feds suspect ransom negotiator ran ShinyHunters extortion site](https://krebsonsecurity.com/2026/10/feds-suspect-ransom-negotiator-ran-shinyhunters-extortion-site/)**
   201 points by `Bender` - [93 comments](https://news.ycombinator.com/item?id=50173487)
