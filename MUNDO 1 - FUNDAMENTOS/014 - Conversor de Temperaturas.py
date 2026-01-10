#014 - Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
print(f"{' CONVERSOR DE TEMPERATURAS ':.^80}")
c = float(input('Insira a temperatura em Celsius: > '))
f = (c * 1.8) + 32
print(f"{c:.02f}°C equivale a {f:.02f}°F")
