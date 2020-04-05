#!/usr/bin/env python3

import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
        name = 'ipwrangle',
        python_requires='>=3',
        version = '0.0.4',
        author = 'Yonathan Klijnsma',
        author_email = 'admin@0x3a.com',
        url = 'https://github.com/0x3a/ipwrangle',
        packages=find_packages(),
        include_package_data=True,
        description = 'Simple python-based command-line utilities to work with CIDRs individual IPs.',
        long_description=read('README.md'),
        long_description_content_type='text/markdown',
        install_requires=[
            'netaddr'
        ],
        entry_points={
            'console_scripts': [
                'ipexpand=ipwrangle:expand_main',
                'ipreduce=ipwrangle:reduce_main',
                'netlen=ipwrangle:netlen_main',
                'innet=ipwrangle:innet_main'
            ],
        }
     )
