#MovieMan 2 [![Build Status](https://travis-ci.org/simon-andrews/movieman2.svg?branch=master)](https://travis-ci.org/simon-andrews/movieman2)

MovieMan is a program for maintaining and voting on a list of movies.

##Commands
MovieMan uses [Paver](https://github.com/paver/paver) for automation of various tasks. These are the commands that are currently built into the pavement.py file:

| Command | Description |
|---------|-------------|
| `apply_hooks` | Apply all the hooks from the git_hooks directory. |
| `check_source` | Check source code for potential issues. |
| `copy_hooks` | Copy files from git_hooks directory into .git/hooks. |
| `inspect` | Checks over the project. |
| `lint` | Check code style of the project. |
| `make_hooks_executable` | Goes into your git hooks directory and makes all the files there executable. |
| `pre_commit` | Task run before every commit. |
| `run_tests` | Run unit tests. |
| `setup` | Makes project (almost) ready to roll. You will still need to configure your config.py. |
| `sort_imports` | Sort Python imports in the entire project. |
| `write_default_config` | Writes you a new config.py if you don't already have one. |
