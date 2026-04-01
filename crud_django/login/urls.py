from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
    path('',views.home, name='home'),
    path('login/',views.login, name='login'),
    path('logout/', views.sair, name='logout'),
]