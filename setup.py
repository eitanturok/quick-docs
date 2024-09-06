#!/usr/bin/env python3

from pathlib import Path
from setuptools import setup

directory = Path(__file__).resolve().parent
with open(directory / 'README.md', encoding='utf-8') as f:
  long_description = f.read()

setup(name='quick-docs',
      version='0.0.1',
      install_requires=[],
      python_requires='>=3.8',
      extras_require={
        'docs': [
            "mkdocs",
            "mkdocs-material",
            "mkdocstrings[python]",
            "markdown-callouts",
            "markdown-exec[ansi]",
            "black"
        ]
      },
      include_package_data=True)