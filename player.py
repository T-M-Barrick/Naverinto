import pygame, cons

class Spaceship():

    def __init__(self, x, y, image):

        self.image = image

        '''# Creamos una superficie (rectangular) para dibujar sobre esta. Este cuadrado transparente
        # sólo servirá para dibujar sobre él. La bandera pygame.SRCALPHA indica que vamos a usar transparencia
        self.superficie = pygame.Surface((cons.ANCHO_SUPERFICIE_NAVE, cons.ALTO_SUPERFICIE_NAVE), pygame.SRCALPHA)'''

        # Obtenemos el rectángulo (cuadrado en este caso), objeto de clase Rect, que delimita la imagen.
        # Rect es una clase que es útil para representar posición, tamaño y colisiones de la nave.
        # self.rect nos permitirá manipular y posicionar a self.image.
        # self.rect será el perímetro del rectángulo que encapsula y delimita la imagen.
        self.rect = self.image.get_rect()

        # Serán las coordenadas de la esquina superior izquierda de self.rect
        self.x = x
        self.y = y
    
        self.angle = 0  # Ángulo inicial de la nave
    
    def rotar(self, angle):

        self.angle += angle # Modificamos el ángulo de rotación

        # Nos aseguramos de que self.angle se mantenga entre 0 y 360 (sin incluir el 360)
        if self.angle >= 360:
            self.angle -= 360
        elif self.angle < 0:
            self.angle += 360

    def dibujar(self, screen):

        '''# Limpiamos la superficie cada vez que se dibuja para evitar dejar trazos
        self.superficie.fill((0, 0, 0, 0))

        pygame.draw.rect(self.superficie, cons.VERDE, (0, 0, cons.ANCHO_SUPERFICIE_NAVE, cons.ALTO_SUPERFICIE_NAVE), 10)'''

        # Actualizamos la posición de la nave. Con esta función, las coordenadas (x, y) harán
        # referencia siempre a la esquina superior izquierda de self.rect
        self.rect.topleft = (self.x, self.y)

        # Rotamos la nave
        sprite_rotado = pygame.transform.rotate(self.image, self.angle)


        # Obtenemos el rectángulo del sprite rotado para obtener sus dimensiones
        rect_sprite_rotado = sprite_rotado.get_rect(center=self.rect.center)

        # Finalmente, dibujamos al sprite en la pantalla principal (screen) en el punto rect_sprite_rotado.topleft
        screen.blit(sprite_rotado, rect_sprite_rotado.topleft)
    


    
