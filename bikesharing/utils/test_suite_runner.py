"""
To use this, run:
heroku addons:add heroku-postgresql:dev
heroku config:set TEST_DATABASE_URL="postgres://..." # replace with the new HEROKU_POSTGRESQL_<COLOR>_URL
Then, make TEST_RUNNER setting a Python path to the HerokuTestSuiteRunner class.
"""

import django
from django.test.runner import DiscoverRunner
from django.conf import settings
from django.core.management import call_command
from django.db.utils import ConnectionHandler

class HerokuTestSuiteRunner(DiscoverRunner):
    def setup_databases(self, **kwargs):
        ###
        # WARNING: NOT handling 'TEST_MIRROR', 'TEST_DEPENDENCIES'
        ###

        # get new connections to test database
        test_connections = ConnectionHandler(settings.TEST_DATABASES)

        for alias in django.db.connections:
            test_connection = test_connections[alias]

            # set django-wide connection to use test connection
            django.db.connections[alias] = test_connection

            # re-initialize database (this "replaces" the CREATE DATABASE which
            # cannot be issued on Heroku)
            cursor = test_connection.cursor()
            cursor.execute('DROP SCHEMA public CASCADE')
            cursor.execute('CREATE SCHEMA public')

            # code below taken from
            # django.test.simple.DjangoTestSuiteRunner.setup_databases and
            # django.db.backends.creation.create_test_db

            # make them tables
            call_command('migrate',
                        verbosity=0,
                        interactive=False,
                        database=test_connection.alias)

            call_command('flush',
                verbosity=0,
                interactive=False,
                database=test_connection.alias)

            from django.core.cache import caches
            from django.core.cache.backends.db import BaseDatabaseCache
            for cache_alias in settings.CACHES:
                cache = caches[cache_alias]
                if isinstance(cache, BaseDatabaseCache):
                    call_command('createcachetable', cache._table,
                                 database=test_connection.alias)

    def teardown_databases(self, *args, **kwargs):
        # NOP
        pass