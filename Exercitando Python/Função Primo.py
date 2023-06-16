'''
Exercício 1: Verificar Número Primo
Escreva uma função chamada is_prime que recebe um número inteiro como argumento e 
retorna True se o número for primo e False caso contrário. 
Em seguida, escreva um programa que pede ao usuário um número e exibe se ele é primo ou não.
'''
import math

def primo(n):
    if n < 2:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return True
        
n = int(input("Digite um número inteiro: "))

if primo(n):
    print("Número Primo.")
else:
    print("O número não é primo")
