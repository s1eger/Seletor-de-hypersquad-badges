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
    print(f'{Fore.MAGENTA}O hypesquad {hypesquad} foi adicionado a sua conta.')
    esperaelimpa()

  if escolha == 'Brilliance':
    brilliance = requests.post(url, json = {'house_id': '2'}, headers = {'authorization': token})
    print(f'{Fore.MAGENTA}O hypesquad {hypesquad} foi adicionado a sua conta.')
    esperaelimpa()

  if escolha == 'Balance':
    balance = requests.post(url, json = {'house_id': '3'}, headers = {'authorization': token})
    print(f'{Fore.MAGENTA}O hypesquad {hypesquad} foi adicionado a sua conta.')
    esperaelimpa()
  
  elif hypesquad not in ('Bravery', 'Brilliance', 'Balance'):
      print(f'{Fore.RED}Digite um hypesquad válido!')
      esperaelimpa()

vazio = ''

if token == vazio:
  print(f'{Fore.RED}Insira o seu token na variavel token!')
  sleep(4)
  clear()


else:
  try:
    while True:
      hypesquad = str(input(f'Digite o hypesquad que você deseja\n[Bravery, Brilliance, Balance]\n\n')).strip().capitalize()
      seletorhypesquad(hypesquad)

  except Exception as erro:
    print(f'{Fore.RED}Houve um erro... Código de erro: {erro}')
