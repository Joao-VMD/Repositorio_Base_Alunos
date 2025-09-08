numero = int(input("Digite o numero: "))

for i in range(1,numero + 1):
    if i % 2 == 0:# % = resto de divisão
        print(f"Pares = {i}")
    else:
        print(f"impares = {i}")