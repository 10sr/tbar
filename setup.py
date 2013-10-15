#!/usr/bin/env python3

from distutils.core import setup

import tbar

setup(name = "tbar",
      version = tbar.__version__,
      description = "Terminal Bar",
      long_description = tbar.__doc__,
      author = "10sr",
      author_email = "sr10@sourceforge.org",
      url = "https://github.com/10sr/tbar",
      download_url = "https://github.com/10sr/tbar/archive/master.zip",
      packages = ["tbar"],
      scripts = ["bin/tbar"],
      keywords = "utility",
      classifiers=['License :: Public Domain']
      )
