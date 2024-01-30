'''
Desenvolver um algoritmo que chame uma função que receba dois
números como parâmetro, realize a soma destes números e mostre
o resultado na tela.
'''
n1 = 0
n2 = 0
resultado = 0

def somar_numeros(numero1, numero2):
    resultado = numero1 + numero2
    print(f"A soma dos números é: {resultado}")

n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))
somar_numeros(n1,n2)