'''
Construa um algoritmo que determine quanto será gasto para encher o tanque de um carro. O usuário fornecerá os seguintes dados: 
Tipo de carro (TC) (G – gasolina ou A – álcool) e Capacidade do tanque (CT), em litros. 
Após a escolha do tipo de veículo e da capacidade do tanque, o sistema irá imprimir uma mensagem falando o tipo do 
carro(Gasolina ou álcool) e pedirá para o usuário informar o valor do preço do litro do combustível.
Como saída, será informado para o usuário, o valor, em reais, do preço de se encher tanque de combustível.
'''

tc = input("Informe o tipo de carro: G - Gasolina | A - Álcool: ")
ct = float(input("Informe a capacidade do tanque em litros: "))

print()

print(f"Tipo de carro: {tc}")
valorLitro = float(input("Informe o valor do litro do combustível: "))

valorf = ct * valorLitro

print(f"O valor para encher o tanque de combutível será R$: {valorf:,.2f}")
print()
