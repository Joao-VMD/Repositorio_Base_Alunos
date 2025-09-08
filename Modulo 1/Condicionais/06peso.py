try:
    nome = input("Digite seu nome: ")
    peso = float(input("digite seu peso: "))
    altura = float(input("digite sua altura: "))
    imc = peso / altura **2

    print(f"{nome} {imc}")

    if imc >= 40.0:
        situaçao = "obesidade grau3"
        print("obesidade grau3")
    elif imc >= 39.9:
        situaçao = "obesidade grau2"
        print("obesidade grau2")
    elif imc >= 34.9:
        situaçao = "obesidade grau1"
        print("obesidade grau1")
    elif imc >= 29.9:
        situaçao = "sobrepeso"
        print("sobrepeso")
    elif imc >= 24.9:
        situaçao = "peso normal"
        print("peso normal")
    elif imc >= 18.5:
        situaçao = "abaixo do peso"
        print("abaixo do peso")
    else:
        situaçao = "muito magro"
        print("muito magro")
except ValueError:
    print("Digite números")
except ZeroDivisionError:
    print("Impossivel dividir por zero")
except Exception as e:
    print(e)

with open("imc.txt","a") as arquivo:
    arquivo.write(f"{nome}  |  {situaçao}  \n")