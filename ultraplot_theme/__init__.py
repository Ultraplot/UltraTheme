"""
UltraPlot docs theme extension.

This keeps the legacy RTD-light-dark theme registration while also injecting
shared UltraPlot docs static assets (CSS/JS) that are used with Shibuya.
"""

from __future__ import annotations

from pathlib import Path

from sphinx_rtd_light_dark import setup as _legacy_setup

_STATIC_DIR = Path(__file__).resolve().parent / "static"


def _add_static_path(app):
    static_path = str(_STATIC_DIR)
    if static_path not in app.config.html_static_path:
        app.config.html_static_path.append(static_path)


def setup(app):
    legacy = _legacy_setup(app) or {}

    app.connect("builder-inited", _add_static_path)
    app.add_css_file("ultraplot-docs.css")
    app.add_js_file("ultraplot-docs.js")

    return {
        "version": legacy.get("version", "0.0"),
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
