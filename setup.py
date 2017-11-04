#!/usr/bin/env python3

from setuptools import setup, find_packages


setup(
    name="pyhow",
    author="Y. SOMDA",
    version="1.0",
    url="https://github.com/yoeo",
    license="MIT",
    description="Master all the bases of python!",
    packages=find_packages(),
    entry_points={
        'console_scripts': ['pyhow = pyhow.__main__:main']
    },
)
