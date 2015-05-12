#!/usr/bin/env python
import os
import sys

import django
import tmdbsimple
from django.conf import settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.test_settings'
from django.test.utils import get_runner

tmdbsimple.API_KEY = os.environ['MM2_TMDB_API_KEY']

django.setup()
TestRunner = get_runner(settings)
test_runner = TestRunner()
failures = test_runner.run_tests(["movieman2"])
sys.exit(bool(failures))
