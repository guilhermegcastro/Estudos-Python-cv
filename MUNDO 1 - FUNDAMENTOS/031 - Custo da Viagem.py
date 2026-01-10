#031 - Desenvolva um programa que pergunte a distância de uma viagem em Km.
#  Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
print('xXx'*20)
print('CUSTEADOR DE VIAGEM'.center(60))
print('xXx'*20)
km = float(input('Informe a distância da viagem em KM > '))
if km <=200:
    print(f"O preço da viagem é R${km*0.5:.2f}")
else:
    print(f"O preço da viagem é R${km*0.45:.2f}")
