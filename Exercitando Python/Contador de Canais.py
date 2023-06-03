'''
Foi feita uma pesquisa de audiência de canal de TV em várias casas de uma certa cidade, num determinado dia.
Para cada casa visitada, é fornecido o número do canal (9, 12, 23 ou 40).
    Fazer um algoritmo que:
       - leia um número indeterminado de dados, até que seja digitado o canal 0(zero);
       - Calcule e mostre a porcentagem de audiência de cada emissora;
       - Caso seja digitado algum canal fora dos apresentado acima, informar como outros canais;
       - O número 0(zero) não pode ser considerado um canal.
'''

cont = 0
canal = 1
canal_9 = 0
canal_12 = 0
canal_23 = 0
canal_40 = 0
outros = 0
audi9 = 0.0
audi12 = 0.0
audi23 = 0.0
audi40 = 0.0
audioutros = 0.0



while(canal != 0):
    canal = int(input(" Informe o canal (9 | 12 | 23 | 40): "))

    if(canal == 9):
        canal_9 += 1
        cont += 1
    else:
        if(canal == 12):
            canal_12 += 1
            cont += 1
        else:
            if(canal == 23):
                canal_23 += 1
                cont += 1
            else:
                if(canal == 40):
                    canal_40 += 1
                    cont += 1
                else:
                    if(canal != 0):
                        outros += 1
                        cont += 1
    
if(cont != 0):
    audi9 = (canal_9 * 100)/cont
    audi12 = (canal_12 * 100)/cont
    audi23 = (canal_23 * 100)/cont
    audi40 = (canal_40 * 100)/cont
    audioutros = (outros * 100)/cont

print(f"Audiencia do canal 9: {audi9:,.2f}%")
print(f"Audiência do Canal 12: {audi12:,.2f}%")
print(f"Audiência do Canal 23: {audi23:,.2f}%")
print(f"Audiência do Canal 40: {audi40:,.2f}%")
print(f"Audiência dos outros canais: {audioutros:,.2f}%")