# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="facebook-graph-analyser",
    version="0.1.0",
    description="A pip package",
    license="MIT",
    author="oprogramador",
    packages=find_packages(),
    install_requires=[
        "networkx",
        "facebook-sdk"
    ],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ]
)
