'''
Exercício 1: Verificação de Número Primo
Escreva um programa que solicite ao usuário um número inteiro 
positivo e verifique se ele é um número primo. Um número primo é aquele que é divisível apenas por 1 e por ele mesmo.
'''

n = int(input("Digite um número inteiro positivo: "))

#todo primo é maior que 1
if n > 1:
    primo = True

    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            primo = False
            break

    if primo:
        print(f"O número {n} é um número primo!")

    else:
        print(f"O número {n} não é um número primo!")
else:
    print("O número digitado não é primo!")       
