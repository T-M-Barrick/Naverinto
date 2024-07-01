import pygame, sys, os

directorio_raiz = os.path.abspath(os.path.dirname(__file__)) # Preguntarle al profe si lo dejo así o lo borro
if directorio_raiz not in sys.path:
    sys.path.append(directorio_raiz)

import cons, player

# Inicializamos Pygame
pygame.init()

screen = pygame.display.set_mode((cons.ANCHO_SCREEN, cons.ALTO_SCREEN)) # Determina el tamaño de la pantalla del juego.
pygame.display.set_caption('Naverinto') # set_caption() permite ponerle nombre al juego.

# Cargamos el sprite de la nave y ajustamos su tamaño
imagen_nave = pygame.image.load(os.path.join(directorio_raiz, 'Imagenes', 'sprite1.png'))
imagen_nave = pygame.transform.scale(imagen_nave, (imagen_nave.get_width() * cons.ESCALA_NAVE,
                                         imagen_nave.get_height() * cons.ESCALA_NAVE))

# Cargamos el sprite de la bala y ajustamos su tamaño
imagen_bullet = pygame.image.load(os.path.join(directorio_raiz, 'Imagenes', 'bala azul.png'))
imagen_bullet = pygame.transform.scale(imagen_bullet, (imagen_bullet.get_width() * cons.ESCALA_BULLET,
                                         imagen_bullet.get_height() * cons.ESCALA_BULLET))

# Instanciamos una nave cargándole su sprite y establecemos su posición inicial
nave = player.Spaceship(cons.ANCHO_SCREEN // 2, cons.ALTO_SCREEN - 300, imagen_nave, imagen_bullet)

balas = pygame.sprite.Group()  # Grupo para almacenar las balas disparadas

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
    if keys[pygame.K_j]:
        nave.rotar(2) # Rota en sentido anti-horario
    if keys[pygame.K_l]:
        nave.rotar(-2) # Rota en sentido horario
    if keys[pygame.K_k]:
        # El método disparar() devuelve una instancia de la clase Bullet pero
        # devuelve None si se aprieta para disparar sin haber dejado pasar el tiempo suficiente
        bala = nave.disparar()
        if bala is not None:
            balas.add(bala)
    
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

    nave.update()
    nave.dibujar(screen)
    
    # Dibujamos las balas y actualizamos sus posiciones, o sea, las movemos.
    # Las balas que ya no pertenecen al grupo balas, ya no se cargarán más y desaparecerán de la pantalla.
    for bullet in balas:
        bullet.dibujar(screen)
        bullet.update() # CHEQUEAR!!!!!: Ver cómo pasarle como argumento al update a la nave enemiga considerando que será online

    # Actualizamos la ventana luego de que se hayan hecho movimientos. Sin esta función, los cambios no se reflejarían en pantalla.
    pygame.display.update()

    # tick() pausa el programa hasta que pase suficiente tiempo desde el último llamado a tick(), asegurando
    # así que el juego no se ejecute más rápido que el límite especificado (el límite son los fps). tick() controla
    # la velocidad del juego haciendo que sea siempre la misma o casi la misma.
    dt = clock.tick(cons.fps) / 1000 # Dividimos por mil para pasar de milisegundos a segundos.

# Para liberar espacio en la memoria y recursos del sistema al cerrar el juego y el programa.
pygame.quit()
sys.exit()