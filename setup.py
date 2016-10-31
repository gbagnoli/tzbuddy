#!/usr/bin/env python

import sys
from distutils.core import setup

VERSION = "0.2.3"
AUTHOR = 'Giacomo Bagnoli'
DOWNLOAD_URL='https://github.com/gbagnoli/tzbuddy/releases/tag/{0}'
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
    download_url=DOWNLOAD_URL.format(VERSION),
    license='MIT',
    packages=["tzbuddy"],
    entry_points="""\
    [console_scripts]
    tzbuddy = tzbuddy:main
    """,
    install_requires=requirements,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities'
    ]
)
