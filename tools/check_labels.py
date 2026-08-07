#!/usr/bin/env python3
"""Sprawdza etykiety UI instrukcji montażu przeciw ARB aplikacji mobilnej.

Deck cytuje etykiety aplikacji w <em>/<b>. Reguła locale (dev-docs/
grafiki-assembly.md, "Teksty i języki"):

  - 8 locale aplikacji (de en es fr it no pl tr) — etykieta wzięta wprost
    z app_<locale>.arb,
  - pozostałe 12 — etykieta ANGIELSKA, bo aplikacja pokazuje im angielski
    fallback,
  - nazwy własne bez tłumaczenia wszędzie.

Kotwicą jest angielski span grupy: pogrubienie, które jest wartością z
app_en.arb, to etykieta UI — wtedy każde locale musi nieść właściwy wariant.
Pogrubienia akcentowe (nie-ARB) nie podlegają kontroli.

Zastrzeżenie z dev-docs/audyt-instrukcji.md obowiązuje: wartość w ARB nie
dowodzi, że etykieta jest wyrenderowana — rozjazd ARB↔deck to sygnał do
sprawdzenia na zrzucie, nie automatyczna poprawka w ciemno.

    python3 tools/check_labels.py            # exit 1 przy rozjazdach
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HTML = ROOT / "docs/assembly/index.html"
ARB_DIR = ROOT.parent / "apisense-mobile/packages/apisense_core/l10n"
APP = ["de", "en", "es", "fr", "it", "no", "pl", "tr"]
ALL = ["pl", "en", "de", "fr", "es", "it", "no", "tr", "cs", "sk", "hu",
       "hr", "ro", "fi", "nl", "sv", "da", "pt", "el", "ar"]
BRANDS = {"Hub", "ColonyLink", "VitalSensor", "Scale", "NFC", "Apisense Pro AI",
          "Apisense Tag", "Apisense", "Apisense BOX", "App Store", "Google Play",
          "PDF", "QR"}


def main() -> int:
    if not ARB_DIR.is_dir():
        print(f"pominięto: brak {ARB_DIR} (repo apisense-mobile nie jest sklonowane obok)")
        return 0

    key2val: dict[str, dict[str, str]] = {}
    for loc in APP:
        data = json.loads((ARB_DIR / f"app_{loc}.arb").read_text(encoding="utf-8"))
        key2val[loc] = {k: v.strip() for k, v in data.items()
                        if isinstance(v, str) and not k.startswith("@")}
    en_v2k: dict[str, str] = {}
    for k, v in key2val["en"].items():
        en_v2k.setdefault(v, k)

    html = HTML.read_text(encoding="utf-8")
    # grupy = przebiegi kolejnych spanów językowych; nowa grupa, gdy locale
    # się powtarza (ten sam parser co tools/check_i18n.py)
    tokens = re.findall(r'<span lang="(\w+)"[^>]*>((?:(?!</span>).)*)</span>', html, re.S)
    groups: list[dict[str, str]] = []
    cur: dict[str, str] = {}
    for loc, body in tokens:
        if loc in cur:
            groups.append(cur)
            cur = {}
        cur[loc] = body
    if cur:
        groups.append(cur)

    def labels(body: str) -> list[str]:
        out = []
        for m in re.finditer(r"<(b|i|em|strong)>(.*?)</\1>", body, re.S):
            t = re.sub(r"<[^>]+>", "", m.group(2)).strip()
            out.append(re.sub(r"\s+", " ", t))
        return out

    def clean(t: str) -> str:
        return t.rstrip(".,:;!").strip()

    bad: list[str] = []
    checked = set()
    for gi, g in enumerate(groups):
        if "en" not in g:
            continue
        for en_lab in labels(g["en"]):
            core = clean(en_lab)
            if core in BRANDS:
                continue
            key = en_v2k.get(core)
            if key is None:
                continue
            checked.add(key)
            for loc in ALL:
                if loc == "en" or loc not in g:
                    continue
                have = [clean(x) for x in labels(g[loc])]
                want = clean(key2val[loc].get(key, "")) if loc in APP else core
                if want and want not in have:
                    bad.append(f"grupa {gi} · {loc} · [{key}]: "
                               f"oczekiwane {want!r}, w decku {have}")

    print(f"  {len(checked)} etykiet UI zakotwiczonych w ARB, "
          f"{len(groups)} grup, {len(ALL)} locale")
    if bad:
        print(f"  ROZJAZDY: {len(bad)}")
        for b in bad:
            print("   ", b)
        return 1
    print("  OK: etykiety zgodne z ARB (8 locale) i z angielskim (12 locale)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
