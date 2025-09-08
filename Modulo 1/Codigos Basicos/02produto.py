try:
    nome_produto = input("digite o nome do produto: ")
    preço  = float(input("digite o preço do produto: "))
    desconto = float(input("digite o percentual de desconto: "))

    valor_desconto = preço * desconto / 100
    preço_final = preço - valor_desconto

    print(f"produto: {nome_produto} - preço final: R$ {preço_final}")
except ValueError:
    print("Digite numeros")
except ZeroDivisionError:
    print("Impossivel dividir por zero")
except Exception as e:
    print(e)