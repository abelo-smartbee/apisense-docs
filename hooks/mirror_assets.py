"""Mirror non-localized asset folders into per-locale build dirs.

mkdocs-static-i18n in suffix mode keeps assets at root only; per-locale
HTML pages reference `../pictures/...` which 404s under `/en/`.
After build, copy each `manual/pictures/`, `overview/pictures/` (etc.) into
`site/<locale>/<same path>/` so relative refs resolve.
"""
import shutil
from pathlib import Path


ASSET_DIRS = ["manual/pictures", "overview/pictures", "downloads/files", "procedures/pictures", "samples/pictures"]


def on_post_build(config):
    site_dir = Path(config["site_dir"])
    plugin = config["plugins"].get("i18n")
    if plugin is None:
        return
    default_lang = plugin.default_language
    for lang_cfg in plugin.config.languages:
        locale = lang_cfg.locale
        if locale == default_lang or not lang_cfg.build:
            continue
        for asset_dir in ASSET_DIRS:
            src = site_dir / asset_dir
            dst = site_dir / locale / asset_dir
            if not src.exists():
                continue
            if dst.exists():
                shutil.rmtree(dst)
            shutil.copytree(src, dst)
