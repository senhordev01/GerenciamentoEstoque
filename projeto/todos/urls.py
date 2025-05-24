from django.urls import path
from . import views

urlpatterns = [
    path('ver_assuntos/', views.ver, name='ver_assunto'),
    path('login_site/', views.login, name="entrar_site"),
    path('site_principal/', views.lista_produtos, name='site_primario')
]