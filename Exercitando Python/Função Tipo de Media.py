'''
Faça um algoritmo que receba três notas de um aluno como parâmetros e o tipo da média que deverá ser calculada.
Se o tipo da média for "A" a função calcula a média aritmética das notas do aluno, se for "P" a 
função calcula a média ponderada pesos 5, 3 e 2. A média calculada deve ser devolvida ao programa principal para, então, ser mostrada.
'''
mediaA = 0.0
mediaP = 0.0
mediaTotal = 0.0
opc = ""

def aritmetica(n1, n2, n3):
    mediaA = (n1 + n2 + n3) / 3
    return mediaA

def ponderada(n1, n2, n3):
    mediaP = ((n1 * 5) + (n2 * 3) + (n3 * 2)) / 10
    return mediaP

print("Bem-Vindo ao sistema de Média de Notas! ")

nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))
print()

print("Escolha o tipo de média: ")
print("Aritmética - A / Ponderada - P")
opc = input("Digite a inicial da média: ").upper()

if(opc == "A"):
    mediaTotal = aritmetica(nota1, nota2, nota3)
else:
    if(opc == "P"):
        mediaTotal = ponderada(nota1, nota2, nota3)
    else:
        print("Média Inválida!")

print(f"A média é: {mediaTotal:,.1f}")

