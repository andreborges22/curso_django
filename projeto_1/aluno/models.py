from django.db import models
# importando o modelo Curso, para usarmos ele como chave estrangeira da tabela Aluno
from curso.models import Curso

# Create your models here.
# aqui criamos uma classe que será convertida em uma tabela no banco de dasdos


class Aluno(models.Model):
    # campo texto
    nome = models.CharField(max_length=100)
    # campo especifico para email
    email = models.EmailField(max_length=50)
    # campo data
    nascimento = models.DateField(null=True)
    # campo texto
    cep = models.CharField(max_length=10)
    # campo texto
    bairro = models.CharField(max_length=100, default="")
    # campo texto
    logradouro = models.CharField(max_length=100, default="")
    # campo texto
    numero = models.CharField(max_length=10, default="")
    # campo texto
    cidade = models.CharField(max_length=100, default="")
    # campo texto
    estado = models.CharField(max_length=2, default="")
    # campo chave estrangeira, aqui estamos fazendo um relacionamento com o model curso
    curso = models.ForeignKey(Curso, default=1, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome
