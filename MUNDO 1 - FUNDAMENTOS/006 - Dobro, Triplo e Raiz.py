# 006 - Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
print(f"{' DOBRO, TRIPLO E RAIZ QUADRADA ':*^80}")
numero = int(input('Insira um número: > '))
print(f"O Dobro de {numero} é {2*numero}")
print(f"O Triplo de {numero} é {3*numero}")
print(f"A Raiz Quadrada de {numero} é {numero**(1/2):.02f}")
