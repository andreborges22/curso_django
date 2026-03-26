from django.contrib import admin
from .models import Aluno

# Register your models here.
# ao registrar um model aqui ele aparece no painel admin
admin.site.register(Aluno)