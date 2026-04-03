from django.db import models
from aluno.models import Sexo

class Titulacao(models.Model):
    descricao = models.CharField(max_length=255)    

    def __str__(self):
        return self.descricao

# Create your models here.
class Professor(models.Model):
    # campo nome
    nome = models.CharField(max_length=255)
    #campo email, do tipo email, e configurado com unique (nao permite duplicacao)
    email = models.EmailField(max_length=100,blank=True, null=True,unique="true")
    # campo titulacao
    titulacao = models.ForeignKey(Titulacao,default=1,blank=False, null=False, on_delete=models.PROTECT)
    #campo sexo vem do model sexo, com a protecao, ou seja, nao é possível deletar um registro da tabela sexo se ele estiver sendo  usado na tabela aluno
    sexo = models.ForeignKey(Sexo, default=1, blank=False, null=False, on_delete=models.PROTECT)    
    #campo telefone do tipo texto
    telefone = models.CharField(max_length=20,default="Não informado")
    #campo telefone do tipo texto
    endereco = models.CharField(max_length=255,blank=True, default="Não informado")
    
    def __str__(self):
        return self.nome
    
