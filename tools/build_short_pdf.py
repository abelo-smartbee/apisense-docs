#!/usr/bin/env python3
"""Print docs/assembly/short/index.html — the one-sheet quick guide — to PDF, per locale.

    python3 tools/build_short_pdf.py            # all locales
    python3 tools/build_short_pdf.py pl en      # just these
    python3 tools/build_short_pdf.py --check    # fit report only, no PDFs

Output: docs/assembly/pdf/short/ — one file per locale, ASCII names for the
same reason build_pdf.py uses them (these travel as e-mail attachments and go
to the print shop).

The page is fixed at one A4 landscape sheet with `overflow: hidden`, so a
locale that runs long does not spill onto a second page — it is clipped, and
`Pages: 1` proves nothing. The page therefore reports every box its content no
longer fits in as `data-overflow` on <html> once loaded; this script reads that
attribute with `--dump-dom` before printing and refuses a locale that overflows.
Fix by shrinking that locale's `.sheet` font-size in the page's last style rule.
"""

from __future__ import annotations

import re
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pdf_lib import check_names, compress, find_chrome, rtl_locales, size_note  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "docs" / "assembly" / "short" / "index.html"
OUT_DIR = ROOT / "docs" / "assembly" / "pdf" / "short"

# Locale → file name, in the locale's own language, ASCII only. `cs` and `sk`
# share a bare stem (Stručný návod / Stručný návod) — the suffix keeps them apart.
LOCALES = {
    "pl": "Apisense_BOX_Instrukcja_skrocona_pl.pdf",
    "en": "Apisense_BOX_Quick_guide_en.pdf",
    "de": "Apisense_BOX_Kurzanleitung_de.pdf",
    "fr": "Apisense_BOX_Guide_rapide_fr.pdf",
    "es": "Apisense_BOX_Guia_rapida_es.pdf",
    "it": "Apisense_BOX_Guida_rapida_it.pdf",
    "no": "Apisense_BOX_Hurtigveiledning_no.pdf",
    "tr": "Apisense_BOX_Hizli_kilavuz_tr.pdf",
    "cs": "Apisense_BOX_Strucny_navod_cs.pdf",
    "sk": "Apisense_BOX_Strucny_navod_sk.pdf",
    "hu": "Apisense_BOX_Rovid_utmutato_hu.pdf",
    "hr": "Apisense_BOX_Kratke_upute_hr.pdf",
    "ro": "Apisense_BOX_Ghid_rapid_ro.pdf",
    "fi": "Apisense_BOX_Pikaohje_fi.pdf",
    "nl": "Apisense_BOX_Beknopte_handleiding_nl.pdf",
    "sv": "Apisense_BOX_Snabbguide_sv.pdf",
    "da": "Apisense_BOX_Kort_vejledning_da.pdf",
    "pt": "Apisense_BOX_Guia_rapido_pt.pdf",
    "el": "Apisense_BOX_Syntomos_odigos_el.pdf",
    "ar": "Apisense_BOX_Al-dalil_al-mukhtasar_ar.pdf",
}

ROOT_TAG = '<html lang="pl" data-lang="pl" dir="ltr">'
CHROME_FLAGS = ["--headless=new", "--disable-gpu", "--no-sandbox", "--allow-file-access-from-files",
                "--virtual-time-budget=15000", "--window-size=1400,1000"]


def localized(html: str, loc: str, rtl: set[str]) -> str:
    """The page with its locale preset on <html>, the way the deck's build_pdf.py does it."""
    if ROOT_TAG not in html:
        raise SystemExit(f"nie znaleziono {ROOT_TAG} — bez tego każdy PDF wyszedłby po polsku")
    return html.replace(
        ROOT_TAG,
        f'<html lang="{loc}" data-lang="{loc}" dir="{"rtl" if loc in rtl else "ltr"}">',
    )


def overflow(chrome: str, src: Path) -> str:
    """The page's own fit report: empty when every box holds its content."""
    dom = subprocess.run(
        [chrome, *CHROME_FLAGS, "--dump-dom", src.as_uri()],
        check=True, capture_output=True, text=True,
    ).stdout
    match = re.search(r'data-overflow="([^"]*)"', dom)
    if match is None:
        raise SystemExit("strona nie zgłosiła data-overflow — sprawdź skrypt na końcu short/index.html")
    return match.group(1)


def main(argv: list[str]) -> int:
    flags = [a for a in argv if a.startswith("--")]
    unknown_flags = [f for f in flags if f != "--check"]
    if unknown_flags:
        # A typo here must not degrade into a full twenty-file build.
        raise SystemExit(f"nieznana opcja: {', '.join(unknown_flags)} (dostępna: --check)")
    check_only = "--check" in flags
    locales = [a for a in argv if not a.startswith("--")] or list(LOCALES)
    unknown = [l for l in locales if l not in LOCALES]
    if unknown:
        raise SystemExit(f"nieznane locale: {', '.join(unknown)} (dostępne: {', '.join(LOCALES)})")

    for stem, locs in check_names(LOCALES):
        print(f"  uwaga: {stem} to nazwa wspólna dla {', '.join(locs)} — rozróżnia je sufiks locale")

    chrome = find_chrome()
    html = SRC.read_text(encoding="utf-8")
    rtl = rtl_locales(html, "docs/assembly/short/index.html")
    if not check_only:
        OUT_DIR.mkdir(parents=True, exist_ok=True)

    failed = []
    # The temp copy sits in the same directory as the source — not a temp
    # subdirectory — so the page's ../figs/ references keep resolving. In a
    # subdirectory they would point at short/figs/, which does not exist, and
    # Chrome would print every figure as blank without a word of complaint.
    for loc in locales:
        with tempfile.NamedTemporaryFile("w", dir=SRC.parent, prefix=f".{loc}-", suffix=".html",
                                         encoding="utf-8", delete=False) as fh:
            fh.write(localized(html, loc, rtl))
            src = Path(fh.name)
        try:
            bad = overflow(chrome, src)
            if bad:
                failed.append(loc)
                print(f"  {loc}  NIE MIEŚCI SIĘ: {bad}")
                continue
            if check_only:
                print(f"  {loc}  mieści się")
                continue
            out = OUT_DIR / LOCALES[loc]
            subprocess.run(
                [chrome, *CHROME_FLAGS, "--no-pdf-header-footer", f"--print-to-pdf={out}", src.as_uri()],
                check=True, capture_output=True,
            )
            raw = out.stat().st_size / 1_048_576
            print(f"  {loc}  → {out.relative_to(ROOT)}  ({size_note(raw, compress(out))})")
        finally:
            src.unlink(missing_ok=True)

    if failed:
        print(f"\nBŁĄD: treść nie mieści się na jednej stronie w: {', '.join(failed)}"
              " — zmniejsz font-size .sheet dla tych locale w short/index.html")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
