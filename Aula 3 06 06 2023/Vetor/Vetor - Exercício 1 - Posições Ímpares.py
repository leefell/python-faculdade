'''
Faça um algoritmo que leia 5 números reais em um vetor e depois mostre os números
localizados nas posição(indices) ímpares.
'''

vet = [0.0]*5
cont = 0

for cont in range(0,5,1):
    vet[cont] = int(input(f"Digite um número real para a posição {cont}: "))
    
print("Números nas posições Ímpares: ")    
for cont in range(0,5,1):   
    if(cont % 2 != 0):
        print(f"{vet[cont]}", end= ' ')

#nesse programa o que esta sendo testado é o INDICE
