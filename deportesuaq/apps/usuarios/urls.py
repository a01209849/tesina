from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('', views.Index, name='index'),
    path('nuevo_usuario/', views.Nuevo_usuario, name='nuevo_usuario'),
    path('crear_usuario/', views.Crear_usuario, name='crear_usuario'),
    path('crear_datos_usuario/<id_user>/', views.Crear_datos_usuario, name='crear_datos_usuario'),
    path('guardar_datos_usuario/<id_user>/', views.Guardar_datos_usuario, name='guardar_datos_usuario'),
    path('cambiar_datos/<id_user>/', views.Cambiar_datos, name='cambiar_datos'),
    path('guardar_cambio_datos/<id_user>/', views.Guardar_cambio_datos, name='guardar_cambio_datos'),
    path('cambiar_contraseña/<id_user>/', views.Cambiar_contrasena, name='cambiar_contrasena'),
    path('guardar_contraseña/<id_user>/', views.Guardar_contrasena, name='guardar_contrasena'),
    path('borrar_usuario/<id_user>/', views.Borrar_usuario, name='borrar_usuario'),
]
