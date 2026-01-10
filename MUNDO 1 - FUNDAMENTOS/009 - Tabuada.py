#009 - Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
n = int(input('Informe o número que você deseja visualizar a tabuada: > '))
titulo = f' TABUADA DO {n} '
print(f"{titulo :-^75}")
# ~ print(f"{n:02} * 01 = {n*1 :02}")
# ~ print(f"{n:02} * 02 = {n*2 :02}")
# ~ print(f"{n:02} * 03 = {n*3 :02}")
# ~ print(f"{n:02} * 04 = {n*4 :02}")
# ~ print(f"{n:02} * 05 = {n*5 :02}")
# ~ print(f"{n:02} * 06 = {n*6 :02}")
# ~ print(f"{n:02} * 07 = {n*7 :02}")
# ~ print(f"{n:02} * 08 = {n*8 :02}")
# ~ print(f"{n:02} * 09 = {n*9 :02}")
# ~ print(f"{n:02} * 10 = {n*10:02}")
for i in range(1,11):
    print(f"{n:} * {i:<2} = {n*i:02}")
    
