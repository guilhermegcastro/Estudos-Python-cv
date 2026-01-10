#011 - Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
from math import ceil
RENDIMENTO = 2
print(f"{' Cálculo para pintura de parede ':x^80}")
largura = float(input('Insira a largura (em metros) da parede: > '))
altura = float(input('Insira a altura (em metros) da parede: > '))
area = largura * altura
print(f"A quantidade de tinta necessária para pintar {area: .2f}m² é de {ceil(area/RENDIMENTO)} litros")
