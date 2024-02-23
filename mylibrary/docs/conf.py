# Configuration file for the Sphinx documentation builder.

# -- Path setup --------------------------------------------------------------
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------
project = 'MyLibrary'
copyright = '2024, Your Name'
author = 'Your Name'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]
templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'alabaster'
html_static_path = ['_static']

# -- Options for autodoc extension -------------------------------------------
autodoc_member_order = 'bysource'
