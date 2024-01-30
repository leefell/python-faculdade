'''
Você esta fazendo um trabalho de classificação de solo. Após
colher uma amostra e verificar a quantidade de pontos de água presentes nela,
classicou em:
Rochosoa: se menos ou igual a 10 pontos de água
Firme: se mais de 10 e menor ou igual a 40 pontos
Pantanosa: se mais de 40 e menos ou igual a 80 pontos
Quantidade inválida: se maior que 80 pontos
'''
#Declaração de Variavel
amostra = 0
classificacao = ""

#Algoritmo
amostra = int(input("Insira a quantidade de água: "))
print("")

if(amostra < 10):
    classificacao = "Rochosa"
else:
    if(amostra > 10 and amostra <= 40):
        classificacao = "Firme"
    else:
        if(amostra > 40 and amostra <= 80):
            classificacao = "Pantanosa"
        else:
            classificacao = "Inválida!"


 
print(f"A situação do solo é: {classificacao}")    


'''
a variavel "classificacao" nao é necessaria se eu colocar print no lugar da variavl classificacao dentro dos ifs
else if = elif

if condicao
elif condicao
elif condicao
elif condicao
'''