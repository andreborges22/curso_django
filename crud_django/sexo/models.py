from django.db import models

# Create your models here.
# model sexo para armazenar tipo de sexo


class Sexo(models.Model):
    descricao = models.CharField(max_length=50, unique=True)

    # método para imprimir a descrição do sexo
    def __str__(self):
        return self.descricao
