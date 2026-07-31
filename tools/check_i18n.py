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
import re
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
DEFAULT_LOCALES = (
    "pl", "en", "de", "fr", "es", "it", "no", "tr",
    "cs", "sk", "hu", "hr", "ro", "fi", "nl", "sv", "da",
)

# How many incomplete groups to name before summarising the rest. A locale
# that has not been started yet would otherwise print one line per group and
# bury the summary.
DEFAULT_LIMIT = 20


# The page names its locales in four independent places, and a locale present in
# some but not others fails as quietly as a missing span: in the CSS but not in
# the <option>s is a locale nobody can reach, in the <option>s but not the CSS is
# an entry that shows every language at once, in the <option>s but not HEAD_TEXT
# is a Polish <title> on a Turkish page. Nothing enforces agreement, so this does.
#
# There were five lists until the pills went away — the switcher is one <select>
# now, so `data-set-lang` no longer exists anywhere on the page. Dropping the
# list costs nothing: the pills were never the only reachability signal, and a
# locale missing from any surviving one is still caught here.
SWITCHER_LISTS = {
    "reguły CSS": re.compile(r'\[data-lang="([a-z]{2})"\] \[lang\]'),
    "allowlist w <head>": re.compile(r"'([a-z]{2})'(?=[,\]])"),
    "<option>": re.compile(r'<option value="([a-z]{2})"'),
    "HEAD_TEXT": re.compile(r"^\s{4}([a-z]{2}): \{$", re.M),
}


def switcher_locales(html: str) -> dict[str, set[str]]:
    """What each of the lists thinks the supported locales are."""
    found = {}
    for name, pattern in SWITCHER_LISTS.items():
        hits = {loc for loc in pattern.findall(html) if loc in LOCALE_ORDER}
        found[name] = hits
    return found


def check_switcher(html: str, locales: list[str]) -> list[str]:
    """Complaints about the lists — empty when they all agree."""
    found = switcher_locales(html)
    problems = []
    for name, hits in found.items():
        # A pattern that matches nothing at all means the markup moved out from
        # under it, not that the page lost every locale. Say so, otherwise the
        # check quietly turns into a no-op the day someone rewrites the header.
        if not hits:
            problems.append(f"{name}: wzorzec nie znalazł ani jednego locale")
            continue
        if missing := [loc for loc in locales if loc not in hits]:
            problems.append(f"{name}: brak {', '.join(missing)}")
    # Also catch the reverse — a locale wired into the page that nobody translated.
    reachable = set().union(*found.values())
    if extra := sorted(reachable - set(locales)):
        problems.append(
            f"locale osiągalne w przełączniku, ale nieuznane za gotowe: {', '.join(extra)}"
        )
    return problems


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

    html = path.read_text(encoding="utf-8")
    groups = parse(html)
    gaps = [(g, missing) for g in groups if (missing := g.missing(locales))]
    switcher = check_switcher(html, locales)

    print(f"  {path}")
    print(f"  {len(groups)} grup  ·  locale: {', '.join(locales)}")

    if switcher:
        print()
        for problem in switcher:
            print(f"  przełącznik — {problem}")

    if not gaps and not switcher:
        print("  OK: komplet we wszystkich grupach, przełącznik spójny")
        return 0
    if not gaps:
        print()
        print(f"  BŁĄD: grupy kompletne, ale przełącznik rozjechany ({len(switcher)})")
        return 1

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
