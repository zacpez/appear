"""Appear Schema CLI build definitions"""
import re
import os
from setuptools import setup, find_packages


def readme(filename):
    """Reads the main readme and places it in the package definition"""
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


def find_version(filename):
    """Grabs the latest version for the package definition"""
    _version_re = re.compile(r'__version__ = "(.*)"')
    for line in open(filename):
        version_match = _version_re.match(line)
        if version_match:
            return str(version_match.group(1))
    return "X.X.X"


version = find_version("appear-schema/__init__.py")

packages = find_packages(include=("appear*"))

setup(
    name='appear-schema',
    version=version,
    description="Appear Schema is a CLI toolkit to generate application code.",
    keywords="meta-programming generator semantic jinja rdf json-ld",
    author="Zac Pez",
    author_email="zacpez@gmail.com",
    maintainer="Appear Schema Team",
    maintainer_email="contact@appear-schema.org",
    url="https://github.com/zacpez/appear-schema",
    license="Apache-2.0 License",
    packages=packages,
    platforms=["any"],
    python_requires=">=3.10",
    install_requires=[
        'requests',
        'importlib; python_version == "3.10"',
    ],
    long_description=readme('README.md'),
    entry_points={
        'console_scripts': [
            'appear-schema = appear_schema:appear_schema'
        ]
    },
)
