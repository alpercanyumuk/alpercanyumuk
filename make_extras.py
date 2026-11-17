"""Render the pixel stat strip and the vim statusline (light and dark SVG)."""
import random
import sys
from pathlib import Path

DIGITS = {
    "0": [".XXX.", "X...X", "X...X", "X...X", "X...X", "X...X", ".XXX."],
    "2": [".XXX.", "X...X", "....X", "...X.", "..X..", ".X...", "XXXXX"],
    "4": ["...X.", "..XX.", ".X.X.", "X..X.", "XXXXX", "...X.", "...X."],
    "5": ["XXXXX", "X....", "XXXX.", "....X", "....X", "X...X", ".XXX."],
    "6": ["..XX.", ".X...", "X....", "XXXX.", "X...X", "X...X", ".XXX."],
    "%": ["XX..X", "XX..X", "...X.", "..X..", ".X...", "X..XX", "X..XX"],
    "-": [".....", ".....", ".....", "XXXXX", ".....", ".....", "....."],
}
STATS = [
    ("600", "Windows VMs under the monolith"),
    ("22", "production AKS clusters"),
    ("40%", "lower compute cost, so far"),
    ("65", "PRs a week with Claude Code"),
]
WIDTH = 720
ROWS = 7
TILE_COLS = 17
CELL, GAP = 7, 2
PITCH = CELL + GAP
FONT_UI = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"
FONT_MONO = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace"

THEMES = {
    "light": {
        "empty": "#ebedf0", "levels": ["#9be9a8", "#40c463", "#30a14e", "#216e39"], "text": "#57606a",
        "bar": "#f6f8fa", "bar_text": "#24292f", "mode_bg": "#216e39", "mode_text": "#ffffff",
        "seg": "#d0d7de", "cmd": "#24292f", "accent": "#1a7f37", "cursor": "#24292f",
    },
    "dark": {
        "empty": "#161b22", "levels": ["#0e4429", "#006d32", "#26a641", "#39d353"], "text": "#8b949e",
        "bar": "#161b22", "bar_text": "#c9d1d9", "mode_bg": "#39d353", "mode_text": "#0d1117",
        "seg": "#30363d", "cmd": "#c9d1d9", "accent": "#39d353", "cursor": "#c9d1d9",
    },
}


def glyph_columns(text):
    cols = []
    for i, ch in enumerate(text):
        g = DIGITS[ch]
        for c in range(5):
            cols.append([g[r][c] == "X" for r in range(ROWS)])
        if i < len(text) - 1:
            cols.append([False] * ROWS)
    return cols


def stats(theme):
    t = THEMES[theme]
    rng = random.Random(7)
    tile_w = WIDTH / len(STATS)
    grid_w = TILE_COLS * PITCH - GAP
    grid_h = ROWS * PITCH - GAP
    height = grid_h + 32
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {height}" width="{WIDTH}" height="{height}" role="img" '
        f'aria-label="{"; ".join(n + " " + label for n, label in STATS)}">',
        "<style>"
        ".on{animation:on .5s ease-out both}"
        "@keyframes on{from{opacity:0}to{opacity:1}}"
        "@media (prefers-reduced-motion:reduce){.on{animation:none}}"
        f"text{{font:12px {FONT_UI};fill:{t['text']};text-anchor:middle}}"
        "</style>",
    ]
    for i, (number, label) in enumerate(STATS):
        x0 = i * tile_w + (tile_w - grid_w) / 2
        cols = glyph_columns(number)
        offset = (TILE_COLS - len(cols)) // 2
        lit = {(c + offset, r) for c, col in enumerate(cols) for r, on in enumerate(col) if on}
        for c in range(TILE_COLS):
            for r in range(ROWS):
                x, y = x0 + c * PITCH, r * PITCH
                if (c, r) in lit:
                    level = rng.choices([2, 3], weights=[3, 4])[0]
                    delay = 0.2 + i * 0.25 + c * 0.02
                    out.append(f'<rect x="{x:.1f}" y="{y}" width="{CELL}" height="{CELL}" rx="1.5" fill="{t["empty"]}"/>')
                    out.append(
                        f'<rect class="on" style="animation-delay:{delay:.2f}s" x="{x:.1f}" y="{y}" '
                        f'width="{CELL}" height="{CELL}" rx="1.5" fill="{t["levels"][level]}"/>'
                    )
                else:
                    out.append(f'<rect x="{x:.1f}" y="{y}" width="{CELL}" height="{CELL}" rx="1.5" fill="{t["empty"]}"/>')
        out.append(f'<text x="{i * tile_w + tile_w / 2:.1f}" y="{grid_h + 22}">{label}</text>')
    out.append("</svg>")
    return "\n".join(out) + "\n"


def statusline(theme):
    t = THEMES[theme]
    bar_h, cmd_h = 24, 26
    height = bar_h + cmd_h
    mode_w = 74
    return "\n".join([
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {height}" width="{WIDTH}" height="{height}" role="img" '
        'aria-label="vim status line: type :help at yumuk.me">',
        "<style>"
        f"text{{font:12px {FONT_MONO}}}"
        ".cur{animation:blink 1.1s steps(1) infinite}"
        "@keyframes blink{50%{opacity:0}}"
        "@media (prefers-reduced-motion:reduce){.cur{animation:none}}"
        "</style>",
        f'<rect width="{WIDTH}" height="{bar_h}" fill="{t["bar"]}"/>',
        f'<rect width="{mode_w}" height="{bar_h}" fill="{t["mode_bg"]}"/>',
        f'<text x="{mode_w / 2}" y="16" text-anchor="middle" font-weight="700" fill="{t["mode_text"]}">NORMAL</text>',
        f'<text x="{mode_w + 12}" y="16" fill="{t["bar_text"]}">alper.md</text>',
        f'<rect x="{WIDTH - 196}" width="1" height="{bar_h}" fill="{t["seg"]}"/>',
        f'<text x="{WIDTH - 12}" y="16" text-anchor="end" fill="{t["bar_text"]}">utf-8 | markdown | 100%</text>',
        f'<text x="12" y="{bar_h + 17}" fill="{t["cmd"]}">:help</text>',
        f'<rect class="cur" x="49" y="{bar_h + 6}" width="7" height="14" fill="{t["cursor"]}"/>',
        f'<text x="{WIDTH - 12}" y="{bar_h + 17}" text-anchor="end" fill="{t["accent"]}">the full buffer is at yumuk.me</text>',
        "</svg>",
    ]) + "\n"


if __name__ == "__main__":
    dest = Path(sys.argv[1])
    for theme in THEMES:
        (dest / f"stats-{theme}.svg").write_text(stats(theme))
        (dest / f"statusline-{theme}.svg").write_text(statusline(theme))
    print("ok")
