#042 - Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
    # EQUILÁTERO: todos os lados iguais
    # ISÓSCELES: dois lados iguais
    # ESCALENO: todos os lados diferentes
print('*'*30, '| ANÁLISE DE TRIÂNGULO |', '*'*30)
lado1 = float(input('Insira o primeiro lado do triângulo: > '))
lado2 = float(input('Insira o segundo lado do triângulo: > '))
lado3 = float(input('Insira o terceiro lado do triângulo: > '))
lMaior = max(lado1, lado2, lado3)
lMenor = min(lado1, lado2, lado3)
lMeio = lado1 + lado2 + lado3 - lMaior - lMenor
if lMenor + lMeio > lMaior:
    if lMaior == lMeio == lMenor:
        tipo = 'EQUILÁTERO'
    elif lMaior == lMeio or lMenor == lMeio:
        tipo = 'ISÓSCELES'
    else:
        tipo = 'ESCALENO'
    print(f"É possível formar um triângulo {tipo} com as retas fornecidas.")
else: 
    print("Não é possível formar um triângulo com as retas fornecidas.")
    