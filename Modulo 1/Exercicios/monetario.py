cotaçãoDolar = float(input("digite o valor do dolar atualmente:"))

def dolarReal(dolar):
    return dolar * cotaçãoDolar
def realDolar(real):
    return  real / cotaçãoDolar
opção = input("converter dolar ou real:\n1- real\n2-dolar\n3- sair \n DIGITE: ")
try:
    if opção == "1":
        real = float(input("Digite o valor em real: "))
        print(f"A conversão do real para dolar é: ${realDolar(real)}")

    elif opção == "2":
        dolar = float(input("Digite o valor em dolar: "))
        print(f"A converção do dolar para o real é: R${dolarReal(dolar)}")

    elif opção == "3":
        print("Saindooo")
except ValueError:
   print("Digite um número")
except ZeroDivisionError:
   print("Impossivel dividir por zero")
except Exception as e:
   print(e)

    



