'''
Exercício 1: Verificar se um número é par ou ímpar
Escreva um programa que peça ao usuário para digitar um número e, 
em seguida, verifique se o número é par ou ímpar. O programa deve exibir uma mensagem adequada na saída.
'''

num = 0

num = int(input("Digite um número: "))

if(num % 2 == 0):
    print("O número é par!")
else:
    print("O número é ímpar!")
