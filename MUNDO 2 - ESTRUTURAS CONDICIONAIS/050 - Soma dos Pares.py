#050 - Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
# Se o valor digitado for ímpar, desconsidere-o.
somap = 0
somai = 0
for n in range(1, 7):
   numero = int(input(f"Insira o {n}º número inteiro: > "))
   if not numero%2:
      somap += numero
   else:
      somai += numero
print(f"* - A soma de todos os números pares foi: {somap}")
print(f"* - A soma de todos os números ímpares foi: {somai}")
