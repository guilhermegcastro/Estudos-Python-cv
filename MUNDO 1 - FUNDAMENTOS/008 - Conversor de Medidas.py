#008 - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
print(f"{' CONVERSOR DE MEDIDAS' :=^80}")
medida = float(input('Informe a medida (metros) para converter: > '))
print(f" A conversão de {medida:.0f}m corresponde a:\n {medida*100:.0f}cm\n {medida*1000:.0f}mm")
