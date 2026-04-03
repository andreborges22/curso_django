"""
URL configuration for sisifba project.

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
from . import views
#namespace do app
app_name = 'sisifba'

#roteamento do sistema
urlpatterns = [
    # se nao digitar nada, vai para raiz do projeto
    path('', views.home, name='home_sisifba'), 
    #ao digitar /login
    path('login/',include('login.urls')),
    #ao digitar /aluno   
    path('usuario/',include('usuario.urls')),
    #ao digitar /admin
    path('admin/', admin.site.urls), 
    #ao digitar /aluno
    path('aluno/',include('aluno.urls')),
    #ao digitar /aluno
    path('professor/',include('professor.urls')),
    #ao digitar /core           
    path('core/',include('core.urls')),   
]
