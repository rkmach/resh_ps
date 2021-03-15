from django.urls import path, include
from rest_framework import routers
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("pages/", include("pages.urls", namespace="pages")),
    path("users/", include("users.urls", namespace="users")),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]  + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)