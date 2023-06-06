'''
Desenvolver um algoritmo que chame uma função que receba dois
números como parâmetro, realize a soma destes números e devolva
o resultado para o programa principal mostrar na tela.
'''
n1 = 0
n2 = 0
resultado = 0

def somar_numeros(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

#1 forma
n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))
print(f"A soma dos números é: {somar_numeros(n1,n2)}")

#2 forma
#result = somar_numeros(int(input("Informe o primeiro número: ")),int(input("Informe o segundo número: ")))
#print(f"A soma dos números é: {result}")