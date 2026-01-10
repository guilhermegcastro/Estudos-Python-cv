#032 - Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
print('\\|/'*20)
print('ANO BISSEXTO'.center(60))
print('/|\\'*20)
ano = int(input('Informe um ano ou digite 0 para inserir o ano atual: > '))
if ano == 0:
    ano = date.today().year
print(f"{ano}", end = " ")
print("É um ano bissexto" if ano % 4 == 0 and (ano % 400 == 0 or ano % 100 != 0) else "Não é um ano bissexto.")
