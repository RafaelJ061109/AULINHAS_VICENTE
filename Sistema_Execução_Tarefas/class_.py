tarefas = []

class Tarefa:
    contador = 1

    def __init__(self, tipo, nome, descricao):
        self.id = Tarefa.contador
        Tarefa.contador += 1 
        self.tipo = tipo
        self.nome = nome
        self.descricao = descricao

    def add_tarefa(self):
        if not self in tarefas:
            tarefas.append(self) 
        else:
            print('Tarefa já existente')

    def remover_por_id(id_tarefa):
        for tarefa in tarefas:
            if tarefa.id == id_tarefa:
                tarefas.remove(tarefa)
                print("Tarefa removida com sucesso!")
                return
        print("Tarefa não encontrada.")

    def __str__(self):
        return f'ID: [{self.id}], Tarefa: {self.tipo}, nome: {self.nome} Descrição: {self.descricao}'

class Tarefa_limitada(Tarefa):
    def __init__(self, nome, tipo, descricao, limite):
        super().__init__(nome, tipo, descricao)
        self.limite = limite
        
        def limite(self):
            if self.limite >= limite:
                print('Tarefa não pode ser mais executada.') 

        def __str__(self):
            return f'ID: [{self.id}], Tarefa: {self.tipo}, nome: {self.nome} Descrição: {self.descricao}, Limite: {self.limite}'

class Tarefa_Alternada(Tarefa):
    def __init__(self, nome, tipo, descricao, ativa):
        super().__init__(nome, tipo, descricao)
        self.ativa = True

    def __str__(self):
        return f'ID: [{self.id}], Tarefa: {self.tipo}, nome: {self.nome} Descrição: {self.descricao}, Ativa: {self.ativa}'


    def __init__(self, nome, tipo, descricao, ativa):
        super().__init__(nome, tipo, descricao)
        self.ativa = True


