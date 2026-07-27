# CONTEXT

> Durable orientation doc for this repo. Kept in the repo, versioned with the
> content it describes. Agents read this first. Keep it short and true; when a
> decision changes an entry here, update it in the same PR.
>
> **Stub** — scaffolded by `/setup`. `domain-modeling` and the grilling skills
> fill this in.

## What this repo is

One paragraph: what it publishes, to whom, and why it exists.

## Surface

- Published at: https://docs.apisense.ai/ (GitHub Pages, `abelo-smartbee/apisense-docs`)
- Generator: MkDocs Material + `mkdocs-static-i18n` (suffix structure, PL default at `/`, EN at `/en/`)
- Pages an agent must not break:

## Content

- Source of pages: `docs/<section>/*.pl.md` + `*.en.md`
- Nav: per-locale under `plugins.i18n.languages[].nav` in `mkdocs.yml` — both locales must be updated together
- Shared assets: `docs/<section>/pictures/`, `docs/assets/`

## External dependencies

- Upstream (where the facts come from):
- Downstream consumers of this:

## Invariants (do not break)

- Every page exists as both `.pl.md` and `.en.md`
- Every new page is added to **both** locale navs
- Public site — nothing internal, no credentials, no unreleased roadmap
- Theme palette `amber`/`orange` (brand); `docs/assets/stylesheets/extra.css` is the only custom stylesheet

## How to run and test

- Run locally: `mkdocs serve` (http://127.0.0.1:8000)
- Build check (what CI runs): `mkdocs build --strict`
- Deploy: automatic on push to `main` via `.github/workflows/deploy.yml`

## Decisions

See `dev-docs/adr/` for architecture decision records. Terms are defined in
`dev-docs/glossary.md`. Both live outside `docs/` on purpose — `docs/` is the
published site root.
