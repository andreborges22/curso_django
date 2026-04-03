# import do path usado para roteamento
from django.urls import path
# import das views
from . import views
# configurando o namespace para ser usado no menu
app_name = 'aluno'

# roteamento do app
urlpatterns = [
    # se estiver na raiz do aluno
    path('', views.home, name='home'),
    # ao clicar no botao salvar
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    # ao clicar no link listar
    path('listar/', views.listar, name='listar'),
    # ao clicar no link buscar
    path('buscar/', views.buscar, name='buscar'),
    # ao clicar no link editar
    path('editar/<int:id>', views.editar, name='editar'),
    # ao clicar no botao salvar da tela de editar
    path('update/<int:id>', views.update, name='update'),
    # ao clicar no botao Excluir na home do aluno
    path('excluir/<int:id>', views.excluir, name='excluir'),
]
