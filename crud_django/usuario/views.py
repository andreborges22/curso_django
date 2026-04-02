# importação referentes a renderização e redirecionamento
from django.shortcuts import render, redirect
# importação referentes a manipulação do usuário do django
from django.contrib.auth.models import User
# importação o objeto messages, para interação na tela
from django.contrib import messages
# importação referentes ao model sexo
from aluno.models import Sexo
# importação referentes atratamento de exceção (mensagem específica de email duplicado)
from django.db import IntegrityError


# Create your views here.
def home(request):
    if not request.user.is_superuser:
        return redirect('core:home')
    else:
        sexos = Sexo.objects.all()
        return render(request, 'usuario/home.html', {'sexos': sexos})


def cadastrar(request):

    if request.method == "GET":
        return redirect('usuario:home')
    else:
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
        except IntegrityError:
            messages.error(request, "Este email já está cadastrado!")
            return redirect('aluno:home_aluno')
        except Exception as erro:
            messages.error(request, f"({erro})")
            return redirect('usuario:home')
