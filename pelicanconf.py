#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Carlos Pita'
SITENAME = 'Jampp Research'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['images', 'extra']

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

THEME = 'theme'
THEME_TEMPLATES_OVERRIDES = ['templates']
BOOTSTRAP_THEME = 'readable'

CUSTOM_CSS = 'extra/custom.css'
CUSTOM_JS = 'extra/custom.js'

JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

MARKDOWN = {
    'extension_configs': {
        'mdx_math': {'enable_dollar_delimiter': True},
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5'
}

DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = True
TAGS_URL = 'tags.html'

PLUGIN_PATHS = ['plugins']
PLUGINS = ['i18n_subsites', 'tag_cloud']
