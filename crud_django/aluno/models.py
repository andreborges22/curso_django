from django.db import models
from curso.models import Curso
from sexo.models import Sexo


# Create your models here.

# modelagem da classe Aluno

# model aluno


class Aluno(models.Model):
    # definicao dos campos para armazenar os dados do Aluno
    # campo nome do tipo texto
    nome = models.CharField(max_length=255, blank=False, null=False)
    # campo email, do tipo email, e configurado com unique (nao permite duplicacao)
    email = models.EmailField(
        max_length=100, default="sememail@gmail.com", unique="true")
    # campo sexo vem do model sexo, com a protecao, ou seja, nao é possível deletar um registro da tabela sexo se ele estiver sendo  usado na tabela aluno
    sexo = models.ForeignKey(
        Sexo, default=1, on_delete=models.PROTECT, blank=False, null=False)
    # campo telefone do tipo texto
    telefone = models.CharField(max_length=20, default="Não informado")
    # campo telefone do tipo texto
    endereco = models.CharField(
        max_length=255, blank=True, default="Não informado")
    curso = models.ForeignKey(
        Curso, on_delete=models.PROTECT, blank=False, null=False)
    #data de criação
    data_criacao = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    #classe interna
    class Meta:
        # Define a ordenação padrão como decrescente pela data de criação
        ordering = ['-data_criacao']

    # método para imprimir o nome do aluno
    def __str__(self):
        return self.nome
