# importando objetos render e redirect, usados nos métodos
from django.shortcuts import render, redirect
# importando httpresponse, responsável por imprimir mensagens na tela
from django.http import HttpResponse
# importando models que são usados para acesso ao banco
from .models import Aluno, Sexo
# importando o objeto messages, para interação na tela
from django.contrib import messages
# importacao para definir que uma função só será acessível para usuarios autenticados
from django.contrib.auth.decorators import login_required
# importacao para consultas (query)
from django.db.models import Q


# Create your views here.

# método para renderizar a home do aluno


def home(request):
    if not request.user.is_authenticated:
        return redirect('login:home')
    else:
        # atribuindos todos os alunos do banco de dados à variável alunos
        alunos = Aluno.objects.all()
        # atribuindos todas as descricoes de sexo do banco de dados à variável sexos
        sexos = Sexo.objects.all()
        # retorna a renderização da home do aluno juntamente com os alunos e os sexcos
        return render(request, 'aluno/home.html', {
            'alunos': alunos,
            'sexos': sexos
        })

# decorator que define que a funcao irá verificar se o usuário está logado
# se não estiver, ele será direcionado para o login


# funcao buscar da página buscar
@login_required(login_url='/login/')
def buscar(request):
    query = request.GET.get('q')  # pega o termo digitado

    alunos = Aluno.objects.all()

    if query:
        alunos = alunos.filter(
            Q(nome__icontains=query) |
            Q(email__icontains=query)
        )

    return render(request, 'aluno/buscar.html', {
        'alunos': alunos,
        'query': query
    })

@login_required(login_url='/login/')
# função para listar/buscar alunos
def listar(request):
    # atribuindos todos os alunos do banco de dados à variável alunos
    alunos = Aluno.objects.all()
    # atribuindos todas as descricoes de sexo do banco de dados à variável sexos
    query = request.GET.get('q')  # pega o termo digitado

    if query:
        alunos = alunos.filter(
            Q(nome__icontains=query) |
            Q(email__icontains=query)
        )

    return render(request, 'aluno/buscar.html', {
        'alunos': alunos,
        'query': query
    })

# método para criar um aluno


@login_required(login_url='/login/')
# função para cadastrar usuários
def cadastrar(request):

    # se os dados foram enviados via get
    # atribuindos todas as descricoes de sexo do banco de dados à variável sexos
    sexos = Sexo.objects.all()
    # testo o tipo da requisição
    # se for GET renderiza o formulário
    if request.method == "GET":
        return render(request, 'aluno/cadastrar.html', {
            'sexos': sexos
        })
    # se os dados foram enviados via POST
    else:
        # resgatando os dados enviado via formulario
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        sexo_id = request.POST.get("sexo")
        telefone = request.POST.get("telefone")
        endereco = request.POST.get("endereco")
        # iniciando tratamento de exceção
        try:
            # criando um objeto aluno
            aluno = Aluno.objects.create(
                # atribuindo os dados vindos do formularios ao objeto aluno
                nome=nome,
                email=email,
                sexo_id=sexo_id,
                telefone=telefone,
                endereco=endereco)
            # salvando no banco
            aluno.save()
            # acrescentando a mensagem de sucesso no objeto messages (isso será recuperado e exibido na página html)
            messages.success(
                request, f"Estudante {nome} cadastrado(a) com sucesso!")
            # redirecionando para a home do aluno
            return redirect('aluno:home')
        # Capturando uma excecao
        except Exception as erro:
            # imprimindo o erro
            messages.error(request, f"Erro: {erro}")
            # redirecionando para a home do aluno
            return redirect('aluno:home')


@login_required(login_url='/login/')
def editar(request, id):
    try:
        # resgatando do banco o aluno cujo id é igual ao id enviado via template
        aluno = Aluno.objects.get(id=id)
        # pegando todos os sexos do banco
        sexos = Sexo.objects.all()
        # renderizando a pagina aluno/editar.html juntamente com o formulario preenchido com os dados do aluno a ser atualizado
        return render(request, "aluno/editar.html", {
            "aluno": aluno,
            "sexos": sexos
        })
    # capturando excecao e printando na tela
    except Exception as erro:
        # imprimindo o erro
        messages.error(request, f"Erro: {erro}")
        # redirecionando para a home do aluno
        return redirect('aluno:home')


# método para atualizar um aluno
@login_required(login_url='/login/')
def update(request, id):
    # resgatando dados do formulario da página editar
    nome = request.POST.get("nome")
    email = request.POST.get("email")
    sexo_id = request.POST.get("sexo")
    telefone = request.POST.get("telefone")
    endereco = request.POST.get("endereco")
    try:
        # resgatando o aluno do banco que esta sendo editado
        aluno = Aluno.objects.get(id=id)
        # atualizando os dados do banco com os dados vindos do formulário
        aluno.nome = nome
        aluno.email = email
        aluno.sexo_id = sexo_id
        aluno.telefone = telefone
        aluno.endereco = endereco
        # salvando os novos dados no banco
        aluno.save()
        # acrescentando a mensagem de sucesso no objeto messages (isso será recuperado e exibido na página html)
        messages.success(
            request, f"Estudante {nome} editado(a) com sucesso!")
        # redirecionando para a home
        return redirect('aluno:listar')
    # capturando exceção
    except Exception as erro:
        # imprimindo o erro
        messages.error(request, f"Erro: {erro}")
        # redirecionando para a home do aluno
        return redirect('aluno:home')

# método para excluir um aluno


@login_required(login_url='/login/')
def excluir(request, id):
    try:
        # pegar o aluno específico do banco
        aluno = Aluno.objects.get(id=id)
        # apagar do banco
        aluno.delete()
        # redirecionando para a home
        messages.warning(
            request, f"Estudante {aluno.nome} removido(a) com sucesso!"
        )
        # redirecionando para a home do aluno
        return redirect('aluno:home')
    # capturando exceção
    except Exception as erro:
        # imprimindo erro
        messages.error(request, f"Erro: {erro}")
        return redirect('aluno:home')
