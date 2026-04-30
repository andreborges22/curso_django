from django import forms
from .models import Aluno

# criação do form


class AlunoForm(forms.ModelForm):
    # classe que, internamente, gerencia metadados do formulário
    class Meta:
        # model que será usado como mocelo para o formulário
        model = Aluno
        # campos do formulário
        fields = ['nome', 'email', 'sexo', 'telefone',
                  'endereco', 'curso',]
        # opções que podem ser habilitadas para cada campo
        nome = forms.CharField(
            required=True,          # obrigatório
            max_length=100,         # tamanho máximo
            min_length=3,           # tamanho mínimo
            label="Nome",           # label exibido
            initial="João",         # valor inicial
            help_text="Seu nome",   # texto de ajuda
            disabled=False,         # campo desabilitado
        )
        #personalização do campo nome
        widgets = {
            # inserindo um placeholder para o campo nome
            'nome': forms.TextInput(attrs={
                'placeholder': 'Digite seu nome completo',
            }),
            'email': forms.EmailInput(attrs={
                # inserindo um placeholder para o campo email
                'placeholder': 'Digite seu email',
                # inserindo um evento "onkeyup", ou seja, a cada tecla pressionada no campo email a função verificarEmail() será invocada
                'onkeyup': 'onkeyup="verificarEmail()'
            }),
        }
