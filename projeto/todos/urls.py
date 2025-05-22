from django.urls import path
from . import views

urlpatterns = [
    path('ver_assuntos/', views.ver, name='ver_assunto')
]