from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    url(r'^applications/$', views.index, name='index'),
    url(r'^application/new$', views.new, name='new'),
    url(r'^application/create$', views.create, name='create'),
    url(r'^application/(?P<application_id>[0-9]+)/$', views.show, name='show'),
    url(r'^application/(?P<application_id>[0-9]+)/download/$', views.download, name='download'),
    url(r'^developer/new$', views.new_developer, name='new_developer'),
    url(r'^developer/create$', views.create_developer, name='create_developer'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
