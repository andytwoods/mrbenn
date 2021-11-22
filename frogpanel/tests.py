import inspect

from django.test import TestCase
from django.urls import reverse
from django.test.client import RequestFactory

from example.frogpanel import views
from example.frogpanel.views import _retrieve_view_name, _retrieve_template_name


class TestLoadInIDE(TestCase):

    def setUp(self):
        self.rf = RequestFactory()
        # below could be retrieved from test.client but for time being hand-coding
        self.testserver = 'testserver'


    def test_retrieve_view_name(self):
        referrer_url = self.testserver + reverse('djdt:open_view')

        my_request = self.rf.get('', HTTP_REFERER=referrer_url)
        view_name = _retrieve_view_name(my_request)

        self.assertEquals(type(view_name), str)
        self.assertEquals(view_name, inspect.getsourcefile(views))

    def test_retrieve_template_name(self):
        referrer_url = self.testserver + reverse('djdt:open_template')

        my_request = self.rf.get('', {'template': 'index.html'}, HTTP_REFERER=referrer_url)
        template_name = _retrieve_template_name(my_request)

        self.assertEquals(type(template_name), str)
        self.assertTrue('example/templates/index.html' in template_name)
