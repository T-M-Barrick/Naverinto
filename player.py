import pygame, math, cons

class Forma:

    def __init__(self):
        pass

class Spaceship():

    def __init__(self, x, y):

        # Creamos una superficie (rectangular) para dibujar sobre esta. Este cuadrado transparente
        # sólo servirá para dibujar sobre él. La bandera pygame.SRCALPHA indica que vamos a usar transparencia
        self.superfice = pygame.Surface((cons.LADO_SUPERFICIE_NAVE, cons.LADO_SUPERFICIE_NAVE), pygame.SRCALPHA)

        # Obtenemos el rectángulo (cuadrado en este caso), objeto de clase Rect, que delimita la imagen.
        # Rect es una clase que es útil para representar posición, tamaño y colisiones de la nave.
        # self.rect nos permitirá manipular y posicionar a self.superficie.
        # self.rect será el perímetro de self.superficie, es decir, la encapsula y delimita.
        self.rect = self.superfice.get_rect()

        # Serán las coordenadas de la esquina superior izquierda de self.superficie o self.rect
        self.x = x
        self.y = y

    def dibujar(self, screen):

        # Limpiamos la superficie cada vez que se dibuja para evitar dejar trazos
        self.superfice.fill((0, 0, 0, 0))

        # Dibujamos un círculo blanco en el centro de la superficie
        pygame.draw.circle(self.superfice, cons.VERDE, (cons.RADIO_CIRC, cons.RADIO_CIRC), cons.RADIO_CIRC)

        # Ahora dibujamos a la superficie que contiene al círculo de color en la pantalla
        screen.blit(self.superfice, self.rect)

        # Actualizamos la posición de la nave. Con esta función, las coordenadas (x, y),
        # a partir de ahora, harán referencia siempre a la esquina superior izquierda de self.rect o self.superficie
        self.rect.topleft = (self.x, self.y)
    
class Cannon():

    def __init__(self, spaceship):

        self.spaceship = spaceship

        self.superficie = pygame.Surface((cons.ANCHO_CANNON, cons.ALTO_CANNON), pygame.SRCALPHA) 

        self.angle = 0  # Ángulo inicial del cañón

    def spaceship_center(self):
       
       '''Obtenemos el centro de la nave'''
       rx = self.spaceship.rect.centerx
       ry = self.spaceship.rect.centery
       return (rx, ry)
      
    def rotar(self, angle):

        self.angle += angle # Rotamos el cañón

        # Nos aseguramos de que self.angle se mantenga entre 0 y 360 (sin incluir el 360)
        if self.angle >= 360:
            self.angle -= 360
        elif self.angle < 0:
            self.angle += 360

    def dibujar(self, screen):

        self.superficie.fill((0, 0, 0, 0))

        sp_center = self.spaceship_center()

        # Dibujamos el cañón en self.superficie antes de rotarlo.
        # Usamos 0, 0 para indicar que se dibuja en la parte superior izquierda de self.superficie
        pygame.draw.rect(self.superficie, cons.VERDE, (0, 0, cons.ANCHO_CANNON, cons.ALTO_CANNON))
        
        # Esta función toma una superficie y un ángulo en grados, y devuelve una nueva superficie que es una versión rotada de la original
        superficie_rotada = pygame.transform.rotate(self.superficie, self.angle)
        
        # Obtenemos rect_rotado, objeto de clase Rect (rectángulo que delimita a superficie_rotada)
        # y luego posicionamos al centro de su lado izquierdo en la superficie de la nave
        rect_rotado = superficie_rotada.get_rect()
        rect_rotado.center = (sp_center[0] + math.cos(math.radians(self.angle)) * (self.spaceship.rect.width / 2 + cons.ANCHO_CANNON / 2),
                              sp_center[1] - math.sin(math.radians(self.angle)) * (self.spaceship.rect.height / 2 + cons.ANCHO_CANNON / 2))

        # Finalmente, dibujamos superficie_rotada en la pantalla principal (screen) en la posición calculada (rect_rotado)
        screen.blit(superficie_rotada, rect_rotado)