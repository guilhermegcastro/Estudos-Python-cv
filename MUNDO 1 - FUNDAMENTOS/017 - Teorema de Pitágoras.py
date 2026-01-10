#017 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
# Calcule e mostre o comprimento da hipotenusa.
from math import hypot
print(f"{' TEOREMA DE PITÁGORAS '::^80}")
ca = float(input('Insira o tamanho do cateto adjecente: > '))
co = float(input('Insira o tamanho do cateto oposto: > '))
print(f"A hipotenusa mede {hypot(ca, co):.02f}")