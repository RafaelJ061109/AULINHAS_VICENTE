from abc import ABC, abstractmethod

class GerenciadorTarefas:

    def __init__(self):
        self._tarefas = []
    def adicionar(self, tarefa):
        self._tarefas.append(tarefa)
    def remover(self, indice):

        if 0 <= indice < len(self._tarefas):
            tarefa = self._tarefas.pop(indice)
            if isinstance(tarefa, TarefaComum):
                TarefaComum.total -= 1
            elif isinstance(tarefa, TarefaLimitada):
                TarefaLimitada.total -= 1
            elif isinstance(tarefa, TarefaAlternada):
                TarefaAlternada.total -= 1
            elif isinstance(tarefa, TarefaBloqueavel):
                TarefaBloqueavel.total -= 1
            return True
        
        return False

    def obter(self, indice):

        if 0 <= indice < len(self._tarefas):
            return self._tarefas[indice]

        return None

    def listar(self):
        return self._tarefas

class Tarefa(ABC):

    total_tarefas = 0
    total_execucoes = 0

    def __init__(self, descricao: str):
        self._descricao = descricao
        self._execucoes = 0
        Tarefa.total_tarefas += 1

    @property
    @abstractmethod
    def tipo(self):
        pass

    @abstractmethod
    def executar(self):
        pass

    def __str__(self):
        return (f'[{self.tipo}] | 'f'{self._descricao} | 'f'(Execuções: {self._execucoes})')

class TarefaComum(Tarefa):

    total = 0

    def __init__(self, descricao: str):
        super().__init__(descricao)
        TarefaComum.total += 1

    @property
    def tipo(self):
        return 'Comum'

    def executar(self):
        self._execucoes += 1
        Tarefa.total_execucoes += 1
        return (f'[COMUM] | 'f'{self._descricao} | 'f'Execuções: {self._execucoes}')

class TarefaLimitada(Tarefa):

    total = 0

    def __init__(self, descricao: str, limite: int):
        super().__init__(descricao)
        self.__limite = limite
        TarefaLimitada.total += 1

    @property
    def tipo(self):
        return 'Limitada'

    def executar(self):

        if self._execucoes >= self.__limite:
            return 'Limite de execuções atingido!'
        self._execucoes += 1
        Tarefa.total_execucoes += 1
        return (f'[LIMITADA] | 'f'{self._descricao} | 'f'{self._execucoes}/{self.__limite}')
    
class TarefaAlternada(Tarefa):

    total = 0

    def __init__(self, descricao: str, ativa: bool):
        super().__init__(descricao)
        self._ativa = ativa.lower() == 's'
        TarefaAlternada.total += 1

    @property
    def tipo(self):
        return 'Alternada'

    def executar(self):

        if not self._ativa:
            self._ativa = True
            return 'Não pode executar agora. Tente na próxima.'
        self._execucoes += 1
        Tarefa.total_execucoes += 1
        self._ativa = False
        return f'[ALTERNADA] | {self._descricao} | Executada!'

class TarefaBloqueavel(Tarefa):

    total = 0

    def __init__(self, descricao: str):
        super().__init__(descricao)
        self._bloqueada = False
        TarefaBloqueavel.total += 1

    @property
    def tipo(self):
        return 'Bloqueavel'

    def bloquear(self):
        self._bloqueada = True

    def desbloquear(self):
        self._bloqueada = False

    def executar(self):

        if self._bloqueada:
            return 'Tarefa bloqueada!'
        self._execucoes += 1
        Tarefa.total_execucoes += 1
        return (f'[BLOQUEAVEL] | 'f'{self._descricao} | 'f'(Execuções: {self._execucoes})')

class Interface:

    gerenciador = GerenciadorTarefas()

    @staticmethod
    def executar_programa():

        while True:

            print("\n==== SISTEMA DE TAREFAS ====")
            print("1 - Criar tarefa")
            print("2 - Listar tarefas")
            print("3 - Remover tarefa")
            print("4 - Executar tarefas")
            print("5 - Bloquear/desbloquear tarefa")
            print("0 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == '0':
                print("Encerrando...")
                break

            elif opcao == '1':
                Interface.criar_tarefa()

            elif opcao == '2':
                Interface.listar_tarefa()

            elif opcao == '3':
                Interface.remover_tarefa()

            elif opcao == '4':
                Interface.executar_tarefa()

            elif opcao == '5':
                Interface.bloq_desbloq_tarefa()

            else:
                print("Opção inválida!")

    @staticmethod
    def criar_tarefa():

        print("\nTipo de tarefa:")
        print("1 - Comum")
        print("2 - Limitada")
        print("3 - Alternada")
        print("4 - Bloqueavel")

        tipo = input("Opção: ")
        descricao = input("Descrição: ")

        try:
            if tipo == '1':
                tarefa = TarefaComum(descricao)

            elif tipo == '2':
                limite = int(input("Limite de execuções: "))
                if limite <= 0:
                    print("O limite deve ser maior que zero.")
                    return
                tarefa = TarefaLimitada(descricao,limite)
            elif tipo == '3':
                ativa = input("Ativa inicialmente? [S/N]: ")
                tarefa = TarefaAlternada(descricao,ativa)
            elif tipo == '4':
                tarefa = TarefaBloqueavel(descricao)
            else:
                print("Tipo inválido!")
                return
            Interface.gerenciador.adicionar(tarefa)
            print("Tarefa criada com sucesso!")
        except ValueError:
            print("Valor inválido!")

    @staticmethod
    def listar_tarefa():

        tarefas = Interface.gerenciador.listar()

        print("\n==== LISTA DE TAREFAS ====")

        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
            return

        for i, tarefa in enumerate(tarefas):
            print(f'[{i}] {tarefa}')

        print(f'\nTotal atual: {len(tarefas)}')

        print(f'Comum: {TarefaComum.total} | 'f'Limitada: {TarefaLimitada.total} | 'f'Alternada: {TarefaAlternada.total} | 'f'Bloqueavel: {TarefaBloqueavel.total}')

        print(f'Total de execuções: 'f'{Tarefa.total_execucoes}')

    @staticmethod
    def remover_tarefa():

        try:

            indice = int(input("Digite o índice da tarefa: "))

            if Interface.gerenciador.remover( indice):
                print("Tarefa removida com sucesso!")
            else:
                print("Índice inválido!")

        except ValueError:
            print("Digite um número válido!")

    @staticmethod
    def executar_tarefa():

        tarefas = Interface.gerenciador.listar()

        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
            return

        print("\n==== EXECUTANDO TAREFAS ====")

        for tarefa in tarefas:
            print(tarefa.executar())

    @staticmethod
    def bloq_desbloq_tarefa():

        try:
            indice = int(input('Digite o índice da tarefa: '))

        except ValueError:
            print("Digite um número válido!")
            return

        tarefa = Interface.gerenciador.obter(indice)

        if tarefa is None:
            print("Índice inválido!")
            return

        if not isinstance(
            tarefa,
            TarefaBloqueavel):
            print("Essa tarefa não é bloqueável!")
            return

        op = input("Bloquear tarefa? [S/N]: ")

        if op.lower() == 's':

            tarefa.bloquear()
            print("Tarefa bloqueada!")

        else:
            tarefa.desbloquear()
            print("Tarefa desbloqueada!")


# INÍCIO DO PROGRAMA
Interface.executar_programa()
