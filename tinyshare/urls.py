from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    url(r'^$', 'tiny_app.views.home', name='home'),
    url(r'^contact/$', 'tiny_app.views.contact', name='contact'),
    url(r'^about/$', 'tinyshare.views.about', name='about'),
    url(r'^admin/', include(admin.site.urls)),
    # Django Registration Redux
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^forums/', include('forums.urls', namespace='forums')),
    url(r'^form/$', 'tiny_app.views.form', name='form'),
    url(r'^upload/$', 'tiny_app.views.upload', name='upload'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_URL)

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
