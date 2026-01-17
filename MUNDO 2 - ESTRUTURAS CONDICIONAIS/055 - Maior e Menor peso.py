#055 - Faça um programa que leia o peso de cinco pessoas.
#  No final, mostre qual foi o maior e o menor peso lidos.
QTDP = 3
for c in range(0, QTDP):
    peso = float(input(f'Insira o peso da {c+1}º pessoa: > '))
    if not c: 
        maior = peso
        menor = peso
        continue
    maior = peso if peso > maior else maior
    menor = peso if peso < menor else menor
print (f"O maior peso cadastrado entre as {QTDP} pessoas foi: {maior:.2f}kg.")
print (f"O menor peso cadastrado entre as {QTDP} pessoas foi: {menor:.2f}kg.")
