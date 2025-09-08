import turtle
t = turtle.Turtle()

t.shape("turtle")
# t.speed(1)

def mov_para_cima():
    y = t.ycor()
    t.sety(y + 10)
def mov_para_baixo():
    y = t.ycor()
    t.sety(y - 10)
def mover_direita():
    x = t.xcor()
    t.setx(x + 10)
def mover_esquerda():
    x = t.xcor()
    t.setx(x - 10)

def m_di():
    x = t.xcor()
    y = t.ycor()
    t.setposition((x + 10, y + 10))
def m_es():
    x = t.xcor()
    y = t.ycor()
    t.setposition((x - 10, y - 10))
def m_c():
    x = t.xcor()
    y = t.ycor()
    t.setposition((x + 10, y - 10))
def m_b():
    x = t.xcor()
    y = t.ycor()
    t.setposition((x - 10, y + 10))

 
def ativa_desativa_desenho():
    desenhando = t.pen()["pendown"]
    if desenhando == True:
        t.penup()
    elif desenhando == False:
        t.pendown()
        
def engrossar_linha():
    grossura_linha = t.pen()["pensize"]
    nova_grosura = t.pensize(grossura_linha + 1)
def linha_normal():
    grosura_linha = t.pen()["pensize"]
    grossura = t.pensize(grosura_linha - 1)

def borracha():
    cor_fundo = tela.bgcolor()
    cor_caneta = t.pen()["pencolor"]
    if cor_fundo != cor_caneta:
        cor_caneta = t.color("white")
        t.shape("square")
    else:
        t.color("black")
        
        
# def borracha():
#     t.color("white")
#     borrar = t.shape("square")
#     borrar = t.color()
def voltar():
    t.color("black")
    t.shape("turtle")
    
# def teste_x():
#     import random
#     tp = random.randint(1,1000)

#     t.teleport(tp)
# def teste_y():
#     t.clone()    
#     mick = turtle()
#     mick = t.clone()
#     joe = mick.clone()



# --- Tartaruga Seguidora --- #
seguidora = turtle.Turtle()
seguidora.shape("turtle")
seguidora.color("blue")
velocidade_seguidora = 5

def mover_seguidora():
    x_jogador = t.xcor()
    y_jogador = t.ycor()


    x_seguidora = seguidora.xcor()
    y_seguidora = seguidora.ycor()
    if abs(x_jogador - x_seguidora) > velocidade_seguidora:
        if x_jogador > x_seguidora:
            x_seguidora += velocidade_seguidora
        else:
            x_seguidora -=  velocidade_seguidora
    else:
        x_seguidora = x_jogador

    if abs(y_jogador - y_seguidora) > velocidade_seguidora:

        if y_jogador > y_seguidora:
            y_seguidora += velocidade_seguidora
        else:
            y_seguidora -= velocidade_seguidora
    else:
        y_seguidora = y_jogador

    seguidora.setposition(x_seguidora, y_seguidora)
    #Colisão#
    if x_jogador == x_seguidora and y_jogador == y_seguidora:
        print("Colisão.")
    else:
        print("Não estão no mesmo lugar.")

    seguidora.setposition(x_seguidora,y_seguidora)
    tela.ontimer(mover_seguidora, 100)
    







tela = turtle.Screen()
tela.listen()
tela.onkeypress(mov_para_cima, "Up")
tela.onkeypress(mov_para_baixo, "Down")
tela.onkeypress(mover_direita, "Right")
tela.onkeypress(mover_esquerda, "Left")
tela.onkeypress(m_di, "e")
tela.onkeypress(m_es, "q")
tela.onkeypress(m_c, "w")
tela.onkeypress(m_b, "s")
tela.onkeypress(ativa_desativa_desenho, "p")
tela.onkeypress(engrossar_linha, "+")
tela.onkeypress(linha_normal, "-")
tela.onkeypress(borracha, "z")
tela.onkeypress(voltar, "x")
# tela.onkeypress(teste_x, "t")
# tela.onkeypress(teste_y, "k")
mover_seguidora()

tela.mainloop()

