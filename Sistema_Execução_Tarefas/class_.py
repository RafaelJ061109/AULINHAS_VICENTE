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

    def rmv_tarefa(self):
        if self in tarefas:
            tarefas.remove(self)

    def __str__(self):
        return f'ID: [{self.id}], Tarefa: {self.tipo}, nome: {self.nome} Descrição: {self.descricao}'

class Tarefa_limitada(Tarefa):
    def __init__(self, nome, tipo, descricao, limite):
        super().__init__(nome, tipo, descricao)
        self.limite = limite
        
        def limite(self):
            self.limite += 0

class Tarefa_Alternada(Tarefa):
    def __init__(self, nome, tipo, descricao, ativa):
        super().__init__(nome, tipo, descricao)
        self.ativa = True


