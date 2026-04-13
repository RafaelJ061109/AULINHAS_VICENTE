mensagens = []

class Mensagem:
    def __init__(self, conteudo):
        self.conteudo = conteudo
        self.status = 'disponivel'

    def visualizar(self, chave=None):
        return f'Conteudo: {self.conteudo}'
    
    def getStatus(self):
        return self.status
    
    def getType(self):
        return "Comum"

class Mensagem_protegida(Mensagem):
    def __init__(self, conteudo, chave):
        super().__init__(conteudo) 
        self.chave = chave

    def visualizar(self, chave):
        if chave == self.chave:
            return f'Conteudo : {self.conteudo}'
        return 'chave incorreta!'
    
    def getType(self):
        return "Protegida"
    

class Mensagem_unica(Mensagem):

    def visualizar(self, chave=None):
        if self.status == 'indisponivel':
            return 'mensagem ja visualizada'
        
        self.status = 'indisponivel'
        return f"Conteúdo: {self.conteudo}"

    def getType(self):
        return "Única"
    

#FUNÇÕES AUXILIARES

def solicitar_conteudo():
    conteudo = input("Digite o conteúdo da mensagem: ")
    return conteudo

def solicitar_chave():
    chave = input("Digite a chave: ")
    return chave

#FUNÇÕES PRINCIPAIS

def criar_mensagem(mensagens):
    print("1. Mensagem Comum\n2. Mensagem Protegida\n Mensagem Única")
    tipo = int(input("Escolha o tipo da mensagem: "))
    
    mensagem = None
    conteudo = solicitar_conteudo()
    
    if tipo == 1:
        mensagem = Mensagem(conteudo)
    elif tipo == 2:
        chave = solicitar_chave()
        mensagem = Mensagem_protegida(conteudo, chave)
    elif tipo == 3:
        mensagem = Mensagem_unica(conteudo)
    else:
        print("Ocorreu um erro!")
        return
        
    mensagens.append(mensagem)
    print("Mensagem criada com sucesso!")
    return
        
def listar_mensagens(mensagens):
    index = 0

    if not mensagens:
        print("Nenhuma mensagem cadastrada!")
        return
    else:
        print("Mensagens cadastradas:")
        for mensagem in mensagens:
            print(f"{index} - [{mensagem.getType()}] {mensagem.getStatus()}")
            index += 1
        

while True:
    print("===== MURAL DE MENSAGENS =====\n")
    print("1 - Criar mensagem\n2 - Listar mensagens\n3 - Visualizar mensagem\n4 - Remover mensagem\n0 - Sair\n")
    opcaoEscolhida = int(input("Escolha uma opção: "))

    if opcaoEscolhida == 1:
        criar_mensagem(mensagens)

