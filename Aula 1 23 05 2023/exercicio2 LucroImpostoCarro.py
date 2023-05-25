'''
O custo ao consumidor de um carro novo é a soma do preço de fabrica com o percentual de lucro do distribuidor
e dos impostos ao preço de fábrica. Faça um programa que receba o preço de fábrica do veículo, o precentual de 
lucro do distribuidor e o percentual de impostos.
Calcule e mostre:
A) o valor correspondente ao lucro do distribuidor;
B) o valor correspondente ao imposto;
C) o preço final do veiculo;
'''

#Declaração de Variavel
precofab = 0.0
perLucro = 0.0
perImposto = 0.0

valorLucro = 0.0
valorImposto = 0.0
precof = 0.0
#Algoritmo

precofab = float(input("Preço de Fabrica do veículo: "))
perLucro = float(input("Percentual de lucro do distribuidor: "))
perImposto = float(input("Percentual de imposto: "))

valorLucro = precofab * perLucro/100
valorImposto = perImposto * precofab/100
precof = precofab + valorLucro + valorImposto
print(f"")
print(f"")


print(f"Lucro do Distribuidor: {valorLucro:,.2f}") #:,.2f -> numero de casas decimais
print(f"Valor correspondente ao Imposto: {valorImposto:,.2f}")
print(f"Preço final: {precof:,.2f}")
