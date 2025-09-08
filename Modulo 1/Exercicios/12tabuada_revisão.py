# numeros_usuario = int(input("Digite o numero para mostrar a tabuada: "))
# for i in range(1,11):
    # multi = i * numeros_usuario 
    # print(f"A tabuada do {numeros_usuario} = {multi} ")





# def tabuada():
#     usuario = int(input("Digite o numero: "))
#     for i in range(1,11):
#         result = i * usuario
#         print(f"Tabuada {usuario} * {i} = {result}")
       

# print(tabuada())






def tabuada():
    numero = int(input("Digite o numero: "))
    i = 1
    while i <= 10:
        result = i * numero
        print(f"tabuada {numero} * {i} = {result}")
        i = i + 1

print(tabuada())