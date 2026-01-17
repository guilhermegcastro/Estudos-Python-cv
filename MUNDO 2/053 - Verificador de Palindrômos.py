#053 - Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. 
# (Exemplos: APOS A SOPA, A SACADA DA CASA, ANOTARAM A DATA DA MARATONA).
frase = input('Insira uma frase: > ').upper()
palavra = frase.replace(' ', '')
inverso = palavra[::-1]

print(f"Original: {palavra}")
print(f"Inverso: {inverso}")
print(f"{'É uma palíndromo!' if palavra == inverso else 'Não é um palíndromo!'}")