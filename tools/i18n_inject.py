#!/usr/bin/env python3
"""Fold translated `tools/i18n/<loc>.json` files back into the assembly HTML.

    python3 tools/i18n_inject.py es it no tr
    python3 tools/i18n_inject.py --check es      # report, write nothing

Each new span goes after the ones already there, so a group ends up in the
canonical order pl, en, de, fr, es, it, no, tr. Re-running is a no-op for a
locale already present — the script never overwrites a hand-edited span, and
a locale you want to redo has to be deleted from the HTML first.

Ids come from `i18n_lib`, which hashes the group's PL and English text. The
same sentence in two places therefore carries one id, and one translation
lands in both.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from i18n_lib import LOCALE_ORDER, Group, parse, separator  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "docs" / "assembly" / "index.html"
I18N = ROOT / "tools" / "i18n"


def load(locale: str) -> dict[str, str]:
    path = I18N / f"{locale}.json"
    if not path.exists():
        raise SystemExit(f"brak {path.relative_to(ROOT)}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise SystemExit(f"{path.name}: oczekiwano obiektu {{id: tekst}}")
    return data


def span(group: Group, locale: str, text: str) -> str:
    model = group.elements[-1]
    return f'<{model.tag} lang="{locale}">{text}</{model.tag}>'


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("locales", nargs="+", help="np. es it no tr")
    ap.add_argument("--check", action="store_true", help="report only, do not write")
    args = ap.parse_args(argv)

    unknown = [l for l in args.locales if l not in LOCALE_ORDER]
    if unknown:
        raise SystemExit(f"nieznane locale: {', '.join(unknown)}")
    # Canonical order, whatever order they were named in.
    locales = [l for l in LOCALE_ORDER if l in args.locales]

    html = SRC.read_text(encoding="utf-8")
    groups = parse(html)
    tables = {loc: load(loc) for loc in locales}

    missing: dict[str, list[Group]] = {loc: [] for loc in locales}
    added = dict.fromkeys(locales, 0)
    skipped = dict.fromkeys(locales, 0)

    # Back to front: every edit shifts the offsets of everything after it.
    for group in reversed(groups):
        present = group.by_locale
        additions = []
        for loc in locales:
            if loc in present and present[loc].inner.strip():
                skipped[loc] += 1
                continue
            text = tables[loc].get(group.id)
            if text is None or not text.strip():
                missing[loc].append(group)
                continue
            additions.append(span(group, loc, text))
            added[loc] += 1
        if not additions:
            continue
        sep = separator(html, group)
        tail = group.elements[-1].end
        html = html[:tail] + sep + sep.join(additions) + html[tail:]

    for loc in locales:
        gaps = len(missing[loc])
        note = f"{added[loc]} dodane, {skipped[loc]} już były"
        if gaps:
            note += f", BRAK {gaps}"
        print(f"  {loc}: {note}")
        for group in missing[loc][:10]:
            print(f"      linia {group.line}  {group.id}  {group.preview()}")
        if gaps > 10:
            print(f"      … i jeszcze {gaps - 10}")

    if any(missing[loc] for loc in locales):
        print("\nniekompletne tłumaczenie — nic nie zapisano")
        return 1
    if args.check:
        print("\n--check: nic nie zapisano")
        return 0

    SRC.write_text(html, encoding="utf-8")
    print(f"\n  → {SRC.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
