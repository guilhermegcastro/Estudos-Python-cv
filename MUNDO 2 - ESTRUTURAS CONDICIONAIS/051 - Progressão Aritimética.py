#051 - Desenvolva um programa que leia o primeiro termo e a razão de uma PA (Progressão Aritmética).
#  No final, mostre os 10 primeiros termos dessa progressão.
print('='*25, 'PROGRESSÃO ARITIMÉTICA', '='*25)
termo = int(input('Insira o primeiro termo: > '))
razaoPA = int(input('Insira a razão da Progressão Aritmética: > '))
print('PA:', end=' ')
for c in range(1,11):
    print(f"{termo}{', ' if c!=10 else ''}", end='')
    termo += razaoPA
print('.')

