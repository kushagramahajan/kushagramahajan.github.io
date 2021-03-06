#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://kushagramahajan.github.io'
RELATIVE_URLS = True

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = False

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

IGNORE_FILES = ['../index.html', 'index.html']
TEMPLATE_PAGES = {'index.html': '../output/index.html'}

MENUITEMS = (
    ('About Me', '/'),
    ('Research', '/output/pages/research.html'),
    ('Projects', '/output/pages/academic-projects.html'),
    ('Resume', 'http://kushagramahajan.me/pdfs/cv.pdf'),
    ('Contact', '/output/pages/contact.html'),
)


# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
