#043 - Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

#     IMC abaixo de 18.5: Abaixo do Peso

#     Entre 18.5 e 25: Peso Ideal

#     Entre 25 e 30: Sobrepeso

#     Entre 30 e 40: Obesidade

#     Acima de 40: Obesidade Mórbida

# (Fórmula do IMC: Peso ÷ [Altura^2] )

print('='*30, 'CÁLCULO IMC', '='*30)
altura = float(input('Informe a sua altura (m): > '))
peso = float(input('Informe o seu peso (kg): > '))
imc = peso / (altura**2)
if imc < 18.5:
    estado = 'Abaixo do peso'
elif imc < 25:
    estado = 'Peso ideal'
elif imc < 30:
    estado = 'Sobrepeso'
elif imc < 40:
    estado = 'Obesidade'
else:
    estado = 'Obesidade mórbida'
print(f"IMC: {imc:.2f} -- Estado: {estado}")
