from django.urls import path
from . import views

urlpatterns = [
    path('ver_assuntos/', views.ver, name='ver_assunto'),
    path('login_site/', views.login, name="entrar_site"),
    path('site_principal/', views.lista_produtos, name='site_primario'),
    path('pagar/', views.pagar_produto, name = "pagar_produto"),
    path('pagamento_sucesso/', views.pagamento_sucesso, name="pagamento_sucesso")
]