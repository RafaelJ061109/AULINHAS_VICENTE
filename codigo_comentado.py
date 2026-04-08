estoque = []

#CLASSES
class Produto: #O nome da classe deve ter a inicial maiúscula
    def __init__(self, nome, quantidade, preco): #função inicial, serve para quando alguém quiser criar um objeto que pertence a classe. Os valores dos atributos (atributos parecem as chaves dos dicionários) do objeto serão os parâmetros dessa função, além do self. Inclusive, para criar um objeto que pertança a classe, a sintaxe é Classe(argumentos [obs: os que foram listados como parâmetros na função inicial])
        self.nome = nome #Nesse caso, cada objeto que pertence a classe Produto possui obrigatoriamente nome, quantidade e preço. Essa linha em específico serve para indicar que a chave nome é igual ao primeiro argumento usado ao criar um objeto da classe Produto 
        self.quantidade = quantidade
        self.preco = preco

    ##FUNÇÕES DENTRO DA CLASSE            
    def adicionar_qt(self, quantidade):
        self.quantidade += quantidade #self se refere ao próprio objeto

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
    produto = Produto(nome, quantidade, preco) #Aqui está criando um objeto da classe produto em que os argumentos são as variávies acima. 

    estoque.append(produto) #Aqui o produto criado é enviado ao estoque (lista)
    
##FUNÇÕES PARA BUSCA E LISTAGEM    
def listar(estoque): #é uma boa prática passar o estoque como parâmetro para evitar dependência de variáveis globais. Aí o argumento vai ser o nome da variável global (estoque)
    if not estoque: #lista vazia = False
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
    return None #None é opcional

##ADICIONAR QT
def adc():
    nome = input('Informe o nome do produto: ')
    produto = encontrar_produto(nome, estoque)
    if produto: #Se o produto for encontrado
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
    
"""------PILARES DA POO------

==ABSTRAÇÃO== 

É o processo de representar um objeto real de forma simplificada no código, mostrando apenas o que é relevante.
EXEMPLO:

class Produto:
    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

Aqui você abstraiu um produto de um estoque: o que importa são nome, quantidade e preço, sem precisar se preocupar com embalagem, fornecedor, etc.

==ENCAPSULAMENTO==

Colocar _ antes de um atributo ou um método para indicar que ele só deve ser acessado dentro da classe
Colocar __ é como o _ só que obrigatório. Internamente, o Python muda o nome para _Produto__nome

Como saber se devo usar um método ou uma função normal?
Use um método quando a função precisar manipular ou acessar os dados do próprio objeto.
"""