import os.path
import shutil

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
def apply_hooks():
    copy_hooks()
    make_hooks_executable()


@task
def copy_hooks():
    """Copies hooks from git_hooks folder into .git/hooks"""
    for item in os.listdir('git_hooks'):
        print('Applying hook: ' + item)
        shutil.copyfile(os.path.join('git_hooks', item), os.path.join('.git/hooks', item))


@task
def make_hooks_executable():
    """Sets git hooks to be executable"""
    for item in os.listdir('.git/hooks'):
        if not os.access(os.path.join('.git/hooks', item), os.X_OK):
            sh("chmod +x " + os.path.join('.git/hooks', item))


@task
def write_default_config():
    """Writes a default config to config.py"""
    if not os.path.isfile('config.py'):
        print('Writing default config.')
        f = open('config.py', 'w')
        f.write(config)
        f.close()
    else:
        print('Config file already exists, will not overwrite.')


@task
def setup():
    write_default_config()
    apply_hooks()


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


@task
def sort_imports():
    sh("isort -rc .")


@task
def pre_commit():
    sort_imports()
    inspect()
