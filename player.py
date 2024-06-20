import pygame, cons

class Forma:

    def __init__(self):
        pass

class Spaceship():

    def __init__(self, x, y):

        # Creamos una superficie (rectangular) para dibujar sobre esta. Este cuadrado transparente
        # sólo servirá para dibujar sobre él. La bandera pygame.SRCALPHA indica que vamos a usar transparencia
        self.superfice = pygame.Surface((cons.LADO_SUPERFICIE_NAVE, cons.LADO_SUPERFICIE_NAVE), pygame.SRCALPHA)

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
    
class Cannon():

    def __init__(self, spaceship):

        self.spaceship = spaceship

        self.superficie = pygame.Surface((cons.LARGO_CANNON, cons.ANCHO_CANNON), pygame.SRCALPHA)

        self.superficie.fill((0, 0, 0, 0))

        self.rect = self.superficie.get_rect()

        self.angle = 0  # Ángulo inicial del cañón

        self.actualizar_posicion()

    def actualizar_posicion(self):
       
       # Alineamos el centro inferior del cañón con el centro de la nave
       rx = cx + cons.LARGO_CANNON/ 2
       ry = cy - cons.ANCHO_CANNON / 2

        
    def rotar(self, angle):

        self.angle += angle # Rotamos el cañón

        # Nos aseguramos de que self.angle se mantenga entre 0 y 360 (sin incluir el 360)
        if self.angle >= 360:
            self.angle -= 360
        elif self.angle < 0:
            self.angle += 360

    def dibujar(self, screen):

        self.actualizar_posicion()

        # Limpiamos la superficie cada vez que se dibuja para evitar dejar trazos
        self.superficie.fill((0, 0, 0, 0))

        # Dibujamos el cañón en self.superficie antes de rotarlo
        pygame.draw.rect(self.superficie, cons.WHITE, (0, 0, cons.LARGO_CANNON, cons.ANCHO_CANNON))
        
        # Esta función toma una superficie y un ángulo en grados, y devuelve una nueva superficie que es una versión rotada de la original
        superficie_rotada = pygame.transform.rotate(self.superficie, self.angle)
        
        # Calculamos el rectángulo rotado y lo posicionamos en el centro de la nave
        rect_rotado = superficie_rotada.get_rect(center=self.rect.center)

        screen.blit(superficie_rotada, rect_rotado)