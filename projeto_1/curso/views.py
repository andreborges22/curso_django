from django.shortcuts import render
from curso.models import Curso
# Create your views here.
# view que renderiza a home


def home(request):
    cursos = Curso.objects.all()
    return render(request, 'curso/home.html', {'cursos': cursos})
