nome = input("qual é o seu nome? ")
idade = int(input("qual sua idade? "))
possui_carteira = input("possui carteira de motorista? ? \n (1-sim / 2-não) ")

if idade >= 18: 
    if possui_carteira == "1":
        print("pode dirigir")
    else:
        print("não pode dirigir")    
else:
    print("menor de idade")
