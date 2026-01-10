#026 - Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Insira uma frase: > ')).lower().strip()
print(f" A letra 'A' apareceu {frase.count('a')} vezes")
print(f" A primeira posição em que 'A' aparece: {frase.find('a')+1}")
print(f" A última posição em que 'A' aparece: {frase.rfind('a')+1}")
