Pares = []
impares = []


for i in range(1,11):
    numero = int(input(f"Digite o numero {i}:  "))

    if numero % 2 == 0:
        print("par")
        Pares.append(numero)
    else:
        print("impar")
        impares.append(numero)


opçao = input("Digite  \n1- lista par \n2- lista impar  \n3- as duas listas\n: ")

if opçao == "1":
    print(f"lista dos numeros pares:  {Pares}")
elif opçao == "2":
    print(f"lista dos numeros impares:  {impares}")
elif opçao == "3":
    print(f"lista par: {Pares} \nlista impar: {impares}")
else:
    print("Error")
