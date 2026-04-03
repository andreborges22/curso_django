from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as login_django


# Create your views here.

#home do app
def home(request):
    # renderiza a página de login
    return render(request, 'login/login.html')

#login no sistema
def login(request):
    # resgata dados do formulário
    nome = request.POST.get('nome')
    senha = request.POST.get('senha')
    # tratamento de exceção
    try:
        # tentando autenticar um usuário
        user = authenticate(username=nome, password = senha)
        # se usuário não for nulo
        if user:   
            # faz login de fato         
            login_django(request,user)
            # redirecionando para a home
            return render(request,'sisifba/home.html') 
        #se o usuaio for vazio (None) a autenticação falhou
        else:
            # adicionando mensagem de erro para ser exibida na tela
            messages.error(
                request, f"Usuário ou senha incorretos")
            # redirecionando para o login
            return redirect('login:home')
    # capturando exceção    
    except Exception as erro:
        # adicionando mensagem de erro para ser exibida na tela
        messages.error(request, f"({erro})")
        # redirecionando para o login
        return redirect('login:home')
# função de logout
def sair(request):    
    # faz o logout do sistema
    logout(request)
    # redirecionando para o login
    return redirect('login:home')  # ou qualquer página que você quiser