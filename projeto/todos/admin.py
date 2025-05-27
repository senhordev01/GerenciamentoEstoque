from django.contrib import admin
from .models import Produto, Pedido, UserProfile#Dados
# Register your models here.

admin.site.site_header = "Estoque Admin"

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'estoque')
    list_filter = ['categoria']
    search_fields = ['name']

class PedidoAdmin(admin.ModelAdmin):
    model = Pedido
    list_display = ("produto", "criado_por", "pedidoQuantidade", "data")
    list_filter = ["data"]
    search_fields = ["produto"]

class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    list_display = ("user", "physical_address", "mobile", "picture")
    list_filter = ["user"]
    search_fields = ["user"]

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(UserProfile, UserProfileAdmin)

#@admin.register(Dados)
#class DadosAdmin(admin.ModelAdmin):
#    list_display = ('nome', 'email', 'senha')
#    list_editable = ('email', 'senha')
#    search_fields = ('nome', 'email')