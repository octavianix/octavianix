#!/usr/bin/env python3
"""Render an animated GitHub contribution graph as a self-contained SVG.

Fetches the last year of contributions with the GraphQL API (needs GH_TOKEN
or GITHUB_TOKEN), or reads them from a JSON file mapping dates to counts.

    python scripts/contrib_graph.py --login octavianix --out assets/contrib.svg
    python scripts/contrib_graph.py --from-json days.json --out assets/contrib.svg
"""
import argparse
import datetime as dt
import json
import os
import urllib.request

QUERY = """query($login: String!) {
  user(login: $login) {
    contributionsCollection {
      contributionCalendar {
        weeks { contributionDays { date contributionCount contributionLevel } }
      }
    }
  }
}"""

LEVELS = {"NONE": 0, "FIRST_QUARTILE": 1, "SECOND_QUARTILE": 2,
          "THIRD_QUARTILE": 3, "FOURTH_QUARTILE": 4}

CELL, GAP = 14, 4
PITCH = CELL + GAP
LEFT, TOP = 40, 78


def fetch(login, token):
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": {"login": login}}).encode(),
        headers={"Authorization": f"bearer {token}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        data = json.load(r)
    if "errors" in data:
        raise SystemExit(f"GraphQL error: {data['errors']}")
    weeks = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
    return [(dt.date.fromisoformat(d["date"]), d["contributionCount"], LEVELS[d["contributionLevel"]])
            for w in weeks for d in w["contributionDays"]]


def from_counts(counts):
    """Assign GitHub-style quartile levels to {date: count}."""
    days = sorted((dt.date.fromisoformat(k), v) for k, v in counts.items())
    nonzero = sorted(v for _, v in days if v)
    def level(v):
        if not v:
            return 0
        q = [nonzero[int(len(nonzero) * f)] for f in (0.25, 0.5, 0.75)]
        return 1 + sum(v > t for t in q)
    return [(d, v, level(v)) for d, v in days]


def streaks(days):
    longest = run = 0
    for _, v, _ in days:
        run = run + 1 if v else 0
        longest = max(longest, run)
    current = 0
    for i, (_, v, _) in enumerate(reversed(days)):
        if v:
            current += 1
        elif i:  # today may still be empty
            break
    return current, longest


def render(days):
    total = sum(v for _, v, _ in days)
    active = sum(1 for _, v, _ in days if v)
    current, longest = streaks(days)
    best = max(days, key=lambda x: x[1])

    start = days[0][0] - dt.timedelta(days=(days[0][0].weekday() + 1) % 7)  # weeks start Sunday
    n_weeks = (days[-1][0] - start).days // 7 + 1
    width = LEFT + n_weeks * PITCH + 20
    height = TOP + 7 * PITCH + 46

    cells, months, last_month = [], [], None
    for d, v, lvl in days:
        week = (d - start).days // 7
        dow = (d.weekday() + 1) % 7
        x, y = LEFT + week * PITCH, TOP + dow * PITCH
        delay = week * 0.035 + dow * 0.012
        pulse = (f";animation:pop .5s cubic-bezier(.3,1.6,.5,1) {delay:.2f}s both,"
                 f"glow 6s ease-in-out {2.4 + week * 0.06:.2f}s infinite") if lvl else ""
        cells.append(f'<rect class="l{lvl}" x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="3" '
                     f'style="animation-delay:{delay:.2f}s{pulse}"><title>{v} on {d:%d %b %Y}</title></rect>')
        if dow == 0 and d.month != last_month:
            last_month = d.month
            months.append(f'<text class="m" x="{x}" y="{TOP - 10}">{d:%b}</text>')

    for i, label in ((1, "Mon"), (3, "Wed"), (5, "Fri")):
        months.append(f'<text class="m" x="{LEFT - 8}" y="{TOP + i * PITCH + 11}" text-anchor="end">{label}</text>')

    legend_x = width - 56 - 5 * PITCH
    legend = "".join(f'<rect class="l{i} lg" x="{legend_x + i * PITCH}" y="{height - 30}" width="{CELL}" '
                     f'height="{CELL}" rx="3"/>' for i in range(5))
    stats = (f"{active} active days  ·  longest streak {longest} days  ·  current streak {current} "
             f"days  ·  busiest day {best[1]} on {best[0]:%d %b}")

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" role="img" aria-labelledby="t">
<title id="t">{total:,} contributions in the last year. {stats}.</title>
<style>
text{{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;fill:#59636e}}
.h{{font-size:22px;font-weight:700;fill:#1f2328}} .s{{font-size:13px}} .m{{font-size:11px}}
.l0{{fill:#ebedf0}} .l1{{fill:#9be9a8}} .l2{{fill:#40c463}} .l3{{fill:#30a14e}} .l4{{fill:#216e39}}
rect{{transform-box:fill-box;transform-origin:center;animation:pop .5s ease-out both}}
.lg{{animation:none}}
@keyframes pop{{from{{opacity:0;transform:scale(.2)}}to{{opacity:1;transform:scale(1)}}}}
@keyframes glow{{0%,88%,100%{{filter:none}}94%{{filter:brightness(1.35) saturate(1.2)}}}}
@media (prefers-color-scheme:dark){{
text{{fill:#8b949e}} .h{{fill:#e6edf3}}
.l0{{fill:#161b22}} .l1{{fill:#0e4429}} .l2{{fill:#006d32}} .l3{{fill:#26a641}} .l4{{fill:#39d353}}}}
@media (prefers-reduced-motion:reduce){{rect{{animation:none!important}}}}
</style>
<text class="h" x="{LEFT}" y="30">{total:,} contributions in the last year</text>
<text class="s" x="{LEFT}" y="52">{stats}</text>
{"".join(months)}
{"".join(cells)}
<text class="m" x="{legend_x - 8}" y="{height - 19}" text-anchor="end">Less</text>{legend}
<text class="m" x="{legend_x + 5 * PITCH + 2}" y="{height - 19}">More</text>
</svg>'''


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--login", default=os.environ.get("GITHUB_REPOSITORY_OWNER"))
    ap.add_argument("--from-json", help="JSON file mapping YYYY-MM-DD to a contribution count")
    ap.add_argument("--out", default="assets/contrib.svg")
    a = ap.parse_args()
    if a.from_json:
        with open(a.from_json) as f:
            days = from_counts(json.load(f))
    else:
        token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
        if not token or not a.login:
            raise SystemExit("Set GH_TOKEN/GITHUB_TOKEN and --login, or pass --from-json")
        days = fetch(a.login, token)
    with open(a.out, "w") as f:
        f.write(render(days))
    print(f"wrote {a.out}: {sum(v for _, v, _ in days)} contributions over {len(days)} days")


if __name__ == "__main__":
    main()
