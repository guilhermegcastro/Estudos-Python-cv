#023 - Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
numerostr = input('Informe um número entre 0 a 9999: > ')
# numero = int(numerostr)
# u = numero // 1 % 10
# d = numero // 10 % 10
# c = numero // 100 % 10
# m = numero // 1000 % 10

# print(f" UNIDADE : {u}")
# print(f" DEZENA  : {d}")
# print(f" CENTENA : {c}")
# print(f" MILHAR  : {m}")

numerostr = numerostr.zfill(4)
print(f" UNIDADE : {numerostr[-1]}")
print(f" DEZENA  : {numerostr[-2]}")
print(f" CENTENA : {numerostr[-3]}")
print(f" MILHAR  : {numerostr[-4]}")