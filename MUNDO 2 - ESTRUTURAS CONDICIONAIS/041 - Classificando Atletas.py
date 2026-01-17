#041 - A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
    # Até 9 anos: MIRIM
    # Até 14 anos: INFANTIL
    # Até 19 anos: JÚNIOR
    # Até 25 anos: SÊNIOR
    # Acima: MASTER
from datetime import date
print("---|"*5, ' CATEGORIA DA CNN PARA ATLETAS DE NATAÇÃO ', "|---"*5)
anoAtual = date.today().year
anoAtleta = int(input('Insira o ano de nascimento do atleta: > '))
idade = anoAtual - anoAtleta
print('CATEGORIA DO ATLETA:', end=' ')
if idade < 10:
    print('MIRIM')
elif idade < 15:
    print('INFANTIL')
elif idade < 20:
    print('JÚNIOR')
elif idade < 26:
    print('SÊNIOR')
else:
    print('MASTER')
    