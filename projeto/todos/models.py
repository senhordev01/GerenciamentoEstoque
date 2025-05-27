from email.policy import default
from django.db import models
from django.contrib.auth.models import User


CATEGORY = (
    ("Stationary", "Stationary"),
    ("Electronics", "Electronics"),
    ("Food", "Food"),
)


# Create your models here.
#class Dados(models.Model):
#    nome = models.CharField(max_length=100)
#    email = models.CharField(max_length= 100, unique=True)
#    senha = models.CharField(max_length=50)

#    def __str__(self):
#        return self.nome

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    physical_address = models.CharField(max_length=40, null=True)
    mobile = models.CharField(max_length=12, null=True)
    picture = models.ImageField(default="avatar.jpeg", upload_to="Pictures")

    def __str__(self) -> str:
        return self.user.username

class Produto(models.Model):
    nome = models.CharField(max_length=100, null=True)
    descricao = models.TextField()
    categoria = models.CharField(max_length=20, choices=CATEGORY, null=True)
    #preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    disponivel = models.BooleanField(default=True)
    def __str__(self):
        return self.nome
    
class Pedido(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, null=True)
    criado_por = models.ForeignKey(User, models.CASCADE, null=True)
    pedidoQuantidade = models.PositiveIntegerField(null=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.produto} pediu: {self.pedidoQuantidade}"