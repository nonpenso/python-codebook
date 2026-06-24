# Configuration file for the Sphinx documentation builder.

project = "Python Codebook"
copyright = "2025, Giovanni Caudullo"
author = "Giovanni Caudullo"

# -- General configuration ---------------------------------------------------

extensions = [
    "myst_parser",
    "sphinx_copybutton",
]

# MyST-Parser settings (enables Markdown support)
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "fieldlist",
]
myst_heading_anchors = 3

# Markdown file support
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

html_theme = "pydata_sphinx_theme"

html_theme_options = {
    "show_toc_level": 2,
    "navigation_depth": 3,
    "show_nav_level": 2,
    "navbar_align": "left",
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/nonpenso/python-codebook",
            "icon": "fa-brands fa-github",
        },
    ],
}

html_static_path = ["_static"]
html_title = "Python Codebook"
