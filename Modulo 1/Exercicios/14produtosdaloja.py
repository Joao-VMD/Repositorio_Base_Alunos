nome = input("Digite o nome do produto: ")
Valor = float(input("Digite o valor: "))
quantidade = int(input("Digite a quantidade: "))

with open("lojinha.txt", "a", encoding= "utf-8") as arquivo:
    arquivo.write(f"{nome} | R$:{Valor} | {quantidade} \n")
    
