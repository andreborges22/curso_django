from django.urls import path
from . import views

app_name = 'aluno'

urlpatterns = [
    # se estiver na raiz do aluno
    path('', views.home_aluno, name='home_aluno'),
    # ao clicar no botao salvar
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    # ao clicar no link editar
    path('listar/', views.listar, name='listar'),
    # ao clicar no link editar
    path('editar/<int:id>', views.editar, name='editar'),
    # ao clicar no botao salvar da tela de editar
    path('update/<int:id>', views.update, name='update'),
    # ao clicar no botao Excluir na home do aluno
    path('excluir/<int:id>', views.excluir, name='excluir'),
]
