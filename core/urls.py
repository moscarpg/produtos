from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)