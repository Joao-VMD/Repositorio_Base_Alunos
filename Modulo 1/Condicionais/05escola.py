try:
    aluno = input("digite o nome do aluno: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    Media = (nota1 + nota2 + nota3) /3      

    print(f"A media final do {aluno} é: {Media}")

    if Media >= 7:
        situaçao = "aprovado"
        print(situaçao)

    elif Media >= 4:
        situaçao = "recuperação"
        print(situaçao)

    else:
        situaçao = "reprovado" 
        print(situaçao)

except ValueError:
    print("Digite números")
except Exception as e:
    print(e)



with open("escola.txt","a") as arquivo:
    arquivo.write(aluno + "|" + "nota:" + str(Media) + "|" + situaçao  + "\n")