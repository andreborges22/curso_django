# importando objetos render e redirect, usados nos métodos
from django.shortcuts import render, redirect
# importando httpresponse, responsável por imprimir mensagens na tela
from django.http import HttpResponse
# importando models que são usados para acesso ao banco
from .models import Aluno, Sexo

# Create your views here.

# método para renderizar a home do aluno


def home(request):
    # atribuindos todos os alunos do banco de dados à variável alunos
    alunos = Aluno.objects.all()
    # atribuindos todas as descricoes de sexo do banco de dados à variável sexos
    sexos = Sexo.objects.all()
    # retorna a renderização da home do aluno juntamente com os alunos e os sexcos
    return render(request, 'aluno/home.html', {
        'alunos': alunos,
        'sexos': sexos
    })

# método para criar um aluno


def cadastrar(request):
    # resgatando os dados enviado via formulario
    nome = request.POST.get("nome")
    email = request.POST.get("email")
    sexo_id = request.POST.get("sexo")
    telefone = request.POST.get("telefone")
    endereco = request.POST.get("endereco")
    # iniciando tratamento de exceção
    try:
        # criando um objeto aluno
        Aluno.objects.create(
            # atribuindo os dados vindos do formularios ao objeto aluno
            nome=nome,
            email=email,
            sexo_id=sexo_id,
            telefone=telefone,
            endereco=endereco)

    # Capturando uma excecao
    except Exception as erro:
        # imprimindo o erro
        print(f"Erro: {erro}")
    # redirecionando para a home
    return redirect(home)

# método para editar um aluno
def editar(request, id):
    try:
        # presgatando do banco o aluno cujo id é igual ao id enviado via template
        aluno = Aluno.objects.get(id=id)
        # pegando todos os sexos do banco
        sexos = Sexo.objects.all()
        # renderizando a pagina aluno/update.html juntamente com o formulario preenchido com os dados do aluno a ser atualizado
        return render(request, "aluno/editar.html", {
            "aluno": aluno,
            "sexos": sexos
        })
    # capturando excecao e printando na tela
    except Exception as erro:
        print(f"Erro: {erro}")


# método para atualizar um aluno
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
    # capturando exceção
    except Exception as erro:
        print(f"Erro: {erro}")
    # redirecionando para a home
    return redirect(home)

# método para excluir um aluno
def excluir(request, id):
    try:
        # pegar o aluno específico do banco
        aluno = Aluno.objects.get(id=id)
        # apagar do banco
        aluno.objects.delete()
        # redirecionar para a home
    except Exception as erro:
        print(f"Erro: {erro}")
    # redirecionando para a home
    return redirect(home)
