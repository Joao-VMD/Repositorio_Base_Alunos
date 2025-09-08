import pygame
import pygame2Turma1
from random import randint

def sortear_direcao_bola(velocidade):
    if randint(0,1) == 1:
        return velocidade
    else:
        return -velocidade
def reset_jogo():
    bola.x = (LARGURA_TELA - TAMANHO_BOLA) // 2
    bola.y = (ALTURA_TELA - TAMANHO_BOLA) // 2
    barra_esquerda.y = (ALTURA_TELA - ALTURA_BARRA) // 2
    barra_direita.y = (ALTURA_TELA - ALTURA_BARRA) // 2
    global velocidade_bola_x 
    velocidade_bola_x = sortear_direcao_bola(VELOCIDADE_BOLA_X)
    global velocidade_bola_y 
    velocidade_bola_y = sortear_direcao_bola(VELOCIDADE_BOLA_Y)

pygame.init()
LARGURA_TELA, ALTURA_TELA = 800,600
PRETO = (0,0,0)
BRANCO = (255,255,255)
#Constantes da barra
LARGURA_BARRA, ALTURA_BARRA = 10, 100
VELOCIDADE_BARRA = 7
#Constantes da bola
TAMANHO_BOLA = 10
VELOCIDADE_BOLA_X = 5
VELOCIDADE_BOLA_Y = 5

#Placar
pontos_esquerda = 0
pontos_direita = 0
fonte = pygame.font.Font(None, 36)

tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Pong Turma 2")
clock = pygame.time.Clock()

#Criação das barras
barra_esquerda = pygame.Rect(10, (ALTURA_TELA - ALTURA_BARRA) // 2, LARGURA_BARRA, ALTURA_BARRA)
barra_direita = pygame.Rect(LARGURA_TELA - 20, (ALTURA_TELA - ALTURA_BARRA) // 2, LARGURA_BARRA, ALTURA_BARRA)
bola = pygame.Rect( (LARGURA_TELA - TAMANHO_BOLA)//2, (ALTURA_TELA - TAMANHO_BOLA)//2, TAMANHO_BOLA, TAMANHO_BOLA)
rodando = True
velocidade_barra_direita = 0
velocidade_barra_esquerda = 0

velocidade_bola_x = sortear_direcao_bola(VELOCIDADE_BOLA_X)
velocidade_bola_y = sortear_direcao_bola(VELOCIDADE_BOLA_Y)


while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_w:
                velocidade_barra_esquerda = -VELOCIDADE_BARRA    
            if evento.key == pygame.K_s:
                velocidade_barra_esquerda = VELOCIDADE_BARRA

            if evento.key == pygame.K_UP:
                velocidade_barra_direita = -VELOCIDADE_BARRA
            if evento.key == pygame.K_DOWN:
                velocidade_barra_direita = VELOCIDADE_BARRA      

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_w or evento.key == pygame.K_s:
                velocidade_barra_esquerda = 0
            if evento.key == pygame.K_UP or evento.key == pygame.K_DOWN:
                velocidade_barra_direita = 0      

    barra_esquerda.y += velocidade_barra_esquerda
    barra_direita.y += velocidade_barra_direita    

    barra_esquerda.y = max(0, min(ALTURA_TELA - ALTURA_BARRA, barra_esquerda.y))
    barra_direita.y = max(0, min(ALTURA_TELA - ALTURA_BARRA, barra_direita.y))

    bola.x += velocidade_bola_x
    bola.y += velocidade_bola_y


    if bola.top <= 0 or bola.bottom >= ALTURA_TELA:
        velocidade_bola_y = - velocidade_bola_y

    if bola.colliderect(barra_esquerda) or bola.colliderect(barra_direita):
        velocidade_bola_x = -velocidade_bola_x 
    



    if bola.left <= 0:
        pontos_direita += 1
        reset_jogo()

    if bola.right >= LARGURA_TELA:
        pontos_esquerda += 1    
        reset_jogo()




    #Desenhando elementos na tela
    tela.fill(PRETO)
    pygame.draw.rect(tela, (30,144,255), barra_esquerda)
    pygame.draw.rect(tela, (178,34,34), barra_direita)
    pygame.draw.rect(tela, BRANCO, bola)
    pygame.draw.aaline(tela, BRANCO, (LARGURA_TELA // 2,0),(LARGURA_TELA // 2, ALTURA_TELA))

    #Desenhar placar
    placar_esquerda = fonte.render(str(pontos_esquerda),True,(30,144,255))
    placar_direita = fonte.render(str(pontos_direita), True, (178,34,34))
    tela.blit(placar_esquerda, (LARGURA_TELA // 4 - placar_esquerda.get_width() // 2, 20))
    tela.blit(placar_direita, (3 * LARGURA_TELA // 4 - placar_direita.get_width() // 2, 20))

    pygame.display.update()
    clock.tick(60)

pygame.quit()