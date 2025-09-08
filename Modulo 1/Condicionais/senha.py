i = 1
senha_correta = "abacate"
while i <= 10 :
    senha = (input("digite sua senha:   caso tenha esqueçido digite sim \n "))
    i = i + 1
    if senha == senha_correta:
        print("senha correta Bem vindo usuario ")
        break
    elif senha == "sim":
        print("esqueçeu a senha escolha uma nova: ")
        nova_senha = (input("digite sua senha nova: "))
        senha_correta = nova_senha
    else:
        print("incorreta Tentar de novo!")