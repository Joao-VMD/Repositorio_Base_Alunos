nome = []
rg = []
idade = []

while True:
    opçao = input("Bem vindo a area de cadastro! \n1- cadastrar\n2- ver cadastros anteriores\n3- excluir cadastro\n4- sair\nDigite: ")
    if opçao == "1":
        nom = input("Digite seu nome: ")
        r = int(input("Numero do seu RG: "))
        idad = int(input("Digite sua idade: "))
        nome.append(nom)
        rg.append(r)
        idade.append(idad)
    elif opçao == "2":
        print(f"Cadastros anteriores: \nnome: {nome}\nRG: {rg}\nIdade: {idade}")
    elif opçao == "3":
        excluir_n = input("Digite o nome no qual quer excluir:")
        excluir_r = int(input("Digite o rg no qual quer excluir:"))
        excluir_i = int(input("Digite a idade no qual quer excluir:"))
        print(f"Deletar da Agenda: {nome} {rg} {idade}")
        selecionar = input("certeza que deseja deletar:\n1-confirmar\n2-cancelar\n:")
        if selecionar == "1":
            nome.remove(excluir_n)
            rg.remove(excluir_r)
            idade.remove(excluir_i)
            print(f"excluido: {nome} {rg} {idade}")
        elif selecionar == "2":
            print("Cancelamento feito")
    elif opçao == "4":
        print("finalizando")
        break
    else:
        print("error")
