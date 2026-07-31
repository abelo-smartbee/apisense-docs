#!/usr/bin/env python3
"""Bundle docs/assembly/index.html into one self-contained HTML file.

Everything the page needs — drawings, fonts, styles, scripts — is inlined,
so the result can be e-mailed as a single attachment and opened offline.

    python3 tools/build_standalone.py

Output: docs/assembly/Apisense_BOX_Instrukcja_montazu_standalone.html
(next to the regular index.html, so it also ships with the docs site)
"""

from __future__ import annotations

import base64
import re
import sys
import urllib.request
from pathlib import Path
from typing import NamedTuple

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "docs" / "assembly" / "index.html"
FIGS = ROOT / "docs" / "assembly" / "figs"
OUT = SRC.parent / "Apisense_BOX_Instrukcja_montazu_standalone.html"

SITE = "https://docs.apisense.ai/"

# One stylesheet per family the page links, in the order the <head> links them.
# Three families, because Poppins covers eighteen locales and cannot cover the
# other two: it has zero Greek and zero Arabic glyphs. See
# dev-docs/adr/0003-kroje-greka-arabski.md.
FONT_CSS = {
    "Poppins": (
        "https://fonts.googleapis.com/css2"
        "?family=Poppins:wght@200;300;400;500;600&display=swap"
    ),
    "Noto Sans": (
        "https://fonts.googleapis.com/css2"
        "?family=Noto+Sans:wght@300;400;500;600&display=swap"
    ),
    "Cairo": (
        "https://fonts.googleapis.com/css2"
        "?family=Cairo:wght@300;400;500;600&display=swap"
    ),
}

# Which subsets are worth embedding, *per family* — the three families are here
# for different reasons and a single shared tuple would over-fetch from all of
# them.
#
# Poppins carries the Latin script for every locale: `latin` has ı ø å æ é ü,
# `latin-ext` the rest of the Turkish, Central-European, Baltic and Romanian
# letters (İ ğ ş ł ż ě ő ș ț …). Its one further subset, devanagari, no locale
# needs.
#
# Noto Sans is here *only* for Greek and Cairo *only* for Arabic; their
# `latin`/`latin-ext` subsets would be bytes spent to make `Apisense BOX` look
# different in `el` and `ar` than everywhere else — the ADR measures it and
# rejects it. Poppins stays first in the CSS stack, so the Latin inside Greek and
# Arabic sentences never reaches those families anyway.
#
# Verified by intersecting the cmap of every embedded woff2 with its declared
# unicode-range and checking the union against every codepoint the page actually
# renders — not by reading subset names, which promise more than they carry.
# Two characters do fall outside and always have, in Polish as much as in
# Finnish and Greek: `≤` (U+2264, in the temperature range) and `✱` (U+2731,
# the .ghost marker). Both come from the reader's fallback font, in the bundle
# and in the PDFs, and both are deliberate — no subset of either family supplies
# them.
KEEP_SUBSETS = {
    "Poppins": ("latin", "latin-ext"),
    "Noto Sans": ("greek",),
    "Cairo": ("arabic",),
}
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"

# A data URI carries no filename, so the type has to be declared. Most drawings are
# webp, but the animated mounting illustration is SVG — served as image/webp it just
# does not render, in the bundle and in every PDF printed from it. Fail on anything
# unrecognised rather than guess: a silently blank figure is the worse outcome.
FIG_TYPES = {".webp": "image/webp", ".svg": "image/svg+xml", ".png": "image/png"}


class Face(NamedTuple):
    """One `@font-face` rule: the subset it covers, its weight, its text, its payload."""

    subset: str
    weight: int
    block: str
    raw: bytes


# The one line two collapsible faces are allowed to disagree on.
WEIGHT_LINE = re.compile(r"font-weight:\s*\d+\s*;")


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def inline_family(family: str) -> list[str]:
    """@font-face rules of one family, each woff2 embedded as a data URI.

    Only the subsets listed for that family in KEEP_SUBSETS. A family that
    matches nothing is an error, not an empty result: Google Fonts renaming a
    subset would otherwise silently ship a bundle with no Greek or no Arabic in
    it, and a missing glyph looks like a plausible one from the reader's
    fallback font.

    Faces that turn out to be the *same file* described the *same way* are
    collapsed into a single rule carrying a weight range. Noto Sans and Cairo are
    variable fonts: `css2?...wght@300;400;500;600` answers with four @font-face
    blocks that differ only in their `font-weight` line and point at one URL, and
    embedding that URL four times put 210 688 B of duplicate base64 into a bundle
    whose entire purpose is to fit in an e-mail. `font-weight: 300 600` is how a
    variable font is meant to be declared — the browser sets the `wght` axis
    instead of picking a pre-instanced file.

    Grouped by the bytes, not by the family name: Poppins is a static family
    whose ten faces are ten different files, and it must come out of here
    unchanged. A future family that ships either way needs no decision here.

    Grouped by the rest of the rule as well, because collapsing means keeping one
    block and discarding the others: anything the faces do not already agree on —
    `font-style`, `font-display`, `unicode-range` — would vanish with them, and a
    dropped `font-style: italic` is invisible in a diff and invisible in a byte
    count. Cairo carries a `slnt` axis, so a future `ital,wght@0,…;1,…` query
    really could serve upright and oblique from one file. Keyed this way they
    land in different groups and both survive, rather than one quietly becoming
    the other.
    """
    keep = KEEP_SUBSETS[family]
    css = fetch(FONT_CSS[family]).decode("utf-8")
    blocks = re.findall(r"/\*\s*([\w-]+)\s*\*/\s*(@font-face\s*\{.*?\})", css, re.S)

    downloaded: dict[str, bytes] = {}   # one fetch per URL, however often it repeats
    faces: list[Face] = []
    for subset, block in blocks:
        if subset not in keep:
            continue
        match = re.search(r"url\((https://[^)]+)\)", block)
        if match is None:
            raise SystemExit(f"@font-face bez url() w subsecie {subset} — zmienił się format Google Fonts?")
        weight = re.search(r"font-weight:\s*(\d+)\s*;", block)
        if weight is None:
            # Almost certainly not Google changing anything: this is what a
            # *range* query looks like. `wght@300..600` answers with
            # `font-weight: 300 600;` — already the shape this function
            # produces, but not one it can read back.
            raise SystemExit(
                f"{family}/{subset}: @font-face bez pojedynczej font-weight."
                " Jeśli FONT_CSS pyta o zakres (`wght@300..600`), Google Fonts"
                " odpowiada `font-weight: 300 600;` — wróć do listy grubości"
                " (`wght@300;400;500;600`) albo naucz to miejsce czytać zakres"
            )
        url = match.group(1)
        if url not in downloaded:
            downloaded[url] = fetch(url)
        faces.append(Face(subset, int(weight.group(1)), block, downloaded[url]))

    if not faces:
        raise SystemExit(
            f"{family}: żaden subset z {', '.join(keep)} nie pasował"
            " — zmieniła się odpowiedź Google Fonts?"
        )

    groups: dict[tuple[str, bytes], list[Face]] = {}
    for face in faces:
        groups.setdefault((WEIGHT_LINE.sub("", face.block), face.raw), []).append(face)

    kept: list[str] = []
    for members in groups.values():
        weights = sorted(f.weight for f in members)
        block = re.sub(
            r"url\(https://[^)]+\)",
            "url(data:font/woff2;base64," + base64.b64encode(members[0].raw).decode("ascii") + ")",
            members[0].block,
        )
        if len(members) > 1:
            block = WEIGHT_LINE.sub(f"font-weight: {weights[0]} {weights[-1]};", block, count=1)
        kept.append(block)

    saved = sum(len(f.raw) for f in faces) - sum(len(m[0].raw) for m in groups.values())
    note = f", zwinięte z {len(faces)} (−{saved} B woff2)" if saved else ""
    print(f"  fonts: {family} — {len(kept)} faces ({', '.join(keep)}){note}")
    return kept


def inline_fonts() -> str:
    """Every family's @font-face rules, in the order the <head> links them."""
    faces: list[str] = []
    for family in FONT_CSS:
        faces.extend(inline_family(family))
    return "\n".join(faces)


def main() -> None:
    html = SRC.read_text(encoding="utf-8")

    # 1. fonts: swap the stylesheet <link>s for embedded @font-face rules.
    # One <link> per family, so the pattern has to swallow all of them — and the
    # HTML comment that documents why the second one exists, which sits between
    # them. Compared by family name, not by count: two links and two families
    # match on a count even when the page has swapped Poppins for something else,
    # and the bundle would then embed a family nothing on the page asks for while
    # the one it does ask for arrives from the reader's fallback. Names make that
    # a build error instead of a silently wrong artefact.
    links = re.findall(r'<link href="https://fonts\.googleapis\.com[^>]*>', html)
    linked = {
        fam.replace("+", " ")
        for link in links
        for fam in re.findall(r"family=([^:&\"]+)", link)
    }
    if linked != set(FONT_CSS):
        raise SystemExit(
            f"<head> linkuje {sorted(linked)}, a FONT_CSS ma {sorted(FONT_CSS)}"
            " — rozjechały się"
        )
    faces = inline_fonts()
    html = re.sub(
        r'<link rel="preconnect"[^>]*>\s*'
        r'<link rel="preconnect"[^>]*crossorigin>\s*'
        r'(?:(?:<!--.*?-->|<link href="https://fonts\.googleapis\.com[^>]*>)\s*)+',
        "<style>\n" + faces + "\n</style>\n",
        html,
        count=1,
        flags=re.S,
    )
    if "fonts.googleapis.com" in html:
        raise SystemExit("font <link> was not replaced")

    # 2. drawings: figs/* -> data URIs
    used = set(re.findall(r'src="figs/([^"]+)"', html))
    for name in sorted(used):
        suffix = Path(name).suffix.lower()
        mime = FIG_TYPES.get(suffix)
        if mime is None:
            raise SystemExit(f"nieznany typ rysunku: figs/{name}")
        blob = (FIGS / name).read_bytes()
        uri = f"data:{mime};base64," + base64.b64encode(blob).decode("ascii")
        html = html.replace(f'src="figs/{name}"', f'src="{uri}"')
    print(f"  images: {len(used)} embedded")

    # 3. relative site links only resolve on docs.apisense.ai — make them absolute
    html = html.replace('href="../downloads/', f'href="{SITE}downloads/')
    html = html.replace('href="../"', f'href="{SITE}"')
    # a downloaded file cannot "download" a remote PDF; open it instead
    html = html.replace(f'href="{SITE}downloads/files/Apisense_Box_Assembly_Instruction.pdf" download',
                        f'href="{SITE}downloads/files/Apisense_Box_Assembly_Instruction.pdf" target="_blank" rel="noopener"')

    # 4. deep links write to history — pointless for a local file, and noisy
    html = html.replace(
        "    history.replaceState(null, '', i === 0 ? location.pathname : '#' + slides[i].id);\n",
        "    if (location.protocol !== 'file:') history.replaceState(null, '', i === 0 ? location.pathname : '#' + slides[i].id);\n",
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(html, encoding="utf-8")
    print(f"  → {OUT.relative_to(ROOT)}  ({OUT.stat().st_size / 1_048_576:.1f} MB)")


if __name__ == "__main__":
    sys.exit(main())
