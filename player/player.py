import pygame
from shots.balas import Balas

class Jugador(pygame.sprite.Sprite):
    def __init__(self, width, height, laser_sonido, grupo_balas):
        super().__init__()
        self.image = pygame.image.load('assets/imagenes/spaceship.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.centerx = width // 2
        self.rect.centery = height - 50
        self.width = width
        self.height = height
        self.laser_sonido = laser_sonido
        self.grupo_balas = grupo_balas

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.right < self.width:
            self.rect.x += 5
        if keys[pygame.K_SPACE]:
            self.disparar()

    def disparar(self):
        bala = Balas(self.rect.centerx, self.rect.top)
        self.grupo_balas.add(bala)
        self.laser_sonido.play()