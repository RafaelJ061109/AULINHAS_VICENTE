from class_ import Tarefa, tarefas, Tarefa_Alternada, Tarefa_limitada
#Sistema de Execução de Tarefas

#Menu
while True:
    print(" ==== SISTEMA DE TAREFAS ==== ") 
    print("1 - Criar tarefa") 
    print("2 - Listar tarefas") 
    print("3 - Remover tarefa") 
    print("0 - Sair") 
    
    opcao = input("Escolha uma opção: ")
##Opções do Menu
    if opcao == '0':
        print("Compreensível, Tenha uma ótima vida")
        break
    elif opcao == '1':
        print("Tipo de tarefa:")
        print("1 - Comum")  
        print("2 - Limitada")  
        print("3 - Alternada")
        tarefa_creatore = input("Opção: ")
        if tarefa_creatore == '1':
            tipo = 'Comum'
            nome = input('Digite o nome da sua tarefa: ')
            comum = input('Digite a descrição da sua tarefa: ').strip()
            tarefa = Tarefa(tipo, nome, comum)
            tarefa.add_tarefa()
        
    elif opcao == '2':
        print("Aqui estão suas tarefas:")
        for tarefa in tarefas:
                print(tarefa)
