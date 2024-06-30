import pygame

white = (255, 255, 255)

def texto_puntuacion(frame, text, size, x, y):
    font = pygame.font.SysFont('Small Fonts', size, bold=True)
    text_surface = font.render(text, True, white)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    frame.blit(text_surface, text_rect)

def barra_vida(frame, x, y, nivel):
    longitud = 200  # Longitud de la barra de vida
    alto = 20  # Altura de la barra de vida
    borde_rect = pygame.Rect(x, y, longitud, alto)
    lleno_rect = pygame.Rect(x, y, nivel * 2, alto)  # Calcula el ancho lleno según el nivel de vida
    pygame.draw.rect(frame, (0, 255, 0), lleno_rect)  # Dibuja la parte llena de la barra en color verde
    pygame.draw.rect(frame, (255, 255, 255), borde_rect, 2)  # Dibuja el borde de la barra en color blanco
