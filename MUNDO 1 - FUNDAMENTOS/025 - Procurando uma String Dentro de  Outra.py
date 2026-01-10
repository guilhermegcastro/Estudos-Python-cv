#025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = str(input("Informe o nome completo de alguém: > ")).strip()
print(f"Contém Silva no nome? : {"SILVA" in nome.upper()}")
