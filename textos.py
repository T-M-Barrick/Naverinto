import pygame, cons

def game_over(screen, win=True):

    font = pygame.font.Font(None, cons.SIZE_TEXT_FINAL) # Fuente y tamaño del texto
    sc_ds = screen.get_size() # Retorna una tupla con las dimensiones de la pantalla (ancho y alto)

    if win:
        texto = font.render('Ganaste!!', True, cons.VIOLET) # Creamos superficie con el texto
    else:
        texto = font.render('Game Over', True, cons.VIOLET) # Creamos superficie con el texto

    texto_rect = texto.get_rect(center=(sc_ds[0] // 2, sc_ds[1] // 2)) # Centramos el texto en la pantalla
    screen.blit(texto, texto_rect)  # Dibujamos el texto en la pantalla