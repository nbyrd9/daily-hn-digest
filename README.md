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

## Latest snapshot - [`2026-11-01.md`](./digests/2026-11-01.md)

_Captured 2026-11-01 11:59 UTC._

1. **[Norway makes shithouses great again](https://www.visitnorway.com/plan-your-trip/travel-tips-a-z/norwegian-scenic-routes/worlds-best-toilets/)**
   136 points by `giuliomagnifico` - [51 comments](https://news.ycombinator.com/item?id=50324388)

2. **[HackerTube: YouTube built from videos recommended by HN](https://karpathy.bearblog.dev/hacker-tube/)**
   1449 points by `karpathy` - [392 comments](https://news.ycombinator.com/item?id=50319510)

3. **[A tiny Pacific country rolls out universal basic income](https://www.economist.com/asia/2026/10/29/a-tiny-pacific-country-rolls-out-universal-basic-income)**
   35 points by `motionlessveloc` - [7 comments](https://news.ycombinator.com/item?id=50324118)

4. **[An Italian farmer found some unknown seeds in his attic and planted them](https://www.smithsonianmag.com/science-nature/italian-farmer-found-unknown-seeds-attic-with-nothing-lose-planted-them-result-biblical-180989644/)**
   494 points by `ecares` - [153 comments](https://news.ycombinator.com/item?id=50320963)

5. **[The AI cost of JavaScript frameworks](https://nolanlawson.com/2026/10/28/the-ai-cost-of-javascript-frameworks/)**
   108 points by `luu` - [56 comments](https://news.ycombinator.com/item?id=50323088)

6. **[Brazilian Court Sanctions Lawyers for Prompt Injection in Court Filing](https://jetstream.security/insights/brazilian-court-sanctions-prompt-injection-filing/)**
   152 points by `doodlesdev` - [61 comments](https://news.ycombinator.com/item?id=50322173)

7. **[Running a bootstrapped SaaS for 20 years with my brother](https://blog.zamzar.com/2026/10/30/20-years-766-million-files-two-chameleons/)**
   114 points by `whyleyc` - [29 comments](https://news.ycombinator.com/item?id=50303984)

8. **[TCP Use-After-Free: CVE-2026-98432 / CVSS 9.8](https://atlasum.net/blog/cve-2026-98432-linux-ipv4-tcp-uaf)**
   539 points by `oger` - [249 comments](https://news.ycombinator.com/item?id=50319143)

9. **[Memdoor: A team of 5 Qwen3.8-27B models beats Fable 5 on LiveCodeBench Hard](https://github.com/guregodevo/memdoor/tree/main/examples/workflows/team-solve)**
   266 points by `guregodevo` - [122 comments](https://news.ycombinator.com/item?id=50320995)

10. **[Domain hacks with unusual Unicode characters (2018)](https://xn--69f31l4t57c0mag4b613h.xn--7uh4898msjaso/🆆🆃🅵/)**
   7 points by `n_plus_1_acc` - [2 comments](https://news.ycombinator.com/item?id=50324371)
