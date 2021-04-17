from setuptools import setup, find_packages
import re


def readme(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def find_version(filename):
    _version_re = re.compile(r'__version__ = "(.*)"')
    for line in open(filename):
        version_match = _version_re.match(line)
        if version_match:
            return version_match.group(1)


version = find_version("appear/__init__.py")

packages = find_packages(exclude=("examples*", "test*"))

setup(
    name='appear',
    version=version,
    description="Appear is a CLI toolkit to generate application code.",
    keywords="meta-programming generator semantic jinja rdf json-ld",
    author="Zac Pez",
    author_email="zacpez@gmail.com",
    maintainer="Appear Team",
    maintainer_email="contact@appear-schema.org",
    url="https://github.com/zacpez/appear",
    license="Apache-2.0 License",
    packages=packages,
    platforms=["any"],
    python_requires=">=3.8",
    install_requires=[
        'requests',
        'importlib; python_version == "2.6"',
    ],
    long_description=readme('README'),
    entry_points={
        'console_scripts': [
            'appear = __init__:appear'
        ]
    },
)
