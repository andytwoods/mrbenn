from django.urls import include, path
from django.views.generic import TemplateView
import debug_toolbar

urlpatterns = [
    path("__debug__/", include(debug_toolbar.urls)),
    path("", TemplateView.as_view(template_name='index.html'))
]