#010 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Cotação do dólar baseado no dia que resolvi esse exercício (06/01/2026): 5,37 
COTACAO_ATUAL = 5.37
print(f"{' CONVERSÃO DE REAL PARA DÓLAR (O6/01/2026) ':$^80}")
real = float(input('Informe a quantidade de REAL na carteira: > R$'))
dolar = real/COTACAO_ATUAL
print(f"R${real:.02f} equivale a U${dolar:.02f} ")
