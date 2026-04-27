#FICA COMO ESTUDO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

tarefas = []

class Tarefa:
    contador = 1

    def __init__(self, tipo, nome, descricao, exe):
        self.id = Tarefa.contador
        Tarefa.contador += 1
        self.tipo = tipo
        self.nome = nome
        self.descricao = descricao
        self.exe = exe

    def add_tarefa(self):
        tarefas.append(self)

    def remover_por_id(id_tarefa):
        for tarefa in tarefas:
            if tarefa.id == id_tarefa:
                tarefas.remove(tarefa)
                print("Tarefa removida com sucesso!")
                return
        print("Tarefa não encontrada.")

    def executar(self):
        print(f"[Tarefa {self.id}] {self.exe}")

    def __str__(self):
        return f'ID: [{self.id}] | Tipo: {self.tipo} | Nome: {self.nome} | Descrição: {self.descricao}'


class Tarefa_limitada(Tarefa):
    def __init__(self, tipo, nome, descricao, limite, exe):
        super().__init__(tipo, nome, descricao, exe)
        self.limite = limite
        self.execucoes = 0

    def executar(self):
        if self.execucoes < self.limite:
            self.execucoes += 1
            print(f"[Tarefa {self.id}] {self.exe} ({self.execucoes}/{self.limite})")
        else:
            print("Limite ultrapassado.")

    def __str__(self):
        return f'ID: [{self.id}] | Tipo: {self.tipo} | Nome: {self.nome} | Limite: {self.limite}'


class Tarefa_Alternada(Tarefa):
    def __init__(self, tipo, nome, descricao, ativa, exe):
        super().__init__(tipo, nome, descricao, exe)
        self.ativa = True if ativa.lower() == 's' else False

    def executar(self):
        estado = "ATIVA" if self.ativa else "INATIVA"
        print(f"[Tarefa {self.id}] {self.exe} ({estado})")

    def __str__(self):
        return f'ID: [{self.id}] | Tipo: {self.tipo} | Nome: {self.nome} | Ativa: {self.ativa}'
