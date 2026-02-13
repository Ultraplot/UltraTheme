"""
A clean variant on the read the docs theme with light mode dark mode toggling.
"""
import os

from pygments.formatters import HtmlFormatter

# Declare themes. These should be kept updated with custom.js
# Note the default them is only loaded before the javascript file can
# read user preferences and toggle either the light or dark mode theme.
init_theme = 'default'
light_theme = 'pastie'
dark_theme = 'monokai'

# Create local pygments css files. These are used by custom.js
base = os.path.abspath(os.path.dirname(__file__))
folder = os.path.join(base, 'static', 'pygments')
if not os.path.isdir(folder):
    os.mkdir(folder)
for style in (init_theme, light_theme, dark_theme):  # or get_all_styles()
    file = os.path.join(folder, style + '.css')
    if os.path.isfile(file):
        continue
    with open(file, 'w') as f:
        f.write(HtmlFormatter(style=style).get_style_defs('.highlight'))

# Add entrypoint for theme
# See: https://www.sphinx-doc.org/en/master/development/theming.html
def setup(app):  # noqa: E302
    # Keep legacy name for compatibility and add canonical UltraPlot name.
    app.add_html_theme('sphinx_rtd_light_dark', base)
    app.add_html_theme('ultraplot_theme', base)
