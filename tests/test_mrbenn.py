import inspect
import os
from functools import partial
from unittest import mock

import mrbenn_panel
import pytest
from django.contrib.sites.models import Site
from django.db import transaction
from django.test import TestCase
from django.test import TestCase, override_settings
from django.test.client import RequestFactory
from django.urls import reverse
from mrbenn_panel import views
from mrbenn_panel.views import _retrieve_view_name, _retrieve_template_name

set_env_vars = partial(mock.patch.dict, os.environ)


class DjangoReadOnlyTests(TestCase):

    def setUp(self):
        self.rf = RequestFactory()
        # below could be retrieved from test.client but for time being hand-coding
        self.testserver = 'testserver'

    def test_retrieve_view_name(self):
        referrer_url = self.testserver + reverse('djdt:open_view')

        my_request = self.rf.get('', HTTP_REFERER=referrer_url)
        view_name = _retrieve_view_name(my_request)

        self.assertEqual(type(view_name), str)
        self.assertEqual(view_name, inspect.getsourcefile(views))

    def test_retrieve_template_name(self):
        referrer_url = self.testserver + reverse('djdt:open_template')

        some_site_url = ''

        my_request = self.rf.get(some_site_url, {'template': 'index.html'}, HTTP_REFERER=referrer_url)
        template_name = _retrieve_template_name(my_request)

        self.assertEqual(type(template_name), str)
        template_name = template_name.replace("\\", "/") # potential issue over operating systems elsewise
        self.assertTrue(template_name.endswith('templates/index.html'))
