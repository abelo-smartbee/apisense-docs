# apisense-docs

Public documentation site for Apisense, built with MkDocs Material and deployed to GitHub Pages.

## Local development

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

## Deployment

The site is deployed automatically by GitHub Actions when changes are pushed to `main`.
