import pygame
import random
from player.player import Jugador
from enemies.enemy import Enemigo
from shots.shot import Explosion
from utils.utils import texto_puntuacion, barra_vida

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
width, height = 800, 600  # Puedes ajustar estos valores según tu necesidad
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Naverinto')

# Cargar recursos
fondo = pygame.image.load('assets/imagenes/fondo1.jpg')
laser_sonido = pygame.mixer.Sound('assets/laser.wav')
explosion_sonido = pygame.mixer.Sound('assets/explosion.wav')
golpe_sonido = pygame.mixer.Sound('assets/golpe.wav')

explosion_list = []
for i in range(1, 13):
    explosion = pygame.image.load(f'assets/explosion/{i}.png').convert_alpha()
    explosion_list.append(explosion)

# Ajustar el tamaño de la ventana a las dimensiones del fondo
width = fondo.get_width()
height = fondo.get_height()
window = pygame.display.set_mode((width, height))

# Variables del juego
run = True
fps = 60
clock = pygame.time.Clock()
score = 0
vida = 100
white = (255, 255, 255)
black = (0, 0, 0)

# Grupos de sprites
grupo_jugador = pygame.sprite.Group()
grupo_enemigos = pygame.sprite.Group()
grupo_balas = pygame.sprite.Group()
grupo_balas_jugador = pygame.sprite.Group()
grupo_balas_enemigo = pygame.sprite.Group()

jugador = Jugador(width, height, laser_sonido)
grupo_jugador.add(jugador)

for _ in range(10):
    enemigo = Enemigo(width, height, laser_sonido)
    grupo_enemigos.add(enemigo)

# Bucle principal
try:
    while run:
        clock.tick(fps)
        window.blit(fondo, (0, 0))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                run = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    jugador.disparar(grupo_balas, grupo_balas_jugador)

        grupo_jugador.update()
        grupo_enemigos.update()
        grupo_balas.update()
        grupo_balas_jugador.update()
        grupo_balas_enemigo.update()

        grupo_jugador.draw(window)
        grupo_enemigos.draw(window)
        grupo_balas.draw(window)
        grupo_balas_jugador.draw(window)
        grupo_balas_enemigo.draw(window)

        # Colisiones entre el jugador y los enemigos
        colisiones_jugador_enemigo = pygame.sprite.groupcollide(grupo_jugador, grupo_enemigos, False, True)
        for jugador, enemigos in colisiones_jugador_enemigo.items():
            for enemigo in enemigos:
                score += 10
                explosion = Explosion(enemigo.rect.center, explosion_list)
                grupo_enemigos.add(explosion)
                explosion_sonido.play()

        # Colisiones entre las balas del jugador y los enemigos
        colisiones_balas_enemigo = pygame.sprite.groupcollide(grupo_balas_jugador, grupo_enemigos, True, True)
        for bala, enemigos in colisiones_balas_enemigo.items():
            for enemigo in enemigos:
                score += 10
                explosion = Explosion(enemigo.rect.center, explosion_list)
                grupo_enemigos.add(explosion)
                explosion_sonido.play()

        texto_puntuacion(window, 'SCORE: ' + str(score), 30, width - 85, 2)
        barra_vida(window, 10, 10, vida)

        pygame.display.flip()

except Exception as error:
    print(f"Se produjo un error: {error}")

finally:
    pygame.quit()
