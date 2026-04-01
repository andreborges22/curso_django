# importando objetos render e redirect, usados nos métodos
from django.shortcuts import render, redirect
# importando httpresponse, responsável por imprimir mensagens na tela
from django.http import HttpResponse
# importando models que são usados para acesso ao banco
from .models import Aluno, Sexo
# importando o objeto messages, para interação na tela
from django.contrib import messages



# Create your views here.

# método para renderizar a home_aluno do aluno


def home_aluno(request):
    if not request.user.is_authenticated:
        return redirect('login:home')
    else:        
        # atribuindos todos os alunos do banco de dados à variável alunos
        alunos = Aluno.objects.all()
        # atribuindos todas as descricoes de sexo do banco de dados à variável sexos
        sexos = Sexo.objects.all()
        # retorna a renderização da home_aluno do aluno juntamente com os alunos e os sexcos
        return render(request, 'aluno/home.html', {
            'alunos': alunos,
            'sexos': sexos
        })


def listar(request):
    if not request.user.is_authenticated:
        return redirect('login:home')
    else:
        # atribuindos todos os alunos do banco de dados à variável alunos
        alunos = Aluno.objects.all()
        # atribuindos todas as descricoes de sexo do banco de dados à variável sexos
        sexos = Sexo.objects.all()
        # retorna a renderização da home_aluno do aluno juntamente com os alunos e os sexcos
        return render(request, 'aluno/listar.html', {
            'alunos': alunos,
            'sexos': sexos
        })

# método para criar um aluno


def cadastrar(request):
    if not request.user.is_authenticated:
        return redirect('login:home')
    else:
        # se os dados foram enviados via get    
        # atribuindos todas as descricoes de sexo do banco de dados à variável sexos
        sexos = Sexo.objects.all()
        # testo o tipo da requisição
        # se for GET mostro o formulário
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
                aluno.save()
                messages.success(
                    request, f"Estudante {nome} cadastrado(a) com sucesso!")
            # Capturando uma excecao
            except Exception as erro:
                # imprimindo o erro
                messages.success(
                    request, f"Estudante {nome} cadastrado(a) com sucesso!")
                return redirect('aluno:home_aluno')


def editar(request, id):
    if not request.user.is_authenticated:
        return redirect('login:home')
    else:
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
            messages.error(request, f"Erro: {erro}")
            return redirect('aluno:home_aluno')


# método para atualizar um aluno
def update(request, id):
    if not request.user.is_authenticated:
        return redirect('login:home')
    else:
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
            messages.success(request, f"Estudante {nome} editado(a) com sucesso!")
            # redirecionando para a home_aluno
            return redirect('aluno:listar')
        # capturando exceção
        except Exception as erro:
            messages.error(request, f"Erro: {erro}")
            return redirect('aluno:home_aluno')

# método para excluir um aluno


def excluir(request, id):
    if not request.user.is_authenticated:
        return redirect('login:home')
    else:
        try:
            # pegar o aluno específico do banco
            aluno = Aluno.objects.get(id=id)
            # apagar do banco
            aluno.delete()
            # redirecionando para a home_aluno
            messages.success(
                request, f"Estudante {aluno.nome} removido(a) com sucesso!"
            )
            return redirect('aluno:home_aluno')
        except Exception as erro:
            messages.error(request, f"Erro: {erro}")
            return redirect('aluno:home_aluno')
