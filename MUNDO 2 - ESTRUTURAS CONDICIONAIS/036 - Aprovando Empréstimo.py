#036 - Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#  Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#  A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
print('=-='*20)
print('FINANCIAMENTO IMOBILIÁRIO'.center(60))
print('-=-'*20)

valor = float(input('Informe o valor da casa: > R$'))
salario = float(input('Informe o salário do comprador: > R$'))
anos = int(input('Informe em quantos anos a dívida será quitada: > '))
prestacao = valor/(anos*12.0)
print(f"Valor da prestação mensal: R${prestacao:.2f}")
if prestacao > salario*0.3:
    print(f"O empréstimo não poderá ser realizado.\nO valor da prestação excede 30% do salário do comprador (R${salario*0.30:.2f})")
else:  
    print(f"O empréstimo poderá ser realizado.\nO valor da prestação não excede 30% do salário do comprador (R${salario*0.30:.2f})")
