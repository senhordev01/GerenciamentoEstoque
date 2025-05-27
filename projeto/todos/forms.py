from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from todos.models import Pedido, Produto

class UserRegistry(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ["nome", "categoria", "estoque", "descricao"]

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ["produto", "pedidoQuantidade"]

