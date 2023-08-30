#!/usr/bin/env python

import pathlib

from setuptools import setup, find_packages

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="barkeputils",
    version="0.0.1",
    description="Handy little utils for using with python",
    author="Barrett Kepler",
    url="https://git.dw/kepler-br/keputils.git",
    install_requires=['asyncio_throttle>=1.0.2', 'asyncio>=3.4.3'],
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="MIT",
    long_description_content_type="text/markdown",
    long_description=long_description,
    python_requires=">=3.7",
    package_data={"barkeputils": ["py.typed"]},
)
