# 038 - Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#    O primeiro valor é maior
#    O segundo valor é maior
#    Não existe valor maior, os dois são iguais

print('-=-'*10,'VERIFICADOR DE MAIOR NÚMERO', '-=-'*10)
n1 = float(input('Insira o primeiro número: > '))
n2 = float(input('Insira o segundo número: > '))
if n1 > n2:
    print(f"O primeiro número ({n1}) é maior que o segundo número ({n2})")
elif n1 < n2:
    print(f"O segundo número ({n2}) é maior que o primeiro número ({n1})")
else: 
    print('Não existe valor maior. Ambos são iguais.')
