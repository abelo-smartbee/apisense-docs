#!/usr/bin/env python3
"""Embed a digits-only Lato-Semibold subset into the assembly SVGs that carry
live <text> step numbers.

The designer's files declare `font-family: Lato-Semibold, Lato`, but an SVG
loaded through <img> is an isolated document: it cannot inherit the page's
fonts and cannot fetch a webfont. On any machine without Lato installed --
including this one and CI -- the numbers silently fall back to whatever the
renderer has. Chapter 03's numbers are outlined curves and are immune, so the
two chapters end up looking different.

Embedding the face as a data URI makes the SVG self-contained. Subset to the
eleven characters the numbers actually use, the whole face is ~5 kB.
"""

import base64
import re
import sys
from pathlib import Path

FIGS = Path("docs/assembly/figs")
DEFAULT_SUBSET = Path(__file__).parent / "assets" / "lato-semibold-digits.ttf"
SUBSET = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_SUBSET

TARGETS = [
    "step03-b.svg",
    "step04-a.svg",
    "step04-colonylink-app.svg",
    "step04-c.svg",
    "step04-vitalsensor-app.svg",
]

MARKER = "@font-face"


def face_rule(ttf: bytes) -> str:
    b64 = base64.b64encode(ttf).decode("ascii")
    return (
        "\n      @font-face {\n"
        "        font-family: 'Lato-Semibold';\n"
        "        font-weight: 600;\n"
        "        font-style: normal;\n"
        f"        src: url(data:font/ttf;base64,{b64}) format('truetype');\n"
        "      }\n"
    )


def main() -> int:
    if not SUBSET.exists():
        print(f"font subset not found: {SUBSET}")
        print("usage: svg_embed_font.py [subset.ttf]")
        return 2

    rule = face_rule(SUBSET.read_bytes())
    added = kb = 0

    for name in TARGETS:
        path = FIGS / name
        svg = path.read_text(encoding="utf-8")

        if MARKER in svg:
            print(f"  skip   {name} — already carries a @font-face")
            continue
        if "<style>" not in svg:
            print(f"  MISS   {name} — no <style> block to extend")
            continue

        before = len(svg)
        svg = svg.replace("<style>", "<style>" + rule, 1)
        path.write_text(svg, encoding="utf-8")
        added += 1
        kb += (len(svg) - before) / 1024
        print(f"  ok     {name} (+{(len(svg) - before) / 1024:.1f} kB)")

    print(f"\n{added} file(s) patched, +{kb:.0f} kB total")
    return 0


if __name__ == "__main__":
    sys.exit(main())
