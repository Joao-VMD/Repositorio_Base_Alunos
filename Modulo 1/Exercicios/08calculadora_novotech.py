def soma(n1,n2):
    return n1 + n2

def subtrair(n1,n2):
    return n1 - n2


def multiplique(n1,n2):
  return n1 * n2


def dividir(n1,n2):
   return n1 / n2
   

escolha = input("escolha o que a calculadora vai fazer: \n 1- soma \n 2- subtrair \n 3- multiplique \n 4- dividir \n 5- Sair \n Digite:  ")
try:
   if escolha == "1":
      n1 = float(input("digite o primeiro numero: "))
      n2 = float(input("digite o segundo numero: "))
      print(f"A soma dos numeros é: {soma(n1,n2)} ")
      
   elif escolha == "2":
      n1 = float(input("digite o primeiro numero: "))
      n2 = float(input("digite o segundo numero: "))
      print(f"A subtração dos numeros é: {subtrair(n1,n2)}")

   elif escolha == "3":
      n1 = float(input("digite o primeiro numero: "))
      n2 = float(input("digite o segundo numero: "))
      print(f"A multiplicação dos numeros é: {multiplique(n1,n2)}")

   elif escolha == "4":
      n1 = float(input("digite o primeiro numero: "))
      n2 = float(input("digite o segundo numero: "))
      print(f"A divisão dos numeros é: {dividir(n1,n2)}")

   elif escolha == "5":
      print("saindoooo") 

   else:
      print("ERROR")
except ValueError:
   print("Digite um número")
except ZeroDivisionError:
   print("Impossivel dividir por zero")
except Exception as e:
   print(e)