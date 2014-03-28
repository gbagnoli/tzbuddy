#!/usr/bin/env python

import sys
from distutils.core import setup

VERSION = "0.1"
AUTHOR = 'Giacomo Bagnoli <gbagnoli@gmail.com>'
requirements = ['arrow']

if sys.version_info < (2, 7):
    requirements.append('argparse')

setup(
    name='tzbuddy',
    version=VERSION,
    description='Visual repr of time in different timezones',
    author=AUTHOR,
    py_modules=["tzbuddy.py"],
    author_email='gbagnoli@gmail.com',
    entry_points="""\
    [console_scripts]
    tzbuddy = tzbuddy:main
    """,
    install_requires=requirements
)
