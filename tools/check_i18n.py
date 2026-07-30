#!/usr/bin/env python3
"""Fail loudly when a locale is missing from any group of the assembly page.

    python3 tools/check_i18n.py                          # DEFAULT_LOCALES
    python3 tools/check_i18n.py --locales pl,en,de,fr,es
    python3 tools/check_i18n.py /tmp/index.html          # any other copy

The stylesheet of `docs/assembly/index.html` hides every `[lang]` that is not
the one the reader picked, and there is no fallback rule behind it:

    [data-lang="es"] [lang]:not([lang="es"]) { display: none; }

So a group that never got its `<span lang="es">` does not fall back to English
— it renders as nothing at all. No error, no warning, just a sentence that
silently vanishes for that language. Same for a span that exists but is empty.
Across 150 groups and eight locales that is only findable mechanically, which
is what this script is.

What counts as a group comes from `i18n_lib`, shared with `i18n_extract.py`
and `i18n_inject.py`. The validator must agree with the tools whose output it
is checking; a second parser here would only invent a second opinion.
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from i18n_lib import LOCALE_ORDER, parse  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "docs" / "assembly" / "index.html"

# Locales considered *done* — the ones a reader can already switch to, and so
# the ones every group must carry. This list is the whole point of the script
# being parameterised: while a language is being translated it stays out, and
# it is added here in the same commit that lands its translation. `i18n_lib`
# deliberately holds only the canonical order, never the done-ness.
DEFAULT_LOCALES = ("pl", "en", "de", "fr")

# How many incomplete groups to name before summarising the rest. A locale
# that has not been started yet would otherwise print one line per group and
# bury the summary.
DEFAULT_LIMIT = 20


def resolve(spec: str) -> list[str]:
    """`"pl,en, de"` -> `["pl", "en", "de"]`, in canonical order."""
    wanted = [part.strip() for part in spec.split(",") if part.strip()]
    if not wanted:
        raise SystemExit("--locales: pusta lista")
    unknown = [loc for loc in wanted if loc not in LOCALE_ORDER]
    if unknown:
        raise SystemExit(
            f"nieznane locale: {', '.join(unknown)}"
            f" (znane: {', '.join(LOCALE_ORDER)})"
        )
    return [loc for loc in LOCALE_ORDER if loc in wanted]


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(
        description="Sprawdza, czy każda grupa ma wszystkie gotowe locale."
    )
    ap.add_argument(
        "path",
        nargs="?",
        default=str(SRC),
        help=f"plik HTML do sprawdzenia (domyślnie {SRC.relative_to(ROOT)})",
    )
    ap.add_argument(
        "--locales",
        default=",".join(DEFAULT_LOCALES),
        help=f"locale uznane za gotowe (domyślnie {','.join(DEFAULT_LOCALES)})",
    )
    ap.add_argument(
        "--limit",
        type=int,
        default=DEFAULT_LIMIT,
        help=f"ile niekompletnych grup wypisać, 0 = wszystkie (domyślnie {DEFAULT_LIMIT})",
    )
    args = ap.parse_args(argv)

    locales = resolve(args.locales)
    path = Path(args.path)
    if not path.is_file():
        raise SystemExit(f"brak pliku: {path}")

    groups = parse(path.read_text(encoding="utf-8"))
    gaps = [(g, missing) for g in groups if (missing := g.missing(locales))]

    print(f"  {path}")
    print(f"  {len(groups)} grup  ·  locale: {', '.join(locales)}")

    if not gaps:
        print("  OK: komplet we wszystkich grupach")
        return 0

    shown = gaps if args.limit <= 0 else gaps[: args.limit]
    print()
    for group, missing in shown:
        brak = ", ".join(missing)
        print(f"  linia {group.line:>5}   brak: {brak:<14} {group.preview()}")
    if len(shown) < len(gaps):
        print(f"  … i jeszcze {len(gaps) - len(shown)} niekompletnych grup")

    per_locale = Counter(loc for _, missing in gaps for loc in missing)
    counts = ", ".join(f"{loc} {per_locale[loc]}" for loc in locales if per_locale[loc])
    print()
    print(f"  braki per locale: {counts}")
    print(f"  BŁĄD: {len(gaps)} z {len(groups)} grup niekompletnych")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
