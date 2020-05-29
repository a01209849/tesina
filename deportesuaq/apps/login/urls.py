from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'login'

urlpatterns = [
    path('', views.Index, name='index'),
    path('inicio', views.Inicio, name='inicio'),
    path('user_login/',views.User_login,name='user_login'),
    path('user_logout/',views.User_logout,name='user_logout'),

]
