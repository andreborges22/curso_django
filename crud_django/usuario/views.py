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
# importacao para consultas (query)
from django.db.models import Q

from django.http import JsonResponse


def verificar_email(request):
    email = request.GET.get('email', None)
    existe = User.objects.filter(email=email).exists()
    return JsonResponse({'existe': existe})


def verificar_username(request):
    username = request.GET.get('username', None)
    existe = User.objects.filter(username=username).exists()
    return JsonResponse({'existe': existe})


# Create your views here.
def home(request):
    if not request.user.is_staff:
        return render(request, 'sisifba/home.html')
    else:
        sexos = Sexo.objects.all()
        usuarios = User.objects.all()
        return render(request, 'usuario/home.html',
                      {'sexos': sexos,
                       "usuarios": usuarios,
                       })


def cadastrar(request):
    if not request.user.is_staff:
        return render(request, 'sisifba/home.html')
    else:
        if request.method == "GET":
            return redirect('usuario:home')
        else:
            first_name = request.POST.get('first_name')
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            is_staff = request.POST.get('is_staff')
            is_active = request.POST.get('is_active')
            try:
                user = User.objects.filter(username=username).first()
                if (user):
                    messages.warning(
                        request, f"já existe um usuário com esse username ({username})")
                    return redirect('usuario:home')
                user = User.objects.create_user(
                    first_name=first_name, username=username, email=email, password=password, is_staff=is_staff,is_active = is_active)
                user.save()
                messages.success(
                    request, f"Usuário {first_name} cadastrado com sucesso")
                return redirect('usuario:home')
            except IntegrityError:
                messages.error(request, "Este email já está cadastrado!")
                return redirect('usuario:home')
            except Exception as erro:
                messages.error(request, f"({erro})")
                return redirect('usuario:home')


def listar(request):
    if not request.user.is_staff:
        return render(request, 'sisifba/home.html')
    else:
        usuarios = User.objects.all()

        query = request.GET.get('q')  # pega o termo digitado

        usuarios = User.objects.all()

        if query:
            usuarios = usuarios.filter(
                Q(first_name__icontains=query) |
                Q(username__icontains=query) |
                Q(email__icontains=query)
            )

        return render(request, 'usuario/listar.html', {
            'usuarios': usuarios,
            'query': query
        })


def editar(request, id):
    try:
        # resgatando do banco o aluno cujo id é igual ao id enviado via template
        usuario = User.objects.get(id=id)
        # pegando todos os sexos do banco
        # pegando todos os cursos do banco
        # renderizando a pagina aluno/editar.html juntamente com o formulario preenchido com os dados do aluno a ser atualizado
        return render(request, "usuario/editar.html", {
            "usuario": usuario,
        })
    # capturando excecao e printando na tela
    except Exception as erro:
        # imprimindo o erro
        messages.error(request, f"Erro: {erro}")
        # redirecionando para a home do aluno
        return redirect('usuario:home')

def update(request, id):
    # resgatando dados do formulario da página editar
    first_name = request.POST.get("first_name")
    username = request.POST.get("username")
    email = request.POST.get("email")
    is_staff = request.POST.get("is_staff")
    is_active = request.POST.get("is_active")
    try:
        # resgatando o aluno do banco que esta sendo editado
        usuario = User.objects.get(id=id)
        # atualizando os dados do banco com os dados vindos do formulário
        usuario.first_name = first_name
        usuario.username = username
        usuario.email = email
        usuario.is_staff = is_staff
        usuario.is_active = is_active
        # salvando os novos dados no banco
        usuario.save()
        # acrescentando a mensagem de sucesso no objeto messages (isso será recuperado e exibido na página html)
        messages.success(
            request, f"Usuario {first_name} editado(a) com sucesso!")
        # redirecionando para a home
        return redirect('usuario:home')
    # capturando exceção
    except Exception as erro:
        # imprimindo o erro
        messages.error(request, f"Erro: {erro}")
        # redirecionando para a home do aluno
        return redirect('usuario:home')
    
def excluir(request, id):
    try:
        # pegar o objeto específico do banco
        usuario = User.objects.get(id=id)
        # apagar do banco
        usuario.delete()
        # redirecionando para a home
        messages.warning(
            request, f"Usuário {usuario.username} removido(a) com sucesso!"
        )
        # redirecionando para a home do aluno
        return redirect('usuario:home')
    # capturando exceção
    except Exception as erro:
        # imprimindo erro
        messages.error(request, f"Erro: {erro}")
        return redirect('usuario:home')
