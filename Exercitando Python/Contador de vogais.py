'''
Contar as vogais em uma frase
Crie um programa em Python que solicite ao usuário uma frase e conte quantas vogais (A, E, I, O, U) estão presentes na frase.

Exemplo de entrada: "Olá, tudo bem?"
Saída esperada: A frase contém 4 vogais.
'''

frase = input("Digite uma frase: ")
frase = frase.upper()

cont = 0

for carac in frase:
    if carac in "AEIOU":
        cont += 1

print(f"A frase contém {cont} vogais.")
