"""
pavement.py - Paver Build file

Tasks useful to developers. Nothing that any old casual user would do belongs here.
"""

import os.path
import shutil

from paver.easy import sh, task


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
def inspect():
    """Inspects project source"""
    lint()


@task
def lint():
    """Checks code quality using flake8"""
    sh("flake8 --max-line-length=120 --max-complexity=10 .")


@task
def make_hooks_executable():
    """Sets git hooks to be executable"""
    for item in os.listdir('.git/hooks'):
        if not os.access(os.path.join('.git/hooks', item), os.X_OK):
            sh("chmod +x " + os.path.join('.git/hooks', item))


@task
def pre_commit():
    """Stuff to run before every commit"""
    sort_imports()
    inspect()


@task
def setup():
    apply_hooks()


@task
def sort_imports():
    """Sort imports with isort"""
    sh("isort -rc . --skip run_tests.py")


@task
def test():
    sh("python run_tests.py")
