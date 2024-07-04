import pygame
import random
from sprites import Jugador, Enemigo, Balas, BalasEnemigo

# Inicializar Pygame
pygame.init()
pygame.mixer.init()

# Configurar la pantalla
width, height = 600, 500  # Tamaño de la ventana
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Naverinto')

# Cargar recursos
fondo = pygame.image.load('assets/imagenes/fondo1.jpg')

# Sonidos
laser_sonido = pygame.mixer.Sound('assets/laser.wav')
explosion_sonido = pygame.mixer.Sound('assets/explosion.wav')
golpe_sonido = pygame.mixer.Sound('assets/golpe.wav')

# Imágenes de balas
bala_jugador_img = pygame.image.load('assets/imagenes/b1.png').convert_alpha()
bala_jugador_img = pygame.transform.scale(bala_jugador_img, (10, 20))
bala_enemigo_img = pygame.image.load('assets/imagenes/b2.png').convert_alpha()
bala_enemigo_img = pygame.transform.scale(bala_enemigo_img, (10, 20))

# Variables del juego
run = True
fps = 60
clock = pygame.time.Clock()
score = 0
vida = 100
white = (255, 255, 255)
black = (0, 0, 0)

# Funciones de utilidad
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
    pygame.draw.rect(frame, (0, 255, 0), lleno_rect)  # Barra de vida llena en verde
    pygame.draw.rect(frame, (255, 255, 255), borde_rect, 2)  # Borde blanco de la barra de vida

# Grupos de sprites
grupo_jugador = pygame.sprite.Group()
grupo_enemigos = pygame.sprite.Group()
grupo_balas = pygame.sprite.Group()
grupo_balas_enemigo = pygame.sprite.Group()

# Bucle principal
try:
    jugador = Jugador()
    grupo_jugador.add(jugador)

    for _ in range(10):  # Mantener 10 enemigos
        enemigo = Enemigo(grupo_balas_enemigo, bala_enemigo_img)
        grupo_enemigos.add(enemigo)

    while run:
        clock.tick(fps)

        # Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                run = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    jugador.disparar(grupo_balas, bala_jugador_img)

        # Actualizar
        grupo_jugador.update()
        grupo_enemigos.update()
        grupo_balas.update()
        grupo_balas_enemigo.update()

        # Verificar colisiones entre balas del jugador y enemigos
        for bala in grupo_balas:
            enemigos_golpeados = pygame.sprite.spritecollide(bala, grupo_enemigos, True)
            for enemigo in enemigos_golpeados:
                bala.kill()
                score += 10
                explosion_sonido.play()
                nuevo_enemigo = Enemigo(grupo_balas_enemigo, bala_enemigo_img)
                grupo_enemigos.add(nuevo_enemigo)

        # Verificar colisiones entre balas enemigas y el jugador
        balas_impacto = pygame.sprite.spritecollide(jugador, grupo_balas_enemigo, True)
        for bala in balas_impacto:
            jugador.recibir_danio(10)
            golpe_sonido.play()
            if jugador.vida <= 0:
                jugador = Jugador()
                grupo_jugador.add(jugador)
                grupo_balas_enemigo.empty()
                grupo_balas.empty()
                grupo_enemigos.empty()
                for _ in range(10):
                    enemigo = Enemigo(grupo_balas_enemigo, bala_enemigo_img)
                    grupo_enemigos.add(enemigo)
                score = 0
                vida = 100

        # Dibujar
        window.blit(fondo, (0, 0))
        grupo_jugador.draw(window)
        grupo_enemigos.draw(window)
        grupo_balas.draw(window)
        grupo_balas_enemigo.draw(window)

        # Mostrar puntuación y barra de vida
        texto_puntuacion(window, 'SCORE: ' + str(score), 30, width - 85, 2)
        barra_vida(window, 10, 10, jugador.vida)

        pygame.display.flip()

except Exception as e:
    print(f"Se produjo un error: {e}")

finally:
    pygame.quit()
