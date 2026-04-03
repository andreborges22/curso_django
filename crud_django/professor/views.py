# importando objetos render e redirect, usados nos métodos
from django.shortcuts import render,redirect
from .models import Professor, Titulacao
# importando models que são usados para acesso ao banco
from professor.models import Sexo
# importando o objeto messages, para interação na tela
from django.contrib import messages
# importacao para definir que uma função só será acessível para usuarios autenticados
from django.contrib.auth.decorators import login_required
# importacao para consultas (query)
from django.db.models import Q

# Create your views here.
#login requerido
@login_required(login_url='/login/')
def home(request):
    # pegando os professores do banco
    professores = Professor.objects.all()
    # pegando os titulos do banco para popular a lista de seleção de titulos 
    titulos = Titulacao.objects.all()
    # pegando as descrições de sexos do banco para popular a lista de seleção de sexo
    sexos = Sexo.objects.all()
    # renderizando a home do professor
    return render(request,'professor/home.html',{
            'professores':professores,
            'titulos':titulos,
            'sexos':sexos,
        })

#login requerido
@login_required(login_url='/login/')
# função de cadastro de professor
def cadastrar(request):
    if request.method == 'GET':
        return redirect('professor:home')
    else:
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        titulacao_id = request.POST.get("titulacao")
        sexo_id = request.POST.get("sexo")
        telefone = request.POST.get("telefone")
        endereco = request.POST.get("endereco")
        try:
            # criando um objeto professor
            professor = Professor.objects.create(
                # atribuindo os dados vindos do formularios ao objeto professor
                nome=nome,             
                email = email,                   
                titulacao_id = titulacao_id,
                sexo_id=sexo_id,
                telefone=telefone,
                endereco=endereco)
            # salvando no banco
            professor.save()
            # acrescentando a mensagem de sucesso no objeto messages (isso será recuperado e exibido na página html)
            messages.success(
                request, f"Professor {nome} cadastrado(a) com sucesso!")
            # redirecionando para a home do professor
            return redirect('professor:home')
        # Capturando uma excecao
        except Exception as erro:
            # imprimindo o erro
            messages.error(request, f"Erro: {erro}")
            # redirecionando para a home do professor
            return redirect('professor:home')
        
# funcao buscar da página buscar
@login_required(login_url='/login/')
def buscar(request):
    query = request.GET.get('q')  # pega o termo digitado

    professores = Professor.objects.all()

    if query:
        professores = professores.filter(
            Q(nome__icontains=query) |
            Q(email__icontains=query)
        )

    return render(request, 'professor/buscar.html', {
        'professores': professores,
        'query': query
    })

@login_required(login_url='/login/')
# função para listar/buscar professors
def listar(request):
    # atribuindos todos os professors do banco de dados à variável professors
    professores = Professor.objects.all()
    # atribuindos todas as descricoes de sexo do banco de dados à variável sexos
    query = request.GET.get('q')  # pega o termo digitado

    if query:
        professores = professores.filter(
            Q(nome__icontains=query) |
            Q(email__icontains=query)
        )

    return render(request, 'professor/listar.html', {
        'professores': professores,
        'query': query
    })

@login_required(login_url='/login/')
def editar(request, id):
    try:
        # resgatando do banco o professor cujo id é igual ao id enviado via template
        professor = Professor.objects.get(id=id)
        # pegando os titulos do banco para popular a lista de seleção de titulos 
        titulos = Titulacao.objects.all()
        # pegando todos os sexos do banco
        sexos = Sexo.objects.all()
        # renderizando a pagina professor/editar.html juntamente com o formulario preenchido com os dados do professor a ser atualizado
        return render(request, "professor/editar.html", {
            "professor": professor,
            "titulos":titulos,
            "sexos": sexos
        })
    # capturando excecao e printando na tela
    except Exception as erro:
        # imprimindo o erro
        messages.error(request, f"Erro: {erro}")
        # redirecionando para a home do professor
        return redirect('professor:home')


# método para atualizar um professor
@login_required(login_url='/login/')
def update(request, id):
    # resgatando dados do formulario da página editar
    nome = request.POST.get("nome")
    email = request.POST.get("email")
    titulacao_id = request.POST.get("titulacao")
    sexo_id = request.POST.get("sexo")
    telefone = request.POST.get("telefone")
    endereco = request.POST.get("endereco")
    try:
        # resgatando o professor do banco que esta sendo editado
        professor = Professor.objects.get(id=id)
        # atualizando os dados do banco com os dados vindos do formulário
        professor.nome = nome
        professor.email = email
        professor.sexo_id = sexo_id
        professor.telefone = telefone
        professor.endereco = endereco
        professor.titulacao_id = titulacao_id
        # salvando os novos dados no banco
        professor.save()
        # acrescentando a mensagem de sucesso no objeto messages (isso será recuperado e exibido na página html)
        messages.success(
            request, f"Professor {nome} editado(a) com sucesso!")
        # redirecionando para a home_professor
        return redirect('professor:listar')
    # capturando exceção
    except Exception as erro:
        # imprimindo o erro
        messages.error(request, f"Erro: {erro}")
        # redirecionando para a home do professor
        return redirect('professor:home')

# método para excluir um professor


@login_required(login_url='/login/')
def excluir(request, id):
    try:
        # pegar o professor específico do banco
        professor = Professor.objects.get(id=id)
        # apagar do banco
        professor.delete()
        # redirecionando para a home_professor
        messages.warning(
            request, f"Estudante {professor.nome} removido(a) com sucesso!"
        )
        # redirecionando para a home do professor
        return redirect('professor:home')
    # capturando exceção
    except Exception as erro:
        # imprimindo erro
        messages.error(request, f"Erro: {erro}")
        return redirect('professor:home')