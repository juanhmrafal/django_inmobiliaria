from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inicio.urls')),
    path('contacto/', include('contacto.urls')),
    path('acceso/', include('acceso.urls')),
    path('nosotros/', include('nosotros.urls')),
]
