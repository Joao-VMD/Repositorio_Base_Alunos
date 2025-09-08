import requests

def ping():
    response = requests.get("https://restful-booker.herokuapp.com/ping")
    return response.status_code  


def autenticacao():
    corpo = {
        "username":"admin",
        "password":"password123"
    }

    response = requests.post("https://restful-booker.herokuapp.com/auth", json=corpo)
    return response.json()["token"]


def criar_booking(nome="Fulano",sobrenome="Ciclano",valor=0,
            pago = False, checkin = "2025-08-20", checkout="2025-08-20",
            adicionais="Café da Manhã"):
    corpo = {
            "firstname" : nome,
            "lastname" : sobrenome,
            "totalprice" : valor,
            "depositpaid" : pago,
            "bookingdates" : {
            "checkin" : checkin,
            "checkout" : checkout
            },
            "additionalneeds" : adicionais
            }
    response = requests.post("https://restful-booker.herokuapp.com/booking", json=corpo)
    return response.json()["bookingid"]


def busca_booking(bookingId):
    response = requests.get(f"https://restful-booker.herokuapp.com/booking/{bookingId}")
    return response.json()
# bookingId = criar_booking(nome="Miguel",sobrenome="Oliveira", valor="9000",
#                            pago=False,checkin="2025-08-21",checkout="2025-08-25")

def atualiza_booking(bookingId,nome,sobrenome,valor=45,
            pago = True, checkin = "2025-08-20", checkout="2025-08-20",
            adicionais="Late checkout"):
     cabecalho = {
        "cookie" :f"token={autenticacao()}"
        }
     corpo = {
            "firstname" : nome,
            "lastname" : sobrenome,
            "totalprice" : valor,
            "depositpaid" : pago,
            "bookingdates" : {
            "checkin" : checkin,
            "checkout" : checkout
            },
            "additionalneeds" : adicionais 
            }
     response = requests.put(f"https://restful-booker.herokuapp.com/booking/{bookingId}", json=corpo, headers=cabecalho)
     print(response.text)
     return response.json()
     
print(atualiza_booking)


# id_booking = criar_booking(nome="joao",sobrenome="suarez",valor=1200)
# busca_booking(id_booking)
# atualiza_booking(bookingId=id_booking,nome="joao",sobrenome="atualizado")

def atualiza_parcialmente_booking(bookingId, **kwargs):
    cabecalho= {"cookie" :f"token={autenticacao()}"}
    corpo= kwargs

    response =requests.patch(f"https://restful-booker.herokuapp.com/booking/{bookingId}",json=corpo, headers=cabecalho)
    print(response.text)
    print(response.status_code)


# atualiza_parcialmente_booking(5,firstname="nome",lastname="nome")


def delete_booking(bookingId):
    cabecalho= {"cookie" :f"token={autenticacao()}"}

    response =requests.delete(f"https://restful-booker.herokuapp.com/booking/{bookingId}", headers=cabecalho)
    if response.status_code == 201:
        print("Deletado.")
    print(response.text)
    print(response.status_code)

# AREA DE TESTES#
print("-" * 35)
print("ATIVIDADE-1 \n Health Check")
print(ping())
print("-" * 35)

print("-" * 35)
print("ATIVIDADE-2  \n Criar Token de Autenticação ")
print(autenticacao())
print("-" * 35)


print("-" * 35)
print("ATIVIDADE-3 \n Create / POST")
bookingId = criar_booking(nome="jorgenio", sobrenome="giz",valor=123)
print(bookingId)
print("-" * 35)

print("-" * 35)
print("ATIVIDADE-4 \n Read / GET")
print(busca_booking(bookingId))
print("-" * 35)

print("-" * 35)
print("ATIVIDADE-5 \n Update / PUT")
print(atualiza_booking(bookingId,nome="letta",sobrenome="lucelia"))
print("-" * 35)


print("-" * 35)
print("ATIVIDADE-6 \n  Update / PATCH")
print(atualiza_parcialmente_booking(bookingId,firstname="ernesto",lastname="delacruz"))
print("-" * 35)

print("-" * 35)
print("ATIVIDADE-7 \n  Delete / DELETE")
print(delete_booking(bookingId))
print("-" * 35)




    