from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', 'core.views.home', name='home'),
    url(r'^history/', TemplateView.as_view(template_name="core/history.html"), name="history"),
    url(r'^varsity/', TemplateView.as_view(template_name="core/varsity.html"), name="varsity"),
    url(r'^cuhh/', TemplateView.as_view(template_name="core/cuhh.html"), name="cuhh"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^news/', include('news.urls', namespace="news")),
)
