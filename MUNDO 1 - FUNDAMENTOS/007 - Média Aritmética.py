#007 - Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
print(f"{' CÁLCULO DE MÉDIA ARITMÉTICA ' :#^80}")
nome = input('Informe o nome do/a aluno/a: > ')
n1 = float(input('Informe a nota da primeira prova: > '))
n2 = float(input('Informe a nota da segunda prova: > '))
media = (n1+n2)/2
print(f"{nome} obteve uma média de {media:.2f}")

#* Abaixo é apenas um extra, por eu já vir tendo conhecimento da linguagem C e querer explorar mais o Python antecipadamente.
situacao = 'APROVADO' if media >= 6.0 else 'REPROVADO'
print(f"Situação: {situacao}")
