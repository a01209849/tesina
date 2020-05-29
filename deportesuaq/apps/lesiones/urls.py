from django.urls import path
from . import views

app_name = 'lesiones'

urlpatterns = [
    path('crear_lesion/<id_paciente>/', views.Crear_lesion, name='crear_lesion'),
    path('guardar_lesion/<id_paciente>/', views.Guardar_lesion, name='guardar_lesion'),
    path('perfil_lesion/<id_lesion>/', views.Perfil_lesion, name='perfil_lesion'),
    path('editar_lesion/<id_lesion>/', views.Editar_lesion, name='editar_lesion'),
    path('guardar_editar_lesion/<id_lesion>/', views.Guardar_editar_lesion, name='guardar_editar_lesion'),
    path('terminar_lesion/<id_lesion>/', views.Terminar_lesion, name='terminar_lesion'),
    path('guardar_terminar_lesion/<id_lesion>/', views.Guardar_terminar_lesion, name='guardar_terminar_lesion'),
    path('borrar_lesion/<id_lesion>/', views.Borrar_lesion, name='borrar_lesion'),
]
