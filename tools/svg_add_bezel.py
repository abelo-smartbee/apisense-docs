#!/usr/bin/env python3
"""Draw the phone bezel around every panel in the chapter 04 figures.

The designer changed convention at chapter 04: chapters 01-03 render a phone
body around each screen, chapter 04 drops it and places the bare screenshot.
This restores the earlier look so the deck reads as one document.

The bezel is a single ring path per panel -- an outer rounded rect and an inner
one in the same subpath list, filled with fill-rule="evenodd". Painting a ring
on top of the screen, rather than clipping the screen to a rounded rect, buys
two things: the screenshot's own square corners get covered rather than needing
a clipPath each, and the ring can sit *below* the hand/arrow layer so a hand
that crosses a panel edge is not sliced by beige.

Geometry comes from chapter 03, which is the reference:

    screen 741.6 wide, corner radius 50.4, bezel 14.4 thick

so radius and thickness are carried across as ratios of panel width. Panels
whose screen is a bitmap take their box from the <image> transform; the vector
scanner screens (04.6, 04.9, 04.12) take theirs from the backing <rect>.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

FIGS = Path("docs/assembly/figs")
TARGETS = [
    "step04-a.svg",
    "step04-colonylink-app.svg",
    "step04-vitalsensor-app.svg",
    "step04-c.svg",
]

BEZEL = "#d4c4ae"
REF_W, REF_R, REF_T = 741.6, 50.4, 14.4
MARK = "apisense-bezel"

RE_IMAGE = re.compile(
    r'<image\b[^>]*?\bwidth="([\d.]+)"[^>]*?\bheight="([\d.]+)"'
    r'[^>]*?\btransform="translate\(([-\d.]+)\s+([-\d.]+)\)\s*scale\(([-\d.]+)\)"[^>]*?/>'
)
RE_SCANNER = re.compile(
    r'<rect\b[^>]*?\bx="([\d.]+)"[^>]*?\by="([\d.]+)"'
    r'[^>]*?\bwidth="(7[34]\d(?:\.\d+)?)"[^>]*?\bheight="(16[23]\d(?:\.\d+)?)"[^>]*?/>'
)


def n(v: float) -> str:
    return f"{v:.2f}".rstrip("0").rstrip(".")


def rounded(x: float, y: float, w: float, h: float, r: float) -> str:
    return (
        f"M{n(x + r)},{n(y)} H{n(x + w - r)} A{n(r)},{n(r)} 0 0 1 {n(x + w)},{n(y + r)} "
        f"V{n(y + h - r)} A{n(r)},{n(r)} 0 0 1 {n(x + w - r)},{n(y + h)} "
        f"H{n(x + r)} A{n(r)},{n(r)} 0 0 1 {n(x)},{n(y + h - r)} "
        f"V{n(y + r)} A{n(r)},{n(r)} 0 0 1 {n(x + r)},{n(y)} Z"
    )


def ring(x: float, y: float, w: float, h: float) -> tuple[str, tuple[float, float, float, float]]:
    t = REF_T / REF_W * w
    r = REF_R / REF_W * w
    outer = rounded(x - t, y - t, w + 2 * t, h + 2 * t, r + t)
    inner = rounded(x, y, w, h, r)
    path = (
        f'<path class="{MARK}" fill="{BEZEL}" fill-rule="evenodd" d="{outer} {inner}"/>'
    )
    return path, (x - t, y - t, x + w + t, y + h + t)


def panels(svg: str) -> list[tuple[float, float, float, float]]:
    boxes = []
    for w, h, tx, ty, s in RE_IMAGE.findall(svg):
        boxes.append((float(tx), float(ty), float(w) * float(s), float(h) * float(s)))
    for x, y, w, h in RE_SCANNER.findall(svg):
        boxes.append((float(x), float(y), float(w), float(h)))
    return boxes


def main() -> int:
    for name in TARGETS:
        path = FIGS / name
        svg = path.read_text(encoding="utf-8")

        if MARK in svg:
            print(f"  skip   {name} — already has bezels")
            continue

        boxes = panels(svg)
        if not boxes:
            print(f"  MISS   {name} — no panels matched")
            continue

        rings, bounds = zip(*(ring(*b) for b in boxes))

        # After the last <image> is the seam between the screen layer and the
        # hand/arrow layer in every one of these files.
        last = None
        for m in RE_IMAGE.finditer(svg):
            last = m
        if last is None:
            print(f"  MISS   {name} — no <image> to anchor on")
            continue
        at = last.end()
        svg = svg[:at] + "\n  " + "\n  ".join(rings) + svg[at:]

        # Grow the canvas so the new outer edge is not cropped.
        vb = re.search(r'viewBox="([-\d.]+) ([-\d.]+) ([-\d.]+) ([-\d.]+)"', svg)
        x0, y0, w0, h0 = (float(v) for v in vb.groups())
        x1, y1 = x0 + w0, y0 + h0
        nx0 = min([x0] + [b[0] for b in bounds])
        ny0 = min([y0] + [b[1] for b in bounds])
        nx1 = max([x1] + [b[2] for b in bounds])
        ny1 = max([y1] + [b[3] for b in bounds])
        new_vb = f'viewBox="{n(nx0)} {n(ny0)} {n(nx1 - nx0)} {n(ny1 - ny0)}"'
        svg = svg.replace(vb.group(0), new_vb, 1)

        path.write_text(svg, encoding="utf-8")
        print(
            f"  ok     {name}: {len(boxes)} panels, "
            f"viewBox {n(w0)}x{n(h0)} -> {n(nx1 - nx0)}x{n(ny1 - ny0)}"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
