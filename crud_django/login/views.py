from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as login_django


# Create your views here.


def home(request):
    return render(request, 'login/login.html')


def login(request):
    nome = request.POST.get('nome')
    senha = request.POST.get('senha')

    try:
        user = authenticate(username=nome, password = senha)
        if user:            
            login_django(request,user)
            return redirect('core:home')
        else:
            #return HttpResponse(f"Usuário ou senha incorretos")
            messages.error(
                request, f"Usuário ou senha incorretos")
            return redirect('login:home')
    except Exception as erro:
        messages.error(request, f"({erro})")
        return redirect('login:home')

def sair(request):    
    logout(request)
    return redirect('login:home')  # ou qualquer página que você quiser