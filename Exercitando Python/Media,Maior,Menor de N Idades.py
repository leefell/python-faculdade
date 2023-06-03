'''
Construir um algoritmo que leia a idade de N pessoas.
O sistema deve calcular: a média das idades, a menor e a maior idade informada.
'''

idade_soma = 0.0
cont = 0
n = 0
idademenor = 0
idademaior = 0
idade_soma = 0.0
idade_media = 0.0


n = int(input("Informe o número de pessoas: "))
print()

for cont in range(0, n, 1):
    idade = int(input("Digite a idade da pessoa: "))

    if(cont == 0):
        idademenor = idade
        idademaior = idade
    else:
        if(idade > idademaior):
            idademaior = idade

        if(idade < idademenor):
            idademenor = idade

    idade_soma += idade

idade_media = idade_soma / n

print(f"A maior idade é: {idademaior}")
print(f"A menor idade é: {idademenor}")
print(f"A média das idades é: {idade_media:,.2f}")
    