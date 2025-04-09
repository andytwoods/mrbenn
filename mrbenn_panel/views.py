import os
import subprocess
import sys

from django.conf import settings
from django.http import JsonResponse
from django.template.loader import get_template
from django.urls import resolve


def _retrieve_template_name(request):
    template_name = request.GET.get('template')
    template = get_template(template_name)
    return template.origin.name


def open_template(request):
    template_name = _retrieve_template_name(request)
    return open_element(template_name)


def _extract_func(request):
    host = request.get_host()
    referrer = request.META['HTTP_REFERER']
    url_ending = referrer.split(host)[1].split('?')[0]
    match = resolve(url_ending)
    func, _, _ = match
    return func


def _retrieve_view_name(request):
    func = _extract_func(request)
    # was having issues with parent classes being returned not class itself so using below (and not inspect)
    # https://stackoverflow.com/questions/697320/how-do-i-get-the-filepath-for-a-class-in-python
    el = os.path.abspath(sys.modules[func.__module__].__file__)
    return el


def open_view(request):
    view_name = _retrieve_view_name(request)
    return open_element(view_name)


class MustSpecifyIDE(BaseException):
    pass


class ProblemWithIDEPath(BaseException):
    pass


def open_element(el):
    if sys.platform == 'win32':
        ide = None
        try:
            ide = settings.DJANGO_WINDOWS_IDE
        except AttributeError:
            pass
        if not ide:
            raise MustSpecifyIDE(f'To open {el} with your default IDE please specify '
                                 f'DJANGO_WINDOWS_IDE path in your settings')
        try:
            subprocess.check_call([ide, el])
        except FileNotFoundError:
            raise ProblemWithIDEPath(f'The path your specified for your IDE executable (via DJANGO_WINDOWS_IDE in '
                                     f'settings) is incorrect: {ide}')


    elif sys.platform == 'darwin':
        subprocess.call(('open', el))

    else:
        try:
            subprocess.Popen(['xdg-open', el])
        except OSError:
            pass
    return JsonResponse({})
