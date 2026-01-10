#013 - Faça um algoritmo que leia o salário de um funcionário e o percentual que será aumentado. Calcule e mostre seu novo salário.
print(f"{' CÁLCULO DE NOVO SALÁRIO ':+^80}")
salario = float(input('Insira o valor do salário atual: > R$'))
aumento = float(input('Insira o percentual do aumento: > '))
novosalario = salario * (1 + (aumento/100 ))
print(f"O novo salário é de R${novosalario:.02f}")
