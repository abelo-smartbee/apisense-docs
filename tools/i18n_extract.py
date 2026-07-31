#!/usr/bin/env python3
"""Dump every translatable group of docs/assembly/index.html to JSON.

    python3 tools/i18n_extract.py                  # -> tools/i18n/_source.json

The result is the brief a translator works from: one entry per group, carrying
the locales that already exist. Translating means writing `tools/i18n/<loc>.json`
— a flat `{group id: text}` map over the same ids — which `i18n_inject.py` then
folds back into the HTML.

Going through JSON is what lets four languages be translated at once: each one
owns its own file, so nothing merges into the same 100 kB HTML twice.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from i18n_lib import LOCALE_ORDER, parse  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "docs" / "assembly" / "index.html"
OUT = ROOT / "tools" / "i18n" / "_source.json"


def main() -> None:
    html = SRC.read_text(encoding="utf-8")
    groups = parse(html)

    entries = []
    for g in groups:
        by = g.by_locale
        entries.append(
            {
                "id": g.id,
                "line": g.line,
                "tag": g.elements[0].tag,
                "text": {loc: by[loc].inner for loc in LOCALE_ORDER if loc in by},
            }
        )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(
        json.dumps(entries, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    ids = {e["id"] for e in entries}
    print(f"  {len(entries)} groups, {len(ids)} distinct ids  → {OUT.relative_to(ROOT)}")
    if len(ids) != len(entries):
        print("  (duplicate ids are identical PL+EN sentences — one translation serves both)")


if __name__ == "__main__":
    sys.exit(main())
