#!/usr/bin/env python3

from pathlib import Path

from setuptools import setup

root = Path(__file__).parent
long_description = (root / "README.md").read_text()

setup(
    name = "go-test-can",
    version = "1.0.0",
    description = "A script to test the CAN interfaces",
    url="https://github.com/GOcontroll/go-test-can",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="GOcontroll",
    author_email="info@gocontroll.com",
    maintainer="Maud Spierings",
    install_requires=["python-can", "netifaces"],
    packages=["go_test_can"],
    entry_points={
        "console_scripts": [
            "go-test-can = go_test_can.test_can:test_can",
        ]
    },
    python_requires=">=3.9",
)
