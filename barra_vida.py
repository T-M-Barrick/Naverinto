import pygame, cons

class BarraVida:

    def __init__(self, posicion, ancho, alto, color, vida=cons.VIDA, es_enemigo=False):
        
        self.rect = pygame.Rect(posicion[0],posicion[1], ancho, alto)
        self.ancho = ancho
        self.color = color
        self.vida = vida
        self.es_enemigo = es_enemigo

    def dibujar(self, screen, vida_nave):
        # Calcular el ancho de la barra de vida actual basado en la vida restante
        cant_vida = int((vida_nave / self.vida) * self.ancho)

        # Dibujamos la barra de fondo
        pygame.draw.rect(screen, cons.YELLOW, self.rect)

        # Dibujamos la barra de vida actual
        if self.es_enemigo is False:
            pygame.draw.rect(screen, self.color, (self.rect.x, self.rect.y, cant_vida, self.rect.size[1]))
        else:
            dif = self.vida - cant_vida
            pygame.draw.rect(screen, self.color, (self.rect.x + dif, self.rect.y, cant_vida, self.rect.size[1]))