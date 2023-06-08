'''
Exercício 3: Fibonacci
Escreva um programa que exiba os primeiros "n" termos da sequência de Fibonacci, 
onde "n" é um número inteiro fornecido pelo usuário. A sequência de Fibonacci é uma sequência 
numérica em que cada termo é a soma dos dois termos anteriores.
'''

n = int(input("Digite um número: "))
termo1 = 0
termo2 = 1

print(termo1)
print(termo2)

for i in range(2, n):
    ptermo = termo1 + termo2
    print(ptermo)
    termo1 = termo2
    termo2 = ptermo