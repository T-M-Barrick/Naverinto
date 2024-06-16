import pygame, cons

class Forma:

    def __init__(self):
        pass

class Spaceship():

    def __init__(self, x, y):

        # Creamos una superficie (rectangular) para dibujar sobre esta. Este cuadrado transparente
        # sólo servirá para dibujar sobre él. La bandera pygame.SRCALPHA indica que vamos a usar transparencia
        self.superfice = pygame.Surface((cons.LADO_SUPERFICIE, cons.LADO_SUPERFICIE), pygame.SRCALPHA)

        # El cuadrado será transparente
        self.superfice.fill((0, 0, 0, 0))

        # Obtenemos el rectángulo (cuadrado en este caso), objeto de clase Rect, que delimita la imagen.
        # Rect es una clase que es útil para representar posición, tamaño y colisiones de la nave.
        # self.rect nos permitirá manipular y posicionar a self.superficie.
        # self.rect será el perímetro de self.superficie, es decir, la encapsula y delimita.
        self.rect = self.superfice.get_rect()

        # Serán las coordenadas de la esquina superior izquierda de self.superficie o self.rect
        self.x = x
        self.y = y

        # Para cuando inicialicemos la nave, su centro será (x, y)
        self.rect.center = (self.x, self.y)

    def dibujar(self, screen):

        # Limpiamos la superficie cada vez que se dibuja para evitar dejar trazos
        self.superfice.fill((0, 0, 0, 0))

        # Dibujamos un círculo blanco en el centro de la superficie
        pygame.draw.circle(self.superfice, cons.BLUE, (cons.RADIO_CIRC, cons.RADIO_CIRC), cons.RADIO_CIRC)

        # Ahora dibujamos a la superficie que contiene al círculo de color en la pantalla
        screen.blit(self.superfice, self.rect)

        # Actualizamos la posición de la nave. Con esta función, las coordenadas (x, y),
        # a partir de ahora, harán referencia siempre a la esquina superior izquierda de self.rect o self.superficie
        self.rect.topleft = (self.x, self.y)
    
'''class Cannon():

    def __init__(self, spaceship):
        self.image = pygame.Surface((10, 30))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = spaceship.rect.centerx
        self.rect.bottom = spaceship.rect.top

    def dibujar(self, surface):
        surface.blit(self.image, self.rect)'''