import pygame
import random

# Dimensiones de la pantalla
width, height = 600, 500

# Clase Jugador
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/imagenes/spaceship.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, height - self.image.get_height() // 2)
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

    def disparar(self, grupo_balas, bala_jugador_img):
        bala = Balas(self.rect.centerx, self.rect.top, bala_jugador_img)  # Disparar hacia arriba
        grupo_balas.add(bala)
        laser_sonido = pygame.mixer.Sound('assets/laser.wav')
        laser_sonido.play()

    def recibir_danio(self, danio):
        self.vida -= danio
        if self.vida <= 0:
            self.vida = 0  # Asegurar que la vida no sea negativa
            self.kill()  # Eliminar jugador si la vida llega a cero

# Clase Enemigo
class Enemigo(pygame.sprite.Sprite):
    def __init__(self, grupo_balas_enemigo, bala_enemigo_img):
        super().__init__()
        self.image = pygame.image.load('assets/imagenes/e1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width - self.rect.width)
        self.rect.y = random.randint(-height, -self.rect.height)
        self.velocidad_y = random.uniform(0.5, 1.5)  # Velocidad más lenta para los enemigos
        self.siguiente_disparo = pygame.time.get_ticks() + random.randint(1000, 3000)  # Próximo disparo en 1-3 segundos
        self.grupo_balas_enemigo = grupo_balas_enemigo
        self.bala_enemigo_img = bala_enemigo_img

    def update(self):
        self.rect.y += self.velocidad_y
        if self.rect.top > height:
            self.rect.x = random.randint(0, width - self.rect.width)
            self.rect.y = random.randint(-height, -self.rect.height)
            self.velocidad_y = random.uniform(0.5, 1.5)  # Velocidad más lenta para los enemigos

        # Lógica de disparo
        ahora = pygame.time.get_ticks()
        if ahora >= self.siguiente_disparo:
            self.disparar()
            self.siguiente_disparo = ahora + random.randint(1000, 3000)  # Próximo disparo en 1-3 segundos

    def disparar(self):
        bala = BalasEnemigo(self.rect.centerx, self.rect.bottom, self.bala_enemigo_img)  # Disparar hacia abajo
        self.grupo_balas_enemigo.add(bala)
        laser_sonido = pygame.mixer.Sound('assets/laser.wav')
        laser_sonido.play()

# Clase Bala
class Balas(pygame.sprite.Sprite):
    def __init__(self, x, y, bala_img):
        super().__init__()
        self.image = bala_img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.velocidad_y = -10  # Velocidad de la bala del jugador

    def update(self):
        self.rect.y += self.velocidad_y
        if self.rect.bottom < 0:
            self.kill()

# Clase BalaEnemigo
class BalasEnemigo(pygame.sprite.Sprite):
    def __init__(self, x, y, bala_img):
        super().__init__()
        self.image = bala_img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.top = y
        self.velocidad_y = 5  # Velocidad de la bala del enemigo

    def update(self):
        self.rect.y += self.velocidad_y
        if self.rect.top > height:
            self.kill()
