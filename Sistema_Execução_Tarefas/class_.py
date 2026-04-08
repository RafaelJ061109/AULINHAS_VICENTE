tarefas = []

class Tarefa:
    def __init__(self, tipo, nome, descricao):
        self.tipo = tipo
        self.nome = nome
        self.descricao = descricao

    def add_tarefa(self):
        contador_comum = 0
        if not tarefa_creatore in tarefas:
            contador_comum =+ 1
            tarefas.append(tarefa_creatore) 

    def rmv_tarefa(self):
        if tarefa_creatore in tarefas:
            tarefas.remove(tarefa_creatore)
        
    def __str__(self):
        return f'Tarefa: {self.tipo}, nome: {self.nome} Descrição: {self.descricao}'

class Tarefa_limitada(Tarefa):
    def __init__(self, nome, tipo, descricao, limite):
        super().__init__(add_tarefa, rmv_tarefa)
        self.limite = limite
        
        def limite(self, limite):
            self.limite += 0

class Tarefa_Alternada(Tarefa):
    def __init__(self, nome, tipo, descricao, ativa):
        super.__init__(add_tarefa, rmv_tarefa)
        self.ativa = True





