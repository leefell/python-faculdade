'''
Exercício 2: Contagem Regressiva
Crie um programa que solicite ao usuário um 
número inteiro positivo e faça uma contagem regressiva a partir desse número até zero. Exiba cada número na tela.
'''

n = int(input("Digite um número para iniciar a contagem regressiva: "))

while(n >= 0):
    print(n)
    n -= 1

print("Fim da contagem regressiva!")
