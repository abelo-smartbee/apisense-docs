#!/usr/bin/env python3
"""Render docs/assembly/index.html into a PDF — one step per page, per locale.

Prints the standalone bundle, so fonts and drawings are already inlined and
Chrome needs no network access.

    python3 tools/build_pdf.py            # all locales
    python3 tools/build_pdf.py pl en      # just these

Output: docs/assembly/pdf/ — one file per locale, named in the locale's own
language (see LOCALES), because these travel as e-mail attachments.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STANDALONE = ROOT / "docs" / "assembly" / "Apisense_BOX_Instrukcja_montazu_standalone.html"
BUILD_STANDALONE = ROOT / "tools" / "build_standalone.py"
OUT_DIR = ROOT / "docs" / "assembly" / "pdf"

# One entry per locale the page can be read in — seventeen, matching
# DEFAULT_LOCALES in tools/check_i18n.py. (The epic talks about twenty; `el` and
# `ar` wait on ADR 0003 — Poppins has no Greek and no Arabic glyphs at all — and
# `pt` on ADR 0004. Neither is scaffolded here: an entry with no translation
# behind it would print a Polish PDF under a Portuguese name.)
#
# Each name is that locale's document title from HEAD_TEXT in
# docs/assembly/index.html, transliterated to plain ASCII: á→a, ž→z, ș→s, ő→o,
# å→a, ø→o, æ→ae. Names stay ASCII because these files travel as e-mail
# attachments, where a diacritic still reaches the recipient as `=?utf-8?...?=`
# or as mojibake often enough to matter.
#
# `tr` keeps `Montaj_Talimati` from the first eight rather than following the
# later HEAD_TEXT wording (`Montaj kılavuzu`) — same meaning, and the file has
# already been sent out under that name.
LOCALES = {
    "pl": "Apisense_BOX_Instrukcja_montazu_pl.pdf",
    "en": "Apisense_BOX_Assembly_Instruction_en.pdf",
    "de": "Apisense_BOX_Montageanleitung_de.pdf",
    "fr": "Apisense_BOX_Guide_de_montage_fr.pdf",
    "es": "Apisense_BOX_Instrucciones_de_montaje_es.pdf",
    "it": "Apisense_BOX_Istruzioni_di_montaggio_it.pdf",
    "no": "Apisense_BOX_Monteringsanvisning_no.pdf",
    "tr": "Apisense_BOX_Montaj_Talimati_tr.pdf",
    "cs": "Apisense_BOX_Navod_k_montazi_cs.pdf",
    "sk": "Apisense_BOX_Navod_na_montaz_sk.pdf",
    "hu": "Apisense_BOX_Szerelesi_utmutato_hu.pdf",
    "hr": "Apisense_BOX_Upute_za_montazu_hr.pdf",
    "ro": "Apisense_BOX_Instructiuni_de_montaj_ro.pdf",
    "fi": "Apisense_BOX_Asennusohje_fi.pdf",
    "nl": "Apisense_BOX_Montagehandleiding_nl.pdf",
    "sv": "Apisense_BOX_Monteringsanvisning_sv.pdf",
    "da": "Apisense_BOX_Monteringsvejledning_da.pdf",
}

CHROME_CANDIDATES = ["google-chrome", "google-chrome-stable", "chromium", "chromium-browser"]

# The deck reveals itself on scroll; print needs every slide already settled.
FREEZE = """
<style id="print-freeze">
  .col--text > *, .plate, .item, .ghost { opacity: 1 !important; transform: none !important; }
  .plate img { clip-path: none !important; }
</style>
"""


def check_names() -> list[tuple[str, list[str]]]:
    """Refuse to print if two locales share a file name; report near-misses.

    Sibling languages name this document almost identically — Norwegian and
    Swedish both call it *Monteringsanvisning*, Czech and Slovak differ by one
    preposition. A duplicate would not error: the second locale would simply
    overwrite the first, leaving a full-looking output directory one file short,
    with one language silently replaced by another. So the full names are
    checked hard.

    Stripping the `_<loc>` suffix is checked too, but only reported — the
    collisions there are real (no/sv) and tolerated. That report is the answer
    to "is the suffix load-bearing?": when it lists anything, it is.
    """
    dupes: dict[str, list[str]] = {}
    for loc, name in LOCALES.items():
        dupes.setdefault(name, []).append(loc)
    clashing = {name: locs for name, locs in dupes.items() if len(locs) > 1}
    if clashing:
        raise SystemExit(
            "kolizja nazw plików PDF — jedno locale nadpisałoby drugie: "
            + "; ".join(f"{name} ← {', '.join(locs)}" for name, locs in clashing.items())
        )

    bare: dict[str, list[str]] = {}
    for loc, name in LOCALES.items():
        stem = name.removesuffix(".pdf").removesuffix(f"_{loc}")
        bare.setdefault(stem, []).append(loc)
    return sorted((stem, locs) for stem, locs in bare.items() if len(locs) > 1)


def find_chrome() -> str:
    for name in CHROME_CANDIDATES:
        path = shutil.which(name)
        if path:
            return path
    raise SystemExit("nie znaleziono Chrome ani Chromium — zainstaluj jedno z: " + ", ".join(CHROME_CANDIDATES))


def compress(pdf: Path) -> float | None:
    """Shrink with Ghostscript. /printer keeps images at 300 dpi — anything
    lower starts to soften the QR codes, which have to stay scannable."""
    gs = shutil.which("gs")
    if not gs:
        return None
    tmp = pdf.with_suffix(".gs.pdf")
    subprocess.run(
        [gs, "-q", "-dNOPAUSE", "-dBATCH", "-sDEVICE=pdfwrite",
         "-dPDFSETTINGS=/printer", "-dCompatibilityLevel=1.5",
         f"-sOutputFile={tmp}", str(pdf)],
        check=True, capture_output=True,
    )
    tmp.replace(pdf)
    return pdf.stat().st_size / 1_048_576


def main(argv: list[str]) -> None:
    shared = check_names()
    for stem, locs in shared:
        print(f"  uwaga: {stem} to nazwa wspólna dla {', '.join(locs)} — rozróżnia je sufiks locale")

    locales = argv or list(LOCALES)
    unknown = [l for l in locales if l not in LOCALES]
    if unknown:
        raise SystemExit(f"nieznane locale: {', '.join(unknown)} (dostępne: {', '.join(LOCALES)})")

    # The bundle is a gitignored local artifact, so a checkout routinely leaves one
    # older than index.html. Printing that would produce seventeen PDFs quietly
    # missing whatever the page gained since — rebuild on stale, not just on absent.
    source = ROOT / "docs" / "assembly" / "index.html"
    if not STANDALONE.exists():
        print("brak wersji standalone — buduję")
        subprocess.run([sys.executable, str(BUILD_STANDALONE)], check=True)
    elif STANDALONE.stat().st_mtime < source.stat().st_mtime:
        print("wersja standalone starsza niż index.html — przebudowuję")
        subprocess.run([sys.executable, str(BUILD_STANDALONE)], check=True)

    chrome = find_chrome()
    html = STANDALONE.read_text(encoding="utf-8")
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # The locale is preset by rewriting this exact string on <html>. If index.html
    # ever spells it differently, the replace would quietly do nothing and every
    # PDF would come out Polish — a wrong-language file looks perfectly fine.
    ROOT_TAG = '<html lang="pl" data-lang="pl">'
    if ROOT_TAG not in html:
        raise SystemExit(
            f"nie znaleziono {ROOT_TAG} w wersji standalone — bez tego wszystkie"
            " PDF-y wyszłyby po polsku; sprawdź <html> w docs/assembly/index.html"
        )

    with tempfile.TemporaryDirectory() as tmp:
        for loc in locales:
            page = html.replace(
                ROOT_TAG,
                f'<html lang="{loc}" data-lang="{loc}" data-theme="light">',
            ).replace("</head>", FREEZE + "</head>")
            src = Path(tmp) / f"{loc}.html"
            src.write_text(page, encoding="utf-8")

            out = OUT_DIR / LOCALES[loc]
            subprocess.run(
                [
                    chrome, "--headless=new", "--disable-gpu", "--no-sandbox",
                    "--no-pdf-header-footer",
                    "--virtual-time-budget=20000",
                    f"--print-to-pdf={out}",
                    src.as_uri(),
                ],
                check=True,
                capture_output=True,
            )
            raw = out.stat().st_size / 1_048_576
            saved = compress(out)
            note = f"{raw:.1f} → {saved:.1f} MB" if saved else f"{raw:.1f} MB, bez kompresji"
            print(f"  {loc}  → {out.relative_to(ROOT)}  ({note})")


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
