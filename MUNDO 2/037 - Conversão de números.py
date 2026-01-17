#037 - Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#  1 para binário, 2 para octal e 3 para hexadecimal.
print('=-='*20)
print('\033[1;33;45mCONVERSOR DE NÚMEROS\033[m'.center(70))
print('-=-'*20)
numero = int(input('Insira um número: > '))
print('ESCOLHA A OPÇÃO DE CONVERSÃO:\n',
      '1 - Binário\n',
      '2 - Octal\n',
      '3 - Hexadecimal')
opcao = int(input(' > '))
if opcao == 1:
    print(f"{numero} convertido em binário é: {bin(numero)}")
elif opcao == 2:
    print(f"{numero} convertido em octal é: {oct(numero)}")
elif opcao == 3: 
    print(f"{numero} convertido em hexadecimal é: {hex(numero)}")
else:
    print('Opção não aceita.')
    