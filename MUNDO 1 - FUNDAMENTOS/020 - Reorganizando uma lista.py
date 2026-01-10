#020 - O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. 
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
print(f"{' SORTEIO DE ORDEM ':x^80}")
n1 = input('Informe o nome do/a 1º Aluno/a: ')
n2 = input('Informe o nome do/a 2º Aluno/a: ')
n3 = input('Informe o nome do/a 3º Aluno/a: ')
n4 = input('Informe o nome do/a 4º Aluno/a: ')
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print(f"Ordem dos alunos:\n {lista[0]}\n {lista[1]}\n {lista[2]}\n {lista[3]}")