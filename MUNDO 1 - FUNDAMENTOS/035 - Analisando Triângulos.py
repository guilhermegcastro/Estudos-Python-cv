#035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
reta1 = float(input('Insira o comprimento da primeira reta: > '))
reta2 = float(input('Insira o comprimento da segunda reta: > '))
reta3 = float(input('Insira o comprimento da terceira reta: > '))
reta_maior = max(reta1, reta2, reta3)
reta_menor = min(reta1, reta2, reta3)
reta_meio = reta1 + reta2 + reta3 - reta_maior - reta_menor
if reta_menor + reta_meio <= reta_maior:
    print(f'Não é possível formar um triângulo. {reta_menor} + {reta_meio} = {reta_menor + reta_meio} < {reta_maior}')
else:
    print(f'É possível formar um triângulo. {reta_menor} + {reta_meio} = {reta_menor + reta_meio} > {reta_maior}')