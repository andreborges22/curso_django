from django.db import models

# Create your models here.
# modelagem da classe Aluno


class Aluno(models.Model):
    # definicao do campo para armazenar o nome do Aluno
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=100,default="sememail@gmail.com",unique="true")
    sexo = models.CharField(max_length=20,default="Não informado")
    telefone = models.CharField(max_length=20,default="Não informado")
    endereco = models.CharField(max_length=255,default="Não informado")
    

    # método para imprimir o nome do aluno
    def __str__(self):
        return self.nome

class Sexo(models.Model):
    descricao = models.CharField(max_length=100)

    # método para imprimir a descrição
    def __str__(self):
        return self.descricao
