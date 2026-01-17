#056 - Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:

    # A média de idade do grupo.

    # Qual é o nome do homem mais velho.

    # Quantas mulheres têm menos de 20 anos.
QTDP = 2
idadeTotal = 0
homemMaisVelho = ['null', 0, False]
mulherMenor20 = 0
for c in range (0, QTDP):
    nome = input(f'Insira o nome da {c+1}º pessoa: > ')
    idade = int(input(f'Insira a idade de {nome}: > '))
    sexo = input('Insira o sexo (M - MASC ou F - FEM): > ').upper()
    idadeTotal += idade
    if sexo == 'M':
        if homemMaisVelho[2] == False:
            homemMaisVelho[0] = nome
            homemMaisVelho[1] = idade
            homemMaisVelho[2] = True
            continue
        elif idade > homemMaisVelho[1]:
            homemMaisVelho[0] = nome
            homemMaisVelho[1] = idade
            continue
    if sexo == 'F' and idade < 20:
        mulherMenor20 += 1

print(f"Média de idade do grupo: {idadeTotal/QTDP}")
print(f"{homemMaisVelho[0]} é o homem mais velho com {homemMaisVelho[1]} anos." if homemMaisVelho[2] == True else "Não há homens registrados no grupo.")
print(f"Existem {mulherMenor20} mulheres menores de 20 anos no grupo.")

        

    