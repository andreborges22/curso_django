from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Aluno,Sexo

# Create your views here.

# método para renderizar a home do aluno


def home(request):
    # return HttpResponse("Oi")
    #atribuindos todos os alunos do banco de dados à variável alunos
    alunos = Aluno.objects.all()
    #atribuindos todos os sexos do banco de dados à variável sexos
    sexos = Sexo.objects.all()
    # retorna a renderização da home do aluno juntamente com os alunos do banco
    return render(request, 'aluno/home.html',{
        'alunos':alunos,
        'sexos':sexos
        })  

# método para criar um aluno
def cadastrar(request):
    # resgatando o nome enviado via formulario
    nome =  request.POST.get("nome")  
    email = request.POST.get("email")
    sexo = request.POST.get("sexo")
    telefone = request.POST.get("telefone")
    endereco = request.POST.get("endereco")
    # criando um objeto aluno
    # iniciando tratamento de exceção
    try:
        Aluno.objects.create(
            nome = nome,
            email = email,
            sexo = sexo, 
            telefone = telefone,
            endereco = endereco)
        # redireciona para a view
    #Capturando uma excecao
    except Exception as erro:
        #imprimindo o erro
        #return HttpResponse(f"Erro: {erro}")    
        print(f"Erro: {erro}")
    # redirecionando para a home
    return redirect(home)

def editar(request,id):
    try:
        # pegando o aluno específico do banco
        aluno = Aluno.objects.get(id=id)      
        # pegando todos os sexos do banco
        sexos = Sexo.objects.all() 
        # renderizando a pagina aluno/update.html juntamente com o formulario preenchido com os dados do aluno a ser atualizado
        return render(request, "aluno/editar.html", {
            "aluno": aluno,
            "sexos":sexos
            })
    except Exception as erro:
        print(f"Erro: {erro}")
    
def update(request,id):
    # resgatando dados do formulario da página editar
    nome =  request.POST.get("nome")  
    email = request.POST.get("email")
    sexo = request.POST.get("sexo")
    telefone = request.POST.get("telefone")
    endereco = request.POST.get("endereco")
    try:
        # resgatando o aluno do banco
        aluno = Aluno.objects.get(id = id)
        # atualizando os dados do banco com os dados vindos do formulário
        aluno.nome = nome
        aluno.email = email
        aluno.sexo = sexo
        aluno.telefone = telefone
        aluno.endereco = endereco
        # salvando os novos dados no banco
        aluno.save()
    except Exception as erro:
        print(f"Erro: {erro}")
    # redirecionando para a home
    return redirect(home)

def excluir(request,id):
    try:
        # pegar o aluno específico do banco
        aluno = Aluno.objects.get(id = id)
        # apagar do banco
        aluno.objects.delete()
        # redirecionar para a home
    except Exception as erro:
        print(f"Erro: {erro}")
    # redirecionando para a home
    return redirect(home)