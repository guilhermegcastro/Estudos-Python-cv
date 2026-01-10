#012 - Faça um algoritmo que leia o preço de um produto e o desconto. Calcule e mostre seu novo preço.
print(f"{' CALCUCADOR DE DESCONTO ':§^80}")
preco = float(input('Informe o preço do produto: > R$'))
desconto = float(input('Informe a porcentagem do desconto: > '))
novopreco = preco * (1 - (desconto/100))
print(f"O novo preço do produto é de R${novopreco:.02f}")
