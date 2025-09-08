import pygame
import random
import sys

# Inicialização do Pygame
pygame.init()
pygame.font.init()

# Configurações da janela
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clique no Quadrado")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)

# Fonte para texto
FONT = pygame.font.SysFont(None, 36)

# Dimensões e posição inicial do quadrado
SQUARE_SIZE = 50

def get_random_position():
    """Retorna uma posição (x, y) aleatória para que o quadrado fique totalmente dentro da tela."""
    x = random.randint(0, WIDTH - SQUARE_SIZE)
    y = random.randint(0, HEIGHT - SQUARE_SIZE)
    return x, y

# Posições iniciais
square_x, square_y = get_random_position()

# Variáveis de pontuação e tempo
score = 0
game_duration = 30_000  # 30 segundos em milissegundos
start_time = pygame.time.get_ticks()

# Controle de frames por segundo
clock = pygame.time.Clock()
FPS = 60

# Estados do jogo
running = True
game_over = False

while running:
    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - start_time
    remaining_time = max(0, game_duration - elapsed_time)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Se o jogo não acabou, captura cliques de mouse
        if not game_over and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos
            # Verifica se o clique foi dentro do quadrado
            if (square_x <= mouse_x <= square_x + SQUARE_SIZE) and (square_y <= mouse_y <= square_y + SQUARE_SIZE):
                score += 1
                square_x, square_y = get_random_position()

        # Se o jogo acabou, qualquer clique ou tecla fecha o jogo
        if game_over and event.type in (pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN):
            running = False

    # Verifica se o tempo acabou
    if elapsed_time >= game_duration:
        game_over = True

    # Desenho dos elementos na tela
    SCREEN.fill(WHITE)

    if not game_over:
        # Desenha o quadrado
        pygame.draw.rect(SCREEN, RED, (square_x, square_y, SQUARE_SIZE, SQUARE_SIZE))

        # Renderiza o tempo restante e a pontuação
        seconds_left = remaining_time // 1000
        timer_text = FONT.render(f"Tempo: {seconds_left}s", True, BLACK)
        score_text = FONT.render(f"Pontuação: {score}", True, BLACK)
        SCREEN.blit(timer_text, (10, 10))
        SCREEN.blit(score_text, (10, 50))

    else:
        # Tela de fim de jogo
        game_over_text = FONT.render("Tempo esgotado!", True, BLACK)
        final_score_text = FONT.render(f"Sua pontuação: {score}", True, BLACK)
        instr_text = FONT.render("Clique ou pressione qualquer tecla para sair.", True, BLACK)

        # Centraliza texto
        go_rect  = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40))
        fs_rect  = final_score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        ins_rect = instr_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 40))

        SCREEN.blit(game_over_text, go_rect)
        SCREEN.blit(final_score_text, fs_rect)
        SCREEN.blit(instr_text, ins_rect)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
