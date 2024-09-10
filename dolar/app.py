import requests
import json


url = 'https://economia.awesomeapi.com.br/last/USD-BRL'

response = requests.get(url)

if response.status_code == 200:
    dados = response.json()
    # print(dados['USDBRL']['varBid'])
    print(dados)
else:
    print(f'Status code: {response.status_code}')