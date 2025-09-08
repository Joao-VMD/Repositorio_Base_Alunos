try:
    temperatura = float(input("digite a temperatura em cels: "))

    if temperatura >= 30:
        print("Está quente!")
    elif temperatura >= 20:
        print("Está agradavel.")
    elif temperatura >= 10:
        print("Está frio!")
    else:
        print("Está muito frio!")
except Exception as e:
    print(e)