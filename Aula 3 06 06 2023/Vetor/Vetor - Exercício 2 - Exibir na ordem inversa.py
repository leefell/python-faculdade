'''
Criar um algoritmo que leia 10 números pelo teclado e exiba os números na ordem inversa da que 
os números foram digitados
'''

cont = 0
n = [0.0]*10

for cont in range(0,10,1):
    n[cont] = float(input(f"Digite o {cont + 1} número: ")) # esse + 1 é só pra detalhe de saida


print("Ordem Inversa: ")
for cont in range(9,-1,-1):
    print(f"{n[cont]}", end= ' ')
