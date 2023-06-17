'''
Faça um algoritmo que receba 5 números e ao final mostre quem é o maior e o menor número digitado.
Deve-se fazer uma função para verificar o maior e outra para verificar o menor.
O menor e o maior número devem ser retornados para o programa principal para, então, serem mostrados.
'''
num = 0
maiornumero = 0
menornumero = 0

def maior(num, cont, maior):
    if(cont == 1):
        maior = num
    else:
        if(num >= maior):
            maior = num
    return maior

def menor(num, cont, menor):
    if(cont == 1):
        menor = num
    else:
        if(num <= menor):
            menor = num
    return menor

for cont in range(1, 6, 1):
    numero = int(input("Digite um número inteiro: "))
    maiornumero = maior(numero, cont, maiornumero)
    menornumero = menor(numero, cont, menornumero)


print(f"O maior número é: {maiornumero}")
print(f"O menor número é: {menornumero}")
