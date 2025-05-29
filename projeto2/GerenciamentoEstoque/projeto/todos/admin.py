from django.contrib import admin
from .models import Produto, Dados, Pagamento
# Register your models here.

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'disponivel')
    list_editable = ('preco', 'estoque')

@admin.register(Dados)
class DadosAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'email', 'senha')
    list_editable = ('email', 'senha')
    search_fields = ('usuario', 'email')

@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'produto', 'quantidade', 'total', 'data')