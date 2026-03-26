from rest_framework import viewsets
from aluno.models import Aluno
from curso.models import Curso
from professor.models import Professor
from .serializers import AlunoSerializer, CursoSerializer, ProfessorSerializer

# Create your views here.
# Implementa um crud completo para os alunos de forma automatica


class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

# Implementa um crud completo para os cursos de forma automatica


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

# Implementa um crud completo para os cursos de forma automatica


class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
