#052 - Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
numero = int(input('Insira um número: '))
primo = True
for c in range(2, numero):
    if not numero % c:
        print('O número não é primo.')
        primo = False
        break
if primo == True and numero > 1:
        print('O número é primo.')
