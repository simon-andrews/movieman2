import os

from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='movieman2',
    version='0.2',
    packages=['movieman2'],
    include_package_data=True,
    license='MIT License',
    description='A Django app for managing, voting on, and picking movies',
    long_description=README,
    url='https://github.com/simon-andrews/movieman2',
    author='Simon Andrews',
    author_email='http://scr.im/35r3',
    install_requires=['Django', 'tmdbsimple'],
    test_suite='run_tests',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ]
)
