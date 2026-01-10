#016 - Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc
print(f"{' SISTEMA DE TRUNCAGEM ':>^80}")
numero = float(input('Insira um número real : > '))
print(f"Sua forma inteira é {trunc(numero)}")
# * Jeito mais prático : print(f"Sua forma inteira é {int(numero)}")