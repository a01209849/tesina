from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'analisis'

urlpatterns = [
    path('', views.Index, name='index'),
]
