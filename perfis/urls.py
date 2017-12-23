from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('perfis/<int:perfil>', views.exibir, name='perfil'),
    path('perfis/<int:perfil>/convidar', views.convidar, name='convidar')
]
