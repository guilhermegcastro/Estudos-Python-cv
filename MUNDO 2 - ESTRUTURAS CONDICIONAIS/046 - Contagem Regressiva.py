#046 - Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep 
SEGUNDOS = 10
print(f"Contagem de Fogos em {SEGUNDOS} segundos!")
for contagem in range(SEGUNDOS,-1, -1):
    sleep(1)
    print(contagem, end=' ', flush=True)
sleep(0.05)
print("""!
      \\ | /                \\ | /
    --  *  --            --  *  --
      / | \\                / | \\ 
""")
