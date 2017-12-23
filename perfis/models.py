from django.db import models

# Create your models here.
class Perfil(models.Model):
    nome = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    telefone = models.CharField(max_length=15, null=False)
    nomeEmpresa = models.CharField(max_length=255, null=False)
