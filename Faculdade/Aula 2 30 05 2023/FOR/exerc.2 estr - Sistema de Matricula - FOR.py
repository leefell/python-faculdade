'''
Uma escola está realizando matrículas para um curso aberto à comunidade, com limite de 20 vagas. 
Assumindo que os alunos são cadastrados por computador, escreva um algoritmo que:
- Leia a idade e o sexo do aluno;
- Informe que a turma está lotada quando o número de inscritos atingir a quantidade de vagas;
- Mostre a idade média dos candidatos;
- Mostre a quantidade de mulheres inscritas;
- Mostre os candidatos (homens e mulheres) maiores de idade
'''


idade_soma = 0
idade_media = 0
maiorDeIdade = 0
mulheres = 0

for cont in range(0,20,1): # alterar pra 20
    idade = int(input("Digite sua idade: "))
    if(idade >= 18):
       maiorDeIdade = maiorDeIdade + 1
    sexo = str(input("Digite seu Sexo: M - Masculino / F - Feminino: ")).upper() #upper no fim da frase vai transformar tanto o f quanto o m em upper
    if(sexo == 'F'):
       mulheres = mulheres + 1
    idade_soma += idade   


print("A quantidade de vagas já foi preenchida.")

idade_media = idade_soma / 20

print(f"\nA idade média dos canditados é: {idade_media}")
print(f"A quantideade de mulheres inscritas é: {mulheres}")
print(f"A quantidade de pessoas Maiores de Idade é: {maiorDeIdade}")