#030 - Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
print('-*-'*20)
print('PAR OU ÍMPAR'.center(60))
print('-*-'*20)
numero = int(input('Insira um número inteiro: > '))
if numero % 2 == 0:
    print(f"O número {numero} é PAR!")
else: 
    print(f"O número {numero} é ÍMPAR!")

