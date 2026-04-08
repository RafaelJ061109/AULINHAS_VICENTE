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

##FUNÇÕES PARA ATUALIZAR ESTOQUE
def adicionar_prod(produto):
    estoque.append(produto)
    print(f'Nome: {produto.nome}, Quantidade: {produto.quantidade}, Preço: {produto.preco}')
    
##FUNÇÕES PARA BUSCA E LISTAGEM    
def listar():
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