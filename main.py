import requests; from colorama import init, Fore

init(autoreset = True)

token = '' # coloque o token da sua conta aqui
url = r'https://discord.com/api/v6/hypesquad/online'

try:
  hypesquad = str(input(f'Digite o hypesquad que você deseja [Bravery, Brilliance, Balance]:  ')).strip().capitalize()

  if hypesquad == 'Bravery':
    bravery = requests.post(url, json = {'house_id': '1'}, headers = {'authorization': token})

  if hypesquad == 'Brilliance':
    bravery = requests.post(url, json = {'house_id': '2'}, headers = {'authorization': token})

  if hypesquad == 'Balance':
    bravery = requests.post(url, json = {'house_id': '3'}, headers = {'authorization': token})

except Exception as erro:
  print(f'{Fore.RED}Houve um erro... Código de erro: {erro}')
