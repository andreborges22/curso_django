from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Aluno, Curso
import requests


# Create your views here.
# metodo que renderiza a home dos alunos
def home(request):
    # atribuindo todos os registros da tabela Aluno  para a variavel alunos, para podermos usar na home do aluno
    alunos = Aluno.objects.all()
    # atribuindo todos os registros da tabela Curso  para a variavel cursos, para podermos usar na home do aluno
    cursos = Curso.objects.all()
    # renderizando a home junto com os objetos alunos e cursos
    return render(request, 'aluno/home.html', {"alunos": alunos, "cursos": cursos})


# metodo para cadastrar um aluno
def cadastrar_aluno(request):
    # atribuindo dados que chegam da requisicao (request) para variaveis locais
    nome = request.POST.get("nome")
    email = request.POST.get("email")
    nascimento = request.POST.get("nascimento")
    cep = request.POST.get("cep")
    bairro = request.POST.get("bairro")
    logradouro = request.POST.get("logradouro")
    numero = request.POST.get("numero")
    cidade = request.POST.get("localidade")
    estado = request.POST.get("estado")
    # neste ponto, estamos retornando o id do curso, mas ele chega como string.
    # ao usar o nome 'curso_id' o django converte o valor do campo que chega como string, em um valor inteiro
    # mesmo efeito que curso = int(request.POST.get("curso"))
    curso_id = request.POST.get("curso")
    # agora que ja temos os dados podemos salvar no banco.
    Aluno.objects.create(
        nome=nome,
        email=email,
        nascimento=nascimento,
        cep=cep,
        bairro=bairro,
        logradouro=logradouro,
        numero=numero,
        cidade=cidade,
        estado=estado,
        curso_id=curso_id,
    )
    # caso tudo dê certo, registramos uma mensagem de sucesso que seraá exibida na home
    messages.success(request, f"Estudante {nome} cadastrado(a) com sucesso!")
    # redirecionando para o metodo home
    return redirect(home)


# metodo editar aluno
def editar(request, id):
    # resgata do banco o usuario cujo id é o mesmo que foi passado via requisicao
    aluno = Aluno.objects.get(id=id)
    # resgatando a lista de cursos para ser preenchida no formulario de edicao
    cursos = Curso.objects.all()
    # renderizando a pagina aluno/update.html juntamente com o formulario preenchido com os dados do aluno a ser atualizado
    return render(request, "aluno/update.html", {"aluno": aluno, "cursos": cursos})

# metodo que persiste no banco os dados enviados via formulario


def update(request, id):
    # coletando os dados do formulario de edicao e atribuindo à variáveis locais
    nome = request.POST.get("nome")
    email = request.POST.get("email")
    nascimento = request.POST.get("nascimento")
    cep = request.POST.get("cep")
    bairro = request.POST.get("bairro")
    logradouro = request.POST.get("logradouro")
    numero = request.POST.get("numero")
    cidade = request.POST.get("localidade")
    estado = request.POST.get("estado")
    curso_id = request.POST.get('curso')
    # resgatando o usuario a ser atualizando do banco
    aluno = Aluno.objects.get(id=id)
    # atualizando com os novos dados 
    aluno.nome = nome
    aluno.email = email
    aluno.nascimento = nascimento
    aluno.cep = cep
    aluno.bairro = bairro
    aluno.logradouro = logradouro
    aluno.numero = numero
    aluno.cidade = cidade
    aluno.estado = estado
    aluno.curso = Curso.objects.get(id=curso_id)
    # salvando no banco com os novos dados
    aluno.save()
    # gravando uma mensagem para ser exibida na home do aluno
    messages.success(request, f"Estudante {nome} editado(a) com sucesso!")
    # redirecionando para o metodo home
    return redirect(home)

# metodo para apagar o aluno


def deletar_aluno(request, id):
    # resgatando do banco o aluno a ser apagado
    aluno = Aluno.objects.get(id=id)
    # Apagando de fato
    aluno.delete()
    # gravando mensagem a ser exibida na home
    messages.warning(
        request, f"Estudante {aluno.nome} removido(a) com sucesso!")
    # redirecionando para o metodo home
    return redirect(home)
