#!/usr/bin/env python
# coding=utf-8

import os
from distutils.core import setup

delattr(os, 'link')

setup(
    name='avd',
    version='1.0',
    author='Jerome Belleman',
    author_email='Jerome.Belleman@gmail.com',
    url='http://cern.ch/jbl',
    description="Manage AVDs",
    long_description="Manage AVDs.",
    scripts=['avd'],
    data_files=[('share/man/man1', ['avd.1'])],
)
