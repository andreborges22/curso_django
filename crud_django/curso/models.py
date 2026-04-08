from django.db import models
from professor.models import Professor

# Create your models here.
# modelando a tabela Curso


class Curso(models.Model):
    nome = models.CharField(max_length=50, blank='false', null=False)
    carga_horaria = models.IntegerField(default=0, blank='false', null=False)
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome
