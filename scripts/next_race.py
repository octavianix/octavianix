#!/usr/bin/env python3
"""Render a broadcast-style "next race" card from the Jolpica F1 API.

    python scripts/next_race.py --out assets/next-race.svg
"""
import argparse
import datetime as dt
import json
import urllib.request
from html import escape

API = "https://api.jolpi.ca/ergast/f1/current/next.json"
RED = "#e10600"


def fetch():
    req = urllib.request.Request(API, headers={"User-Agent": "octavianix-profile"})
    with urllib.request.urlopen(req, timeout=60) as r:
        races = json.load(r)["MRData"]["RaceTable"]["Races"]
    return races[0] if races else None


def when(session):
    return dt.datetime.fromisoformat(f'{session["date"]}T{session.get("time", "00:00:00Z").replace("Z", "+00:00")}')


def render(race, today):
    W, H = 1000, 130
    font = '-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif'
    mono = 'ui-monospace,SFMono-Regular,Menlo,Consolas,monospace'
    if race is None:
        title, place, count, sessions = "Season complete", "See you next year", "OFF-SEASON", ""
        label = "Off-season: no race scheduled"
    else:
        start = when(race)
        days = (start.date() - today).days
        count = "RACE WEEK" if days <= 0 else f"IN {days} DAY{'S' if days != 1 else ''}"
        title = race["raceName"]
        loc = race["Circuit"]["Location"]
        place = f'{race["Circuit"]["circuitName"]} · {loc["locality"]}, {loc["country"]}'
        parts = [("FP1", race.get("FirstPractice")), ("QUALI", race.get("Qualifying")), ("RACE", race)]
        sessions = "".join(
            f'<text x="{560 + i * 140}" y="104" class="m">{name}</text>'
            f'<text x="{560 + i * 140}" y="86" class="d">{when(s):%a %d %b}</text>'
            for i, (name, s) in enumerate(p for p in parts if p[1])
        )
        label = f'Next race: round {race["round"]}, {title}, {place}, {start:%d %B %Y}, {count.lower()}'
        title = f'R{race["round"]} · {title}'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{escape(label)}">
<defs><clipPath id="c"><rect width="{W}" height="{H}" rx="14"/></clipPath>
<pattern id="cf" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="4" height="8" fill="#fff" fill-opacity=".025"/></pattern></defs>
<style>
text{{font-family:{font}}} .m{{font-family:{mono};font-size:11px;letter-spacing:1.2px;fill:#8b8b96}}
.t{{font-size:24px;font-weight:700;fill:#f5f5f7}} .p{{font-size:13px;fill:#b9b9c3}} .d{{font-size:15px;font-weight:600;fill:#f5f5f7}}
.k{{font-family:{mono};font-size:12px;letter-spacing:1.4px;fill:#fff;font-weight:700}}
.dot{{animation:bl 1s ease-in-out infinite alternate}}@keyframes bl{{to{{opacity:.2}}}}
.in{{animation:in .7s cubic-bezier(.2,.8,.2,1) both}}@keyframes in{{from{{opacity:0;transform:translateX(-30px)}}}}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important}}}}
</style>
<g clip-path="url(#c)"><rect width="{W}" height="{H}" fill="#17171f"/><rect width="{W}" height="{H}" fill="url(#cf)"/>
<rect width="6" height="{H}" fill="{RED}"/>
<g class="in">
<text x="30" y="34" class="m" style="fill:{RED}">NEXT RACE</text>
<text x="30" y="72" class="t">{escape(title)}</text>
<text x="30" y="98" class="p">{escape(place)}</text>
{sessions}
<rect x="{W - 190}" y="20" width="166" height="28" rx="5" fill="{RED}"/><circle class="dot" cx="{W - 174}" cy="34" r="4" fill="#fff"/>
<text x="{W - 162}" y="39" class="k">{count}</text>
</g></g></svg>'''


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="assets/next-race.svg")
    a = ap.parse_args()
    race = fetch()
    with open(a.out, "w") as f:
        f.write(render(race, dt.datetime.now(dt.timezone.utc).date()))
    print(f"wrote {a.out}: {race['raceName'] if race else 'off-season'}")


if __name__ == "__main__":
    main()
