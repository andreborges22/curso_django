from django.urls import path
from . import views

app_name = 'usuario'

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('listar/', views.listar, name='listar'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('update/<int:id>', views.update, name='update'),
    path('excluir/<int:id>', views.excluir, name='excluir'),
    path('verificar-username/', views.verificar_username, name='verificar_username'),
    path('verificar-email/', views.verificar_email, name='verificar_email'),
]
