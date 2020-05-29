from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'pacientes'

urlpatterns = [
    path('', views.Index, name='index'),
    path('nuevo_paciente/', views.Nuevo_paciente, name='nuevo_paciente'),
    path('guardar_paciente/', views.Guardar_paciente, name='guardar_paciente'),
    path('antecedentes_paciente/<id_paciente>/', views.Antecedentes_paciente, name='antecedentes_paciente'),
    path('guardar_antecedentes/<id_paciente>/', views.Guardar_antecedentes, name='guardar_antecedentes'),
    path('borrar_paciente/<id_paciente>/', views.Borrar_paciente, name='borrar_paciente'),
    path('perfil_paciente/<id_paciente>/', views.Perfil_paciente, name='perfil_paciente'),
    path('editar_paciente/<id_paciente>/', views.Editar_paciente, name='editar_paciente'),
    path('guardar_editar_paciente/<id_paciente>/', views.Guardar_editar_paciente, name='guardar_editar_paciente'),
    path('editar_antecedente/<id_antecedente>/', views.Editar_antecedente, name='editar_antecedente'),
    path('guardar_editar_antecedente/<id_antecedente>/', views.Guardar_editar_antecedente, name='guardar_editar_antecedente'),
    path('borrar_antecedente/<id_antecedente>/', views.Borrar_antecedente, name='borrar_antecedente'),
    url(r'descargar_lesiones', views.Descargar_lesiones, {},name="descargar_lesiones")
]
