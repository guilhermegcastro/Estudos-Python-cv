#005 - Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
print(f"{' ANTECESSOR E SUCESSOR ':-^50}")
numero = int(input('Insira um número: '))
an = numero - 1
su = numero + 1
print(f"O antecessor de {numero} é {an} \nO sucessor de {numero} é {su}")
