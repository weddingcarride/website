from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.views.static import serve
from django.urls import re_path as url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('gallery/', include('gallery.urls')),

    url(r'^static/(?P<path>.*)$', serve,
        {'document_root': settings.STATIC_ROOT})
]