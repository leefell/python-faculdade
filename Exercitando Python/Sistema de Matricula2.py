'''
Uma escola está realizando matrículas para um curso aberto à comunidade, com limite de 20 vagas. 
Assumindo que os alunos são cadastrados por computador, escreva um algoritmo que:
- Leia a idade e o sexo do aluno;
- Informe que a turma está lotada, quando o número de inscritos atingir a quantidade de vagas;
- Mostre a idade média dos candidatos;
- Mostre a quantidade de mulheres inscritas;
- Mostre os candidatos (homens e mulheres) maiores de idade.
'''

qtd_mulheres = 0
maioridade = 0
somaidades = 0.0

print("Preencha os dados abaixo para realizar o cadastro:")

for cont in range(0,20,1):
    idade = int(input("Digite sua idade: "))
    sexo = input("Digite seu sexo: M - Masculino | F - Feminino: ")

    if(sexo.upper() == "F"):
        qtd_mulheres += 1
    
    if(idade > 18):
        maioridade += 1

    somaidades += idade

idade_media = somaidades / 20

print("Todas as vagas foram preenchidas!")
print(f"Idade média dos canditados: {idade_media}")
print(f"Quantidade de Mulheres Inscritas: {qtd_mulheres}")
print(f"Maiores de idade: {maioridade}")

