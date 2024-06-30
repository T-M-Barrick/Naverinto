import pygame

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
        if self.rect.top > 600:  # Asumiendo un tamaño de pantalla de 600 de alto
            self.kill()

class Explosion(pygame.sprite.Sprite):
    def __init__(self, position, explosion_list):
        super().__init__()
        self.image = explosion_list[0]
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50  # Velocidad de la animación de la explosión
        self.frame = 0
        self.explosion_list = explosion_list

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame < len(self.explosion_list):
                center = self.rect.center
                self.image = self.explosion_list[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
            else:
                self.kill()
