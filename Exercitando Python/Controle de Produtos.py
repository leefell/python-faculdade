#Inicialização variáveis
contador = 0
opc = 1
QuantidadeAcougue = 0
QuantidadeLimpeza = 0
QuantidadePadaria = 0
QuantidadeQuitanda = 0
PrecoAcougue = 0
PrecoLimpeza = 0
PrecoPadaria = 0
PrecoQuitanda = 0

#Loop
while opc != 0:
    print("Escolha uma opção de grupo para o produto ou digite 0 para encerrar: ")
    print("1 - Açougue ")
    print("2 - Produto de Limpeza ")
    print("3 - Padaria")
    print("4 - Quitanda ")
    opc = int(input("Informe a opção: "))
    print()

    if opc == 1:
        QuantidadeAcougue = int(input("| Açougue | Quantidade de kg's: "))
        if QuantidadeAcougue > 5:
            PrecoAcougue = 25 * QuantidadeAcougue * 0.95
        else:
            PrecoAcougue = 25 * QuantidadeAcougue
        print()

    if opc == 2:
        QuantidadeLimpeza = int(input("| Produto de limpeza | Quantidade de produtos: "))
        if QuantidadeLimpeza > 5:
            PrecoLimpeza = 18 * QuantidadeLimpeza * 0.95
        else:
            PrecoLimpeza = 18 * QuantidadeLimpeza
        print()

    if opc == 3:
        QuantidadePadaria = int(input("| Padaria | Quantidade de produtos: "))
        if QuantidadePadaria > 5:
            PrecoPadaria = 10 * QuantidadePadaria * 0.95
        else:
            PrecoPadaria = 10 * QuantidadePadaria
        print()

    if opc == 4:
        QuantidadeQuitanda = int(input("| Quitanda | Quantidade de produtos:"))
        if QuantidadeQuitanda > 5:
            PrecoQuitanda = 12 * QuantidadeQuitanda * 0.95
        else:
            PrecoQuitanda = 12 * QuantidadeQuitanda
        print()

