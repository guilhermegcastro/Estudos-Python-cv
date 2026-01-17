#040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#    Média abaixo de 5.0: REPROVADO
#    Média entre 5.0 e 6.9: RECUPERAÇÃO
#    Média 7.0 ou superior: APROVADO
print('--='*10,'CÁLCULO DE MÉDIA','=--'*10)
nota1 = float(input('Insira a primeira nota do aluno: > '))
nota2 = float(input('Insira a segunda nota do aluno: > '))
media = (nota1+nota2)/2
print(f"Média: {media}")
if media < 5.0:
    print('STATUS: REPROVADO')
elif media < 7:
    print('STATUS: RECUPERAÇÃO')
else:
    print('STATUS: APROVADO')
