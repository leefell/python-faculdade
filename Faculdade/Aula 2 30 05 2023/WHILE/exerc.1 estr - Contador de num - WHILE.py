'''
Faça um algoritmo que solicite N números inteiros até que o número 0 seja digitado.
Ao final o algoritmo deve informar o maior e o menor número digitado
O número 0 não deve ser contado.
'''
n = 0
maior = 0
menor = 0

n = int(input("Informe o número ou digite 0 para encerrar: "))
maior = n
menor = n
while(n != 0):
    if(n > maior):
        maior = n

    if(n < menor) and (n != 0):
        menor = n

    n = int(input("Informe o número ou digite 0 para encerrar: "))

print(f"O maior número digitado é: {maior}")
print(f"O menor número digitado é: {menor}")
