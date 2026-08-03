#!/usr/bin/env python3
"""Validate in-page anchor links across `docs/`, differentially against a git ref.

    python3 tools/check_anchors.py                  # every broken link (noisy)
    python3 tools/check_anchors.py --against main   # only links THIS branch broke
    python3 tools/check_anchors.py --against main --quiet

`mkdocs build --strict` does not fail on a dangling in-page anchor — it reports
it at INFO level and builds anyway (verified: a build carrying three of them
still exits 0). So a link like `[…](#42-przeglad)` that no longer matches any
heading ships silently. This script is the gate that the build is not, and it
agrees finding-for-finding with what mkdocs logs.

`--against REF` computes the same set on a git ref and prints only what got
worse. Use it on a branch that reorganises headings: it lets pre-existing
breakage stay pre-existing instead of drowning the diff you care about.

`--against` reads the ref through `git show` and never touches the working tree.
That is deliberate. The obvious implementation — stash, checkout, compare, pop —
will happily pop somebody else's older stash when the tree happens to be clean,
which is a good way to lose unrelated work.

## What counts as an anchor

Three sources, because the manual uses all three. Each of the three has already
produced a wave of phantom findings when modelled too narrowly, so the shape of
these patterns is load-bearing:

- headings, slugified the way python-markdown's `toc` extension does it
  (NFKD → ASCII, strip non-word, lowercase, spaces → dashes). Note this drops
  `ł` entirely (no canonical decomposition), so `## Wysyłka` is `#wysyka`.
- explicit `id="…"` on **any** tag, not just `<a>`. The video embeds are
  `<div class="yt-embed" id="wideo-…">`, and matching only `<a id="` reports
  every one of them as broken.
- attr_list ids, which here are frequently non-ASCII and may sit in a padded
  or multi-attribute block: `{#fig-hub}`, `{#wysyłka}`, `{ #foulbrood-exception }`

## What it deliberately does NOT do

It does not resolve links into `docs/assembly/*.html` (hand-written pages
outside the mkdocs page graph) and it does not check external URLs.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

RE_HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
# Any tag, not just <a> — see module docstring.
RE_EXPLICIT_ID = re.compile(r'\bid="([^"]+)"')
# attr_list blocks, and the ids inside them. Both spellings occur in this repo
# and a stricter pattern turns real anchors into phantom breakage:
#   `{#fig-hub}` `{#wysyłka}` `{ #foulbrood-exception }`
# So: ids may be non-ASCII, and the braces may carry padding or other attributes.
RE_ATTR_BLOCK = re.compile(r"\{[^}\n]*\}")
RE_ATTR_ID = re.compile(r"#([^\s}]+)")
RE_MD_LINK = re.compile(r"\]\(([^)\s]+)\)")
RE_INLINE_MARKUP = re.compile(r"[*_`]")
# Content parked in an HTML comment neither renders nor defines an anchor.
RE_HTML_COMMENT = re.compile(r"<!--.*?-->", re.DOTALL)

DOCS_DIR = "docs"


def slugify(value: str, separator: str = "-") -> str:
    """Reimplementation of `markdown.extensions.toc.slugify` (unicode → ascii)."""
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    value = re.sub(r"[^\w\s-]", "", value).strip().lower()
    return re.sub(rf"[{separator}\s]+", separator, value)


def attr_list_ids(line: str) -> set[str]:
    return {
        anchor
        for block in RE_ATTR_BLOCK.findall(line)
        for anchor in RE_ATTR_ID.findall(block)
    }


def anchors_of(text: str) -> set[str]:
    found: set[str] = set()
    for line in RE_HTML_COMMENT.sub("", text).split("\n"):
        if heading := RE_HEADING.match(line):
            title = RE_ATTR_BLOCK.sub("", heading.group(2))
            found.add(slugify(RE_INLINE_MARKUP.sub("", title)))
        found |= set(RE_EXPLICIT_ID.findall(line))
        found |= attr_list_ids(line)
    return found


def locale_suffix(path: str) -> str:
    """`.pl` / `.en` for the i18n suffix layout; a link to `x.md` resolves per locale."""
    return ".pl" if path.endswith(".pl.md") else ".en"


def resolve_target(source: str, page: str) -> str:
    """Resolve a relative link target to a repo-relative path, applying the locale suffix."""
    base = (Path(source).parent / page).as_posix()
    normalised = Path(base).resolve().relative_to(Path.cwd().resolve()).as_posix()
    stem = normalised[: -len(".md")] if normalised.endswith(".md") else normalised
    return f"{stem}{locale_suffix(source)}.md"


def broken_links(pages: dict[str, str]) -> set[str]:
    """`{"path: target -> reason"}` for every in-page link that resolves to nothing."""
    anchors = {path: anchors_of(text) for path, text in pages.items()}
    broken: set[str] = set()

    for path, text in pages.items():
        for target in RE_MD_LINK.findall(RE_HTML_COMMENT.sub("", text)):
            if target.startswith("http") or "#" not in target:
                continue
            page, _, fragment = target.partition("#")
            if not fragment:
                continue
            if page == "":
                destination = path
            else:
                destination = resolve_target(path, page)
                if destination not in anchors:
                    broken.add(f"{path}: {target} -> no such page")
                    continue
            if fragment not in anchors[destination]:
                broken.add(f"{path}: {target} -> no such anchor")
    return broken


def pages_from_worktree() -> dict[str, str]:
    return {
        p.as_posix(): p.read_text(encoding="utf-8")
        for p in sorted(Path(DOCS_DIR).rglob("*.md"))
    }


def pages_from_ref(ref: str) -> dict[str, str]:
    """Read the ref's `docs/**/*.md` through git, leaving the working tree alone."""
    listing = subprocess.run(
        ["git", "ls-tree", "-r", "--name-only", ref, "--", DOCS_DIR],
        capture_output=True, text=True, check=True,
    )
    pages = {}
    for path in listing.stdout.splitlines():
        if not path.endswith(".md"):
            continue
        blob = subprocess.run(
            ["git", "show", f"{ref}:{path}"], capture_output=True, text=True, check=True
        )
        pages[path] = blob.stdout
    return pages


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument(
        "--against",
        metavar="REF",
        help="report only links broken relative to this git ref (e.g. main)",
    )
    parser.add_argument("--quiet", action="store_true", help="print counts, not every link")
    args = parser.parse_args()

    current = broken_links(pages_from_worktree())

    if not args.against:
        for entry in sorted(current):
            print(entry)
        print(f"\n{len(current)} broken link(s) — run with --against main to see only new ones")
        return 1 if current else 0

    baseline = broken_links(pages_from_ref(args.against))
    introduced = current - baseline
    fixed = baseline - current

    if introduced:
        print(f"Broken by this branch ({len(introduced)}):")
        for entry in sorted(introduced):
            print(f"  {entry}")
    if fixed and not args.quiet:
        print(f"\nFixed relative to {args.against} ({len(fixed)}):")
        for entry in sorted(fixed):
            print(f"  {entry}")
    if not introduced:
        print(f"No new breakage relative to {args.against} "
              f"({len(current)} broken link(s) still in the branch).")
    return 1 if introduced else 0


if __name__ == "__main__":
    sys.exit(main())
