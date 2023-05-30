'''
Faça um algoritmo que solicite a resposta de x pessoas sobre a preferência de um produto. Esta pessoa deverá responder 1 se gostou do primeiro produto
ou 2 se gostou do segundo produto e 3 pra quem gostou do terceiro produto. Ao final deve ser impresso na tela a quantidade de pessoas que gostaram do produto 1, do 2 e do 3.
Para finalizar o sistema deve ser digitado 0.
'''
n = 1
p1 = 0
p2 = 0
p3 = 0

while(n != 0):
    n = int(input("Informe qual produto você mais gostou (1 | 2 | 3): "))
    
    if(n == 1):
        p1 += 1
    else:
        if(n == 2):
            p2 += 1
        else:
            if(n == 3):
                p3 += 1
        

print(f"Gostaram do primeiro produto: {p1}")
print(f"Gostaram do segundo produto: {p2}")
print(f"Gostaram do terceiro produto: {p3}")