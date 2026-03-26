# https://www.weatherapi.com/
# importa a biblioteca requests (pip install requests)
import requests
import pprint

api_key = "7ecfc760bcad488f93f21445262302"
api_link = "http://api.weatherapi.com/v1/current.json"

parametros = {
    "key":api_key,
     "q":"Salvador",
     "lang":"pt"
}

response = requests.get(api_link,params=parametros)
#print(response.status_code)
#print(response.content)
if response.status_code==200:
    dados = response.json()
pprint.pprint(dados)
temperatura = dados["current"]["temp_c"]
Indice_UV = dados["current"]["uv"]
condicao = dados["current"]["condition"]["text"]

print(f"Temperatura atual: {temperatura}")
print(f"Indice_UV: {Indice_UV}")
print(f"Condição do tempo: {condicao}")