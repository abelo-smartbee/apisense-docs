#!/usr/bin/env python3
"""Render docs/assembly/index.html into a PDF — one step per page, per locale.

Prints the standalone bundle, so fonts and drawings are already inlined and
Chrome needs no network access.

    python3 tools/build_pdf.py            # all locales
    python3 tools/build_pdf.py pl en      # just these

Output: docs/assembly/pdf/Apisense_BOX_Instrukcja_montazu_<locale>.pdf
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

LOCALES = {
    "pl": "Apisense_BOX_Instrukcja_montazu_pl.pdf",
    "en": "Apisense_BOX_Assembly_Instruction_en.pdf",
    "de": "Apisense_BOX_Montageanleitung_de.pdf",
    "fr": "Apisense_BOX_Guide_de_montage_fr.pdf",
    # File names stay ASCII — they travel as e-mail attachments.
    "es": "Apisense_BOX_Instrucciones_de_montaje_es.pdf",
    "it": "Apisense_BOX_Istruzioni_di_montaggio_it.pdf",
    "no": "Apisense_BOX_Monteringsanvisning_no.pdf",
    "tr": "Apisense_BOX_Montaj_Talimati_tr.pdf",
}

CHROME_CANDIDATES = ["google-chrome", "google-chrome-stable", "chromium", "chromium-browser"]

# The deck reveals itself on scroll; print needs every slide already settled.
FREEZE = """
<style id="print-freeze">
  .col--text > *, .plate, .item, .ghost { opacity: 1 !important; transform: none !important; }
  .plate img { clip-path: none !important; }
</style>
"""


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
    locales = argv or list(LOCALES)
    unknown = [l for l in locales if l not in LOCALES]
    if unknown:
        raise SystemExit(f"nieznane locale: {', '.join(unknown)} (dostępne: {', '.join(LOCALES)})")

    if not STANDALONE.exists():
        print("brak wersji standalone — buduję")
        subprocess.run([sys.executable, str(BUILD_STANDALONE)], check=True)

    chrome = find_chrome()
    html = STANDALONE.read_text(encoding="utf-8")
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory() as tmp:
        for loc in locales:
            page = html.replace(
                '<html lang="pl" data-lang="pl">',
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
