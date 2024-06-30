# Cargar recursos
fondo = pygame.image.load('imagenes/fondo1.jpg')
laser_sonido = pygame.mixer.Sound('laser.wav')
explosion_sonido = pygame.mixer.Sound('explosion.wav')
golpe_sonido = pygame.mixer.Sound('golpe.wav')

explosion_list = []
for i in range(1, 13):
    explosion = pygame.image.load(f'explosion/{i}.png')
    explosion_list.append(explosion)

# Configurar la pantalla
width = fondo.get_width()
height = fondo.get_height()
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Naverinto')

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

# Clases de sprites
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('imagenes/spaceship.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.centerx = width // 2
        self.rect.centery = height - 50
        self.velocidad_x = 0
        self.vida = 100

    def update(self):
        self.velocidad_x = 0
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            self.velocidad_x = -5
        elif teclas[pygame.K_RIGHT]:
            self.velocidad_x = 5

        self.rect.x += self.velocidad_x
        if self.rect.right > width:
            self.rect.right = width
        elif self.rect.left < 0:
            self.rect.left = 0

    def disparar(self):
        bala = Balas(self.rect.centerx, self.rect.top)
        grupo_balas.add(bala)
        grupo_balas_jugador.add(bala)
        laser_sonido.play()

class Enemigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('imagenes/e1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width - self.rect.width)
        self.rect.y = random.randint(-height, -self.rect.height)
        self.velocidad_y = random.randint(1, 3)

    def update(self):
        self.rect.y += self.velocidad_y
        if self.rect.top > height:
            self.rect.x = random.randint(0, width - self.rect.width)
            self.rect.y = random.randint(-height, -self.rect.height)
            self.velocidad_y = random.randint(1, 3)

    def disparar(self):
        bala = BalasEnemigo(self.rect.centerx, self.rect.bottom)
        grupo_balas.add(bala)
        grupo_balas_enemigo.add(bala)
        laser_sonido.play()

class Balas(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 20))
        self.image.fill((255, 0, 0))  # Color rojo para la bala del jugador
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.velocidad = -10

    def update(self):
        self.rect.y += self.velocidad
        if self.rect.bottom < 0:
            self.kill()

class BalasEnemigo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 20))
        self.image.fill((0, 0, 255))  # Color azul para la bala del enemigo
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.velocidad = 4

    def update(self):
        self.rect.y += self.velocidad
        if self.rect.top > height:
            self.kill()

class Explosion(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = explosion_list[0]
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50  # Velocidad de la animación de la explosión
        self.frame = 0

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame < len(explosion_list):
                center = self.rect.center
                self.image = explosion_list[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
            else:
                self.kill()

# Grupos de sprites
grupo_jugador = pygame.sprite.Group()
grupo_enemigos = pygame.sprite.Group()
grupo_balas = pygame.sprite.Group()
grupo_balas_jugador = pygame.sprite.Group()
grupo_balas_enemigo = pygame.sprite.Group()

jugador = Jugador()
grupo_jugador.add(jugador)

for _ in range(10):
    enemigo = Enemigo()
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
                    jugador.disparar()

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

        colisiones_jugador_enemigo = pygame.sprite.groupcollide(grupo_jugador, grupo_enemigos, False, True)
        for jugador, enemigos in colisiones_jugador_enemigo.items():
            for enemigo in enemigos:
                score += 10
                explosion = Explosion(enemigo.rect.center)
                grupo_enemigos.add(explosion)
                explosion_sonido.play()

        colisiones_balas_enemigo = pygame.sprite.groupcollide(grupo_balas, grupo_enemigos, True, True)
        for bala, enemigos in colisiones_balas_enemigo.items():
            for enemigo in enemigos:
                score += 10
                explosion = Explosion(enemigo.rect.center)
                grupo_enemigos.add(explosion)
                explosion_sonido.play()

        texto_puntuacion(window, 'SCORE: ' + str(score), 30, width - 85, 2)
        barra_vida(window, 10, 10, vida)

        pygame.display.flip()

except Exception as error:
    print(f"Se produjo un error: {error}")

finally:
    pygame.quit()
