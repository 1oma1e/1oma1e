"""Generate the SVG assets (header + project cards, dark and light) for the profile README.

Run: python build_assets.py   ->  writes into ./assets
"""

from html import escape
from pathlib import Path

OUT = Path(__file__).parent / "assets"
OUT.mkdir(exist_ok=True)

FONT = "'Segoe UI', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, 'Cascadia Code', SFMono-Regular, Menlo, Consolas, monospace"

THEMES = {
    "dark": {
        "bg": "#0d1117",
        "card": "#161b22",
        "border": "#30363d",
        "text": "#e6edf3",
        "muted": "#8b949e",
        "chip": "#21262d",
        "term": "#010409",
    },
    "light": {
        "bg": "#ffffff",
        "card": "#ffffff",
        "border": "#d0d7de",
        "text": "#1f2328",
        "muted": "#59636e",
        "chip": "#f6f8fa",
        "term": "#f6f8fa",
    },
}

STATUS = {
    "live": ("Live", "#2da44e"),
    "released": ("v1.0 released", "#6366f1"),
    "wip": ("In progress", "#d29922"),
    "private": ("Private", "#8b949e"),
    "selfhosted": ("Self-hosted", "#0ea5e9"),
}


def write(name: str, svg: str) -> None:
    (OUT / name).write_text(svg.strip() + "\n", encoding="utf-8")


# --------------------------------------------------------------------------- header


def header(theme: str) -> str:
    t = THEMES[theme]
    w, h = 1200, 360
    orb_opacity = "0.55" if theme == "dark" else "0.35"
    term_lines = [
        ("$", "whoami", t["text"]),
        ("", "cs student · france · builder", t["muted"]),
        ("$", "cat principles.txt", t["text"]),
        ("", "free · local-first · no telemetry", "#a5b4fc" if theme == "dark" else "#4f46e5"),
        ("", "docs → mockup → code → tests", "#a5b4fc" if theme == "dark" else "#4f46e5"),
        ("$", "ls ~/projects | wc -l", t["text"]),
        ("", "10", t["muted"]),
    ]
    rows = []
    for i, (prompt, txt, color) in enumerate(term_lines):
        y = 150 + i * 26
        delay = 0.4 + i * 0.35
        p = f'<tspan fill="#22c55e">{prompt} </tspan>' if prompt else ""
        rows.append(
            f'<text class="ln" style="animation-delay:{delay:.2f}s" x="760" y="{y}" '
            f'font-family="{MONO}" font-size="15" fill="{color}">{p}{escape(txt)}</text>'
        )
    cursor_y = 150 + len(term_lines) * 26
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="1oma1e — I build honest software">
  <defs>
    <linearGradient id="title" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#6366f1"/>
      <stop offset="0.5" stop-color="#0ea5e9"/>
      <stop offset="1" stop-color="#c026d3"/>
    </linearGradient>
    <filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="60"/></filter>
    <clipPath id="frame"><rect width="{w}" height="{h}" rx="20"/></clipPath>
    <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse">
      <path d="M32 0H0V32" fill="none" stroke="{t['border']}" stroke-width="1" opacity="0.45"/>
    </pattern>
    <style>
      .orb {{ animation: drift 18s ease-in-out infinite alternate; transform-box: fill-box; transform-origin: center; }}
      .o2 {{ animation-duration: 22s; animation-direction: alternate-reverse; }}
      .o3 {{ animation-duration: 26s; }}
      @keyframes drift {{ 0% {{ transform: translate(0,0) scale(1); }} 100% {{ transform: translate(60px,-30px) scale(1.15); }} }}
      .ln {{ opacity: 0; animation: show .01s forwards; }}
      @keyframes show {{ to {{ opacity: 1; }} }}
      .fade {{ opacity: 0; animation: up .9s cubic-bezier(.2,.7,.2,1) forwards; }}
      @keyframes up {{ from {{ opacity: 0; transform: translateY(12px); }} to {{ opacity: 1; transform: none; }} }}
      .cur {{ animation: blink 1s steps(1) infinite; animation-delay: 3s; opacity: 0; }}
      @keyframes blink {{ 0% {{ opacity: 1; }} 50% {{ opacity: 0; }} }}
      @media (prefers-reduced-motion: reduce) {{ .orb, .cur {{ animation: none; }} .ln, .fade {{ animation: none; opacity: 1; }} }}
    </style>
  </defs>
  <g clip-path="url(#frame)">
    <rect width="{w}" height="{h}" fill="{t['bg']}"/>
    <rect width="{w}" height="{h}" fill="url(#grid)"/>
    <g filter="url(#blur)" opacity="{orb_opacity}">
      <circle class="orb" cx="180" cy="60" r="150" fill="#6366f1"/>
      <circle class="orb o2" cx="620" cy="330" r="140" fill="#0ea5e9"/>
      <circle class="orb o3" cx="1080" cy="40" r="160" fill="#c026d3"/>
    </g>
    <rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="20" fill="none" stroke="{t['border']}"/>
  </g>

  <g class="fade">
    <text x="64" y="104" font-family="{MONO}" font-size="16" fill="{t['muted']}">// hi there, I'm</text>
    <text x="60" y="186" font-family="{FONT}" font-size="88" font-weight="800" letter-spacing="-3" fill="url(#title)">1oma1e</text>
  </g>
  <g class="fade" style="animation-delay:.25s">
    <text x="64" y="236" font-family="{FONT}" font-size="24" font-weight="600" fill="{t['text']}">I build honest software.</text>
    <text x="64" y="270" font-family="{FONT}" font-size="17" fill="{t['muted']}">Desktop apps that show what they do, real-time web games,</text>
    <text x="64" y="294" font-family="{FONT}" font-size="17" fill="{t['muted']}">and a self-hosted homelab that runs it all.</text>
  </g>

  <g class="fade" style="animation-delay:.15s">
    <rect x="730" y="70" width="410" height="250" rx="14" fill="{t['term']}" fill-opacity="0.85" stroke="{t['border']}"/>
    <circle cx="756" cy="96" r="6" fill="#ff5f57"/>
    <circle cx="776" cy="96" r="6" fill="#febc2e"/>
    <circle cx="796" cy="96" r="6" fill="#28c840"/>
    <text x="935" y="101" text-anchor="middle" font-family="{MONO}" font-size="12" fill="{t['muted']}">~/1oma1e</text>
    <line x1="730" y1="116" x2="1140" y2="116" stroke="{t['border']}"/>
    {''.join(rows)}
    <rect class="cur" x="760" y="{cursor_y - 14}" width="9" height="18" fill="#22c55e"/>
  </g>
</svg>"""


# --------------------------------------------------------------------------- cards

PROJECTS = [
    {
        "slug": "safesweep",
        "name": "SafeSweep",
        "accent": ("#10b981", "#059669"),
        "glyph": "S",
        "status": "private",
        "kind": "Windows desktop app",
        "lines": [
            "Shows what fills your disk and what you can",
            "delete without breaking your PC. Locked safe",
            "zones, explained files, a 7-day undo bin.",
        ],
        "stack": ["Rust", "Tauri 2", "React", "TypeScript"],
    },
    {
        "slug": "hyphn",
        "name": "Hyphn",
        "accent": ("#0ea5e9", "#2563eb"),
        "glyph": "H",
        "status": "wip",
        "kind": "iPhone ↔ Windows companion",
        "lines": [
            "Turns an iPhone into a 4K60 HEVC webcam",
            "and OBS source, plus resumable file drop.",
            "Paired by QR code, 100% local, no cloud.",
        ],
        "stack": ["Rust", "Tauri", "SwiftUI", "TLS"],
    },
    {
        "slug": "tchinz",
        "name": "Tchinz",
        "accent": ("#d946ef", "#9333ea"),
        "glyph": "T",
        "status": "live",
        "kind": "Real-time party games",
        "lines": [
            "Host a room, share a 4-letter code, play",
            "with 2 to 30 friends in real time. Four",
            "languages, light and dark, tested at scale.",
        ],
        "stack": ["Next.js", "Colyseus", "TypeScript", "Turborepo"],
    },
    {
        "slug": "tchop",
        "name": "tchop",
        "accent": ("#f43f5e", "#e11d48"),
        "glyph": "t",
        "status": "live",
        "kind": "Media downloader",
        "lines": [
            "Paste a TikTok or YouTube link, get an MP4",
            "up to 4K or a tagged 320 kbps MP3. Async",
            "job queue, rate limits, non-root container.",
        ],
        "stack": ["FastAPI", "yt-dlp", "ffmpeg", "Docker"],
    },
    {
        "slug": "apphome",
        "name": "AppHome Nexus",
        "accent": ("#f59e0b", "#ea580c"),
        "glyph": "A",
        "status": "selfhosted",
        "kind": "Smart home dashboard",
        "lines": [
            "A friendly layer over Home Assistant: solar,",
            "cameras, network, gate and robot vacuum,",
            "with a Simple mode and an Expert mode.",
        ],
        "stack": ["Svelte 5", "Fastify", "Zod", "WireGuard"],
    },
    {
        "slug": "powkey",
        "name": "Powkey",
        "accent": ("#5865f2", "#7c3aed"),
        "glyph": "P",
        "status": "selfhosted",
        "kind": "Discord bot",
        "lines": [
            "Music with autoplay and lyrics, voice blind",
            "tests, XP levels with image profile cards,",
            "anonymous confessions and an AI companion.",
        ],
        "stack": ["Node.js", "discord.js", "SQLite", "Groq"],
    },
    {
        "slug": "stormisland",
        "name": "Storm Island",
        "accent": ("#14b8a6", "#0891b2"),
        "glyph": "SI",
        "status": "wip",
        "kind": "Roblox co-op survival game",
        "lines": [
            "Build a base, craft tools, survive hunger,",
            "thirst and natural disasters with up to four",
            "players. Server-authoritative, strict types.",
        ],
        "stack": ["Luau", "Rojo", "Blender", "Selene"],
    },
    {
        "slug": "spotifymigrate",
        "name": "Spotify Migrator",
        "accent": ("#1db954", "#15803d"),
        "glyph": "♪",
        "status": "private",
        "kind": "Python CLI",
        "lines": [
            "Moves a whole Spotify account to another,",
            "in order and without duplicates. Idempotent,",
            "resumable, handles rate limits gracefully.",
        ],
        "stack": ["Python", "Spotify API", "Ruff", "CI"],
    },
]


def chip_row(stack: list[str], t: dict, x0: int, y: int) -> str:
    out, x = [], x0
    for s in stack:
        wdt = int(len(s) * 7.6 + 22)
        out.append(
            f'<rect x="{x}" y="{y}" width="{wdt}" height="26" rx="13" fill="{t["chip"]}" stroke="{t["border"]}"/>'
            f'<text x="{x + wdt / 2}" y="{y + 17.5}" text-anchor="middle" font-family="{MONO}" '
            f'font-size="12.5" fill="{t["muted"]}">{escape(s)}</text>'
        )
        x += wdt + 8
    return "".join(out)


def card(p: dict, theme: str) -> str:
    t = THEMES[theme]
    w, h = 600, 250
    a1, a2 = p["accent"]
    label, scolor = STATUS[p["status"]]
    pill_w = int(len(label) * 7.4 + 38)
    pulse = (
        f'<circle cx="{w - 28 - pill_w + 16}" cy="38" r="4" fill="{scolor}">'
        '<animate attributeName="opacity" values="1;.3;1" dur="2s" repeatCount="indefinite"/></circle>'
        if p["status"] == "live"
        else f'<circle cx="{w - 28 - pill_w + 16}" cy="38" r="4" fill="{scolor}"/>'
    )
    glyph_size = 26 if len(p["glyph"]) == 1 else 20
    desc = "".join(
        f'<text x="28" y="{124 + i * 24}" font-family="{FONT}" font-size="16" fill="{t["muted"]}">{escape(line)}</text>'
        for i, line in enumerate(p["lines"])
    )
    gid = f"g-{p['slug']}-{theme}"
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(p['name'])}: {escape(' '.join(p['lines']))}">
  <defs>
    <linearGradient id="{gid}" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{a1}"/><stop offset="1" stop-color="{a2}"/>
    </linearGradient>
    <radialGradient id="{gid}-glow" cx="1" cy="0" r="0.9">
      <stop offset="0" stop-color="{a1}" stop-opacity="{'0.22' if theme == 'dark' else '0.12'}"/>
      <stop offset="1" stop-color="{a1}" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="16" fill="{t['card']}" stroke="{t['border']}"/>
  <rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="16" fill="url(#{gid}-glow)"/>
  <rect x="28" y="24" width="52" height="52" rx="14" fill="url(#{gid})"/>
  <text x="54" y="{50 + glyph_size * 0.36:.1f}" text-anchor="middle" font-family="{FONT}" font-size="{glyph_size}" font-weight="800" fill="#ffffff">{escape(p['glyph'])}</text>
  <text x="96" y="47" font-family="{FONT}" font-size="22" font-weight="700" fill="{t['text']}">{escape(p['name'])}</text>
  <text x="96" y="70" font-family="{FONT}" font-size="14" fill="{a1}">{escape(p['kind'])}</text>
  <rect x="{w - 28 - pill_w}" y="25" width="{pill_w}" height="26" rx="13" fill="{scolor}" fill-opacity="0.12" stroke="{scolor}" stroke-opacity="0.45"/>
  {pulse}
  <text x="{w - 28 - pill_w + 28}" y="42.5" font-family="{FONT}" font-size="13" font-weight="600" fill="{scolor}">{label}</text>
  {desc}
  {chip_row(p['stack'], t, 28, 198)}
</svg>"""


# --------------------------------------------------------------------------- featured (Drivn)


def featured(theme: str) -> str:
    t = THEMES[theme]
    w, h = 1200, 300
    facts = [
        ("6", "official sources only"),
        ("1", "admin prompt per pass"),
        ("0", "ads, accounts or telemetry"),
    ]
    fx = []
    for i, (n, label) in enumerate(facts):
        x = 64 + i * 230
        fx.append(
            f'<text x="{x}" y="236" font-family="{FONT}" font-size="40" font-weight="800" fill="url(#dv-{theme})">{n}</text>'
            f'<text x="{x}" y="262" font-family="{FONT}" font-size="14" fill="{t["muted"]}">{label}</text>'
        )
    checks = [
        "Exact hardware-ID match, never a downgrade",
        "SHA-256 + signature checked on every package",
        "Restore point, driver backup, 1-click rollback",
        "Unprivileged UI, separate elevated installer",
    ]
    cx = []
    for i, c in enumerate(checks):
        y = 104 + i * 42
        cx.append(
            f'<circle cx="790" cy="{y - 5}" r="11" fill="#6366f1" fill-opacity="0.15"/>'
            f'<path d="M784.5 {y - 5} l3.8 3.8 l6.5 -7" fill="none" stroke="#818cf8" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<text x="812" y="{y}" font-family="{FONT}" font-size="16" fill="{t["text"]}">{escape(c)}</text>'
        )
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="Drivn: your drivers and apps, up to date, from official sources only.">
  <defs>
    <linearGradient id="dv-{theme}" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#6366f1"/><stop offset="0.55" stop-color="#0ea5e9"/><stop offset="1" stop-color="#c026d3"/>
    </linearGradient>
    <radialGradient id="dvg-{theme}" cx="0" cy="0" r="1">
      <stop offset="0" stop-color="#6366f1" stop-opacity="{'0.25' if theme == 'dark' else '0.12'}"/>
      <stop offset="1" stop-color="#6366f1" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="20" fill="{t['card']}" stroke="{t['border']}"/>
  <rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="20" fill="url(#dvg-{theme})"/>
  <rect x="0.5" y="0.5" width="{w - 1}" height="4" rx="2" fill="url(#dv-{theme})"/>
  <text x="64" y="64" font-family="{MONO}" font-size="13" letter-spacing="2" fill="#818cf8">FEATURED · WINDOWS 11 · v1.0.0</text>
  <text x="62" y="118" font-family="{FONT}" font-size="52" font-weight="800" letter-spacing="-1.5" fill="{t['text']}">Drivn</text>
  <text x="64" y="152" font-family="{FONT}" font-size="19" fill="{t['muted']}">Your drivers and apps, up to date.</text>
  <text x="64" y="177" font-family="{FONT}" font-size="19" fill="{t['muted']}">From official sources only.</text>
  {''.join(fx)}
  <line x1="740" y1="56" x2="740" y2="250" stroke="{t['border']}"/>
  {''.join(cx)}
  <text x="770" y="268" font-family="{MONO}" font-size="13" fill="{t['muted']}">Rust · Tauri · JavaScript · NSIS</text>
</svg>"""


def main() -> None:
    for theme in THEMES:
        write(f"header-{theme}.svg", header(theme))
        write(f"drivn-{theme}.svg", featured(theme))
        for p in PROJECTS:
            write(f"{p['slug']}-{theme}.svg", card(p, theme))
    print(f"wrote {len(list(OUT.glob('*.svg')))} files to {OUT}")


if __name__ == "__main__":
    main()
