from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=255)
    genero = models.CharField(max_length=12)

    objectos = models.Manager()

