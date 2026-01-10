# 033 - Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
print('¨¨¨'*20)
print('MAIOR E MENOR\n'.center(60))
print('¨¨¨'*20)
n1 = int(input('Insira o primeiro número: > '))
n2 = int(input('Insira o segundo número: > '))
n3 = int(input('Insira o terceiro número: > '))
menor = n1
if n2 < menor:
    menor = n2 
if n3 < menor:
    menor = n3
maior = n3
if n1 > maior:
    maior = n1
if n2 > maior:
    maior = n2
print(f"Maior número: {maior} // Menor número: {menor}")
