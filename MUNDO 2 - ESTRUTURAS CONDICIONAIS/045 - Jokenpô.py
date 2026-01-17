#045 - Crie um programa que faça o computador jogar Jokenpô (Pedra, Papel e Tesoura) com você.
# Desafios desse código:
#     O Computador: Ele precisa escolher aleatoriamente (Lembra do import random? Vai precisar de algo como randint ou choice).
#     A Lógica: São muitas combinações.
#         Pedra ganha de Tesoura.
#         Tesoura ganha de Papel.
#         Papel ganha de Pedra.
#         Iguais = Empate.
from random import randint
print(" ✂️  📄 🪨   JOKENPÔ!  ✂️  📄 🪨".center(60))
lista = ['null', '🪨  (Pedra)', '📄 (Papel)', '✂️  (Tesoura)']
PCJP = randint(1,3)
USJP = int(input(f"\n1 - {lista[1]}\n2 - {lista[2]}\n3 - {lista[3]}\nEscolha uma opção: > "))
if  USJP > 3 or USJP < 1:
    # Opção que o programa é honesto quando o usuário informa uma opção inválida:
    # USJP = randint(1,3)
    # Opção que não é (O PC sempre ganha):
    if PCJP == 1:
        USJP = 3
    elif PCJP == 2:
        USJP = 1
    else:
        USJP = 2
    print(f"Opção inválida, então escolhi {lista[USJP]} (sem roubo!) como SUA opção! ;)")
if PCJP == USJP:
   situacao = 'DEU EMPATE'
elif USJP == 1:
    situacao = 'VOCÊ PERDEU' if PCJP == 2 else 'VOCÊ VENCEU'
elif USJP == 2:
     situacao = 'VOCÊ PERDEU' if PCJP == 3 else 'VOCÊ VENCEU'
else: 
    situacao = 'VOCÊ PERDEU' if PCJP == 1 else 'VOCÊ VENCEU'
print(f"Você jogou {lista[USJP]} e o PC {lista[PCJP]}! {situacao}!")
