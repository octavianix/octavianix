#!/usr/bin/env python3
"""Render an animated GitHub contribution graph as a self-contained SVG.

Fetches the last year of contributions with the GraphQL API (needs GH_TOKEN
or GITHUB_TOKEN), or reads them from a JSON file mapping dates to counts.

    python scripts/contrib_graph.py --login octavianix --out assets/contrib.svg
    python scripts/contrib_graph.py --from-json days.json --out assets/contrib.svg
"""
import argparse
import base64
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
LEFT, TOP = 40, 96
LAP = 12  # seconds between laps of the little car

# Side-view F1 car, about 245 x 64 units, drawn facing right.
CAR = (
    '<path fill="#1b1b24" d="M0 10h30v6H0z"/><path fill="#e10600" d="M4 16h6v24H4z"/> <path fill="#e1'
    '0600" d="M8 47 L11 36 L38 33 L72 26 L94 23 L99 14 L107 13 L111 25 L126 25 L138 30 L194 36 L222 4'
    '2 L232 48 L8 51 Z"/> <path fill="#fff" d="M44 38 L194 40.5 L194 43 L44 41 Z"/> <circle cx="121" '
    'cy="22" r="5.5" fill="#ffd400"/> <path fill="none" stroke="#1b1b24" stroke-width="3" stroke-line'
    'cap="round" d="M110 26 Q120 12 137 27"/> <path fill="#1b1b24" d="M18 49 H216 V53 H18 Z"/> <path '
    'fill="#1b1b24" d="M206 50 H244 V55 H206 Z"/><path fill="#e10600" d="M239 42 h5 v13 h-5z"/> <g tr'
    'ansform="translate(46 49)"><g class="spin"><circle r="15" fill="#111"/><circle r="7.5" fill="#9a'
    'a0a6"/><path d="M-7.5 0H7.5M0-7.5V7.5" stroke="#111" stroke-width="2.4"/></g></g> <g transform="'
    'translate(186 50)"><g class="spin"><circle r="13" fill="#111"/><circle r="6.5" fill="#9aa0a6"/><'
    'path d="M-6.5 0H6.5M0-6.5V6.5" stroke="#111" stroke-width="2.2"/></g></g>'
)


FONT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts")


def font_css():
    """Titillium Web as inline @font-face rules, so the font loads inside an <img> SVG."""
    rules = []
    for weight, name in ((400, "Regular"), (600, "SemiBold"), (700, "Bold")):
        with open(os.path.join(FONT_DIR, f"TitilliumWeb-{name}.woff2"), "rb") as f:
            data = base64.b64encode(f.read()).decode()
        rules.append(f'@font-face{{font-family:"Titillium Web";font-weight:{weight};'
                     f'src:url(data:font/woff2;base64,{data}) format("woff2")}}')
    return "".join(rules)


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
    lane_y = TOP + 7 * PITCH + 6
    height = TOP + 7 * PITCH + 70

    cells, months, last_month = [], [], None
    best_xy = None
    for d, v, lvl in days:
        week = (d - start).days // 7
        dow = (d.weekday() + 1) % 7
        x, y = LEFT + week * PITCH, TOP + dow * PITCH
        if (d, v) == (best[0], best[1]):
            best_xy = (x, y)
        delay = week * 0.035 + dow * 0.012
        pulse = (f";animation:pop .5s cubic-bezier(.3,1.6,.5,1) {delay:.2f}s both,"
                 f"glow 6s ease-in-out {2.4 + week * 0.06:.2f}s infinite") if lvl else ""
        cells.append(f'<rect class="cell l{lvl}" x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="3" '
                     f'style="animation-delay:{delay:.2f}s{pulse}"><title>{v} on {d:%d %b %Y}</title></rect>')
        if dow == 0 and d.month != last_month:
            last_month = d.month
            months.append(f'<text class="m" x="{x}" y="{TOP - 10}">{d:%b}</text>')

    for i, label in ((1, "Mon"), (3, "Wed"), (5, "Fri")):
        months.append(f'<text class="m" x="{LEFT - 8}" y="{TOP + i * PITCH + 11}" text-anchor="end">{label}</text>')

    legend_x = width - 56 - 5 * PITCH
    legend = "".join(f'<rect class="l{i} lg" x="{legend_x + i * PITCH}" y="{height - 30}" width="{CELL}" '
                     f'height="{CELL}" rx="3"/>' for i in range(5))
    stats = f"{active} active days  ·  Longest streak {longest} days  ·  Current streak {current} days"

    # Fastest lap: the busiest day, outlined in purple with a tag above the grid.
    fastest = ""
    if best_xy and best[1]:
        bx, by = best_xy
        tag_x = min(max(bx - 60, LEFT), width - 190)
        fastest = (f'<rect class="fl" x="{bx - 2}" y="{by - 2}" width="{CELL + 4}" height="{CELL + 4}" rx="4"/>'
                   f'<line class="fll" x1="{bx + CELL / 2}" x2="{bx + CELL / 2}" y1="{TOP - 20}" y2="{by - 2}"/>'
                   f'<rect x="{tag_x}" y="{TOP - 40}" width="170" height="20" rx="4" fill="#a855f7"/>'
                   f'<text class="flt" x="{tag_x + 10}" y="{TOP - 26}">FASTEST LAP · {best[1]} on {best[0]:%d %b}</text>')

    # Flag board: green while the streak is alive, virtual safety car when it is not.
    flag_txt, flag_col = ("GREEN FLAG", "#22c55e") if current else ("VSC DEPLOYED", "#eab308")
    board = (f'<rect class="fb" x="{width - 170}" y="14" width="150" height="26" rx="5" fill="{flag_col}"/>'
             f'<text class="fbt" x="{width - 95}" y="31" text-anchor="middle">{flag_txt}</text>')

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" role="img" aria-labelledby="t">
<title id="t">{total:,} contributions in the last year. {stats}.</title>
<style>
{font_css()}
text{{font-family:"Titillium Web",-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;fill:#59636e}}
.h{{font-size:22px;font-weight:700;fill:#1f2328}} .s{{font-size:13px}} .m{{font-size:11px}}
.l0{{fill:#ebedf0}} .l1{{fill:#9be9a8}} .l2{{fill:#40c463}} .l3{{fill:#30a14e}} .l4{{fill:#216e39}}
.cell{{transform-box:fill-box;transform-origin:center;animation:pop .5s ease-out both}}
.spin{{transform-box:fill-box;transform-origin:center;animation:sp .3s linear infinite}}
.car{{animation:lap {LAP}s linear 2.6s infinite both}}
.lane{{stroke:#d1d9e0;stroke-dasharray:6 6}}
.fl{{fill:none;stroke:#a855f7;stroke-width:2.5;animation:flp 1.6s ease-in-out infinite alternate}}
.fll{{stroke:#a855f7;stroke-width:1.5;stroke-dasharray:2 3}}
.flt{{font-size:10.5px;font-weight:700;fill:#fff;letter-spacing:.6px}}
.fbt{{font-size:11px;font-weight:700;fill:#111;letter-spacing:1.2px}}
.fb{{animation:fbp 2s ease-in-out infinite alternate}}
@keyframes flp{{from{{stroke-opacity:1}}to{{stroke-opacity:.25}}}}
@keyframes fbp{{from{{opacity:1}}to{{opacity:.75}}}}
@keyframes sp{{to{{transform:rotate(360deg)}}}}
@keyframes lap{{0%{{transform:translate({LEFT - 70}px,{lane_y}px)}}35%,100%{{transform:translate({width + 10}px,{lane_y}px)}}}}
@keyframes pop{{from{{opacity:0;transform:scale(.2)}}to{{opacity:1;transform:scale(1)}}}}
@keyframes glow{{0%,88%,100%{{filter:none}}94%{{filter:brightness(1.35) saturate(1.2)}}}}
@media (prefers-color-scheme:dark){{
text{{fill:#8b949e}} .h{{fill:#e6edf3}} .lane{{stroke:#30363d}}
.l0{{fill:#161b22}} .l1{{fill:#0e4429}} .l2{{fill:#006d32}} .l3{{fill:#26a641}} .l4{{fill:#39d353}}}}
@media (prefers-reduced-motion:reduce){{.cell,.car,.spin{{animation:none!important}}.car{{display:none}}}}
</style>
<text class="h" x="{LEFT}" y="30">{total:,} contributions in the last year</text>
<text class="s" x="{LEFT}" y="52">{stats}</text>
{"".join(months)}
{"".join(cells)}
{fastest}
{board}
<line class="lane" x1="{LEFT}" x2="{LEFT + n_weeks * PITCH - GAP}" y1="{lane_y + 18}" y2="{lane_y + 18}"/>
<g class="car"><g transform="scale(0.27)">{CAR}</g></g>
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
