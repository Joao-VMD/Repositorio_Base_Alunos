import pygame

pygame.init()
LARGURA_TELA, ALTURA_TELA = 800, 600
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
clock = pygame.time.Clock()

pos_x = 50
pos_y = 50
velocidade_x = 5
velocidade_y = 5
LARGURA_RET, ALTURA_RET = 50, 50
cor = (255,0,0)
rodando = True
def colorido (cor):
    cores = [
        (255,0,0),
        (0,255,0),
        (0,0,255),
        (255,255,0),
        (0,255,255),
        (255,0,255),
        (0,160,160),
        (0,0,64),
        (0,0,160),
        (255, 255, 224),
        (173, 255, 47),
        (255, 191, 0),
        (221, 160, 221),
        (0, 0, 156),
        (35, 35, 142),
        (50, 50, 205),
        (47, 79, 79),
        (105, 105, 105),
        (0, 0, 128),
        (0, 0, 139),
        (0, 0, 205),
        (0, 0, 255),
        (0, 100, 0),
        (0, 128, 0),
        (34, 139, 34),
        (50, 205, 50)
    
    ]
    proxima_cor = cores.index(cor) + 1

    return cores[proxima_cor % len(cores)]




while rodando:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    pos_x = pos_x + velocidade_x
    pos_y = pos_y + velocidade_y

    if pos_x + LARGURA_RET > LARGURA_TELA or pos_x < 0:
        velocidade_x = -velocidade_x
        cor = colorido(cor)
    if pos_y + ALTURA_RET > ALTURA_TELA or pos_y < 0:
        velocidade_y = -velocidade_y
        cor = colorido(cor)


    tela.fill((0,0,0))



    pygame.draw.rect(tela, (cor), (pos_x, pos_y, LARGURA_RET, ALTURA_RET))
    pygame.display.update()
    clock.tick(60)





pygame.quit()
