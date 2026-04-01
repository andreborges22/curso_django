from django.urls import path
from . import views

app_name = 'usuario'

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
]
