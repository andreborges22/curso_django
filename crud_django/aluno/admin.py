from django.contrib import admin
# importando a model Aluno
from .models import Aluno,Sexo

# Register your models here.
#registrando o model Aluno no admin
admin.site.register(Aluno)
admin.site.register(Sexo)