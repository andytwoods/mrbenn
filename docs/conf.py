# -- Project information -----------------------------------------------------
import datetime

project = "mrbenn-toolbar-plugin"
copyright = "{}, Andy Woods and contributors"
copyright = copyright.format(datetime.date.today().year)
author = "Andy Woods and contributors"

version = "0.0.2"

html_theme = "default"

master_doc = 'index'

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]