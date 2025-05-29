from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.FloatField()
    estoque = models.IntegerField()
    descricao = models.CharField(max_length=200)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Dados(models.Model):
    usuario = models.CharField(max_length=100)
    email = models.CharField(max_length= 100, unique=True)
    senha = models.CharField(max_length=50)

    def __str__(self):
        return self.usuario
    

class Pagamento(models.Model):
    usuario = models.ForeignKey('Dados', on_delete=models.CASCADE)
    produto = models.ForeignKey('Produto', on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    total = models.FloatField()
    data = models.DateTimeField(auto_now_add=True)



