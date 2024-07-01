import pygame, cons, math

class Spaceship():

    def __init__(self, x, y, image, image_bullet):

        self.image = image
        self.image_bullet = image_bullet

        # Obtenemos el rectángulo (cuadrado en este caso), objeto de clase Rect, que delimita la imagen.
        # Rect es una clase que es útil para representar posición, tamaño y colisiones de la nave.
        # self.rect nos permitirá manipular y posicionar a self.image.
        # self.rect será el perímetro del rectángulo que encapsula y delimita la imagen.
        self.rect = self.image.get_rect()

        # Serán las coordenadas de la esquina superior izquierda de self.rect
        self.x = x
        self.y = y
    
        self.angle = 0  # Ángulo inicial de la nave

        # pygame.time.get_ticks() mide el tiempo absoluto en milisegundos desde
        # el inicio del programa y sirve para calcular diferencias de tiempo, entre otras cosas
        self.ultimo_disparo = pygame.time.get_ticks()

        self.vida = cons.VIDA
    
    def rotar(self, angle):

        self.angle += angle # Modificamos el ángulo de rotación

        # Nos aseguramos de que self.angle se mantenga entre 0 y 360 (sin incluir el 360)
        if self.angle >= 360:
            self.angle -= 360
        elif self.angle < 0:
            self.angle += 360
    
    def disparar(self):
        tiempo = pygame.time.get_ticks()

        # Creamos una nueva bala desde el centro de la nave
        if tiempo - self.ultimo_disparo >= cons.TIEMPO_DISPARO:
            bala = Bullet(self.rect.centerx, self.rect.centery, self, self.image_bullet, self.angle)
            self.ultimo_disparo = pygame.time.get_ticks() # Actualizo el valor de self.ultimo_disparo
            return bala
    
    def update(self):
        if self.vida <= 0:
            print('Game Over') # CAMBIAR!!!!

    def dibujar(self, screen):

        # Actualizamos la posición de la nave. Con esta función, las coordenadas (x, y) harán
        # referencia siempre a la esquina superior izquierda de self.rect
        self.rect.topleft = (self.x, self.y)

        # Rotamos la nave
        sprite_rotado = pygame.transform.rotate(self.image, self.angle)


        # Obtenemos el rectángulo del sprite rotado para obtener sus dimensiones
        rect_sprite_rotado = sprite_rotado.get_rect(center=self.rect.center)

        # Finalmente, dibujamos al sprite en la pantalla principal (screen) en el punto rect_sprite_rotado.topleft
        screen.blit(sprite_rotado, rect_sprite_rotado.topleft)

class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y, nave_disparadora, image, angle):

        super().__init__()

        self.nave = nave_disparadora
        self.angle = angle  # Ángulo de la bala
        self.imagen_original = image
        self.image = pygame.transform.rotate(self.imagen_original, self.angle)
        self.rect = self.image.get_rect(center=(x, y))

        # Movimiento de la bala
        self.dx = math.cos(math.radians(self.angle)) * cons.BULLET_SPEED
        self.dy = -math.sin(math.radians(self.angle)) * cons.BULLET_SPEED

        self.rebotes = 0

    def update(self, nave_enemiga=None):
        '''Sirve para mover la bala y para manejar las colisiones'''

        self.rect.x += self.dx
        self.rect.y += self.dy

        if self.rebote == 3: # La bala solo puede rebotar 2 veces
            # kill() es un método de la clase superior Sprite que elimina a este sprite
            # de todos los grupos de sprites a los que pertenece. Esto permite que la bala se elimine
            # de pantalla y además optimiza el juego eliminando los sprites innecesarios de los grupos
            self.kill()
        
        if self.rect.colliderect(self.nave) and self.rebotes >= 1:
            self.nave.vida -= cons.DAMAGE * 2/3
            self.kill()
        
        if self.rect.colliderect(nave_enemiga):
            nave_enemiga.vida -= cons.DAMAGE
            self.kill()
    
    def dibujar(self, screen):
        screen.blit(self.image, (self.rect.centerx, self.rect.centery))