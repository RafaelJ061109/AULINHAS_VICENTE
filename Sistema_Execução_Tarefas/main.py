#GRUPO: Rafael Joaquim, Kleiwan e Layse.

from class_ import Tarefa, tarefas, Tarefa_Alternada, Tarefa_limitada
#CLASSES IMPORTADAS DE class_.py

while True:
    print("\n==== SISTEMA DE TAREFAS ====")
    print("1 - Criar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("4 - Executar tarefa")
    print("0 - Sair")
#MENU
    opcao = input("Escolha uma opção: ")
#OPÇÃO DE ESCOLHA DO MENU

    if opcao == '0':
        print("Compreensivel, tenha uma otima vida.")
        break
    #FECHAMENTO DO PROGRAMA

    elif opcao == '1':
        print("Tipo de tarefa:")
        print("1 - Comum")
        print("2 - Limitada")
        print("3 - Alternada")
    #MENU DE TAREFAS

        tipo_op = input("Opção: ")
        #ESCOLHA DO TIPO

        nome = input("Nome: ")
        descricao = input("Descrição: ")
        #FIXO POR ESTAR EM TODAS

        if tipo_op == '1':
            exe = input("Execução: ")
            tarefa = Tarefa("comum", nome, descricao, exe)
        #TIPO COMUM

        elif tipo_op == '2':
            limite = int(input("Limite de execuções: "))
            exe = input('Execução: ')
            tarefa = Tarefa_limitada("limitada", nome, descricao, limite, exe)
        #TIPO LIMITADO

        elif tipo_op == '3':
            ativa = input("Ativa? [S/N]: ")
            exe = input('Execução: ')
            tarefa = Tarefa_Alternada("alternada", nome, descricao, ativa, exe)
        #TIPO ALTERNADO

        else:
            print("Opção inválida!")
            continue
        #SE NENHUM INPUT FOR EXECUTADO IGUAIS AS OPÇÕES O CODIGO MOSTRARÁ O PRINT

        tarefa.add_tarefa()
        print("Tarefa criada!")
        #FIXO, APÓS TODOS OS DADOS FOREM DADOS TODOS OS TIPOS VÃO PRA LISTAPRESENTE EM class_.py

    elif opcao == '2':
        print("Lista de tarefas:")
        for tarefa in tarefas:
            print(tarefa)
    #LISTA TODAS AS TAREFAS

    elif opcao == '3':
        id_tarefa = int(input("ID da tarefa: "))
        Tarefa.remover_por_id(id_tarefa)
    #REMOVE PELO INDICE/ID DA TAREFA

    elif opcao == '4':
        id_tarefa = int(input("ID da tarefa: "))

        for tarefa in tarefas:
            if tarefa.id == id_tarefa:
                tarefa.executar()
                break
        else:
            print("Tarefa não encontrada")
    #EXECUTA AS TAREFAS POR ID

    else:
        print("Opção inválida!")
