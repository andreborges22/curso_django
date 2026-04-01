from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# importando o objeto messages, para interação na tela
from django.contrib import messages
from aluno.models import Sexo


# Create your views here.
def home(request):
    sexos = Sexo.objects.all()
    return render(request, 'usuario/home.html', {'sexos': sexos})


def cadastrar(request):

    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    try:
        user = User.objects.filter(username=nome).first()
        if (user):
            messages.error(
                request, f"já existe um usuário com esse nome ({nome})")
            return redirect('usuario:home')
        user = User.objects.create_user(
            username=nome, email=email, password=senha)
        user.save()
        messages.success(
            request, f"Usuário {nome} cadastrado com sucesso")
        return redirect('usuario:home')
    except Exception as erro:
        messages.error(request, f"({erro})")
        return redirect('usuario:home')
