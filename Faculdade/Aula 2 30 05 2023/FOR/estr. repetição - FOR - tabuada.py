#declaracao pra nao pegar lixo de memoria
contador = 0
numero = 0

numero = int(input("Informe o número para tabuada: "))

for contador in range(1,11,1): #o ultimo 1 do passo é dispensavel porque o computador assume que o passo é 1 quando nao especificado
    print(f"{numero} X {contador} = {numero * contador}")