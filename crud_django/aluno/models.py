from django.db import models


# Create your models here.
# modelagem da classe Aluno


class Aluno(models.Model):
    #definicao dos campos para armazenar os dados do Aluno
    #campo nome do tipo texto
    nome = models.CharField(max_length=255)
    #campo email, do tipo email, e configurado com unique (nao permite duplicacao)
    email = models.EmailField(max_length=100,default="sememail@gmail.com",unique="true")
    #campo sexo vem do model sexo, com a protecao, ou seja, nao é possível deletar um registro da tabela sexo se ele estiver sendo  usado na tabela aluno
    sexo = models.ForeignKey("Sexo", default=1, on_delete=models.PROTECT)    
    #campo telefone do tipo texto
    telefone = models.CharField(max_length=20,default="Não informado")
    #campo telefone do tipo texto
    endereco = models.CharField(max_length=255,default="Não informado")
    

    # método para imprimir o nome do aluno
    def __str__(self):
        return self.nome

# model sexo para armazenar tipo de sexo
class Sexo(models.Model):
    descricao = models.CharField(max_length=100)

    # método para imprimir a descrição do sexo
    def __str__(self):
        return self.descricao
