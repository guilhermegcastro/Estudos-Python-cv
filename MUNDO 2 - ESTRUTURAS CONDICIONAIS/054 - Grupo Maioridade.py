#054 - Crie um programa que leia o ano de nascimento de sete pessoas.
#  No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
#  Regra: Considere a maioridade com 18 anos.
from datetime import date
YEAR = date.today().year
QTDP = 2
maioridade = 0
for n in range (1, QTDP+1):
    pessoa = int(input(f'Insira o ano de nascimento da {n}º pessoa: > '))
    if YEAR - pessoa > 17 :
        maioridade+=1
print(f"{QTDP - maioridade}/{QTDP} pessoas não atingiram a maioridade. ")
print(f"{maioridade}/{QTDP} pessoas já atingiram a maioridade. ")
