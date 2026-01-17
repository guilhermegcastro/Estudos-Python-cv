#049 - Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
# n = int(input('Escolha o número da tabuada: > '))
# print('='*10, f'TABUADA DO {n}','='*10)
# for m in range(1, 11):
#     print(f"{n:02} x {m:02} = {n*m:02}")

print('='*10, f'TABUADA DO 1 A0 9','='*10)
for n in range(1, 11):
    print(f"TABUADA DO {n}:")
    for m in range(1,11):
        print(f"{n:02} x {m:02} = {n*m:02}")
