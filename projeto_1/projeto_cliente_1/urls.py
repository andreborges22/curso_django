"""
URL configuration for projeto_cliente_1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.viewsets import AlunoViewSet, CursoViewSet, ProfessorViewSet

# Routers provide an easy way of automatically determining the URL conf.
# Gera URLs automaticamente
# Cria as rotas do CRUD com base na ViewSet
# Adiciona a rota raiz da API (API Root)
router = routers.DefaultRouter()
router.register(r'alunos', AlunoViewSet)
router.register(r'cursos', CursoViewSet)
router.register(r'professores', ProfessorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('meu_app/', include('meu_app.urls')),
    path('aluno/', include('aluno.urls')),
    path('professor/', include('professor.urls')),
    path('curso/', include('curso.urls'),)
]