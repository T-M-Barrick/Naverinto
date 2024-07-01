import pygame

class Explosion(pygame.sprite.Sprite):
    def __init__(self, position, explosion_list):
        super().__init__()
        self.image = explosion_list[0]
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.explosion_list = explosion_list
        self.index = 0
        self.update_time = pygame.time.get_ticks()
        self.frame_rate = 50  # Cambia el frame cada 50 milisegundos

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.update_time > self.frame_rate:
            self.index += 1
            if self.index >= len(self.explosion_list):
                self.kill()
            else:
                self.image = self.explosion_list[self.index]
                self.update_time = current_time
