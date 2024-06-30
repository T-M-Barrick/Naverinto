import pygame

from shots.shot import Balas

class Jugador(pygame.sprite.Sprite):
    def __init__(self, laser_sonido, width, height):
        super().__init__()
        self.image = pygame.image.load('assets/imagenes/spaceship.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.centerx = width // 2
        self.rect.centery = height - 50
        self.velocidad_x = 0
        self.vida = 100
        self.laser_sonido = laser_sonido
        self.width = width

    def update(self):
        self.velocidad_x = 0
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            self.velocidad_x = -5
        elif teclas[pygame.K_RIGHT]:
            self.velocidad_x = 5

        self.rect.x += self.velocidad_x
        if self.rect.right > self.width:
            self.rect.right = self.width
        elif self.rect.left < 0:
            self.rect.left = 0

    def disparar(self, grupo_balas, grupo_balas_jugador):
        bala = Balas(self.rect.centerx, self.rect.top)
        grupo_balas.add(bala)
        grupo_balas_jugador.add(bala)
        self.laser_sonido.play()
