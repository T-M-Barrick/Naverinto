import pygame
import sys
from player import Jugador
from enemy import Enemigo
from balas import Balas, BalasEnemigo
from explosion import Explosion

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Naverinto')

# Cargar recursos
fondo = pygame.image.load('assets/imagenes/fondo1.jpg')
laser_sonido = pygame.mixer.Sound('assets/laser.wav')
explosion_sonido = pygame.mixer.Sound('assets/explosion.wav')
golpe_sonido = pygame.mixer.Sound('assets/golpe.wav')

# Crear grupos de sprites
grupo_jugadores = pygame.sprite.Group()
grupo_enemigos = pygame.sprite.Group()
grupo_balas = pygame.sprite.Group()
grupo_balas_enemigo = pygame.sprite.Group()
grupo_explosiones = pygame.sprite.Group()

# Crear instancia del jugador
jugador = Jugador(width, height, laser_sonido, grupo_balas)
grupo_jugadores.add(jugador)

# Crear instancias de enemigos
for i in range(5):
    enemigo = Enemigo(width, height, grupo_balas_enemigo)
    grupo_enemigos.add(enemigo)

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualizar
    grupo_jugadores.update()
    grupo_enemigos.update()
    grupo_balas.update()
    grupo_balas_enemigo.update()
    grupo_explosiones.update()

    # Dibujar
    window.blit(fondo, (0, 0))
    grupo_jugadores.draw(window)
    grupo_enemigos.draw(window)
    grupo_balas.draw(window)
    grupo_balas_enemigo.draw(window)
    grupo_explosiones.draw(window)
    
    pygame.display.flip()

pygame.quit()
sys.exit()
