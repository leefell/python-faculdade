'''
Faça um programa quew receba o salário base de um funcionário
Calcule e mostre o salário a receber, sabendo que esse funcionário tem gratificação
de R$50,00 e paga 10% de imposto sobre o salário base
'''

#Declaração de Variavel
salario = 0.0
imposto = 0.0
grat = 0.0
nsal = 0.0
#grat = 50.0 (uma das opcoes é declarar a gratificacao aqui em cima porque ela é uma variavel como qualquer outra)

#Algoritmo
salario = float(input("Informe seu salario: "))
imposto = salario * 0.10 # ou imposto = salario * (10/100)
grat = 50
nsal = (salario - imposto) + grat

#cls limpa o terminal
#print(f"Salario: {salario} Imposto: {imposto} Novo salario com gratificação: {nsal}")
print(f"Salario: {salario}")
print(f"Imposto: {imposto}")
print(f"Gratificação: {grat}")
print(f"Novo salario com gratificação: {nsal}")

