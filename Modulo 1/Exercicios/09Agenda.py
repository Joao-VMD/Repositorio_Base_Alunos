Agenda = []
while True:
    opçao = input("Liata de contatos: \n 1- Cadastrar pessoa: \n 2- listar pessoas \n 3- Excluir pessoa \n 0- sair\n Digite: ")
    
    if opçao == "1":
        nome = input("Digete o nome da pessoa: ")
        Agenda.append (nome)
    elif opçao == "2":
        print(f"Lista de contatos: {Agenda}")
    elif opçao == "3":
        excluir = input("Digite o nome no qual quer excluir:")
        print(f"Deletar da Agenda: {Agenda}")
        selecionar = input("certeza que deseja deletar:\n1-confirmar\n2-cancelar\n:")
        if selecionar == "1":
            Agenda.remove(excluir)
            print(f"excluido: {Agenda}")
        elif selecionar == "2":
            print("Cancelamento feito")
    elif opçao == "0":
        print("Fechando")
        break
    else:
        print("Error")




