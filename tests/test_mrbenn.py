import os
from functools import partial
from unittest import mock

import pytest
from django.contrib.sites.models import Site
from django.db import transaction
from django.test import TestCase, override_settings

import mrbenn_panel

set_env_vars = partial(mock.patch.dict, os.environ)


class DjangoReadOnlyTests(TestCase):
    def tearDown(self):
        # reset after every test
        super().tearDown()

    def test_set_read_only_default_false(self):
        """
        Check that, in the absence of a value for the setting and environment
        variable, AppConfig.ready() defaults read only mode to OFF.
        """
        pass
