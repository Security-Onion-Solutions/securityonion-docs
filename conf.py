# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from datetime import datetime

from recommonmark.parser import CommonMarkParser

extensions = [
    'notfound.extension'
]
templates_path = ['templates', '_templates', '.templates']
source_suffix = ['.rst', '.md']
source_parsers = {
            '.md': CommonMarkParser,
        }
master_doc = 'index'
project = u'Security Onion'
copyright = str(datetime.now().year)
version = '2.3'
release = '2.3'
exclude_patterns = ['_build']
pygments_style = 'sphinx'
htmlhelp_basename = 'securityonion'
html_theme = 'sphinx_rtd_theme'
html_logo = 'images/so-logo.png'
html_theme_options = {
    'logo_only': True,
    'style_nav_header_background': 'black',
}
file_insertion_enabled = False
latex_documents = [
  ('index', 'securityonion.tex', u'Security Onion Documentation',
   u'', 'manual'),
]

# sphinx-notfound-page
# https://github.com/readthedocs/sphinx-notfound-page
notfound_context = {
    'title': 'Page Not Found',
    'body': '''
<h1>Page Not Found</h1>
<p>Sorry, we couldn't find that page.</p>
<p>Try using the search box or go to the homepage.</p>
''',
}

###########################################################################
#          auto-created readthedocs.org specific configuration            #
###########################################################################


#
# The following code was added during an automated build on readthedocs.org
# It is auto created and injected for every build. The result is based on the
# conf.py.tmpl file found in the readthedocs.org codebase:
# https://github.com/rtfd/readthedocs.org/blob/master/readthedocs/doc_builder/templates/doc_builder/conf.py.tmpl
#


import importlib
import sys
import os.path
from six import string_types

from sphinx import version_info

# Get suffix for proper linking to GitHub
# This is deprecated in Sphinx 1.3+,
# as each page can have its own suffix
if globals().get('source_suffix', False):
    if isinstance(source_suffix, string_types):
        SUFFIX = source_suffix
    elif isinstance(source_suffix, (list, tuple)):
        # Sphinx >= 1.3 supports list/tuple to define multiple suffixes
        SUFFIX = source_suffix[0]
    elif isinstance(source_suffix, dict):
        # Sphinx >= 1.8 supports a mapping dictionary for mulitple suffixes
        SUFFIX = list(source_suffix.keys())[0]  # make a ``list()`` for py2/py3 compatibility
    else:
        # default to .rst
        SUFFIX = '.rst'
else:
    SUFFIX = '.rst'

# Add RTD Static Path. Add to the end because it overwrites previous files.
if not 'html_static_path' in globals():
    html_static_path = []
if os.path.exists('_static'):
    html_static_path.append('_static')

# Add RTD Theme only if they aren't overriding it already
using_rtd_theme = (
    (
        'html_theme' in globals() and
        html_theme in ['default'] and
        # Allow people to bail with a hack of having an html_style
        'html_style' not in globals()
    ) or 'html_theme' not in globals()
)
if using_rtd_theme:
    theme = importlib.import_module('sphinx_rtd_theme')
    html_theme = 'sphinx_rtd_theme'
    html_style = None
    html_theme_options = {}
    html_static_path = ['_static']
    if 'html_theme_path' in globals():
        html_theme_path.append(theme.get_html_theme_path())
    else:
        html_theme_path = [theme.get_html_theme_path()]

if globals().get('websupport2_base_url', False):
    websupport2_base_url = 'https://readthedocs.org/websupport'
    websupport2_static_url = 'https://assets.readthedocs.org/static/'


#Add project information to the template context.
context = {
    'using_theme': using_rtd_theme,
    'html_theme': html_theme,
    'current_version': "2.3",
    'version_slug': "2.3",
    'MEDIA_URL': "https://media.readthedocs.org/",
    'STATIC_URL': "https://assets.readthedocs.org/static/",
    'PRODUCTION_DOMAIN': "readthedocs.org",
    'versions': [
    ("latest", "/en/latest/"),
    ],
    'downloads': [ 
    ("pdf", "//readthedocs.org/projects/securityonion/downloads/pdf/latest/"),
    ("htmlzip", "//readthedocs.org/projects/securityonion/downloads/htmlzip/latest/"),
    ("epub", "//readthedocs.org/projects/securityonion/downloads/epub/latest/"),
    ],
    'subprojects': [ 
    ],
    'slug': 'securityonion',
    'name': u'Security Onion',
    'rtd_language': u'en',
    'programming_language': u'words',
    'canonical_url': 'https://securityonion.readthedocs.io/en/latest/',
    'analytics_code': 'None',
    'single_version': False,
    'conf_py_path': '/',
    'api_host': 'https://readthedocs.org',
    'github_user': 'Security-Onion-Solutions',
    'github_repo': 'securityonion-docs',
    'github_version': '2.3',
    'display_github': True,
    'bitbucket_user': 'None',
    'bitbucket_repo': 'None',
    'bitbucket_version': 'master',
    'display_bitbucket': False,
    'gitlab_user': 'None',
    'gitlab_repo': 'None',
    'gitlab_version': 'master',
    'display_gitlab': False,
    'READTHEDOCS': True,
    'using_theme': (html_theme == "default"),
    'new_theme': (html_theme == "sphinx_rtd_theme"),
    'source_suffix': SUFFIX,
    'ad_free': False,
    'user_analytics_code': '',
    'global_analytics_code': 'UA-17997319-1',
    'commit': '525fc0c7',
    'css_files': [
        '_static/theme_overrides.css',  # overrides for wide tables in RTD theme
    ],
}




if 'html_context' in globals():
    html_context.update(context)
    
else:
    html_context = context

# Add custom RTD extension
if 'extensions' in globals():
    # Insert at the beginning because it can interfere
    # with other extensions.
    # See https://github.com/rtfd/readthedocs.org/pull/4054
    extensions.insert(0, "readthedocs_ext.readthedocs")
else:
    extensions = ["readthedocs_ext.readthedocs"]
