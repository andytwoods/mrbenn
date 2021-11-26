# -- Project information -----------------------------------------------------
import datetime

project = "MrBenn Toolbar Plugin"
copyright = "{}, Andy Woods and contributors"
copyright = copyright.format(datetime.date.today().year)
author = "Andy Woods and contributors"

release = "0.0.1"

html_theme = "default"

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]