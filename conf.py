# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'Bullet'
copyright = '2020, Shengyu Zhang'
author = 'Shengyu Zhang'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = []

extensions.append('sphinx_rtd_theme')
# The theme to use for HTML and HTML Help pages.
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
        'navigation_depth': -1,
        'titles_only': True,
}

extensions.append('sphinx.ext.graphviz')

extensions.append('sphinx.ext.todo')
todo_include_todos = True

extensions.append('sphinx.ext.githubpages')

extensions.append('sphinxnotes.peopledomain')

extensions.append('sphinxcontrib.email')

extensions.append('sphinxnotes.lilypond')

extensions.append('sphinxcontrib.images')
images_config = {
    'override_image_directive': True,
    'default_image_width': '48%', # 2 images a row
    'default_group': 'default',
    'default_show_title': True,
    'download': False,
}

extensions.append('sphinx.ext.extlinks')
extlinks = {
    'zhwiki': ('https://zh.wikipedia.org/wiki/%s', ''),
    'enwiki': ('https://wikipedia.org/wiki/%s', ''),
    'search': ('https://duckduckgo.com/?q=%s', ''),
    'twitter': ('https://twitter.com/%s', '@'),
    'github': ('https://github.com/%s', '@'),
    'weibo': ('https://weibo.com/%s', '@'),
}

extensions.append('sphinx.ext.githubpages')

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'zh_CN'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# I dont want a default py domain.
primary_domain = None

# Use :code: as default role, so we can write `content` instead of ``content``.
default_role = 'code'

# Auto numbered figures, tables and code-blocks if they have a caption.
numfig = True

# Show codeauthor and sectionauthor directives produce any output in the built
# files.
show_authors = True

# -- Options for HTML output -------------------------------------------------

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = ['style.css']

html_baseurl = 'https://silverrainz.me'

html_title = project

# If true, the reST sources are included in the HTML build as _sources/name.
# I don't want to public my sources, so set it to false.
html_copy_source = False

html_search_language = 'zh'
