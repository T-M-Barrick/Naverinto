import pygame, sys, os

lista_de_modulos = ['cons', 'player']
for modulo in lista_de_modulos:
    sys.path.append(os.path.join(os.path.dirname(__file__), modulo))

import cons, player

# Inicializamos Pygame
pygame.init()

screen = pygame.display.set_mode((cons.ANCHO_SCREEN, cons.ALTO_SCREEN)) # Determina el tamaño de la pantalla del juego.
pygame.display.set_caption('Naverinto') # set_caption() permite ponerle nombre al juego.

# Instanciamos una nave y establecemos su posición inicial.
nave = player.Spaceship(cons.ANCHO_SCREEN // 2, cons.ALTO_SCREEN - 300)

clock = pygame.time.Clock() # Creamos un objeto de la clase Clock. Esta clase proporciona métodos para controlar el tiempo y el framerate del juego.
dt = 0 # Inicializamos la variable dt que servirá para controlar los tiempos de cada ciclo. Su unidad será el segundo.

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Moveremos a la nave con las teclas. La cantidad de píxeles que se moverá,
    # será su velocidad (píxeles/segundos) por el tiempo dt (segundos).
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        nave.y -= cons.SHIP_SPEED * dt # Mueve hacia arriba
    if keys[pygame.K_s]:
        nave.y += cons.SHIP_SPEED * dt # Mueve hacia abajo
    if keys[pygame.K_a]:
        nave.x -= cons.SHIP_SPEED * dt # Mueve hacia la izquierda
    if keys[pygame.K_d]:
        nave.x += cons.SHIP_SPEED * dt # Mueve hacia la derecha
    
    # Limitamos la posición de la nave dentro de los límites de la pantalla
    if nave.x < 0:
        nave.x = 0
    elif nave.x > cons.ANCHO_SCREEN - nave.rect.width:
        nave.x = cons.ANCHO_SCREEN - nave.rect.width
    
    if nave.y < 0:
        nave.y = 0
    elif nave.y > cons.ALTO_SCREEN - nave.rect.height:
        nave.y = cons.ALTO_SCREEN - nave.rect.height
    
    # Repintea la pantalla, haciendo que los espacios dejados atrás por la nave no se queden pintados, simulando la idea de movimiento.
    screen.fill(cons.BLACK)

    nave.dibujar(screen)

    # Actualizamos la ventana luego de que se hayan hecho movimientos. Sin esta función, los cambios no se reflejarían en pantalla.
    pygame.display.update()

    # tick() pausa el programa hasta que pase suficiente tiempo desde el último llamado a tick(), asegurando
    # así que el juego no se ejecute más rápido que el límite especificado (el límite son los fps). tick() controla
    # la velocidad del juego haciendo que sea siempre la misma o casi la misma.
    dt = clock.tick(cons.fps) / 1000 # Dividimos por mil para pasar de milisegundos a segundos.

pygame.quit() # Para liberar espacio en la memoria y recursos del sistema al cerrar el juego y el programa.
sys.exit()