from django.urls import path
from . import views
# namespace do app
app_name = 'login'

# roteamento
urlpatterns = [
    path('',views.home, name='home'),
    path('login/',views.login, name='login'),
    path('logout/', views.sair, name='logout'),
]