import pygame, cons

class Pared(pygame.sprite.Sprite):

    def __init__(self, x, y, ancho, alto, color):

        super().__init__()

        self.image = pygame.Surface((ancho, alto))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))