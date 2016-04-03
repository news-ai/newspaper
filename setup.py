# -*- coding: utf-8 -*-
"""
Lucas Ou 2014 -- http://lucasou.com

Setup guide: http://guide.python-distribute.org/creation.html
python setup.py sdist bdist_wininst upload
"""
import sys
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')  # bdist_wininst
    sys.exit()


packages = [
    'newspaper',
]


with open('requirements.txt') as f:
    required = f.read().splitlines()


setup(
    name='newspaper',
    version='0.1.8',
    description='Simplified python article discovery & extraction.',
    url='https://github.com/news-ai/newspaper/tree/python-2-head'
    packages=packages,
    include_package_data=True,
    install_requires=required,
    license='MIT',
    zip_safe=False,
)
