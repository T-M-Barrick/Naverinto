import pygame, sys
import random
#INICIALIZO PYGAME
pygame.init()

size = (500, 400)

#CREAR PANTALLA
screen_width = 500
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mi PRIMER JUEGO")

#DEFINO COLORES
BLACK   = (   0,   0,   0)
WHITE   = ( 255, 255, 255)
GREEN   = (   0, 255,   0)
RED     = ( 255,   0,   0)
BLUE    = (   0,   0, 255)


HC74225 = (199, 66, 37)
H61CD35 = (97, 205, 53)

#RELOJ
clock = pygame.time.Clock()
#COLOR DE FONDO
screen.fill(WHITE)


# JUGADOR

player_size = 50
player_color = BLUE
player_x = 50
player_y = screen_height // 2
player_speed = 5

# IA
class Enemy:
    def __init__(self, x, y, size, color, speed):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.speed = speed
        self.direction = random.choice(['up', 'down'])
        self.shoot_cooldown = 0

    def move(self):
        if self.direction == 'up':
            self.y -= self.speed
            if self.y <= 0:
                self.direction = 'down'
        else:
            self.y += self.speed
            if self.y >= screen_height - self.size:
                self.direction = 'up'

    def shoot(self, bullets):
        if self.shoot_cooldown == 0:
            bullet = pygame.Rect(self.x - 10, self.y + self.size // 2 - 5, 10, 10)
            bullets.append((bullet, 'left'))
            self.shoot_cooldown = 60  # Cooldown para disparar
        else:
            self.shoot_cooldown -= 1

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

# Inicializar enemigo IA
enemy = Enemy(screen_width - 100, screen_height // 2, player_size, RED, 3)

# Balas
bullets = []
bullet_speed = 10

# Obstáculos
obstacles = [
    pygame.Rect(300, 150, 50, 300),
    pygame.Rect(500, 150, 50, 300)
]

# Puntuaciones
score1 = 0
score2 = 0
font = pygame.font.Font(None, 74)













