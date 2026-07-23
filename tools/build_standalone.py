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
# Only the subsets Polish and English need; devanagari would double the size.
KEEP_SUBSETS = ("latin", "latin-ext")
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"


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
        url = re.search(r"url\((https://[^)]+)\)", block).group(1)
        data = base64.b64encode(fetch(url)).decode("ascii")
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

    # 2. drawings: figs/*.webp -> data URIs
    used = set(re.findall(r'src="figs/([^"]+)"', html))
    for name in sorted(used):
        blob = (FIGS / name).read_bytes()
        uri = "data:image/webp;base64," + base64.b64encode(blob).decode("ascii")
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
