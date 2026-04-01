from django.db import models

class Titulacao(models.Model):
    descricao = models.CharField(max_length=255)    

    def __str__(self):
        return self.descricao

# Create your models here.
class Professor(models.Model):
    nome = models.CharField(max_length=255)
    titulacao = models.ForeignKey(Titulacao,default=1,blank=False, null=False, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.nome
    
