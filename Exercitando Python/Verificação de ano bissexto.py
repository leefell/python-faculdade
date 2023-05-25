'''
Exercício 1: Verificação de ano bissexto
Escreva um programa que peça ao usuário para inserir um ano e, em seguida, determine e exiba se o ano é bissexto ou não. 
Um ano é bissexto se for divisível por 4, exceto quando também for divisível por 100. No entanto, 
anos divisíveis por 400 também são considerados bissextos.
'''

ano = int(input("Digite um ano: "))

if(ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print("É um ano bissexto.")
else:
    print("Não é um ano bissexto.")