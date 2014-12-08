from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'core.views.home', name='home'),
    url(r'^history/', 'core.views.just_render', {"template": "core/history.html"}, name="history"),
    url(r'^varsity/', 'core.views.just_render', {"template": "core/varsity.html"}, name="varsity"),
    url(r'^cuhh/', 'core.views.just_render', {"template": "core/cuhh.html"}, name="cuhh"),
    url(r'^chugsbunny/', 'core.views.just_render', {"template": "core/Chugsbunny.html"}, name='Chugsbunny'),
    url(r'^admin/', include(admin.site.urls)),
)
