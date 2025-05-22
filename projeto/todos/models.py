from django.db import models

# Create your models here.
class Dados(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length= 100, unique=True)
    senha = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
