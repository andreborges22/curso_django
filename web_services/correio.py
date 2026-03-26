# importa a biblioteca requests (pip install requests)
import requests
import pprint

# metodo para consumir uma API


def retorna_dados(cep):
    # criando uma requisicao que consume uma api
    response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    # se a resposta for ok
    if response.status_code == 200:
        # recupera os dados no formato json
        return response.json()
    else:
        # retorna vazio
        return None


# passando o dado para a api
cep = input("Informe um CEP no formato 00000000: ")
dados = retorna_dados(cep)
# se existrem dados
if dados:
    # imprima
    #pprint.pprint(dados)
    print(f"Bairro: {dados["bairro"]}")
else:
    # informe erro
    print("Falha ao recuperar dados")
