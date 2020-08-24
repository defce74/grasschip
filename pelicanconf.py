#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

SITENAME = 'grasschip'
SITESUBTITLE = 'An independent news aggregator'
SITEURL = 'https://grasschip.netlify.app'
RELATIVE_URLS = False

PATH = 'content'

TIMEZONE = 'Australia/Perth'
DEFAULT_DATE_FORMAT = '%H:%M, %-d %-B %Y'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Email', 'grasschip@protonmail.com'),
	("Twitter", "https://twitter.com/grasschip1"))
	
TWITTER_USERNAME = 'grasschip1'

DEFAULT_PAGINATION = False

PLUGIN_PATHS = ['/home/daniel/dev/pelican/pelican-plugins']
PLUGINS = ['summary', 'share_post', 'sitemap']

# THEME = "/home/daniel/dev/pelican/pelican-themes/simple"
THEME = "/home/daniel/dev/pelican/grasschip/theme"

MENUITEMS = [
	('tags', SITEURL + '/tags.html')
]

DIRECT_TEMPLATES = ('index', 'tags')
CATEGORY_SAVE_AS = ''
DEFAULT_CATEGORY = 'news'
DISPLAY_PAGES_ON_MENU = True

STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {'extra/favicon.ico': {'path': 'favicon.ico'}, 'extra/robots.txt': {'path': 'robots.txt'} }

ARTICLE_ORDER_BY = 'reversed-modified'

ARTICLE_URL = 'posts/{slug}/'
ARTICLE_SAVE_AS = 'posts/{slug}.html'

SITEMAP = { "format": "xml", 
	"priorities": { "articles": 0.5, "indexes": 0.5, "pages": 0.5 },
    "changefreqs": { "articles": "daily", "indexes": "monthly", "pages": "monthly" }
}
