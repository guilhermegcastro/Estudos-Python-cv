#029 - Escreva um programa que leia a velocidade de um carro.
#  Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#  A multa vai custar R$7,00 por cada Km acima do limite.
MULTA = 7.0
LIMITE = 80.0
print('=-='*20)
print('RADAR ELETRÔNICO'.center(60))
print('=-='*20)
km = float(input('Qual foi a velocidade do carro? > '))
if km <= LIMITE:
    print('O motorista não foi multado.')
else: 
    km_acima = km - LIMITE
    print(f"O motorista foi multado no valor de R${km_acima*MULTA:.2f} (R${MULTA:.2f} por cada km acima de {LIMITE:.0f}km [{km_acima}km])")