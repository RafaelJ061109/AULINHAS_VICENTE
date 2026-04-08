from classe import Produto, adicionar_prod, listar, adc, rmv
  
#MENU
while True:
    print(f'1 - Adicionar produto\n2 - Adicionar quantidade a produto\n3 - Remover quantidade de produto\n4 - Listar estoque\n0 - Sair')
    op = input('Escolha uma opção: ')

    if op == "0":
        break
    elif op == '1':
        while True:
            nome = input('Escreva o nome do produto: ')
            if nome == '':
                print('Nome vazio.')
                continue
            if not nome.isalpha():
                print('Invalido')
                continue
            try:
                quantidade = int(input('Insira a quantidade do produto: '))
                if quantidade < 0:
                    continue
            except ValueError:
                print('Digite um numero válido')
                continue
            try:
                preco = float(input('Insira o preço do produto: '))
                if preco < 0.0:
                    continue
            except ValueError:
                print('Digite um numero valido')
                continue
            produto = Produto(nome, quantidade, preco)
            adicionar_prod(produto)
            break
    elif op == '2':
        adc()
    elif op == '3':
        rmv()
    elif op == '4':
        listar()
    else:
        print('Erro! Tente novamente')