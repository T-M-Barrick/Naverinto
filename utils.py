import pygame

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        super().__init__()
        self.size = size
        self.image = pygame.Surface(size)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0  # Frame de la animación
        self.frame_rate = 10  # Velocidad de la animación
        self.last_update = pygame.time.get_ticks()
        self.explosion_anim = []

        # Cargar imágenes de la explosión desde la carpeta assets
        for i in range(9):
            filename = f'assets/Explosion_0{i + 1}.png'
            img = pygame.image.load(filename).convert_alpha()
            img = pygame.transform.scale(img, size)
            self.explosion_anim.append(img)

    def update(self):
        # Actualizar la animación de la explosión
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(self.explosion_anim):
                self.kill()  # Eliminar la explosión cuando termina la animación
            else:
                center = self.rect.center
                self.image = self.explosion_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

# Función para cargar imágenes
def cargar_imagen(nombre_archivo):
    return pygame.image.load(f'assets/imagenes/{nombre_archivo}').convert_alpha()

# Función para cargar sonidos
def cargar_sonido(nombre_archivo):
    return pygame.mixer.Sound(f'assets/{laser.wav}')
