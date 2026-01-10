 #018 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, cos, tan, sin
print(f"{' SENO, COSSENO E TANGENTE ':!^80}")
grau = int(input('Informe o grau que deseja calcular: > '))
radiano = radians(grau)
print(f"SEN : {sin(radiano):.2f}\nCOS: {cos(radiano):.2f}\nTAN: {tan(radiano):.2f}")