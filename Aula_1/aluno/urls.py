from django.urls import path
from . import views

urlpatterns = [  
    # se estiver na raiz do aluno  
    path('', views.home, name='home_aluno'),
    path('home/', views.home, name='home'),
    # ao clicar no botao salvar
    path('cadastrar/',views.cadastrar,name='cadastrar_aluno'),
    # ao clicar no link editar
    path('editar/<int:id>',views.editar,name='editar_aluno'),
    # ao clicar no botao salvar da tela de editar
    path('update/<int:id>',views.update,name='update_aluno'),
    # ao clicar no botao Excluir na home do aluno
    path('excluir/<int:id>',views.excluir,name='excluir_aluno'),
]
