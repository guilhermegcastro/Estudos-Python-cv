#015 - Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
DIARIA = 60.0
KM_RODADO = 0.15
print(f"{' CÁLCULO DO ALUGUEL DO CARRO ':º^80} ")
dias = int(input('Quantos dias alugados? > '))
km = float(input('Quantos km rodados? > '))
preco = dias * DIARIA + km * KM_RODADO
print(f"O total a ser pago é R${preco:.02f}")
