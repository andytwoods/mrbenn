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

from mrbenn_panel import views


class MrBennPanel(TemplatesPanel):
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
        Show abbreviated name of view function as subtitle.

        Reads from the stats recorded in ``generate_stats`` rather than from
        the live request/templates so the subtitle renders correctly when the
        toolbar is persisted and replayed (e.g. via the History panel). See
        https://github.com/django-commons/django-debug-toolbar/pull/2138
        """
        stats = self.get_stats()
        template = loader.get_template('mrbenn_panel/mrbenn_title.html')
        context = {
            'template_name': stats.get('mrbenn_template_name', ''),
            'view_name': stats.get('mrbenn_view_name', ''),
        }
        return mark_safe(template.render(context=context))

    template = "mrbenn_panel/mrbenn_panel.html"

    @classmethod
    def get_urls(cls):
        return [
            path("open_template/", views.open_template, name="open_template"),
            path("open_view/", views.open_view, name="open_view"),
        ]

    def generate_stats(self, request, response):
        # Store plain, serializable strings for the nav subtitle so it survives
        # persistence and replay (e.g. the History panel), instead of reading
        # live request/template state at render time.
        try:
            match = resolve(request.path)
            view_name = get_name_from_obj(match.func)
        except Exception:
            view_name = ''

        self.record_stats({
            'mrbenn_view_name': view_name,
            'mrbenn_template_name': self.templates[0]["template"].name if self.templates else '',
        })

