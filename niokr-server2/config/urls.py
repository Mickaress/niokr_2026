import os

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('api/', include('api.urls')),
]

# Локально (DEBUG): Django отдаёт uploads. В проде обычно nginx/CDN; при необходимости —
# DJANGO_SERVE_MEDIA=1 (не рекомендуется как долгосрочное решение).
_serve_media = settings.DEBUG or os.environ.get('DJANGO_SERVE_MEDIA', '').lower() in (
    '1',
    'true',
    'yes',
)
if _serve_media:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
