#019 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice
print(f"{' SORTEIO DE ALUNO ':.^80}")
n1 = input(f" Informe o nome do 1º Aluno/a: > ")
n2 = input(f" Informe o nome do 2º Aluno/a: > ")
n3 = input(f" Informe o nome do 3º Aluno/a: > ")
n4 = input(f" Informe o nome do 4º Aluno/a: > ")
lista = [n1, n2, n3, n4]
print(f" O/A aluno/a sorteado/a foi: {choice(lista)}")
