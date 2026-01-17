#044 - Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
    # À vista dinheiro/cheque (*vou por pix por ser mais atual): 10% de desconto
    # À vista no cartão: 5% de desconto
    # Em até 2x no cartão: preço normal
    # 3x ou mais no cartão: 20% de juros
print('*/'*10,'CAIXA', '/*'*10)
valor = float(input('Informe o valor do produto: > R$'))
tipo = input("Vai pagar  à vista em dinheiro/pix? (S/n) > ").lower()
if tipo in ['s', 'sim', 'y', 'yes']:
    print("Produto pago a vista em dinheiro/pix (10% de desconto)")
    valor*= 0.90
else:
    parcela = int(input("Método de pagamento: Cartão de Crédito.\nInforme o número de parcelas: > "))
    if parcela == 1:
        print("Produto pago a vista no cartão (5% de desconto)")
        valor*= 0.95
    elif parcela == 2:
        print("Produto pago em 2x no cartão")
    elif parcela > 2:
        print(f"Produto pago em {parcela}x no cartão (20% de juros)")
        valor*= 1.2
    else:
        print("Parcela inválida. Pela gracinha vou te cobrar 200% de juros!")
        valor*= 3
print(f"Valor: R${valor:.2f}")
