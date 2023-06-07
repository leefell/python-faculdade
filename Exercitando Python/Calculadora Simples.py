'''
Exercício: Calculadora Simples
Escreva um programa que simule uma calculadora simples. 
O programa deve solicitar ao usuário dois números e uma operação (adição, subtração, multiplicação ou divisão). 
Em seguida, deve executar a operação selecionada e exibir o resultado.
'''

def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

print("Calculadora")

while True:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    print("Escolha a operação: ")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    opcao = int(input("Digite o número correspondente a operação desejada: "))

    if(opcao == 1):
        resultado = adicao(num1, num2)
    else:
        if(opcao == 2):
            resultado = subtracao(num1, num2)
        else:
            if(opcao == 3):
                resultado = multiplicacao(num1, num2)
            else:
                if(opcao == 4):
                    resultado = divisao(num1, num2)
                else:
                    print("Opção Inválida.")
                    continue

    print(f"Resultado: {resultado}")

    repetir = input("Deseja realizar uma nova operação? (s/n): ")
    if repetir.lower() != "s":
        break
