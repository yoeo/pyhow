#!/usr/bin/env python3

from setuptools import setup, find_packages


setup(
    name="pyhow",
    author="yoeo",
    version="0.1",
    url="https://github.com/yoeo",
    license="MIT",
    description="Master all the bases of python!",
    package_dir={'': 'src'},
    packages=find_packages('src'),
    test_suite="tests",
    scripts=['bin/pyhow'],
)

