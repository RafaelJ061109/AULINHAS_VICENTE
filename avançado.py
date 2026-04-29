from abc import ABC, abstractmethod

tarefas = []

def add_tarefa(tarefa):
    tarefas.append(tarefa)

class Tarefa(ABC):
    total_tarefas = 0
    total_execucoes = 0

    def __init__(self, descricao):
        self._descricao = descricao
        self._execucoes = 0
        self._bloqueada = False
        Tarefa.total_tarefas += 1

    @abstractmethod
    def executar(self):
        pass

    @property
    def tipo(self):
        return 'Generica'

    def __str__(self):
        return f'[{self.tipo}] | {self._descricao} | (Execuções: {self._execucoes})'


class TarefaComum(Tarefa):
    total = 0

    def __init__(self, descricao):
        super().__init__(descricao)
        TarefaComum.total += 1

    @property
    def tipo(self):
            return 'Comum'

    def executar(self):
        if self._bloqueada:
            return "Tarefa bloqueada!"

        self._execucoes += 1
        Tarefa.total_execucoes += 1

        return f'[COMUM] | {self._descricao} | Execuções: {self._execucoes}'


class TarefaLimitada(Tarefa):
    total = 0

    def __init__(self, descricao, limite):
        super().__init__(descricao)
        self.__limite = limite
        TarefaLimitada.total += 1

    @property
    def tipo(self):
            return 'Limitada'

    def executar(self):
        if self._bloqueada:
            return "Tarefa bloqueada!"

        if self._execucoes >= self.__limite:
            self._bloqueada = True
            return "Limite atingido! Tarefa bloqueada."

        self._execucoes += 1
        Tarefa.total_execucoes += 1

        return f'[LIMITADA] | {self._descricao} | {self._execucoes}/{self.__limite}'

class TarefaAlternada(Tarefa):
    total = 0

    def __init__(self, descricao, ativa):
        super().__init__(descricao)
        self._ativa = ativa.lower() == 's'
        TarefaAlternada.total += 1

    @property
    def tipo(self):
            return 'Alternada'

    def executar(self):
        if self._bloqueada:
            return "Tarefa bloqueada!"

        if not self._ativa:
            self._ativa = True
            return "Não pode executar agora. Tente na próxima."

        self._execucoes += 1
        Tarefa.total_execucoes += 1
        self._ativa = False

        return f'[Alternada] | {self._descricao} | Executada!'

while True:
    print("\n==== SISTEMA DE TAREFAS ====")
    print("1 - Criar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("4 - Executar tarefas")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '0':
        print("Encerrando...")
        break

    elif opcao == '1':
        print("Tipo de tarefa:")
        print("1 - Comum")
        print("2 - Limitada")
        print("3 - Alternada")

        tipo_op = input("Opção: ")
        descricao = input("Descrição: ")

        if tipo_op == '1':
            tarefa = TarefaComum(descricao)

        elif tipo_op == '2':
            limite = int(input("Limite de execuções: "))
            tarefa = TarefaLimitada(descricao, limite)

        elif tipo_op == '3':
            ativa = input("Ativa? [S/N]: ")
            tarefa = TarefaAlternada(descricao, ativa)

        else:
            print("Opção inválida!")
            continue

        add_tarefa(tarefa)
        print("Tarefa criada!")

    elif opcao == '2':
        print("Lista de tarefas:")
        for i, tarefa in enumerate(tarefas):
            print(f"{i} - {tarefa}")
        print(f'Total de tarefas: {len(tarefas)}')
        print(f'Comum: {TarefaComum.total}, Limitada: {TarefaLimitada.total}, Alternada: {TarefaAlternada.total}')

    elif opcao == '3':
        ind = int(input("Digite o índice da tarefa: "))
        if 0 <= ind < len(tarefas):
            tarefas.pop(ind)
            print("Tarefa removida com sucesso!")
        else:
            print("Índice inválido.")

    elif opcao == '4':
        print("Executando tarefas:")
        for tarefa in tarefas:
            print(tarefa.executar())

    else:
        print("Opção inválida!")
