from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('launcher.urls')),
    path('estoque/', include('estoque.urls')),
    path('whatsapp/', include('whatsapp.urls')),
]

handler404 = 'django.views.defaults.page_not_found'