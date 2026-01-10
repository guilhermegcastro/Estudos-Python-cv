#027 - Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza (primeiro = Ana; último = Souza
nome = str(input('Insira um nome: > ')).strip()
lista_nome = nome.split()
print(f" Primeiro nome: {lista_nome[0]}\n Último nome: {lista_nome[-1]}")
