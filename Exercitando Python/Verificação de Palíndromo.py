'''
Escreva um programa que verifique se uma palavra ou frase digitada pelo 
usuário é um palíndromo. Um palíndromo é uma palavra ou frase que se lê da mesma forma tanto da esquerda 
para a direita quanto da direita para a esquerda, desconsiderando espaços e diferenciação entre letras maiúsculas e 
minúsculas.
'''

palavra = input("Digite uma palavra ou uma frase: ")
palavra = palavra.replace(" "," ").lower()

palindromo = True
for i in range(len(palavra)):
    if palavra[i] != palavra[len(palavra) - 1 - i]:
        palindromo = False
        break

if palindromo:
    print("A palavra/frase é um palindromo.")
else:
    print("A palavra/frase não é um palindromo.")

