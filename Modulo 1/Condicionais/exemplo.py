palavra = "banana"

letras_na_palavra = list(set(palavra))

palavra_exibida = len(palavra) * "_"

while True:
    letra_usuario = input("Digite a letra que deseja: ")
    print(palavra_exibida)
    if letra_usuario in letras_na_palavra:
        print("Letra que o usuário chutou existe na palavra")
    elif letra_usuario == letras_na_palavra:
        print("usuario Venceu parabens!!!")
        break
    else:
        print("Ele errou a letra, não existe na palavra.")