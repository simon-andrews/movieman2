import os

from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="movieman2",
    version="0.0.1",
    packages=["movieman2"],
    include_package_data=True,
    license='MIT License',
    description='A Django app for managing, voting on, and picking movies',
    long_description=README,
    url='https://github.com/simon-andrews/movieman2',
    author='Simon Andrews',
)
