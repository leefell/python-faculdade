'''
A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e número de filhos.        
Elabore um algoritmo para apresentar:
 a) Média do salário da população;
 b) Média do número de filhos;
 c) Maior salário;
 d) Percentual de pessoas com salário até R$ 100,00.
O sistema deve ficar solicitando novos dados até o usuário mandar parar usando o menu:
- Escolha uma opção:
    1 - para cadastrar
    2 - para sair
'''

opc = 1
somasal = 0.0
totalfilho = 0
cadastrados = 0
qtd100 = 0
maiorsal = 0

while (opc == 1):
    print("Escolha uma opcção:")
    print("1 - Cadastro")
    print("2 - Sair")
    opc = int(input())

    if(opc == 1):
        salario = float(input("Digite o salário: "))
        filho = int(input("Digite o número de filhos: "))

        somasal += salario
        totalfilho += filho
        cadastrados += 1

        if(salario > maiorsal):
            maiorsal = salario
        
        if(salario <= 100):
            qtd100 += 1
    
mediasal = somasal/cadastrados
mediafilho = totalfilho/cadastrados
percentual = qtd100/cadastrados*100

print(f"A média de salário é: {mediasal:,.2f}")
print(f"A média de filhos é: {mediafilho:,.2f}")
print(f"O maior salário é: {maiorsal}")
print(f"{percentual:,.2f}% Recebem até R$ 100,00")