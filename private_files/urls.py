from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('files.urls', namespace='files')),
    path('api-v2/', include('files.api.urls', namespace='api'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
