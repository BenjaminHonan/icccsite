#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'ICCC'
SITENAME = u'Imperial College Caving Club'
SITEURL = '/'

THEME = 'themes/ICTheme'

PATH = 'content'
ARTICLE_EXCLUDES = ['caves', 'cavers']

STATIC_PATHS = ['assets', 'photo_archive', 'extra']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'}
}

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

CATEGORY_SAVE_AS = ''
TAG_SAVE_AS = ''

AUTHOR_URL            = 'author/{slug}/'
AUTHOR_SAVE_AS        = 'author/{slug}/index.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DEFAULT_PAGINATION = 10
DEFAULT_ORPHANS = 4
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

DEFAULT_DATE_FORMAT = '%d-%m-%Y'

PLUGIN_PATHS = ["plugins"]
PLUGINS = ['photoarchive', 'acyear', 'cavepeeps', 'subsites', 'oldurl', 'metainserter', 'inlinephotos']

SLUGIFY_SOURCE = 'basename'

ARTICLE_URL = 'articles/{slug}.html'
ARTICLE_SAVE_AS = 'articles/{slug}.html'

FAVICON = "assets/iclogo.png"

DISQUS_SITENAME = u'iccc'

SUBSITES = ["_newzealand", "_slovenia"]
