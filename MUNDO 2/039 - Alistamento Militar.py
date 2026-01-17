# 039 - Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
print('-=-'*10,'CALCULADORA DE ALISTAMENTO MILITAR', '-=-'*10)
anoAtual = date.today().year
anoUsuario = int(input('Informe o seu ano de nascimento: > '))
idade = anoAtual - anoUsuario
if idade == 18:
    print("Esta é o ano exato para se alistar no serviço militar!")
elif idade < 18:
    print("Você ainda irá se alistar no serviço militar.")
    print(f"Falta {18-idade} ano{'s' if 18-idade!=1 else ''}!")
else:
    print("O seu prazo para alistamento passou!")
    print(f"O prazo foi há {idade-18} ano{'s' if idade-18!=1 else ''}!")
    