from django.urls import path
from . import views

urlpatterns = [
    path("dash/", views.index, name="dash"),
    path("products/", views.produtos, name="products"),
    path("orders/", views.pedidos, name="orders"),
    path("users/", views.users, name="users"),
    path("user/", views.user, name="user"),
    path("register/", views.register, name="register"),
    path('deletar-pedido/<int:pedido_id>/', views.deletar_pedido, name='deletar_pedido'),
    path('products/add_stock/<int:id>/', views.aumentar_estoque, name='add_stock'),
    path('products/delete/<int:id>/', views.deletar_produto, name='delete_product'),
    

    
    #path('ver_assuntos/', views.ver, name='ver_assunto'),
    #path('login_site/', views.login, name="entrar_site"),
    #path('site_principal/', views.lista_produtos, name='site_primario')
]