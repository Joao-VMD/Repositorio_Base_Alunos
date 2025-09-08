import pygame

vermelho = 0
verde = 0
azul = 0

def muda_cor():
    global vermelho
    global verde
    global azul
    vermelho = (vermelho + 1) % 255
    verde = (verde + 1) % 255
    azul = (azul + 1) % 255

pygame.init() 
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Exemplo com Pygame")
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    tela.fill((vermelho, verde, azul))
    muda_cor()

    pygame.display.update()

pygame.quit()