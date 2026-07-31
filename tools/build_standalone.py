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

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "docs" / "assembly" / "index.html"
FIGS = ROOT / "docs" / "assembly" / "figs"
OUT = SRC.parent / "Apisense_BOX_Instrukcja_montazu_standalone.html"

SITE = "https://docs.apisense.ai/"
FONT_CSS = (
    "https://fonts.googleapis.com/css2"
    "?family=Poppins:wght@200;300;400;500;600&display=swap"
)
# Enough for all seventeen locales, all of them Latin-script: `latin` carries
# ı ø å æ é ü, `latin-ext` the rest of the Turkish, Central-European, Baltic and
# Romanian letters (İ ğ ş ł ż ě ő ș ț …). Verified by intersecting the cmap of
# every embedded woff2 with its declared unicode-range and checking the union
# against every codepoint the page actually renders — not by reading subset
# names, which promise more than they carry. Two characters do fall outside and
# always have, in Polish as much as in Finnish: `≤` (U+2264, in the temperature
# range) and `✱` (U+2731, the .ghost marker). Both come from the reader's
# fallback font, in the bundle and in the PDFs, and both are deliberate — there
# is no Poppins subset that would supply them.
#
# Poppins offers exactly one further subset, devanagari, which no locale needs.
# Greek and Arabic are not a KEEP_SUBSETS question at all: Poppins has zero
# glyphs for either script, so `el` and `ar` need a second family — see
# dev-docs/adr/0003-kroje-greka-arabski.md, still unsigned. Adding them means
# fetching more than one stylesheet here and filtering subsets per family, which
# this single tuple cannot express.
KEEP_SUBSETS = ("latin", "latin-ext")
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"

# A data URI carries no filename, so the type has to be declared. Most drawings are
# webp, but the animated mounting illustration is SVG — served as image/webp it just
# does not render, in the bundle and in every PDF printed from it. Fail on anything
# unrecognised rather than guess: a silently blank figure is the worse outcome.
FIG_TYPES = {".webp": "image/webp", ".svg": "image/svg+xml", ".png": "image/png"}


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def inline_fonts() -> str:
    """Download the Poppins @font-face rules and embed each woff2 as a data URI."""
    css = fetch(FONT_CSS).decode("utf-8")
    blocks = re.findall(r"/\*\s*([\w-]+)\s*\*/\s*(@font-face\s*\{.*?\})", css, re.S)
    kept = []
    for subset, block in blocks:
        if subset not in KEEP_SUBSETS:
            continue
        match = re.search(r"url\((https://[^)]+)\)", block)
        if match is None:
            raise SystemExit(f"@font-face bez url() w subsecie {subset} — zmienił się format Google Fonts?")
        data = base64.b64encode(fetch(match.group(1))).decode("ascii")
        kept.append(
            re.sub(
                r"url\(https://[^)]+\)",
                f"url(data:font/woff2;base64,{data})",
                block,
            )
        )
    if not kept:
        raise SystemExit("no @font-face blocks matched — Google Fonts response changed?")
    print(f"  fonts: {len(kept)} faces embedded")
    return "\n".join(kept)


def main() -> None:
    html = SRC.read_text(encoding="utf-8")

    # 1. fonts: swap the stylesheet <link> for embedded @font-face rules
    faces = inline_fonts()
    html = re.sub(
        r'<link rel="preconnect"[^>]*>\s*'
        r'<link rel="preconnect"[^>]*crossorigin>\s*'
        r'<link href="https://fonts\.googleapis\.com[^>]*>',
        "<style>\n" + faces + "\n</style>",
        html,
        count=1,
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
