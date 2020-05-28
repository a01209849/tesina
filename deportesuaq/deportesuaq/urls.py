from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.login.urls')),
    path('usuarios/', include('apps.usuarios.urls')),
    path('pacientes/', include('apps.pacientes.urls')),
    path('terapias/', include('apps.terapias.urls')),
    path('lesiones/', include('apps.lesiones.urls')),
    path('analisis/', include('apps.analisis.urls')),
]
