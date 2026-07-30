#!/usr/bin/env python3
"""Shared parsing for the assembly instruction's inline i18n.

`docs/assembly/index.html` carries every string once per locale, as a run of
sibling elements that each declare `lang`:

    <h2>
      <span lang="pl">Montaż wagi</span>
      <span lang="en">Scale assembly</span>
    </h2>

A *group* is one such run — the same sentence in every locale it has been
translated into. Groups are what the validator counts and what the extractor
and injector address, so all three agree on one definition, kept here.

Group identity is the SHA-1 of the Polish and English text, not the position
in the file. Positions move whenever a step is inserted; the source sentence
does not. Two groups that say exactly the same thing in PL and EN share an id
on purpose — they want the same translation.
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field

# Canonical span order inside a group. Kept identical everywhere so that the
# diff of each new language reads as an append, not a reshuffle.
# Which of them count as done lives in check_i18n.py — one list, one owner.
LOCALE_ORDER = ("pl", "en", "de", "fr", "es", "it", "no", "tr")

# `(?<![-\w])` and not `\b`: the language switcher's buttons carry
# `data-set-lang="pl"`, which a word boundary happily matches. Those buttons are
# chrome, not content — they must stay visible in every locale.
_OPEN = re.compile(r'<(span|button)\b([^>]*?)(?<![-\w])lang="([a-z]{2})"([^>]*)>', re.I)


@dataclass
class Element:
    """One `<span lang="xx">…</span>` — the locale, its text, and its extent."""

    locale: str
    tag: str
    attrs_before: str
    attrs_after: str
    inner: str
    start: int
    end: int
    line: int


@dataclass
class Group:
    """A run of sibling elements separated by whitespace only."""

    elements: list[Element] = field(default_factory=list)

    @property
    def line(self) -> int:
        return self.elements[0].line

    @property
    def by_locale(self) -> dict[str, Element]:
        return {e.locale: e for e in self.elements}

    @property
    def id(self) -> str:
        by = self.by_locale
        pl = by["pl"].inner.strip() if "pl" in by else ""
        en = by["en"].inner.strip() if "en" in by else ""
        raw = f"{pl}\x00{en}".encode()
        return hashlib.sha1(raw).hexdigest()[:12]

    def preview(self, width: int = 60) -> str:
        by = self.by_locale
        src = by.get("en") or by.get("pl") or self.elements[0]
        text = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", src.inner)).strip()
        return text[:width] + ("…" if len(text) > width else "")

    def missing(self, locales) -> list[str]:
        by = self.by_locale
        return [
            loc
            for loc in locales
            # An empty span hides just as silently as an absent one.
            if loc not in by or not by[loc].inner.strip()
        ]


def _close(html: str, tag: str, after_open: int) -> int:
    """End offset of the element whose opening tag ended at `after_open`.

    Walks forward counting nested tags of the same name, so a `<span>` inside a
    translated string does not end the element early.
    """
    depth = 1
    pos = after_open
    pattern = re.compile(rf"<(/?){tag}\b", re.I)
    while depth:
        m = pattern.search(html, pos)
        if not m:
            raise ValueError(f"unterminated <{tag}> at offset {after_open}")
        depth += -1 if m.group(1) else 1
        pos = html.index(">", m.end()) + 1
    return pos


def parse(html: str) -> list[Group]:
    """Every group in document order."""
    elements: list[Element] = []
    pos = 0
    while (m := _OPEN.search(html, pos)) is not None:
        tag = m.group(1)
        end = _close(html, tag, m.end())
        inner_end = html.rindex(f"</{tag}", m.end(), end)
        elements.append(
            Element(
                locale=m.group(3),
                tag=tag,
                attrs_before=m.group(2),
                attrs_after=m.group(4),
                inner=html[m.end() : inner_end],
                start=m.start(),
                end=end,
                line=html.count("\n", 0, m.start()) + 1,
            )
        )
        pos = end

    groups: list[Group] = []
    current = Group()
    for el in elements:
        if current.elements:
            gap = html[current.elements[-1].end : el.start]
            adjacent = gap.strip() == ""
            fresh = el.locale in current.by_locale
            # A repeated locale means the previous run ended and a new one began
            # even where no markup separates them.
            if not adjacent or fresh:
                groups.append(current)
                current = Group()
        current.elements.append(el)
    if current.elements:
        groups.append(current)
    return groups


def separator(html: str, group: Group) -> str:
    """The whitespace the file already uses between two spans of this group.

    Some groups are one span per line, some are packed onto a single line.
    Reusing what is there keeps the injected language from reformatting the
    file around it.
    """
    if len(group.elements) < 2:
        return ""
    return html[group.elements[-2].end : group.elements[-1].start]
