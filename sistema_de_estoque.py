estoque = []

#CLASSES
class Produto:
    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    ##FUNÇÕES DENTRO DA CLASSE            
    def adicionar_qt(self, quantidade):
        self.quantidade += quantidade

    def remover_qt(self, quantidade):
        if quantidade <= self.quantidade:
            self.quantidade -= quantidade
        else:
            print('Quantidade insuficiente!')

#FUNÇÕES FORA DA CLASSE

##FUNÇÕES PARA ATUALIZAR ESTOQUE
def adicionar_prod(estoque):
    nome = input('Escreva o nome do produto: ')
    quantidade = int(input('Insira a quantidade do produto: '))
    preco = float(input('Insira o preço do produto: '))
    produto = Produto(nome, quantidade, preco)

    estoque.append(produto)
    
##FUNÇÕES PARA BUSCA E LISTAGEM    
def listar(estoque):
    if not estoque:
        print('Estoque vazio!')
    else:
        for produto in estoque:
            print(f'Nome: {produto.nome}, Quantidade: {produto.quantidade}, Preço: {produto.preco}')
            
##FUNÇÕES PARA MANIPULAÇÕES DE QUANTIDADE

##ADICIONAR NA LISTA
def encontrar_produto(nome, estoque):
    for produto in estoque:
        if produto.nome == nome:
            return produto
    return None

##ADICIONAR QT
def adc():
    nome = input('Informe o nome do produto: ')
    produto = encontrar_produto(nome, estoque)
    if produto:
        qt = int(input('quantidade a adicionar: '))
        produto.adicionar_qt(qt)
    else:
        print('produto não encontrado')

##REMOVER QT
def rmv():
    nome = input('Informe o nome do produto: ')
    produto = encontrar_produto(nome, estoque)
    if produto:
        qt = int(input('quantidade a remover: '))
        produto.remover_qt(qt)
    else:
        print('produto não encontrado')
        
#MENU
while True:
    print(f'1 - Adicionar produto\n2 - Adicionar quantidade a produto\n3 - Remover quantidade de produto\n4 - Listar estoque\n0 - Sair')
    op = input('Escolha uma opção: ')

    if op == "0":
        break
    elif op == '1':
        adicionar_prod(estoque)
    elif op == '2':
        adc()
    elif op == '3':
        rmv()
    elif op == '4':
        listar(estoque)
    else:
        print('Erro! Tente novamente')