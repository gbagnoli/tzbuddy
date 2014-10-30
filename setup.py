#!/usr/bin/env python

import sys
from distutils.core import setup

VERSION = "0.2.1"
AUTHOR = 'Giacomo Bagnoli'
requirements = ['arrow']

if sys.version_info < (2, 7):
    requirements.append('argparse')

setup(
    name='TZBuddy',
    version=VERSION,
    description='Visual repr of time in different timezones',
    author=AUTHOR,
    author_email='gbagnoli@gmail.com',
    url='https://github.com/gbagnoli/tzbuddy',
    download_url='https://github.com/gbagnoli/tzbuddy/tarball/0.1',
    license='MIT',
    packages=["tzbuddy"],
    entry_points="""\
    [console_scripts]
    tzbuddy = tzbuddy:main
    """,
    install_requires=requirements,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities'
    ]
)
