'''Exercício 4: Tabuada
Peça ao usuário para digitar um número inteiro e exiba a tabuada desse número de 1 a 10.'''

n = int(input("Digite um número: "))

print(f"Tabuada do {n}: ")
for i in range(1, 11):
    r = n * i
    print(f"{n} X {i} = {r}")
