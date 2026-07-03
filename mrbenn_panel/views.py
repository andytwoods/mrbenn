import os
import subprocess
import sys

from debug_toolbar.decorators import require_show_toolbar
from django.conf import settings
from django.http import Http404, HttpResponseBadRequest, JsonResponse
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.urls import Resolver404, resolve
from django.views.decorators.http import require_POST


class MustSpecifyIDE(Exception):
    pass


class ProblemWithIDEPath(Exception):
    pass


def _param(request, name):
    """Read a parameter from POST (preferred) or GET."""
    return request.POST.get(name) or request.GET.get(name)


def _retrieve_template_name(request):
    """Resolve the on-disk path of the template named in the request.

    Returns ``None`` if no template is given or it cannot be resolved. Django's
    template loaders (``safe_join``) reject ``..`` and absolute paths, so this
    can only ever point at a real template on the configured search path.
    """
    template_name = _param(request, 'template')
    if not template_name:
        return None
    try:
        template = get_template(template_name)
    except TemplateDoesNotExist:
        return None
    origin = getattr(template, 'origin', None)
    return getattr(origin, 'name', None)


def _extract_func(request):
    """Resolve the view callable for the request-supplied URL path.

    The path is taken from an explicit ``path`` parameter (not the ``Referer``
    header, which is attacker-controlled) and must resolve against the project's
    URLconf, so it can only ever reference a real, routed view.
    """
    path = _param(request, 'path')
    if not path:
        return None
    try:
        match = resolve(path)
    except Resolver404:
        return None
    return match.func


def _retrieve_view_name(request):
    func = _extract_func(request)
    if func is None:
        return None
    module = sys.modules.get(func.__module__)
    filename = getattr(module, '__file__', None)
    if not filename:
        return None
    # was having issues with parent classes being returned not class itself so using below (and not inspect)
    # https://stackoverflow.com/questions/697320/how-do-i-get-the-filepath-for-a-class-in-python
    return os.path.abspath(filename)


@require_show_toolbar
@require_POST
def open_template(request):
    template_name = _retrieve_template_name(request)
    if not template_name:
        return HttpResponseBadRequest("Unknown or missing template")
    return open_element(template_name)


@require_show_toolbar
@require_POST
def open_view(request):
    view_name = _retrieve_view_name(request)
    if not view_name:
        return HttpResponseBadRequest("Unknown or missing view")
    return open_element(view_name)


def open_element(el):
    # Defence in depth: never hand a path that isn't a real file to the OS.
    if not el or not os.path.exists(el):
        raise Http404(f"{el} does not exist")

    if sys.platform == 'win32':
        ide = getattr(settings, 'DJANGO_WINDOWS_IDE', None)
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
