#047 - Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
NMAX = 50
print(f"PARES DE 1 A {NMAX}")
for numero in range(2, NMAX+1,2):
    if numero != NMAX:
         print(numero, end=', ')
    else:
         print(f'{numero}.')
