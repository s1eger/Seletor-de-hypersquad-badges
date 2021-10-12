import requests
from colorama import init, Fore
from os import system, name
from time import sleep
from pyfiglet import Figlet

token = '' # coloque o token da sua conta aqui
url = r'https://discord.com/api/v6/hypesquad/online'

init(autoreset = True)

figlet = Figlet(font = 'slant')

print(figlet.renderText('SELETOR HYPESQUAD'))

def clear():
  system('clear' if name != 'nt' else 'cls') 


def esperaelimpa():
  sleep(1.5)
  clear()


def seletorhypesquad(escolha):
  str(escolha)
  if escolha == 'Bravery':
    bravery = requests.post(url, json = {'house_id': '1'}, headers = {'authorization': token})

    if bravery.status_code == 204:
      print(f'{Fore.MAGENTA}O hypesquad Bravery foi adicionado a sua conta.')
      esperaelimpa()
    if bravery.status_code == 401:
      print(f'{Fore.RED}Insira o seu token na variavel token!')
      sleep(4)
      clear()
    if bravery.status_code == 429:
      print(f'{Fore.RED}Taixa limitada!')
      sleep(4)
      clear()
      

  if escolha == 'Brilliance':
    brilliance = requests.post(url, json = {'house_id': '2'}, headers = {'authorization': token})
    if brilliance.status_code == 204:
      print(f'{Fore.MAGENTA}O hypesquad Brilliance foi adicionado a sua conta.')
      esperaelimpa()
    if bravery.status_code == 401:
      print(f'{Fore.RED}Insira o seu token na variavel token!')
      sleep(4)
      clear()
    if bravery.status_code == 429:
      print(f'{Fore.RED}Taixa limitada!')
      sleep(4)
      clear()

  if escolha == 'Balance':
    balance = requests.post(url, json = {'house_id': '3'}, headers = {'authorization': token})
    if balance.status_code == 204:
      print(f'{Fore.MAGENTA}O hypesquad Balance foi adicionado a sua conta.')
      esperaelimpa()
    if bravery.status_code == 401:
      print(f'{Fore.RED}Insira o seu token na variavel token!')
      sleep(4)
      clear()
    if bravery.status_code == 429:
      print(f'{Fore.RED}Taixa limitada!')
      sleep(4)
      clear()
  
  elif escolha not in ('Bravery', 'Brilliance', 'Balance'):
    print(f'{Fore.RED}Digite um hypesquad válido!')
    esperaelimpa()


try:
  while True:
    hypesquad = str(input(f'{Fore.MAGENTA}Digite o hypesquad que você deseja\n[Bravery, Brilliance, Balance]\n\n')).strip().capitalize()
    seletorhypesquad(hypesquad)

except Exception as erro:
  print(f'{Fore.RED}Houve um erro... Código de erro: {erro}')
