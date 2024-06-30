import pygame
import random
from shots.shot import BalasEnemigo

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, width, height, laser_sonido):
        super().__init__()
        self.image = pygame.image.load('assets/imagenes/e1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width - self.rect.width)
        self.rect.y = random.randint(-height, -self.rect.height)
        self.velocidad_y = random.randint(1, 3)
        self.laser_sonido = laser_sonido
        self.width = width
        self.height = height

    def update(self):
        self.rect.y += self.velocidad_y
        if self.rect.top > self.height:
            self.rect.x = random.randint(0, self.width - self.rect.width)
            self.rect.y = random.randint(-self.height, -self.rect.height)
            self.velocidad_y = random.randint(1, 3)

    def disparar(self):
        bala = BalasEnemigo(self.rect.centerx, self.rect.bottom)
        return bala, self.laser_sonido
