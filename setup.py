#!/usr/bin/env python
# -*- coding: utf-8 -*

from __future__ import absolute_import

import os

from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

setup(
    name='hasattr-safe',
    version='0.1.2.dev0',
    packages=find_packages('src', exclude=('tests',)),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    description='A non-harmful hasattr',
    author='Richard O\'Dwyer',
    author_email='richard@richard.do',
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=(
        'https://github.com/richardasaurus/hasattr-safe'
    ),
    install_requires=install_requires,
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP'
    ]
)
