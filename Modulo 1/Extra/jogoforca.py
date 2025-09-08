import random
lista_palavras = ["banana","fruta","pera"]



palavra = random.choice(lista_palavras)

while True:
    usuario = input("Digite a letra da palavra: ")
    letras = list(set(palavra))
    p_exibida = len(palavra) * "_"
    print(p_exibida)
    if usuario == palavra:
        print("Parabens!!!!")
        break
    elif usuario in palavra:
        print("Letra que o usuário chutou existe na palavra")
    else:
        print("Ele errou a letra, não existe na palavra.")