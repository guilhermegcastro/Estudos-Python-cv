# Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre: 
#   -  O nome com todas as letras maiúsculas e minúsculas.
#   -  Quantas letras ao todo (sem considerar espaços).
#   -  Quantas letras tem o primeiro nome.

nome = input('Digite um nome completo: > ')
print(nome.upper())
divisao = nome.split()
# contador = "".join(divisao)
# print(f"Quantidade de letras sem espaços: {len(contador)}")
print(f"Quantidade de letras sem espaços: {len(nome) - nome.count(' ')}")
print(f"O primeiro nome possui {len(divisao[0])} letras")
