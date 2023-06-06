'''
Criar um algoritmo que leia os elementos de uma matriz inteira 5x5 e escreva os elementos da diagonal principal
'''

linha = 0
coluna = 0
mat = [[0]*5,[0]*5,[0]*5,[0]*5,[0]*5]

for linha in range(0,5,1):
    for coluna in range(0,5,1):
        mat[linha][coluna] = int(input(f"Digite o número para a posição {linha + 1} {coluna + 1}: "))

print("Diagonal principal: ")
for linha in range(0,5,1):
    for coluna in range(0,5,1):
        if(linha == coluna):
            print(f"[{mat[linha][coluna]}]", end = ' ')
    
    