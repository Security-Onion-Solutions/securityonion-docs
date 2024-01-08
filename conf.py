from datetime import datetime

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Security Onion Documentation'
author = 'Security Onion Solutions, LLC'
copyright = str(datetime.now().year)
release = '2.4'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.venv']

root_doc = 'index'


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = 'images/logo/so-logo.png'
html_theme_options = {
    'logo_only': True,
    'style_nav_header_background': 'black',
}
html_css_files = [
    'theme_overrides.css'
]
html_js_files = [
    'theme_overrides.js'
]
