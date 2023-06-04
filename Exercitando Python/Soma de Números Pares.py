'''
Exercício 3: Soma dos Números Pares
Escreva um programa que solicite ao usuário um número inteiro positivo e calcule a soma de todos os números pares de 1 até esse número.
'''

soma = 0
max = int(input("Digite um número inteiro: "))

for n in range(1, max + 1):
    if n % 2 == 0:
        soma += n
        print(n)

print(f"A soma de todos números pares até {max} é: {soma}")