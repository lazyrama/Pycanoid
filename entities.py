import pygame

from settings import VIRTUAL_PIXEL
from settings import WIDTH, HEIGHT


class Racket:
    def __init__(self):
        self.x = WIDTH // 2 - 3 * VIRTUAL_PIXEL
        self.y = HEIGHT - VIRTUAL_PIXEL
        self.rect = pygame.Rect(self.x, self.y, 6 * VIRTUAL_PIXEL, VIRTUAL_PIXEL)
        pass

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.rect)
        pass


"""
class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_destroyed = False

    def update(self):
        pass

    def draw(self, screen):
        pygame.draw.rect()
        pass
"""


class Ball:
    def __init__(self):
        self.x = WIDTH // 2 - VIRTUAL_PIXEL // 2
        self.y = HEIGHT - 2 * VIRTUAL_PIXEL
        self.x_speed = 0.35
        self.y_speed = -0.35
        self.coeff = 5
        self.rect = pygame.Rect(self.x, self.y, VIRTUAL_PIXEL, VIRTUAL_PIXEL)
        pass

    def update(self, delta):
        self.rect.x += self.x_speed * delta
        self.rect.y += self.y_speed * delta
        if self.rect.x >= (WIDTH - VIRTUAL_PIXEL) or self.rect.x <= VIRTUAL_PIXEL:
            self.x_speed *= -1
        if self.rect.y >= (HEIGHT - VIRTUAL_PIXEL) or self.rect.y <= VIRTUAL_PIXEL:
            self.y_speed *= -1

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)
        pass
