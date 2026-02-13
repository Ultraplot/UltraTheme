Read the Docs Light-Dark Theme
------------------------------

[![pypi](https://img.shields.io/pypi/v/sphinx-rtd-light-dark?color=83%20197%2052)](https://pypi.org/project/sphinx-rtd-light-dark/)
[![licence](https://img.shields.io/github/license/lukelbd/sphinx-rtd-light-dark.svg)](LICENSE.txt)

A clean variant of the [read the docs theme](https://github.com/readthedocs/sphinx_rtd_theme)
with grayscale styling and optional light mode / dark mode toggling.
This theme is currently used with the [proplot](https://proplot.readthedocs.io)
and [climopy](https://climopy.readthedocs.io) projects.

Theme Usage
-----------

Install with `pip install sphinx-rtd-light-dark`. Then in your `conf.py` file,
add the entry ``'ultraplot_theme'`` to the `extensions` list,
and set `html_theme` to ``'ultraplot_theme'``.
The legacy extension/theme name ``'sphinx_rtd_light_dark'`` remains supported.

Example `conf.py`:

```python
extensions = [
  ...
  'ultraplot_theme',
  ...
]
html_theme = 'ultraplot_theme'
```
