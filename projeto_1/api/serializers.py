from rest_framework import serializers
from aluno.models import Aluno
from curso.models import Curso
from professor.models import Professor


# cria campos do aluno com base no modelo
class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        # retorna todos os campos do banco
        fields = "__all__"
        # se quiser apenas alguns campos especificos, faz dessa forma:
        # fields = ["id","nome"]

# cria campos do curso com base no modelo
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        # retorna todos os campos do banco
        fields = "__all__"
        # se quiser apenas alguns campos especificos, faz dessa forma:
        # fields = ["id","nome"]

# cria campos do curso com base no modelo
class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        # retorna todos os campos do banco
        fields = "__all__"
        # se quiser apenas alguns campos especificos, faz dessa forma:
        # fields = ["id","nome"]