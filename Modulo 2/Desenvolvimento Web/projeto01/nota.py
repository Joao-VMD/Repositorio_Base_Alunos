def situaçao(media):
    if media >= 7:
        situaçao = "aprovado"

    elif media >= 4:
        situaçao = "recuperação"

    else:
        situaçao = "reprovado" 
    return situaçao
def calcular_media(*notas):
    return sum(notas)/len(notas)

def sistema():
    menu = int(input("Digite o que deseja:\n 1-Nota padrão dos 4 bimestres:\n 2-Coloque as notas:\n"))
    notas = []
    if menu == 1:
        n1 = float(input("Nota 1:"))
        n2 = float(input("Nota 2:"))
        n3 = float(input("Nota 3:"))
        n4 = float(input("Nota 4:"))
        media = calcular_media(n1,n2,n3,n4)
        print(f"Media final = {media} {situaçao(media)}")
    elif menu == 2:
        quant_NOT = int(input("Quantas notas deseja adicionar: "))
        for i in range(quant_NOT):
            nota = float(input("Digite sua nota: "))
            notas.append(nota)
        media = calcular_media(*notas)
        print(f"Media final = {media} {situaçao(media)}")

if __name__ == "__main__":
     sistema()
        



        
