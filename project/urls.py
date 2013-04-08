from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^example/', include('example.urls')),
)

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns("django.views.static",
        (r'^media/(?P<path>.*)$', 'serve',
         {'document_root': settings.MEDIA_ROOT}),
    )