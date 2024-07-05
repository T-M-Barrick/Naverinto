import pygame, sys, os

directorio_raiz = os.path.abspath(os.path.dirname(__file__)) # Preguntarle al profe si lo dejo así o lo borro
if directorio_raiz not in sys.path:
    sys.path.append(directorio_raiz)

import cons, player, paredes, barra_vida, textos

# Inicializamos Pygame
pygame.init()

screen = pygame.display.set_mode((cons.ANCHO_SCREEN, cons.ALTO_SCREEN)) # Determina el tamaño de la pantalla del juego.
pygame.display.set_caption('Naverinto') # set_caption() permite ponerle nombre al juego.

# Cargamos los sprites y ajustamos los tamaños
cant_sprites = 4
sprites = []
escalas = [cons.ESCALA_NAVE, cons.ESCALA_NAVE, cons.ESCALA_BULLET, cons.ESCALA_BULLET]
for n, escala in zip(range(1, cant_sprites + 1), escalas):
    ruta_imagen = os.path.join(directorio_raiz, 'Imagenes', f'sprite{n}.png')
    imagen = pygame.image.load(ruta_imagen)
    imagen = pygame.transform.scale(imagen, (imagen.get_width() * escala,
                                         imagen.get_height() * escala))
    sprites.append(imagen)

# Instanciamos las naves cargándole su sprite y su bala y luego establecemos su posiciones iniciales
nave = player.Spaceship(int(cons.ANCHO_SCREEN * 0.1), cons.ALTO_SCREEN // 2, sprites[0], sprites[2])
nave_enemiga = player.Enemy(int(cons.ANCHO_SCREEN * 0.9), cons.ALTO_SCREEN // 2, sprites[1], sprites[3], nave)

balas = pygame.sprite.Group()  # Grupo para almacenar las balas disparadas
balas_nave_enemiga = pygame.sprite.Group()  # Grupo para almacenar las balas disparadas

barra_nave = barra_vida.BarraVida((0, 0), cons.VIDA, 20, cons.VERDE)
barra_enemiga = barra_vida.BarraVida((cons.ANCHO_SCREEN - cons.VIDA, 0), cons.VIDA, 20, cons.BLUE, es_enemigo=True)

clock = pygame.time.Clock() # Creamos un objeto de la clase Clock. Esta clase proporciona métodos para controlar el tiempo y el framerate del juego.
dt = 0 # Inicializamos la variable dt que servirá para controlar los tiempos de cada ciclo. Su unidad será el segundo.

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Para liberar espacio en la memoria y recursos del sistema al cerrar el juego y el programa.
            pygame.quit()
            sys.exit()

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
    
    # Limitamos las posiciones de las naves dentro de los límites de la pantalla

    if nave.x < 0:
        nave.x = 0
    elif nave.x > cons.ANCHO_SCREEN - nave.rect.width:
        nave.x = cons.ANCHO_SCREEN - nave.rect.width
    
    if nave.y < 0:
        nave.y = 0
    elif nave.y > cons.ALTO_SCREEN - nave.rect.height:
        nave.y = cons.ALTO_SCREEN - nave.rect.height
    
    if nave_enemiga.x < 0:
        nave_enemiga.x = 0
    elif nave_enemiga.x > cons.ANCHO_SCREEN - nave_enemiga.rect.width:
        nave_enemiga.x = cons.ANCHO_SCREEN - nave_enemiga.rect.width
    
    if nave_enemiga.y < 0:
        nave_enemiga.y = 0
    elif nave_enemiga.y > cons.ALTO_SCREEN - nave_enemiga.rect.height:
        nave_enemiga.y = cons.ALTO_SCREEN - nave_enemiga.rect.height
    
    # Repintea la pantalla, haciendo que los espacios dejados atrás por la nave no se queden pintados, simulando la idea de movimiento.
    screen.fill(cons.BLACK)

    # Dibujamos las naves y actualizamos sus situaciones
    vive1 = nave.update()
    nave.dibujar(screen)
    vive2 = nave_enemiga.update(dt)
    nave_enemiga.dibujar(screen)

    # Este condicional nos permitirá salir del bucle en caso de que haya muerto una nave
    if vive1 is False or vive2 is False:
        running = False

    # Dibujamos las barras de vida
    barra_nave.dibujar(screen, nave.vida)
    barra_enemiga.dibujar(screen, nave_enemiga.vida)
    
    # Dibujamos las balas y actualizamos sus posiciones, o sea, las movemos.
    # Las balas que ya no pertenecen al grupo balas, ya no se cargarán más y desaparecerán de la pantalla.
    for bullet in balas:
        bullet.dibujar(screen)
        bullet.update(nave_enemiga)

    # Hacemos ahora que la nave enemiga dispare
    bala_enemiga = nave_enemiga.disparar()
    if bala_enemiga is not None:
        balas_nave_enemiga.add(bala_enemiga)
    for bullet in balas_nave_enemiga:
        bullet.dibujar(screen)
        bullet.update(nave)

    # Actualizamos la ventana luego de que se hayan hecho movimientos. Sin esta función, los cambios no se reflejarían en pantalla.
    pygame.display.update()

    # tick() pausa el programa hasta que pase suficiente tiempo desde el último llamado a tick(), asegurando
    # así que el juego no se ejecute más rápido que el límite especificado (el límite son los fps). tick() controla
    # la velocidad del juego haciendo que sea siempre la misma o casi la misma.
    dt = clock.tick(cons.fps) / 1000 # Dividimos por mil para pasar de milisegundos a segundos.

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
        # Para liberar espacio en la memoria y recursos del sistema al cerrar el juego y el programa.
            pygame.quit()
            sys.exit()

    if vive1 is False:
        textos.game_over(screen, win=False)
    elif vive2 is False:
        textos.game_over(screen)
    
    pygame.display.update()