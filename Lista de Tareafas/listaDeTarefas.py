tasks = []


def addTask():
    task = input("Insira a Tarefa: ")
    tasks.append(task)  # esse append vai adicionando as tarefas ao final da lista
    print("Tarefa Adicionada.")

def listTask():
    if len(tasks) == 0:  # len retorna o tamanho de um objeto, seja string, int, double, nesse caso o len verifica o tamanho de "tasks"
        print("Nenhuma tarefa encontrada.")
    else:
        print("Tarefas: ")
        for index, task in enumerate(tasks):  # index é pra adicionar o índice na tarefa, 1. 2. 3.
            print(f"{index + 1}. {task}")  # + 1 porque o indice começa em 0 e {task} é a tarefa


def concludeTask():
    listTask()  # exibe a lista de tarefas a serem concluidas
    task_index = int(input("Digite o número da tarefa concluída: ")) - 1  # inicia a contagem em 1
    if task_index < 0 or task_index >= len(tasks):
        print("Nenhuma tarefa com esse número foi localizada.")
    else:
        concludedTask = tasks.pop(task_index)  # .pop remove um elemento e retorna o mesmo, task_index é o parametro do pop.
        print(f"Tarefa '{concludedTask}' concluída!")


def menu():
    print("======== Aplicativo de Gerenciamento de Tarefas ========")
    print("Selecione uma opção: ")
    print("1. Adicionar nova Tarefa.")
    print("2. Listar Tarefas Adicionadas.")
    print("3. Concluir Tarefa.")
    print("0. Sair.")

    opc = input("Opção: ")
    return opc
    print("")


def main():
    opc = menu()
    while opc != '0':
        if opc == '1':
            addTask()
        elif opc == '2':
            listTask()
        elif opc == '3':
            concludeTask()
        else:
            print("Opção Inválida.")

        opc = menu()

    print("Aplicativo Encerrado.")


if __name__ == '__main__':
    main()
