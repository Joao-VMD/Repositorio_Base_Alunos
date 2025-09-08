import random
def gerador_numero():
    dificuldade = input("Digite a dificuldade: \n1- normal\n2- medio\n3- dificil\ndigite:")
    if dificuldade == "1":
        valor_dificuldade = 10
    elif dificuldade == "2":
        valor_dificuldade = 50
    elif dificuldade == "3":
        valor_dificuldade = 100
    
    return random.randint(1,valor_dificuldade)

numero_secreto = gerador_numero()
vitoria = []

while True:
    numero_usuario = int(input("Qual é o numero: "))
    if numero_usuario == numero_secreto:
        print("Parabens você achou o numero!!!!! :)")
        vitoria.append(numero_secreto)
        
        continuar = input("1-continuar\n2-finalizar\nDigite:")
        if continuar == "1":
            numero_secreto = gerador_numero()
            numero_usuario = int(input("Qual é o numero:"))
            if numero_usuario == numero_secreto:
                print("Parbens!!!!!")
            elif numero_usuario > numero_secreto:
                print("Numero menor esta perto")
            else:
                print("Numero maior Esta perto")

        elif continuar == "2":
            print("Ate a proxima")
            break
    elif numero_usuario > numero_secreto:
        print("Numero menor Quase la")
    else:
        print("Numero maior Esta perto")


vitoria.append(numero_secreto)

opção = input("ver numeros usados ate agora: \n1- Mostrar\n2- finalizar\nDigite: ")
if opção == "1":
    print(f"lista de numeros usados: {vitoria}")
elif opção == "2":
    print("Finalizado")
else:
    print("Error")