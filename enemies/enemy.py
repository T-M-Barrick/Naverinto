import pygame
import random
from shots.balas import BalasEnemigo

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, width, height, grupo_balas_enemigo):
        super().__init__()
        self.image = pygame.image.load('assets/imagenes/e1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width - self.rect.width)
        self.rect.y = random.randint(-height, -self.rect.height)
        self.velocidad_y = random.randint(1, 3)
        self.width = width
        self.height = height
        self.grupo_balas_enemigo = grupo_balas_enemigo

    def update(self):
        self.rect.y += self.velocidad_y
        if self.rect.top > self.height:
            self.rect.x = random.randint(0, self.width - self.rect.width)
            self.rect.y = random.randint(-self.height, -self.rect.height)
            self.velocidad_y = random.randint(1, 3)

    def disparar(self):
        bala = BalasEnemigo(self.rect.centerx, self.rect.bottom)
        self.grupo_balas_enemigo.add(bala)