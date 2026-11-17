"""Render YUMUK.ME as a GitHub-style contribution grid (light and dark SVG)."""
import random
import sys
from pathlib import Path

FONT = {
    "Y": ["X...X", "X...X", ".X.X.", "..X..", "..X..", "..X..", "..X.."],
    "U": ["X...X", "X...X", "X...X", "X...X", "X...X", "X...X", ".XXX."],
    "M": ["X...X", "XX.XX", "X.X.X", "X.X.X", "X...X", "X...X", "X...X"],
    "K": ["X...X", "X..X.", "X.X..", "XX...", "X.X..", "X..X.", "X...X"],
    "E": ["XXXXX", "X....", "X....", "XXXX.", "X....", "X....", "XXXXX"],
    ".": [".", ".", ".", ".", ".", ".", "X"],
}
TEXT = "YUMUK.ME"
COLS, ROWS = 53, 7
CELL, GAP = 10, 3
PITCH = CELL + GAP
PAD = 2
LEGEND_H = 26

THEMES = {
    "light": {"empty": "#ebedf0", "levels": ["#9be9a8", "#40c463", "#30a14e", "#216e39"], "text": "#57606a"},
    "dark": {"empty": "#161b22", "levels": ["#0e4429", "#006d32", "#26a641", "#39d353"], "text": "#8b949e"},
}


def lit_cells():
    columns = []
    for i, ch in enumerate(TEXT):
        glyph = FONT[ch]
        for c in range(len(glyph[0])):
            columns.append([glyph[r][c] == "X" for r in range(ROWS)])
        if i < len(TEXT) - 1:
            columns.append([False] * ROWS)
    offset = (COLS - len(columns)) // 2
    rng = random.Random(2026)
    cells = {}
    for c, col in enumerate(columns):
        for r, on in enumerate(col):
            if on:
                # weight toward the stronger greens so the letters stay legible
                cells[(c + offset, r)] = rng.choices([1, 2, 3], weights=[2, 4, 3])[0]
    return cells


def render(theme):
    t = THEMES[theme]
    cells = lit_cells()
    width = COLS * PITCH - GAP + 2 * PAD
    height = ROWS * PITCH - GAP + 2 * PAD + LEGEND_H
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" role="img" aria-label="yumuk.me written in a contribution grid">',
        "<style>"
        ".on{animation:on .5s ease-out both}"
        "@keyframes on{from{opacity:0}to{opacity:1}}"
        "@media (prefers-reduced-motion:reduce){.on{animation:none}}"
        f"text{{font:10px -apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;fill:{t['text']}}}"
        "</style>",
    ]
    for c in range(COLS):
        for r in range(ROWS):
            x, y = PAD + c * PITCH, PAD + r * PITCH
            out.append(f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="2" fill="{t["empty"]}"/>')
    for (c, r), level in sorted(cells.items()):
        x, y = PAD + c * PITCH, PAD + r * PITCH
        delay = 0.2 + c * 0.03 + r * 0.01
        out.append(
            f'<rect class="on" style="animation-delay:{delay:.2f}s" x="{x}" y="{y}" '
            f'width="{CELL}" height="{CELL}" rx="2" fill="{t["levels"][level]}"/>'
        )
    ly = PAD + ROWS * PITCH + 6
    swatches = [t["empty"]] + t["levels"]
    more_w, less_w = 26, 24
    lx = width - PAD - more_w - len(swatches) * PITCH - less_w - 4
    out.append(f'<text x="{lx}" y="{ly + 9}">Less</text>')
    for i, colour in enumerate(swatches):
        out.append(f'<rect x="{lx + less_w + 2 + i * PITCH}" y="{ly}" width="{CELL}" height="{CELL}" rx="2" fill="{colour}"/>')
    out.append(f'<text x="{lx + less_w + 4 + len(swatches) * PITCH}" y="{ly + 9}">More</text>')
    out.append("</svg>")
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    dest = Path(sys.argv[1])
    for theme in THEMES:
        (dest / f"grid-{theme}.svg").write_text(render(theme))
    print(len(lit_cells()), "lit cells")
