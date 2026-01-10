#034 - Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#  Para salários superiores a R$1250,00, calcule um aumento de 10%.
#  Para os inferiores ou iguais, o aumento é de 15%.
print('[-]'*20)
print('AUMENTO DE SALÁRIO'.center(60))
print('[-]'*20)
salario = float(input('Informe o salário do funcionário > R$'))
if salario > 1250:
    aumento = 0.10
else:
    aumento = 0.15
salario+= salario*aumento
print(f'O novo salário do funcionário será de: R${salario:.2f} (aumento de {aumento*100:.0f}%)')
