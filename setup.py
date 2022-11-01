#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
samplotlib

@author: Sam Passaglia
"""

from setuptools import setup, find_packages

setup(
    name="samplotlib",
    version="0.0.1",
    description="Plotting scripts extending matplotlib",
    author="Sam Passaglia",
    license="MIT",
    packages=find_packages(),
    install_requires=["matplotlib", "numpy"],
)
