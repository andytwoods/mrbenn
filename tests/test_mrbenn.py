import inspect

from django.test import TestCase, override_settings
from django.test.client import RequestFactory
from django.urls import reverse
from unittest import mock

from mrbenn_panel import views
from mrbenn_panel.views import _retrieve_view_name, _retrieve_template_name


class HelperTests(TestCase):
    """Unit tests for the request -> on-disk-path resolution helpers."""

    def setUp(self):
        self.rf = RequestFactory()

    def test_retrieve_view_name(self):
        # The view to open is derived from an explicit `path` param, resolved
        # against the URLconf -- not from the Referer header.
        request = self.rf.post('', {'path': reverse('djdt:open_view')})
        view_name = _retrieve_view_name(request)

        self.assertEqual(type(view_name), str)
        self.assertEqual(view_name, inspect.getsourcefile(views))

    def test_retrieve_view_name_unresolvable_path(self):
        request = self.rf.post('', {'path': '/does/not/resolve/'})
        self.assertIsNone(_retrieve_view_name(request))

    def test_retrieve_view_name_missing_path(self):
        self.assertIsNone(_retrieve_view_name(self.rf.post('')))

    def test_retrieve_template_name(self):
        request = self.rf.post('', {'template': 'index.html'})
        template_name = _retrieve_template_name(request)

        self.assertEqual(type(template_name), str)
        template_name = template_name.replace("\\", "/")  # normalise across OSes
        self.assertTrue(template_name.endswith('templates/index.html'))

    def test_retrieve_template_name_unknown_template(self):
        request = self.rf.post('', {'template': 'no_such_template.html'})
        self.assertIsNone(_retrieve_template_name(request))

    def test_retrieve_template_name_traversal_blocked(self):
        # Django's template loaders reject `..` / absolute paths.
        request = self.rf.post('', {'template': '../../../../etc/passwd'})
        self.assertIsNone(_retrieve_template_name(request))


@override_settings(DEBUG=True, INTERNAL_IPS=['127.0.0.1'])
class EndpointSecurityTests(TestCase):
    """The open_* endpoints must only ever run for the local developer."""

    # The test settings mark every DB with ATOMIC_REQUESTS, so a client request
    # opens a transaction on each connection.
    databases = '__all__'

    def setUp(self):
        self.open_template = reverse('djdt:open_template')
        self.open_view = reverse('djdt:open_view')

    def _mock_subprocess(self):
        calls = []
        patchers = [
            mock.patch.object(views.subprocess, 'call', lambda a, *x, **k: calls.append(a)),
            mock.patch.object(views.subprocess, 'Popen', lambda a, *x, **k: calls.append(a)),
            mock.patch.object(views.subprocess, 'check_call', lambda a, *x, **k: calls.append(a)),
        ]
        for p in patchers:
            p.start()
            self.addCleanup(p.stop)
        return calls

    def test_non_internal_ip_is_rejected(self):
        calls = self._mock_subprocess()
        resp = self.client.post(self.open_template, {'template': 'index.html'},
                                REMOTE_ADDR='203.0.113.7')
        self.assertEqual(resp.status_code, 404)
        self.assertEqual(calls, [])

    @override_settings(DEBUG=False)
    def test_debug_off_is_rejected(self):
        calls = self._mock_subprocess()
        resp = self.client.post(self.open_template, {'template': 'index.html'},
                                REMOTE_ADDR='127.0.0.1')
        self.assertEqual(resp.status_code, 404)
        self.assertEqual(calls, [])

    def test_get_not_allowed(self):
        calls = self._mock_subprocess()
        resp = self.client.get(self.open_template + '?template=index.html',
                               REMOTE_ADDR='127.0.0.1')
        self.assertEqual(resp.status_code, 405)
        self.assertEqual(calls, [])

    def test_internal_post_opens_template(self):
        calls = self._mock_subprocess()
        resp = self.client.post(self.open_template, {'template': 'index.html'},
                                REMOTE_ADDR='127.0.0.1')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(calls), 1)
        opened = calls[0][-1]
        self.assertTrue(opened.replace('\\', '/').endswith('templates/index.html'))

    def test_internal_post_opens_view(self):
        calls = self._mock_subprocess()
        resp = self.client.post(self.open_view, {'path': '/'},
                                REMOTE_ADDR='127.0.0.1')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(calls), 1)

    def test_unknown_template_is_bad_request(self):
        calls = self._mock_subprocess()
        resp = self.client.post(self.open_template, {'template': 'no_such.html'},
                                REMOTE_ADDR='127.0.0.1')
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(calls, [])

    def test_missing_path_is_bad_request(self):
        calls = self._mock_subprocess()
        resp = self.client.post(self.open_view, {}, REMOTE_ADDR='127.0.0.1')
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(calls, [])
