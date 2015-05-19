#MovieMan 2 [![Build Status](https://travis-ci.org/simon-andrews/movieman2.svg?branch=master)](https://travis-ci.org/simon-andrews/movieman2)

MovieMan is a program for maintaining and voting on a list of movies.

##Requirements
To run, MovieMan requires:

 * Django
 * tmdbsimple

##Development
You want to help create MovieMan? Great! Just a few things you need to know first...

###Tools
Install the following tools; they will save you from a lot of headaches:

 * Paver
 * flake8
 * isort

###Git Hooks
MovieMan has a pre-commit git hook to help you make sure that your pull request won't fail the CI build. You can install it in two different ways:

 * Manually copy it from the git_hooks folder into .git/hooks and mark it as executable
 * Let `paver apply_hooks` handle it all for you!

##Paver Commands
MovieMan makes extensive use of [Paver](https://github.com/paver/paver) for automation of various development-related tasks. These are the commands that are currently built into the `pavement.py` file:

| Command                 | Description                                                                  |
|-------------------------|------------------------------------------------------------------------------|
| `apply_hooks`           | Apply all the hooks from the git_hooks directory.                            |
| `copy_hooks`            | Copy files from git_hooks directory into .git/hooks.                         |
| `inspect`               | Checks over the project.                                                     |
| `lint`                  | Check code style of the project.                                             |
| `make_hooks_executable` | Goes into your git hooks directory and makes all the files there executable. |
| `pre_commit`            | Task run before every commit.                                                |
| `setup`                 | Makes development environment ready to roll.                                 |
| `sort_imports`          | Sort Python imports in the entire project.                                   |
| `test`                  | Run unit tests.                                                              |

