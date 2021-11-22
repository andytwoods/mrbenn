from debug_toolbar.panels import Panel
# Code taken and adapted from Simon Willison and Django Snippets:
# https://www.djangosnippets.org/snippets/766/
from debug_toolbar.panels.templates import TemplatesPanel
from debug_toolbar.utils import get_name_from_obj
from django.template import loader
from django.test.signals import template_rendered
from django.urls import path, resolve
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from frogpanel import views


class FrogPanel(TemplatesPanel):
    """
    A panel that lists all templates used during processing of a response.
    """
    template_names = []

    nav_title = _("Load in IDE")

    @property
    def title(self):
        return 'From panel'

    @property
    def nav_subtitle(self):
        """
        Show abbreviated name of view function as subtitle
        """

        match = resolve(self.toolbar.request.path)
        func, args, kwargs = match
        view_name = get_name_from_obj(func)

        template = loader.get_template('frogpanel/frogtitle.html')
        context = {
            'template_name': self.templates[0]["template"].name if self.templates else '',
            'view_name': view_name,
        }
        return mark_safe(template.render(context=context))

    template = "frogpanel/frogpanel.html"

    @classmethod
    def get_urls(cls):
        return [
            path("open_template/", views.open_template, name="open_template"),
            path("open_view/", views.open_view, name="open_view"),
        ]

    def generate_stats(self, request, response):
        pass

