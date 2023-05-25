'''
Questão 2: Classificar o tipo de triângulo
Crie um programa que solicite ao usuário que insira três comprimentos de lados de um triângulo e, em seguida, 
determine e exiba o tipo de triângulo na saída. O programa deve verificar se é um triângulo válido e, 
em seguida, classificá-lo como equilátero, isósceles ou escaleno.
'''

lado1 = float(input("Digite o valor do primeiro lado: "))
lado2 = float(input("Digite o valor do segundo lado: "))
lado3 = float(input("Digite o valor do terceiro lado: ")) 

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado3 + lado2 > lado1:
    if(lado1 == lado2 == lado3):
        print("Triângulo Equilátero.")
    else:
        if(lado1 == lado2 or lado1 == lado3 or lado2 == lado3):
            print("Triângulo Isóceles.")
        else:
            print("Triângulo Escaleno.")
else:
    print("Não é um triângulo válido.")