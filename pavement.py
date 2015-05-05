import os.path
from paver.easy import sh, task


config = """# replace pass with values you would like to overwrite from DefaultConfig in
# default_config.py. Values you do not explicitly overwrite will be inherited
# from DefaultConfig. At the very least, you must set secret_key and
# tmdb_api_key.

from default_config import DefaultConfig


class Config(DefaultConfig):
    pass
"""


@task
def setup():
    """Writes a default config to config.py"""
    if not os.path.isfile('config.py'):
        print('Writing default config.')
        f = open('config.py', 'w')
        f.write(config)
        f.close()
    else:
        print('Config file already exists, will not overwrite.')


@task
def lint():
    """Checks code quality using flake8"""
    sh("flake8 --max-line-length=120 --max-complexity=10 .")


@task
def run_tests():
    """Run unit tests"""
    sh("./manage.py test")


@task
def check_source():
    """Identify any potential problems with code"""
    sh("./manage.py check")


@task
def inspect():
    """Inspects project source for a variety of problems"""
    lint()
    check_source()
    run_tests()
