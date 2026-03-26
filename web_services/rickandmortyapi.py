# importa a biblioteca requests (pip install requests)
import requests
import pprint

# metodo para consumir uma API


def retorna_dados(link_api, endpoint):
    # criando uma requisicao que consume uma api
    response = requests.get(f"{link_api}{endpoint}")
    # se a resposta for ok
    if response.status_code == 200:
        # recupera os dados no formato json
        return response.json()
    else:
        # retorna vazio
        return None


# passando o dado para a api
link_api = "https://rickandmortyapi.com/api/"
personagem = input("Informe o numero do personagem: ")
endpoint = f"character/{personagem}"
dados = retorna_dados(link_api, endpoint)
# se existrem dados
if dados:
    # imprima
    #pprint.pprint(dados)
    print(f"Nome: {dados["name"]}")
else:
    # informe erro
    print("Falha ao recuperar dados")
