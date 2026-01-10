#024 - Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
cidade = str(input(' Insira o nome da cidade : > ')).strip()
print(f" A cidade {cidade} começa com Santo? : {cidade[:5].capitalize()=='Santo'}")
