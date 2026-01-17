#048 - Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 e que se encontram no intervalo de 1 até 500.
soma = 0
for numero in range(1, 501, 2):
    if numero%3 == 0:
        soma= soma + numero
print(f'Soma de todos os números ímpares múltiplos de 3 entre 1 a 500:{soma}')