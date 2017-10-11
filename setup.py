try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


config = {
    "description": "Check integrity of new public dataset",
    "author": "bps",
    "author_email": "xander@numer.ai",
    "install_requires": [],
    "packages": ["integrity"],
    "name": "Numerai Public Dataset Integrity Check"
}

setup(**config)
