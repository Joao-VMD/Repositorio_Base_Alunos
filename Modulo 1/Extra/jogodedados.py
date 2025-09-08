import random
dados_jogados = []
def dados_1():
    escolha = input("Escolha o tipo de dado:\n1- D6\n2- D8\n3- D12\n4- D20\n:")
    quantidade = int(input("Digite a quantidade de dados:"))
    for _ in range(0,quantidade):
        if escolha == "1":
            dado = 6
        elif escolha == "2":
            dado = 8
        elif escolha == "3":
            dado = 12
        elif escolha == "4":
            dado = 20
        else:
            dado = 0
        print(random.randint(1,dado))
dados_1()


    


