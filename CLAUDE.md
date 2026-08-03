# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

Public Apisense documentation site. MkDocs Material with PL/EN i18n, deployed to GitHub Pages via Actions. Part of the Apisense monorepo — see `../CLAUDE.md` for the broader system map.

## Commands

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

mkdocs serve              # local dev server (http://127.0.0.1:8000)
mkdocs build --strict     # same build CI runs; fails on broken links/refs

python3 tools/check_anchors.py --against main      # in-page anchors
python3 tools/check_image_refs.py --against main   # image-filename contract
```

Run both checkers before opening a PR that moves headings or images. They cover
two gaps the build leaves open: `mkdocs build --strict` reports a dangling
in-page anchor at INFO level and builds anyway, and nothing here notices when an
image is renamed — `apisense-mobile` keys its screenshot suite by image
**filename**, so a rename breaks the next screenshot sync in that repo, days
later, rather than this build.

Deployment is automatic on push to `main` via `.github/workflows/deploy.yml` — no manual publish step.

## Content architecture

i18n uses the **suffix** structure (`mkdocs-static-i18n`): each page is authored as two files side-by-side, `page.pl.md` and `page.en.md`. Plain `page.md` is not used.

- PL is the default locale, served at `/`
- EN is served at `/en/`
- Nav is defined **per-locale** inside `plugins.i18n.languages[].nav` in `mkdocs.yml`. The top-level `nav:` is a fallback — when adding a page, update both locale navs, not just the top-level one.
- Images are shared across locales under `docs/<section>/pictures/` or `docs/assets/`. Reference them with relative paths so both `.pl.md` and `.en.md` resolve correctly.

Current page set: `index`, `overview/index` (system overview — what Apisense is: hardware, app ecosystem, value props), `manual/app-manual` (step-by-step Apisense Pro AI usage guide). When adding a new page, create both `.pl.md` and `.en.md` and add entries under **both** `pl` and `en` navs.

## Style

- `docs/assets/stylesheets/extra.css` is the single custom stylesheet (wired via `extra_css` in `mkdocs.yml`). Prior commits have gone back and forth between heavier and simpler styling — keep customizations minimal unless asked.
- Theme palette: Material `amber`/`orange` (brand colors). Don't change without explicit ask.

## Agent skills

This repo is configured for the Apisense skill pipeline. Config:
`.claude/apisense-flow.json` (mode: `lib`, tracker: `github`). Durable domain
docs live in `CONTEXT.md`, `dev-docs/adr/`, `dev-docs/glossary.md`, and
`dev-docs/audyt-instrukcji.md` — these sit outside `docs/` on purpose, since
`docs/` is the published public site root.

Before updating `manual/app-manual.*` against the app, read
`dev-docs/audyt-instrukcji.md`. It carries the verification protocol (an ARB
value is not evidence that a label is rendered), the prod-vs-QA rule, and why
the per-release `auto_docs` workflow in `apisense-mobile` does not remove the
need for a periodic audit.
Work items are tracked as GitHub Issues in `abelo-smartbee/apisense-docs`.
