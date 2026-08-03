#!/usr/bin/env python3
"""Guard the image-filename contract between this repo and the screenshot suite.

    python3 tools/check_image_refs.py                  # missing files only
    python3 tools/check_image_refs.py --against main   # + what this branch renamed/dropped

Screenshots under `docs/manual/pictures/` are not authored here. They are
captured on a CI emulator in `apisense-mobile` (`.github/workflows/screenshots.yml`)
and land as a PR against this repo. That pipeline keys its shots by **image file
stem** through `integration_test/screenshots/manifest.yaml`.

The consequence is easy to miss while editing prose: renaming an image, or
dropping the last reference to one, does not break the site — mkdocs is happy,
the page still renders, nothing goes red. It breaks the *next* screenshot sync,
in the other repo, days later, as a shot that suddenly has nowhere to land.

So a docs branch that reorganises chapters may move image references around
freely, but the set of referenced filenames is a contract with a pipeline that
cannot see this branch. This script makes a change to that set visible while it
is still a diff.

Two checks:

- **missing** — a referenced image that does not exist on disk. Always an error.
- **dropped** (with `--against`) — a filename referenced on the ref but on no
  page here. Usually a rename, which is the contract break. Reported as an error;
  if the removal is deliberate (a screenshot genuinely retired), say so in the PR
  and pair it with the manifest change on the mobile side.

Newly referenced filenames are printed but never fail: adding a reference is how
a new screenshot gets adopted.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

# ![alt](path) — the manual's images are all plain markdown, no HTML <img>.
RE_IMAGE = re.compile(r"!\[[^\]]*\]\(([^)\s]+)\)")
# Rows parked in an HTML comment are not references. The manual carries at least
# one such block (`beehive_details_humidity_risk.png`, waiting on the asset), and
# counting it reports a missing file that nothing actually renders.
RE_HTML_COMMENT = re.compile(r"<!--.*?-->", re.DOTALL)

DOCS_DIR = "docs"


def image_refs(text: str) -> set[str]:
    """Referenced image paths, ignoring the `{width=200}` attr suffix mkdocs allows."""
    live = RE_HTML_COMMENT.sub("", text)
    return {ref.split("{")[0] for ref in RE_IMAGE.findall(live) if not ref.startswith("http")}


def refs_by_page(pages: dict[str, str]) -> dict[str, set[str]]:
    return {path: image_refs(text) for path, text in pages.items()}


def filenames(by_page: dict[str, set[str]]) -> set[str]:
    """Flatten to bare filenames — the manifest keys by stem, not by path."""
    return {Path(ref).name for refs in by_page.values() for ref in refs}


def pages_from_worktree() -> dict[str, str]:
    return {
        p.as_posix(): p.read_text(encoding="utf-8")
        for p in sorted(Path(DOCS_DIR).rglob("*.md"))
    }


def pages_from_ref(ref: str) -> dict[str, str]:
    listing = subprocess.run(
        ["git", "ls-tree", "-r", "--name-only", ref, "--", DOCS_DIR],
        capture_output=True, text=True, check=True,
    )
    pages = {}
    for path in listing.stdout.splitlines():
        if path.endswith(".md"):
            blob = subprocess.run(
                ["git", "show", f"{ref}:{path}"], capture_output=True, text=True, check=True
            )
            pages[path] = blob.stdout
    return pages


def missing_files(by_page: dict[str, set[str]]) -> list[str]:
    missing = []
    for page, refs in by_page.items():
        for ref in refs:
            if not (Path(page).parent / ref).exists():
                missing.append(f"{page}: {ref}")
    return sorted(missing)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument(
        "--against",
        metavar="REF",
        help="also report filenames referenced on REF but no longer referenced here",
    )
    args = parser.parse_args()

    current = refs_by_page(pages_from_worktree())
    failed = False

    if missing := missing_files(current):
        failed = True
        print(f"Referenced but not on disk ({len(missing)}):")
        for entry in missing:
            print(f"  {entry}")

    if args.against:
        before = filenames(refs_by_page(pages_from_ref(args.against)))
        after = filenames(current)

        if dropped := sorted(before - after):
            failed = True
            print(f"\nNo longer referenced — renamed or removed ({len(dropped)}):")
            for name in dropped:
                print(f"  {name}")
            print("  ^ breaks the screenshot-suite contract unless the mobile "
                  "manifest changes with it")

        if added := sorted(after - before):
            print(f"\nNewly referenced ({len(added)}) — fine, just confirm the files exist:")
            for name in added:
                print(f"  {name}")

        if not dropped and not missing:
            print(f"Image filename set unchanged relative to {args.against} "
                  f"({len(after)} referenced).")
    elif not missing:
        print(f"All referenced images present "
              f"({len(filenames(current))} distinct filenames).")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
