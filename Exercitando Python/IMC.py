'''
Exercício 2: Cálculo de IMC
Crie um programa que solicite ao usuário que insira sua altura em metros e seu peso em quilogramas. Em seguida, calcule o 
Índice de Massa Corporal (IMC) e exiba a categoria correspondente de acordo com a tabela abaixo:

IMC < 18.5: Abaixo do peso
18.5 <= IMC < 25: Peso normal
25 <= IMC < 30: Sobrepeso
IMC >= 30: Obeso
'''

altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso em KG: "))

imc = peso / (altura ** 2)

if(imc < 18.5): 
    categoria = "Abaixo do peso"
else:
    if(imc >= 18.5 and imc < 25):
        categoria = "Peso normal"
    else:
        if(imc >= 25 and imc < 30):
            categoria = "Sobrepeso"
        else:
            if(imc >= 30):
                categoria = "Obeso"

print(f"Seu IMC é: {imc:,.2f}")
print(f"Categoria: {categoria}")