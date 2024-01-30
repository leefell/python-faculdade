'''
Construir um algoritmo que leia a idade de N pessoas.
O sistema deve calcular: a média das idades, a menor e a maior idade informada.
'''

cont = 0
idade_soma = 0.0
idadeMaior = 0

qtd = int(input("Insira a quantidade de pessoas: "))

for cont in range(1,qtd+1,1): #esse qtd + 1 faz o programa contar o numero do n ate o n+1 // ou poderia ser 0,qtd,1
    idade = int(input(f"Insira a {cont} idade: "))

    if(cont == 1):
       idadeMaior = idade
       idadeMenor = idade
    else:
        if(idade > idadeMaior):
           idadeMaior = idade
        
        if(idade < idadeMenor):
           idadeMenor = idade
      
idade_soma += idade
idade_media = idade_soma / qtd

print(f"A idade média é: {idade_soma:,.2f}")
print(f"A menor idade é: {idadeMenor}")
print(f"A maior idade é: {idadeMaior}")