# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import os

from setuptools import setup

from forgive import __version__


def get_long_description():
    readme_file = 'README.rst'
    if not os.path.exists(readme_file):
        readme_file = 'README.md'
    with open(readme_file, 'rb') as f:
        long_description = f.read().decode('utf-8')
    return long_description


setup(
    name='forgive',
    version=__version__,
    description='Coding should be simple and fun. Certainly I will choose ForgiveDB.',
    long_description=get_long_description(),
    author='Lirian Su',
    author_email='liriansu@gmail.com',
    url='https://github.com/hui-z/ForgiveDB',
    license='WTFPL',
    packages=['forgive'],
)
