saldo = 1000
contas = []
def segurança():
    log = input("Ola seja bem vindo ao Banco py!\n1)logar\n2)criar conta\n3)esqueçeu a senha\n:")
    if log =="1":
        nome = input("Digite seu nome ou seu cpf: ")
        senha = int(input("Digite sua senha para logar: "))
    elif log == "2": 
        nome = input("Digite seu nome ou seu cpf: ")
        senha = int(input("Crie uma senha para logar: "))
        contas.append(segurança())
    elif log == "3":
        nome = input("Digite seu nome ou seu cpf: ")
        senha_1 = int(input("Digite sua nova senha para logar: "))
        senha = senha_1
        contas.append(segurança())
    else:
        "Error"


def menu():
    segurança()
    while True:
        caixa = input("Caixa Eletronico\n1)Saque\n2)Deposito\n3)Visualizar\n:")
        if caixa == "1":
            valor_saque = int(input("Digite o valor que deseja sacar: "))
            if valor_saque <= saldo:
                valor_final = saldo - valor_saque
            else:
                print("impossivel sacar um valor maior que seu saldo")        
        elif caixa == "2":
            valor_do_deposito = int(input("Digite o valor que quer depositar: "))
            valor_final = valor_do_deposito + valor_final
        elif caixa == "3":
            print(f"Seu saldo é de: {valor_final}")
        elif caixa == "0":
            print("Saindo!!")
            break
        else:
            "error"

menu()