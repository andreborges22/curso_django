from django.urls import path
from . import views

app_name = 'usuario'

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('excluir/<int:id>', views.excluir, name='excluir'),
]
