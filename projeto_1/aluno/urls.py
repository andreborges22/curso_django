from django.urls import path
from . import views

urlpatterns = [
    #rota para a raiz do aluno. Quando o usuario digitar: enderecodosistema/aluno
    path('', views.home, name='home_aluno'),
    #rota para o cadastro do aluno. Quando o usuario enviar o formulario de cadastro: (enderecodosistema/aluno/cadastrar)
    path('cadastrar/', views.cadastrar_aluno, name="cadastrar"),
    #rota para o formulario de edição do aluno. Quando o usuario clicar em editar: (enderecodosistema/aluno/editar/id)
    path('editar/<int:id>', views.editar, name="editar"),
    #rota interna para edição de fato. Os dados do formulario de edo vao para persistencia em banco
    path('update/<int:id>', views.update, name="update"),
    #rota para o remocao do aluno. Quando o usuario clicar em deletar: (enderecodosistema/aluno/deletar/id)
    path('deletar/<int:id>', views.deletar_aluno, name="deletar")
]
