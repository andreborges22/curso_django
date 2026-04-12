from django.shortcuts import render, redirect
from curso.models import Curso, Professor
# importando o objeto messages, para interação na tela
from django.contrib import messages
# importacao para definir que uma função só será acessível para usuarios autenticados
from django.contrib.auth.decorators import login_required
# importacao para consultas (query)
from django.db.models import Q

# Create your views here.
# view que renderiza a home


def home(request):
    cursos = Curso.objects.all()
    professores = Professor.objects.all()
    # testo o tipo da requisição
    # se for GET renderiza o formulário
    if request.method == "GET":
        return render(request, 'curso/home.html', {
            'professores': professores,
            'cursos': cursos,
        })


def cadastrar(request):

    # se os dados foram enviados via get
    # atribuindos todas as descricoes de sexo do banco de dados à variável sexos
    professores = Professor.objects.all()
    cursos = Curso.objects.all()
    # testo o tipo da requisição
    # se for GET renderiza o formulário
    if request.method == "GET":
        return render(request, 'curso/cadastrar.html', {
            'professores': professores,
            'cursos': cursos,
        })
    # se os dados foram enviados via POST
    else:
        # resgatando os dados enviado via formulario
        nome = request.POST.get("nome")
        carga_horaria = request.POST.get("carga_horaria")
        professor_id = request.POST.get("professor")
        # iniciando tratamento de exceção
        try:
            # criando um objeto aluno
            curso = Curso.objects.create(
                # atribuindo os dados vindos do formularios ao objeto aluno
                nome=nome,
                carga_horaria=carga_horaria,
                professor_id=professor_id,
            )
            # salvando no banco
            curso.save()
            # acrescentando a mensagem de sucesso no objeto messages (isso será recuperado e exibido na página html)
            messages.success(
                request, f"Curso {nome} cadastrado(a) com sucesso!")
            # redirecionando para a home do aluno
            return redirect('curso:home')
        # Capturando uma excecao
        except Exception as erro:
            # imprimindo o erro
            messages.error(request, f"Erro: {erro}")
            # redirecionando para a home do aluno
            return redirect('curso:home')


def buscar(request):
    cursos = Curso.objects.all()
    query = request.GET.get('q')  # pega o termo digitado

    if query:
        cursos = cursos.filter(
            Q(nome__icontains=query)
        )

    return render(request, 'curso/listar.html', {
        'cursos': cursos,
        'query': query
    })


def listar(request):
    cursos = Curso.objects.all()
    query = request.GET.get('q')  # pega o termo digitado

    if query:
        cursos = cursos.filter(
            Q(nome__icontains=query)
        )

    return render(request, 'curso/listar.html', {
        'cursos': cursos,
        'query': query
    })


def editar(request, id):
    try:
        # pegando todos os cursos do banco
        curso = Curso.objects.get(id=id)
        cursos = Curso.objects.all()
        professores = Professor.objects.all()
        # renderizando a pagina aluno/editar.html juntamente com o formulario preenchido com os dados do aluno a ser atualizado
        return render(request, "curso/editar.html", {
            "curso": curso,
            "cursos": cursos,
            'professores': professores,
        })
    # capturando excecao e printando na tela
    except Exception as erro:
        # imprimindo o erro
        messages.error(request, f"Erro: {erro}")
        # redirecionando para a home do curso
        return render(request, "curso/editar.html", {
            "professores": professores,
        })


def update(request, id):
    # resgatando dados do formulario da página editar
    nome = request.POST.get("nome")
    carga_horaria = request.POST.get("carga_horaria")
    professor_id = request.POST.get("professor")
    try:
        # resgatando o professor do banco que esta sendo editado
        curso = Curso.objects.get(id=id)
        # atualizando os dados do banco com os dados vindos do formulário
        curso.nome = nome
        curso.carga_horaria = carga_horaria
        curso.professor_id = professor_id
        # salvando os novos dados no banco
        curso.save()
        # acrescentando a mensagem de sucesso no objeto messages (isso será recuperado e exibido na página html)
        messages.success(
            request, f"Curso {nome} editado(a) com sucesso!")
        # redirecionando para a home_professor
        return redirect('curso:listar')
    # capturando exceção
    except Exception as erro:
        # imprimindo o erro
        messages.error(request, f"Erro: {erro}")
        # redirecionando para a home do professor
        return redirect('curso:home')


def excluir(request, id):
    try:
        # pegar o aluno específico do banco
        curso = Curso.objects.get(id=id)
        # apagar do banco
        curso.delete()
        # redirecionando para a home
        messages.warning(
            request, f"Curso {curso.nome} removido(a) com sucesso!"
        )
        # redirecionando para a home do aluno
        return redirect('curso:home')
    # capturando exceção
    except Exception as erro:
        # imprimindo erro
        messages.error(request, f"Erro: {erro}")
        return redirect('curso:home')
