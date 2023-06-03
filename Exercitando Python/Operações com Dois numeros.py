'''
Exercício 2: Calculadora básica
Crie um programa que funcione como uma calculadora simples. 
Peça ao usuário para digitar dois números e a operação desejada (+, -, *, /). 
Em seguida, execute a operação e exiba o resultado na saída.
'''

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
op = input("Digite a operação desejada (+, -, *, /): ")

if(op == "+"):
    resultado = numero1 + numero2
else:
    if(op == "-"):
        resultado = numero1 - numero2
    else:
        if(op == "*"):
            resultado = numero1 * numero2
        else:
            if(op == "/"):
                resultado = numero1 / numero2
            else:
                print("Opção Inválida!")
                
               
print(f"O resultado é: {resultado}")