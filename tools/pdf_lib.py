#!/usr/bin/env python3
"""Shared pieces of the two PDF printers, build_pdf.py (the deck) and
build_short_pdf.py (the one-sheet quick guide): finding Chrome, reading the
page's own RTL declaration, and the Ghostscript pass. Kept here so the two do
not drift — the same reasoning as i18n_lib.py (ADR 0002)."""

from __future__ import annotations

import re
import shutil
import subprocess
from pathlib import Path

CHROME_CANDIDATES = ["google-chrome", "google-chrome-stable", "chromium", "chromium-browser"]


def find_chrome() -> str:
    for name in CHROME_CANDIDATES:
        path = shutil.which(name)
        if path:
            return path
    raise SystemExit("nie znaleziono Chrome ani Chromium — zainstaluj jedno z: " + ", ".join(CHROME_CANDIDATES))


def rtl_locales(html: str, where: str) -> set[str]:
    """The right-to-left locales, read out of the page instead of copied here.

    A second hand-maintained copy is a copy that drifts, and the failure it
    drifts into is silent: a PDF printed LTR from a mirrored page looks
    perfectly well-typeset to anyone who cannot read the language. So this
    parses `window.APISENSE_RTL` from the markup and refuses to print if the
    declaration is not where it expects. `where` names the file in the error.
    """
    match = re.search(r"window\.APISENSE_RTL\s*=\s*\[([^\]]*)\]", html)
    if match is None:
        raise SystemExit(
            f"nie znaleziono window.APISENSE_RTL w {where} — bez tego"
            " nie wiadomo, które locale drukować od prawej do lewej;"
            " sprawdź skrypt startowy strony"
        )
    return set(re.findall(r"'([a-z]{2})'", match.group(1)))


def check_names(locales: dict[str, str]) -> list[tuple[str, list[str]]]:
    """Refuse to print if two locales share a file name; report near-misses.

    Sibling languages name a document almost identically — Norwegian and
    Swedish both call the deck *Monteringsanvisning*, Czech and Slovak call the
    quick guide *Stručný návod*. A duplicate would not error: the second locale
    would simply overwrite the first, leaving a full-looking output directory
    one file short, with one language silently replaced by another. So the
    full names are checked hard.

    Stripping the `_<loc>` suffix is checked too, but only reported — the
    collisions there are real and tolerated. That report is the answer to
    "is the suffix load-bearing?": when it lists anything, it is.
    """
    dupes: dict[str, list[str]] = {}
    for loc, name in locales.items():
        dupes.setdefault(name, []).append(loc)
    clashing = {name: locs for name, locs in dupes.items() if len(locs) > 1}
    if clashing:
        raise SystemExit(
            "kolizja nazw plików PDF — jedno locale nadpisałoby drugie: "
            + "; ".join(f"{name} ← {', '.join(locs)}" for name, locs in clashing.items())
        )

    bare: dict[str, list[str]] = {}
    for loc, name in locales.items():
        stem = name.removesuffix(".pdf").removesuffix(f"_{loc}")
        bare.setdefault(stem, []).append(loc)
    return sorted((stem, locs) for stem, locs in bare.items() if len(locs) > 1)


def compress(pdf: Path) -> float | None:
    """Shrink with Ghostscript. /printer keeps images at 300 dpi — anything
    lower starts to soften the QR codes, which have to stay scannable.
    Returns the new size in MB, or None when Ghostscript is not installed."""
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


def size_note(raw_mb: float, saved_mb: float | None) -> str:
    return f"{raw_mb:.1f} → {saved_mb:.1f} MB" if saved_mb else f"{raw_mb:.1f} MB, bez kompresji"
