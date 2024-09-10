import requests
import json


restaurantes = {}

class Restaurante:
    def __init__(self, Company, Item, price, description) -> None:
        self._company = Company
        self._item = Item
        self._price = price
        self._description = description
    
    @property    
    def company(self):
        return self._company
    
    def __str__(self) -> str:
        return f'{self._company}'

def salvar_restaurante(dados, nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf8') as file:
        json.dump(dados, file, indent=2)

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url)

if response.status_code == 200:
    dados = response.json()
    
    for item in dados:
        restaurante = Restaurante(**item)
        
        if restaurante.company not in restaurantes:
            restaurantes[restaurante.company] = []
        
        restaurantes[restaurante.company].append(item)
else:
    print(response.status_code)
    
for chave, valor in restaurantes.items():
    arquivo = f'{chave}.json'
    salvar_restaurante(valor, arquivo)
