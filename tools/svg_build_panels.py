#!/usr/bin/env python3
"""Rebuild the assembly-manual app figures (chapters 02-05) from screenshots.

Every phone-panel figure in the deck is generated from `FIGURES` below; the
designer's SVGs are no longer the source, only the origin of the shared shapes
in `tools/assets/`. A panel renders from `shots/<locale>/` with fallback to
English, and a panel that has no screenshot anywhere renders its vector
stand-in (the QR scanner, the welcome screen). Everything here follows
`dev-docs/grafiki-assembly.md`:

- panel module and bezel from chapter 03 (741.6 x 1629, r 50.4, bezel 14.4),
- screenshots padded to the module, never cropped,
- hands and arrows lifted from the designer's chapter 04 file so the drawing
  vocabulary stays his,
- step numbers as <text> with the Lato subset embedded, so they render the same
  everywhere.
"""

from __future__ import annotations

import argparse
import base64
import json
import re
from io import BytesIO
from pathlib import Path

from PIL import Image

ROOT = Path(".")
FIGS = ROOT / "docs/assembly/figs"
SHOT_ROOT = ROOT / "docs/assembly/shots"
LEGACY_SHOTS = ROOT / "docs/manual/pictures"
FONT = ROOT / "tools/assets/lato-semibold-digits.ttf"
ASSETS = ROOT / "tools/assets"
THUMB = ROOT / "tools/assets/thumbs-up.path"
HAND = ROOT / "tools/assets/hand-point.path"
ARROW_FLOW = ROOT / "tools/assets/arrow-flow.svg"
ARROW_POINT = ROOT / "tools/assets/arrow-point.svg"

# The deck ships one figure per locale only where a locale actually has its own
# screenshots. Everything else falls back, so a missing translation degrades to
# English rather than to a broken image.
BASE_LOCALE = "en"

# Chapter 03 module.
SCREEN_W, SCREEN_H = 741.6, 1629.0
RADIUS, BEZEL = 50.4, 14.4
PITCH = 854.17
TOP = 93.27
NUM_Y = 61.92
BEZEL_COLOR = "#d4c4ae"

# Measured on the designer's own shapes. The hand's ANATOMY is easy to get
# backwards and one whole evening went to exactly that: the top-left extreme of
# the shape is the KNUCKLE of the curled hand, and the index finger extends
# DOWN-RIGHT, ending in a touch halo. The tap point is the centre of that halo,
# measured on the rasterised outline as the centroid of the halo arcs (the two
# components that are not the hand itself). Anchoring the top-left corner put
# the back of the hand on every control while the finger pointed at nothing.
HAND_BBOX, HAND_TIP = (2076.2, 1385.3, 338.5, 318.1), (271.0, 254.2)
FLOW_BBOX, FLOW_TIP = (1400.2, 757.6, 497.7, 189.8), (495.1, 73.4)     # panel -> panel
FLOW_TAIL = (1400.7, 937.0)   # leftmost point of the rendered stroke
POINT_BBOX, POINT_TIP = (485.5, 656.1, 484.4, 312.6), (481.4, 309.7)   # -> a control
THUMB_BBOX = (2183.0, 1153.1, 356.5, 315.1)

PANEL_MARGIN = 10.0

# Where the fingertip parks in "press" mode. Chosen so the hand still ends above
# the phone's bottom edge; the designer uses the same trick on 04.3 and 04.4.
PRESS_Y = 0.80


# Roughly 60% of the suite already carries a phone frame in the deck's own bezel
# colour, the rest does not. Compositing an unnormalised shot inside our bezel
# draws the frame twice, which reads as a heavy dark outline once the plate is
# scaled down. Strip whatever is there and let the figure draw the only frame.
FRAME_RGB = (212, 196, 175)

FIGURES = [
    # Every target below is the control's centre *measured on our screenshot*
    # (fraction of the normalised image), read off a 0.05 grid overlay -- build
    # one with `--grid <shot>`. Never transplant positions from the designer's
    # files: his screenshots laid the same screens out differently, so his
    # fractions put the hand next to our controls, not on them. Measured this
    # way the target survives a locale swap for free -- a translated screenshot
    # keeps its layout, so the control keeps its fraction.
    #
    # Check any change with `--debug`, which draws a crosshair on each target:
    # the visible fingertip must touch the cross.
    {
        "name": "step02-account.svg",
        "panels": [
            {"n": "02", "shot": "02_signup.png"},
        ],
    },
    {
        "name": "step03-a.svg",
        "panels": [
            # The suite has no English welcome screenshot yet, only a Polish
            # one -- so the base figure keeps the designer's vector welcome
            # screen and a locale switches to its screenshot the moment
            # shots/<locale>/03_welcome.png exists (issue #81).
            {"n": "03.1", "shot": "03_welcome.png", "vector": "welcome-screen",
             "point": (0.5, 0.75), "vpoint": (0.5, 0.744)},
            {"n": "03.2", "shot": "03_add_apiary.png", "point": (0.5, 0.295)},
        ],
    },
    {
        "name": "step03-b.svg",
        "panels": [
            {"n": "03.4", "shot": "03_add_apiary_hub.png", "point": (0.895, 0.53)},
            {"n": "03.5", "vector": "scanner-screen"},
            {"n": "03.6", "shot": "03_hub_power_tile.png"},
            {"n": "03.7", "shot": "04_apiaries_home.png", "thumb": (0.85, 0.62)},
        ],
    },
    {
        "name": "step04-a.svg",
        "panels": [
            {"n": "04.1", "shot": "04_apiaries_home.png", "point": (0.583, 0.462)},
            {"n": "04.2", "shot": "04_apiary_empty.png", "point": (0.5, 0.603)},
            {"n": "04.3", "shot": "04_hive_details.png", "point": (0.869, 0.949)},
            {"n": "04.4", "shot": "04_hive_queen.png", "point": (0.869, 0.949)},
        ],
    },
    {
        "name": "step04-colonylink-app.svg",
        "panels": [
            {"n": "04.5", "shot": "04_equip_colonylink_empty.png", "point": (0.901, 0.456)},
            {"n": "04.6", "vector": "scanner-screen"},
            {"n": "04.7", "shot": "04_equip_colonylink_filled.png", "thumb": (0.640, 0.650)},
        ],
    },
    {
        "name": "step04-vitalsensor-app.svg",
        "panels": [
            {"n": "04.8", "shot": "04_equip_sensor_empty.png", "point": (0.901, 0.476)},
            {"n": "04.9", "vector": "scanner-screen"},
            {"n": "04.10", "shot": "04_equip_sensor_filled.png", "thumb": (0.641, 0.659)},
        ],
    },
    {
        "name": "step04-c.svg",
        "panels": [
            {"n": "04.11", "shot": "04_equip_scale_empty.png", "point": (0.901, 0.521)},
            {"n": "04.12", "vector": "scanner-screen"},
            {"n": "04.13", "shot": "04_equip_scale_filled.png", "point": (0.908, 0.935)},
            {"n": "04.14", "shot": "04_hive_awaiting_connection.png", "thumb": (0.634, 0.585)},
        ],
    },
    {
        "name": "step05-a.svg",
        "panels": [
            # The Add... menu already open: pointing at the nav bar itself is
            # hopeless -- four icons side by side and a hand 46% of the screen
            # wide -- while the menu item sits high enough for the hand to fit.
            {"n": "05.1", "shot": "04_hive_awaiting_connection.png",
             "point": (0.55, 0.782)},
            {"n": "05.2", "shot": "add_beehive_details.png"},
            {"n": "05.3", "shot": "add_beehive_queen.png"},
        ],
    },
    {
        "name": "step05-b.svg",
        "panels": [
            {"n": "05.4", "shot": "add_beehive_devices_colonylink.png"},
            {"n": "05.5", "shot": "add_beehive_devices_sensor.png"},
            {"n": "05.6", "shot": "add_beehive_devices_scale.png",
             "point": (0.909, 0.935)},
        ],
    },
]


def find_shot(name: str, locale: str) -> Path:
    """Resolve a screenshot for a locale, falling back rather than failing.

    Order: the locale's own directory, then English, then the manual's shared
    pictures, which is where the suite lands today while it is still
    single-locale. A figure therefore builds for any locale from day one and
    simply improves as `shots/<locale>/` fills up (issue #81).
    """
    for candidate in (SHOT_ROOT / locale / name,
                      SHOT_ROOT / BASE_LOCALE / name,
                      LEGACY_SHOTS / name):
        if candidate.exists():
            return candidate
    raise FileNotFoundError(f"{name}: not in shots/{locale}, shots/{BASE_LOCALE} or manual pictures")


def n(v: float) -> str:
    return f"{v:.2f}".rstrip("0").rstrip(".")


def rounded(x, y, w, h, r) -> str:
    return (
        f"M{n(x + r)},{n(y)} H{n(x + w - r)} A{n(r)},{n(r)} 0 0 1 {n(x + w)},{n(y + r)} "
        f"V{n(y + h - r)} A{n(r)},{n(r)} 0 0 1 {n(x + w - r)},{n(y + h)} "
        f"H{n(x + r)} A{n(r)},{n(r)} 0 0 1 {n(x)},{n(y + h - r)} "
        f"V{n(y + r)} A{n(r)},{n(r)} 0 0 1 {n(x + r)},{n(y)} Z"
    )


def parts() -> dict[str, str]:
    """Hand, arrows and thumbs-up, kept as repo assets.

    They were lifted from the designer's delivery once and committed here. They
    must not be read back out of `figs/` -- the generator overwrites those files,
    so sourcing the shapes from them would work exactly once and then destroy
    itself.
    """
    return {
        "hand": HAND.read_text(encoding="utf-8").strip(),
        "flow": ARROW_FLOW.read_text(encoding="utf-8").strip(),
        "point": ARROW_POINT.read_text(encoding="utf-8").strip(),
        "thumb": THUMB.read_text(encoding="utf-8").strip(),
    }


def vector_screen(stem: str) -> tuple[str, str, str]:
    """A vector app screen from tools/assets, as (style, defs, body).

    These stand in where the suite has no screenshot: the QR scanner (never
    captured) and any screen a locale is still missing. Each asset is
    normalised to the panel module (0,0 741.6x1629) and carries its own class
    prefix (sc-, ws-, ...) so it cannot collide with the figure's styles.
    """
    svg = (ASSETS / f"{stem}.svg").read_text(encoding="utf-8")
    style = re.search(r"<style>(.*?)</style>", svg, re.S)
    defs = re.search(r"<defs>.*?</style>(.*?)</defs>", svg, re.S)
    if style is None:                      # asset without a <style> block
        d = re.search(r"<defs>(.*?)</defs>", svg, re.S)
        return "", (d.group(1).strip() if d else ""), \
            svg[svg.index("</defs>") + len("</defs>"):svg.rindex("</svg>")].strip()
    body = svg[svg.index("</defs>") + len("</defs>"):svg.rindex("</svg>")]
    return style.group(1).strip(), defs.group(1).strip(), body.strip()


def unframed(img: Image.Image) -> Image.Image:
    """Drop a phone frame the screenshot already carries, if it carries one.

    The suite is not consistent about this -- some shots are bare screens, some
    arrive inside an 8 px frame, one inside 30 px -- so measure rather than
    assume. Only a border that is uniform on all four sides counts.
    """
    rgb = img.convert("RGB")
    w, h = rgb.size
    row, col = h // 2, w // 2

    def run(pixels) -> int:
        k = 0
        for c in pixels:
            if max(abs(a - b) for a, b in zip(c, FRAME_RGB)) > 6:
                break
            k += 1
        return k

    edges = [
        run(rgb.getpixel((x, row)) for x in range(40)),
        run(rgb.getpixel((w - 1 - x, row)) for x in range(40)),
        run(rgb.getpixel((col, y)) for y in range(40)),
        run(rgb.getpixel((col, h - 1 - y)) for y in range(40)),
    ]
    k = min(edges)
    if k < 3 or max(edges) - k > 2:
        return img
    return img.crop((k, k, w - k, h - k))


def pad_colour(img: Image.Image) -> tuple[int, int, int]:
    """The colour to letterbox with when the shot does not fill the module.

    Never sample a corner: the screen has a rounded one, so a pixel at (2, 2)
    still belongs to the phone frame. Padding with that paints a second bezel
    around the panel -- which is what the first two attempts at chapter 05 did.
    Take the middle of the top edge instead, where the screen runs straight.
    """
    rgb = img.convert("RGB")
    w, h = rgb.size
    return rgb.getpixel((w // 2, 2))


def crosshair(x: float, y: float) -> str:
    """A debug marker on a gesture target; the fingertip must touch it."""
    return (
        f'\n  <g stroke="#e00" stroke-width="4" fill="none">'
        f'<circle cx="{n(x)}" cy="{n(y)}" r="22"/>'
        f'<path d="M{n(x - 40)},{n(y)} H{n(x + 40)} M{n(x)},{n(y - 40)} V{n(y + 40)}"/></g>'
    )


def build(fig: dict, art: dict[str, str], locale: str, floor: float = 0.0,
          debug: bool = False) -> str:
    panels = fig["panels"]
    body: list[str] = []
    # Hands and arrows go on top of every panel, the way chapter 04 layers them --
    # an arrow appended next to its own panel is painted over by the following one.
    gestures: list[str] = []
    defs: list[str] = []
    used_vectors: set[str] = set()
    right = bottom = 0.0
    left = -BEZEL
    top = -17.29

    def emit_flow(i: int, bx: float, tip: tuple[float, float] | None = None) -> None:
        if i + 1 >= len(panels):
            return
        gutter = bx + SCREEN_W + (PITCH - SCREEN_W) / 2
        dx = gutter - (FLOW_BBOX[0] + FLOW_BBOX[2] / 2)

        # When the panel's pointing hand sits in the arrow's default band, the
        # tail would cut across the hand's back -- which is exactly what made
        # the three QR panels unreadable. The designer's own answer (KROK 04c):
        # start the arrow at the fingertip and let it sweep into the next
        # screen. Anchor the tail there whenever the two would collide;
        # everywhere else the arrow keeps its usual gutter position, so the
        # rule is stable under locale screenshot swaps.
        if tip is not None:
            hand = (tip[0] - HAND_TIP[0], tip[1] - HAND_TIP[1])
            band_x = (FLOW_BBOX[0] + dx, FLOW_BBOX[0] + FLOW_BBOX[2] + dx)
            collides = (hand[0] < band_x[1] and hand[0] + HAND_BBOX[2] > band_x[0]
                        and hand[1] < FLOW_BBOX[1] + FLOW_BBOX[3]
                        and hand[1] + HAND_BBOX[3] > FLOW_BBOX[1])
            if collides:
                gestures.append(
                    f'\n  <g transform="translate({n(tip[0] + 36 - FLOW_TAIL[0])} '
                    f'{n(tip[1] - 28 - FLOW_TAIL[1])})">{art["flow"]}</g>'
                )
                return
        gestures.append(f'\n  <g transform="translate({n(dx)} 0)">{art["flow"]}</g>')

    def emit_number(bx: float, num: str) -> None:
        body.append(
            f'\n  <text class="num" transform="translate({n(bx - 8.5)} {NUM_Y})">'
            f'<tspan x="0" y="0">{num}</tspan></text>'
        )

    for i, p in enumerate(panels):
        bx = i * PITCH
        clip = f"p{i}"
        defs.append(
            f'<clipPath id="{clip}">'
            f'<path d="{rounded(bx, TOP, SCREEN_W, SCREEN_H, RADIUS)}"/></clipPath>'
        )

        # A panel renders from its locale screenshot when one resolves, else
        # from its vector stand-in (the scanner always, the welcome screen
        # until a locale ships that screenshot). Both paths land in the same
        # (ox, oy, dw, dh) box, so gestures below need no branching.
        img = None
        if p.get("shot"):
            try:
                img = unframed(Image.open(find_shot(p["shot"], locale)))
            except FileNotFoundError:
                if "vector" not in p:
                    raise

        if img is not None:
            iw, ih = img.size
            scale = min(SCREEN_W / iw, SCREEN_H / ih)
            dw, dh = iw * scale, ih * scale
            ox, oy = bx + (SCREEN_W - dw) / 2, TOP + (SCREEN_H - dh) / 2
            pad = "#%02x%02x%02x" % pad_colour(img)
            buf = BytesIO()
            img.save(buf, format="PNG", optimize=True)
            data = base64.b64encode(buf.getvalue()).decode("ascii")

            body.append(
                f'\n  <g clip-path="url(#{clip})">'
                f'<path d="{rounded(bx, TOP, SCREEN_W, SCREEN_H, RADIUS)}" fill="{pad}"/>'
                f'<image width="{iw}" height="{ih}" '
                f'transform="translate({n(ox)} {n(oy)}) scale({scale:.5f})" '
                f'xlink:href="data:image/png;base64,{data}"/></g>'
            )
        else:
            stem = p["vector"]
            used_vectors.add(stem)
            body.append(
                f'\n  <g clip-path="url(#{clip})">'
                f'<g transform="translate({n(bx)} {n(TOP)})">{VECTOR_ART[stem][2]}</g></g>'
            )
            ox, oy, dw, dh = bx, TOP, SCREEN_W, SCREEN_H
        body.append(
            f'\n  <path class="bezel" d="'
            f'{rounded(bx - BEZEL, TOP - BEZEL, SCREEN_W + 2 * BEZEL, SCREEN_H + 2 * BEZEL, RADIUS + BEZEL)} '
            f'{rounded(bx, TOP, SCREEN_W, SCREEN_H, RADIUS)}"/>'
        )

        right = max(right, bx + SCREEN_W + BEZEL)
        bottom = max(bottom, TOP + SCREEN_H + BEZEL)

        # Targets are fractions of the screen, never pixels, so a figure rebuilt
        # from another locale's screenshot still points at the same control.
        #
        # point — the touch halo (HAND_TIP, the centre of the arc around the
        # index finger's end) lands on the control; the hand's body spreads
        # up-left from there, so the finger visibly descends onto the control.
        # Nothing above the target gets pointed at, so a control's label --
        # which Material puts above or left of it -- stays readable.
        gesture = "point" if "point" in p else ("press" if "press" in p else None)
        if gesture:
            # A vector stand-in lays the screen out differently than the
            # screenshot it substitutes for, so it carries its own target.
            fx, fy = p["vpoint"] if (img is None and "vpoint" in p) else p[gesture]
            tx, ty = ox + fx * dw, oy + fy * dh
            tip = (HAND_BBOX[0] + HAND_TIP[0], HAND_BBOX[1] + HAND_TIP[1])

            if gesture == "point":
                hx, hy = tx, ty
            else:
                hy = TOP + PRESS_Y * SCREEN_H
                hx = tx - HAND_BBOX[2] / 2 + HAND_TIP[0]

            # Do NOT clamp the hand into its panel. The designer lets it spill
            # into the gutter -- his 04.8 reaches 918 on a panel that ends at
            # 741.6 -- and clamping drags every right-hand target sharply left,
            # which is what made four panels look like they pressed the wrong
            # spot. The figure widens instead.
            if p.get("mirror"):
                gestures.append(
                    f'\n  <g transform="translate({n(hx)} {n(hy - tip[1])}) scale(-1 1) '
                    f'translate({n(-tip[0])} 0)"><path class="hand" d="{art["hand"]}"/></g>'
                )
            else:
                gestures.append(
                    f'\n  <g transform="translate({n(hx - tip[0])} {n(hy - tip[1])})">'
                    f'<path class="hand" d="{art["hand"]}"/></g>'
                )
                right = max(right, hx + HAND_BBOX[2] - HAND_TIP[0] + PANEL_MARGIN)
            bottom = max(bottom, hy + HAND_BBOX[3] - HAND_TIP[1] + PANEL_MARGIN)
            if debug:
                gestures.append(crosshair(tx, ty))
            emit_flow(i, bx, (tx, ty) if gesture == "point" else None)
        else:
            emit_flow(i, bx)

        if "thumb" in p:
            # A confirmation mark rather than a pointer: it sits half off the
            # panel by design, so the figure has to widen to hold it.
            fx, fy = p["thumb"]
            tx, ty = bx + fx * SCREEN_W, TOP + fy * SCREEN_H
            gestures.append(
                f'\n  <g transform="translate({n(tx - THUMB_BBOX[0])} '
                f'{n(ty - THUMB_BBOX[1])})"><path d="{art["thumb"]}"/></g>'
            )
            right = max(right, tx + THUMB_BBOX[2] + PANEL_MARGIN)
            bottom = max(bottom, ty + THUMB_BBOX[3] + PANEL_MARGIN)

        emit_number(bx, p["n"])

    for stem in sorted(used_vectors):
        if VECTOR_ART[stem][1]:
            defs.insert(0, VECTOR_ART[stem][1])

    font = base64.b64encode(FONT.read_bytes()).decode("ascii")
    style = (
        "\n      @font-face {\n"
        "        font-family: 'Lato-Semibold';\n"
        "        font-weight: 600;\n"
        "        font-style: normal;\n"
        f"        src: url(data:font/ttf;base64,{font}) format('truetype');\n"
        "      }\n\n"
        "      .num {\n        fill: #1d1d1b;\n"
        "        font-family: Lato-Semibold, Lato;\n"
        "        font-size: 72px;\n        font-weight: 600;\n      }\n\n"
        f"      .bezel {{\n        fill: {BEZEL_COLOR};\n        fill-rule: evenodd;\n      }}\n\n"
        "      .hand {\n        fill: none;\n        stroke: #1d1d1b;\n"
        "        stroke-linecap: round;\n        stroke-linejoin: round;\n"
        "        stroke-width: 18px;\n      }\n"
        + "".join("\n" + VECTOR_ART[s][0] + "\n"
                   for s in sorted(used_vectors) if VECTOR_ART[s][0])
    )

    bottom = max(bottom, floor)
    vb = f"{n(left)} {n(top)} {n(right - left)} {n(bottom - top)}"
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
        f'viewBox="{vb}">\n  <defs>\n    <style>{style}    </style>\n    '
        + "\n    ".join(defs)
        + "\n  </defs>"
        + "".join(body)
        + "".join(gestures)
        + "\n</svg>\n"
    ), (right - left, bottom - top)


def out_name(stem: str, locale: str | None) -> str:
    """`step05-a.svg` for the fallback build, `step05-a.de.svg` for a locale."""
    return stem if locale is None else stem.replace(".svg", f".{locale}.svg")


# (style, defs, body) per vector screen, loaded once for every stem FIGURES uses.
VECTOR_ART = {stem: vector_screen(stem)
              for fig in FIGURES for p in fig["panels"]
              for stem in ([p["vector"]] if "vector" in p else [])}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument(
        "--locale", metavar="XX",
        help="build the locale variant from shots/XX, falling back per screenshot; "
             "omit to rebuild the fallback figures the deck ships by default",
    )
    ap.add_argument(
        "--grid", metavar="SHOT",
        help="write SHOT with a 0.05 fraction grid to grid_SHOT in the current "
             "directory, for reading a control's target off the screenshot",
    )
    ap.add_argument(
        "--debug", action="store_true",
        help="draw a crosshair on every gesture target; the fingertip must touch it",
    )
    args = ap.parse_args()
    locale = args.locale

    if args.grid:
        from PIL import ImageDraw
        img = unframed(Image.open(find_shot(args.grid, locale or BASE_LOCALE))).convert("RGB")
        w, h = img.size
        d = ImageDraw.Draw(img)
        for i in range(1, 20):
            f = i / 20
            d.line([(0, int(f * h)), (w, int(f * h))], fill=(255, 0, 0), width=2)
            d.text((6, int(f * h) + 4), f"{f:.2f}", fill=(255, 0, 0))
            d.line([(int(f * w), 0), (int(f * w), h)], fill=(0, 120, 255), width=1)
            d.text((int(f * w) + 3, 6), f"{f:.2f}", fill=(0, 120, 255))
        out = Path(f"grid_{args.grid}")
        img.save(out)
        print(out)
        return 0

    art = parts()
    # A first pass just to learn how far the tallest hand reaches. Both figures
    # then share that floor, so panels scale identically across the chapter.
    floor = max(build(f, art, locale or BASE_LOCALE)[1][1] - 17.29 for f in FIGURES)
    dims, borrowed = {}, set()
    for fig in FIGURES:
        # A locale variant is only worth shipping when at least one panel has
        # that locale's own screenshot; otherwise it would be a byte-for-byte
        # duplicate of the fallback figure, and the deck's fallback already
        # covers it. Report what the locale did not actually have, so a variant
        # that is entirely English does not look like a finished translation.
        if locale:
            own = False
            for p in fig["panels"]:
                shot = p.get("shot")          # panele wektorowe nie mają zrzutu
                if shot and (SHOT_ROOT / locale / shot).exists():
                    own = True
                elif shot:
                    borrowed.add(shot)
            if not own:
                print(f"  {out_name(fig['name'], locale)}: pominięty — "
                      f"shots/{locale} nie ma żadnego zrzutu tej figury")
                continue

        svg, (w, h) = build(fig, art, locale or BASE_LOCALE, floor, debug=args.debug)
        name = out_name(fig["name"], locale)
        (FIGS / name).write_text(svg, encoding="utf-8")
        dims[name] = (round(w), round(h))
        print(f"  {name}: {len(fig['panels'])} panels, "
              f"viewBox {w:.0f}x{h:.0f}, {len(svg) / 1024:.0f} kB")

    if borrowed:
        print(f"\n  {len(borrowed)} zrzut(y) spoza shots/{locale} — wzięte z fallbacku:")
        for s in sorted(borrowed):
            print(f"    {s}")
    print(json.dumps(dims))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
