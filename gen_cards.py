"""
gen_cards.py — builds the animated SVG cards for the haitham72 profile README.

  assets/terminal-card.svg   ASCII portrait generated from assets/portrait.jpg
  assets/info-card.svg       neofetch-style info card (content from the CV)
  assets/contributions.svg   real contribution calendar (GitHub GraphQL), diagonal reveal
  assets/rag-pipeline.svg    animated retrieval pipeline diagram

Run:  pip install Pillow numpy  &&  python gen_cards.py
Contributions are fetched with `gh api graphql` (or GITHUB_TOKEN if gh is unavailable).
"""

import html, json, os, subprocess, urllib.request
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageOps

USER = "haitham72"
NAME = "Haitham Mohamed"
HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")
MONO = 'ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace'

BG_A, BG_B, LINE = "#111722", "#0d1117", "#30363d"
FG, GRAY = "#c9d1d9", "#7d8590"
ORANGE, BLUE, GREEN, CYAN = "#ffa657", "#58a6ff", "#3fb950", "#22d3ee"


def xe(s):
    return html.escape(str(s), quote=True)


def chrome(w, h, title, gid):
    return (
        f'<defs><linearGradient id="{gid}" x1="0" y1="0" x2="0" y2="1">'
        f'<stop offset="0" stop-color="{BG_A}"/><stop offset="1" stop-color="{BG_B}"/></linearGradient></defs>'
        f'<rect width="{w}" height="{h}" rx="12" fill="url(#{gid})"/>'
        f'<rect x=".5" y=".5" width="{w-1}" height="{h-1}" rx="12" fill="none" stroke="{LINE}"/>'
        f'<line x1="0" y1="30" x2="{w}" y2="30" stroke="{LINE}"/>'
        f'<circle cx="20" cy="15" r="5" fill="#ff5f56"/><circle cx="36" cy="15" r="5" fill="#ffbd2e"/>'
        f'<circle cx="52" cy="15" r="5" fill="#27c93f"/>'
        f'<text x="{w/2:.1f}" y="19" fill="{GRAY}" font-size="12" text-anchor="middle">{xe(title)}</text>'
    )


def write(name, svg):
    path = os.path.join(ASSETS, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"[ok] {name:22s} {os.path.getsize(path)//1024} KB")


# ── 1. ASCII portrait ────────────────────────────────────────────────────────
def ascii_rows(cols=96):
    im = Image.open(os.path.join(ASSETS, "portrait.jpg")).convert("L")
    w, h = im.size
    # Soft mask (head ellipse + shoulders) blanks the blurred office background.
    # Coordinates are for the 1086x1448 source photo; scale if the photo changes.
    sx, sy = w / 1086, h / 1448
    mask = Image.new("L", (w, h), 0)
    d = ImageDraw.Draw(mask)
    d.ellipse((280 * sx, 135 * sy, 790 * sx, 900 * sy), fill=255)
    d.polygon([(360 * sx, 800 * sy), (740 * sx, 800 * sy), (w, 980 * sy), (w, h), (0, h), (0, 1020 * sy)], fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(18))
    box = (int(110 * sx), int(110 * sy), int(976 * sx), int(1120 * sy))
    im, mask = im.crop(box), mask.crop(box)
    im = ImageOps.equalize(im, mask=mask).filter(ImageFilter.UnsharpMask(radius=4, percent=160, threshold=2))
    a = np.asarray(im, float) / 255 * np.asarray(mask, float) / 255
    rows_n = round(cols * (box[3] - box[1]) / (box[2] - box[0]) * 0.5)  # glyph cell ≈ 1:2
    g = np.asarray(Image.fromarray((a * 255).astype("uint8")).resize((cols, rows_n), Image.LANCZOS), float) / 255
    g = np.clip((g - 0.22) / 0.75, 0, 1) ** 1.1
    ramp = " .'`-:;=+*csS%#@"
    return ["".join(ramp[min(int(v * len(ramp)), len(ramp) - 1)] for v in r) for r in g]


def terminal_card():
    rows = ascii_rows()
    W, ROW_H, Y0, TX = 840, 15, 40, 20
    TW, DUR = 800, 0.08
    foot = Y0 + len(rows) * ROW_H + 6
    H = foot + 43
    body = []
    for i, r in enumerate(rows):
        t, y = i * DUR, Y0 + i * ROW_H
        body.append(
            f'<clipPath id="r{i}"><rect x="{TX}" y="{y}" height="{ROW_H}" width="0">'
            f'<animate attributeName="width" from="0" to="{TW}" begin="{t:.2f}s" dur="{DUR}s" fill="freeze"/></rect></clipPath>'
            f'<text clip-path="url(#r{i})" xml:space="preserve" x="{TX}" y="{y+11.1:.1f}" fill="{FG}" '
            f'font-size="12.9" textLength="{TW}" lengthAdjust="spacing">{xe(r)}</text>'
        )
    prompt = f"{USER}@github:~$ whoami "
    cx = TX + len(prompt) * 7.8 + len(NAME) * 7.8 + 4
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family=\'{MONO}\'>'
        + chrome(W, H, f"{USER}@github: ~$ ./portrait.sh", "tbg")
        + "".join(body)
        + f'<line x1="0" y1="{foot}" x2="{W}" y2="{foot}" stroke="{LINE}"/>'
        f'<text x="{TX}" y="{foot+25}" fill="{GRAY}" font-size="13">{xe(prompt)}<tspan fill="{FG}">{xe(NAME)}</tspan></text>'
        f'<rect x="{cx:.0f}" y="{foot+12}" width="8" height="15" fill="{FG}">'
        f'<animate attributeName="opacity" values="1;1;0;0" keyTimes="0;.5;.51;1" dur="1s" repeatCount="indefinite"/></rect>'
        "</svg>"
    )
    write("terminal-card.svg", svg)
    return H


# ── 2. neofetch info card (every line traceable to the CV) ───────────────────
INFO = [
    ("header",),
    ("section", "— About"),
    ("field", "Role", "Applied AI Engineer / Architect"),
    ("field", "Focus", "GenAI · RAG · Agents · LLM Eval"),
    ("field", "Based", "Dubai, UAE"),
    ("field", "Exp", "15+ years shipping to stakeholders"),
    ("field", "Langs", "Arabic (native) · English"),
    ("section", "— Stack"),
    ("field", "LLMs", "Claude API · OpenAI API"),
    ("field", "Agents", "LangGraph · LangChain · MCP"),
    ("field", "Retrieval", "pgvector · hybrid search · RRF"),
    ("field", "Backend", "Python · FastAPI · Redis"),
    ("field", "Cloud", "Docker · AWS · Vercel"),
    ("section", "— Highlights"),
    ("bullet", "Production Arabic RAG, Dubai gov office"),
    ("bullet", "150+ query LLM evaluation harness"),
    ("bullet", "ReguLense live: version-aware health RAG"),
    ("bullet", "DBA in AI (Walsh College), in progress"),
]


def info_card(min_h):
    W = 480
    parts, t, y = [], 0.15, 62.0

    def row(inner, t):
        return (
            f'<g opacity="0" transform="translate(0,5)">{inner}'
            f'<animate attributeName="opacity" from="0" to="1" begin="{t:.2f}s" dur=".4s" fill="freeze"/>'
            f'<animateTransform attributeName="transform" type="translate" from="0 5" to="0 0" begin="{t:.2f}s" '
            f'dur=".4s" fill="freeze" calcMode="spline" keySplines=".2 .8 .2 1"/></g>'
        )

    for r in INFO:
        if r[0] == "header":
            x1 = 20 + (len(USER) + 8) * 8.4
            parts.append(row(
                f'<text x="20" y="{y}" font-size="14" font-weight="700"><tspan fill="{GREEN}">{USER}</tspan>'
                f'<tspan fill="{GRAY}">@</tspan><tspan fill="{CYAN}">github</tspan></text>'
                f'<line x1="{x1:.0f}" y1="{y-4}" x2="460" y2="{y-4}" stroke="{LINE}"/>', t))
            y += 26; t += 0.06
        elif r[0] == "section":
            x1 = 20 + len(r[1]) * 7.8 + 6
            parts.append(row(
                f'<text x="20" y="{y}" fill="{BLUE}" font-size="12.5" font-weight="700">{xe(r[1])}</text>'
                f'<line x1="{x1:.0f}" y1="{y-4}" x2="460" y2="{y-4}" stroke="{LINE}"/>', t))
            y += 26; t += 0.12
        elif r[0] == "field":
            parts.append(row(
                f'<text x="20" y="{y}" fill="{ORANGE}" font-size="12.5" font-weight="700">{xe(r[1])}</text>'
                f'<text x="112" y="{y}" fill="{FG}" font-size="12.5">{xe(r[2])}</text>', t))
            y += 21; t += 0.06
        else:
            parts.append(row(
                f'<circle cx="23" cy="{y-4}" r="2.5" fill="{GREEN}"/>'
                f'<text x="34" y="{y}" fill="{FG}" font-size="12.5">{xe(r[1])}</text>', t))
            y += 21; t += 0.06
    H = max(min_h, int(y) + 20)
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family=\'{MONO}\'>'
        + chrome(W, H, f"{USER}@github: ~$ neofetch", "ibg") + "".join(parts) + "</svg>"
    )
    write("info-card.svg", svg)


# ── 3. Real contribution calendar ────────────────────────────────────────────
QUERY = ('query{user(login:"%s"){contributionsCollection{contributionCalendar{totalContributions '
         "weeks{contributionDays{date contributionCount contributionLevel}}}}}}" % USER)


def fetch_calendar():
    try:
        out = subprocess.run(["gh", "api", "graphql", "-f", f"query={QUERY}"],
                             capture_output=True, text=True, check=True).stdout
    except (OSError, subprocess.CalledProcessError):
        req = urllib.request.Request(
            "https://api.github.com/graphql", data=json.dumps({"query": QUERY}).encode(),
            headers={"Authorization": f"bearer {os.environ['GITHUB_TOKEN']}", "User-Agent": USER})
        out = urllib.request.urlopen(req, timeout=30).read().decode()
    return json.loads(out)["data"]["user"]["contributionsCollection"]["contributionCalendar"]


def contributions():
    cal = fetch_calendar()
    LV = {"NONE": 0, "FIRST_QUARTILE": 1, "SECOND_QUARTILE": 2, "THIRD_QUARTILE": 3, "FOURTH_QUARTILE": 4}
    COL = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]
    GLOW = ["#21262d", "#3dffa0", "#57ffb0", "#8dffcc", "#c8ffe8"]
    W, H, SQ, STEP, GX, GY = 850, 175, 11, 14, 40, 30
    weeks = cal["weeks"]
    reveal, hold = 4.5, 3.0
    total = reveal + hold
    maxd = (len(weeks) - 1) + 6 * 0.6
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
        f'font-family="-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif">',
        '<defs><filter id="gl" x="-70%" y="-70%" width="240%" height="240%"><feGaussianBlur stdDeviation="2" result="b"/>'
        '<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>',
        f'<rect width="{W}" height="{H}" rx="16" fill="{BG_B}" stroke="{LINE}"/>',
    ]
    last_month = None
    for c, wk in enumerate(weeks):
        m = wk["contributionDays"][0]["date"][5:7]
        if m != last_month and c < len(weeks) - 2:
            label = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"][int(m) - 1]
            out.append(f'<text x="{GX + c*STEP}" y="20" fill="#8b949e" font-size="10">{label}</text>')
            last_month = m
    for i, lbl in ((1, "Mon"), (3, "Wed"), (5, "Fri")):
        out.append(f'<text x="8" y="{GY + i*STEP + SQ - 1}" fill="#8b949e" font-size="9">{lbl}</text>')
    for c, wk in enumerate(weeks):
        for day in wk["contributionDays"]:
            r = int(np.datetime64(day["date"]).astype("datetime64[D]").view("int64") + 4) % 7  # 0 = Sunday
            lv = LV[day["contributionLevel"]]
            x, y = GX + c * STEP, GY + r * STEP
            t0 = (c + r * 0.6) / maxd * reveal / total
            t1, t2 = min(t0 + 0.012, 0.97), min(t0 + 0.05, 0.99)
            fil = ' filter="url(#gl)"' if lv >= 3 else ""
            tip = f'<title>{day["contributionCount"]} on {day["date"]}</title>'
            anim = (f'<animate attributeName="opacity" values="0;0;1;1" keyTimes="0;{t0:.4f};{t1:.4f};1" '
                    f'dur="{total}s" repeatCount="indefinite"/>')
            if lv:
                anim += (f'<animate attributeName="fill" values="{COL[lv]};{COL[lv]};{GLOW[lv]};{COL[lv]}" '
                         f'keyTimes="0;{t0:.4f};{t1:.4f};{t2:.4f}" dur="{total}s" repeatCount="indefinite"/>')
            out.append(f'<rect x="{x}" y="{y}" width="{SQ}" height="{SQ}" rx="2" fill="{COL[lv]}" opacity="0"{fil}>{tip}{anim}</rect>')
    ly = GY + 7 * STEP + 18
    out.append(f'<text x="{GX}" y="{ly}" fill="#8b949e" font-size="11">'
               f'{cal["totalContributions"]} contributions in the last year</text>')
    lx = W - 150
    out.append(f'<text x="{lx}" y="{ly}" fill="#8b949e" font-size="10">Less</text>')
    for i, col in enumerate(COL):
        out.append(f'<rect x="{lx + 28 + i*14}" y="{ly-9}" width="10" height="10" rx="2" fill="{col}"/>')
    out.append(f'<text x="{lx + 28 + 5*14 + 4}" y="{ly}" fill="#8b949e" font-size="10">More</text>')
    out.append("</svg>")
    write("contributions.svg", "".join(out))


# ── 4. Animated retrieval pipeline (Hamdan / ReguLense pattern from the CV) ──
def pipeline():
    W, H = 520, 420
    stages = [
        ("Query", "Arabic / English", FG),
        ("Hybrid retrieval", "semantic · lexical · entity", BLUE),
        ("RRF fusion", "reciprocal rank fusion", CYAN),
        ("Rerank", "multi-stage", ORANGE),
        ("Validator gate", "eval · regression check", GREEN),
        ("Cited answer", "abstains below confidence floor", FG),
    ]
    bx, bw, bh, gap, y0 = 120, 280, 44, 18, 44
    parts = []
    for i, (title, sub, col) in enumerate(stages):
        y = y0 + i * (bh + gap)
        t = 0.2 + i * 0.25
        parts.append(
            f'<g opacity="0"><rect x="{bx}" y="{y}" width="{bw}" height="{bh}" rx="10" fill="#161b22" stroke="{col}" stroke-opacity=".55"/>'
            f'<text x="{bx+16}" y="{y+19}" fill="{col}" font-size="13" font-weight="700">{xe(title)}</text>'
            f'<text x="{bx+16}" y="{y+35}" fill="{GRAY}" font-size="11">{xe(sub)}</text>'
            f'<animate attributeName="opacity" from="0" to="1" begin="{t:.2f}s" dur=".4s" fill="freeze"/></g>'
        )
        if i < len(stages) - 1:
            ya, yb = y + bh, y + bh + gap
            parts.append(f'<line x1="{W/2}" y1="{ya}" x2="{W/2}" y2="{yb}" stroke="{LINE}" stroke-width="2"/>')
    # a token travelling down the pipeline, drawn first so it shows only between the opaque boxes
    top, bot = y0 + bh / 2, y0 + (len(stages) - 1) * (bh + gap) + bh / 2
    parts.insert(0,
        f'<circle cx="{W/2}" cy="{top}" r="4" fill="{GREEN}" opacity="0">'
        f'<animate attributeName="cy" values="{top};{bot}" begin="2s" dur="3.2s" repeatCount="indefinite"/>'
        f'<animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.08;.9;1" begin="2s" dur="3.2s" repeatCount="indefinite"/></circle>'
    )
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family=\'{MONO}\'>'
        + chrome(W, H, "rag_pipeline.py --trace", "pbg") + "".join(parts) + "</svg>"
    )
    write("rag-pipeline.svg", svg)


if __name__ == "__main__":
    h = terminal_card()
    info_card(min_h=0)
    contributions()
    pipeline()
