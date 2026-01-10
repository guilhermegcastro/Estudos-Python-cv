# 028 - Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
n = randint(0,5)
print('-=-'*20)
print(f"{('ADIVINHE O NÚMERO').center(60)}")
print('-=-'*20)
resposta = int(input('O PC escolheu um número de 0 a 5. Insira o seu palpite: > '))
print(f"O número escolhido foi...", end =' ', flush=True)
sleep(2)
print(f"{n}!")
print('Você ganhou!' if resposta == n else 'Você perdeu!')
