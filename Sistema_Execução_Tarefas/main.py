tarefas = []

def add_tarefa(tarefa):
        tarefas.append(tarefa)

def remover_por_ind():
    for tarefa in tarefas:
            tarefas.remove(tarefa)
            print("Tarefa removida com sucesso!")
            return
    print("Tarefa não encontrada.")
    
class Tarefa_comum():
    def __init__(self, descricao):
        self.descricao = descricao

    def __str__(self):
            return f'Tipo: Comum | Descrição: {self.descricao} | Executando...'

class Tarefa_limitada(Tarefa_comum):
    def __init__(self, descricao, limite):
        super().__init__(descricao)
        self.limite = limite
        self.execucoes = 0

    def __str__(self):
        if self.execucoes == self.limite:
            return f'Limite atingido!'
        else:
            self.execucoes += 1
            return f'Tipo: Limitada | Descrição: {self.descricao} | Limite: {self.limite} | Executando...'


class Tarefa_Alternada(Tarefa_comum):
    def __init__(self, descricao, ativa):
        super().__init__(descricao)
        self.ativa = True if ativa.lower() == 's' else False

    def __str__(self):
        if self.ativa == True:
            self.ativa = False
            return f'Tipo: Alternada | Descrição: {self.descricao} | Executando...' 
        else:
            self.ativa = True
            return 'Proxima vez pode ser executada'

while True:
    print("\n==== SISTEMA DE TAREFAS ====")
    print("1 - Criar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("0 - Sair")
#MENU
    opcao = input("Escolha uma opção: ")
#OPÇÃO DE ESCOLHA DO MENU

    if opcao == '0':
        print("Compreensivel, tenha uma otima vida.")
        break
    #FECHAMENTO DO PROGRAMA

    elif opcao == '1':
        print("Tipo de tarefa:")
        print("1 - Comum")
        print("2 - Limitada")
        print("3 - Alternada")
    #MENU DE TAREFAS

        tipo_op = input("Opção: ")
        #ESCOLHA DO TIPO

        descricao = input("Descrição: ")
        #FIXO POR ESTAR EM TODAS

        if tipo_op == '1':
            tarefa = Tarefa_comum(descricao)
        #TIPO COMUM

        elif tipo_op == '2':
            limite = int(input("Limite de execuções: "))
            tarefa = Tarefa_limitada(descricao, limite)
        #TIPO LIMITADO

        elif tipo_op == '3':
            ativa = input("Ativa? [S/N]: ")
            tarefa = Tarefa_Alternada(descricao, ativa)
        #TIPO ALTERNADO

        else:
            print("Opção inválida!")
            continue
        #SE NENHUM INPUT FOR EXECUTADO IGUAIS AS OPÇÕES O CODIGO MOSTRARÁ O PRINT

        add_tarefa(tarefa)
        print("Tarefa criada!")
        #FIXO, APÓS TODOS OS DADOS FOREM DADOS TODOS OS TIPOS VÃO PRA LISTA

    elif opcao == '2':
        print("Lista de tarefas:")
        for i, tarefa in enumerate(tarefas):    
            print(f"{i} - {tarefa}")
    #LISTA TODAS AS TAREFAS

    elif opcao == '3':
        ind = int(input("Digite o índice da tarefa: "))
        if 0 <= ind < len(tarefas):
            tarefas.pop(ind)
            print("Tarefa removida com sucesso!")
        else:
            print("Índice inválido.")
    #REMOVE PELO INDICE DA TAREFA

    else:
        print("Opção inválida!")
