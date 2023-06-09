import pygame

from settings import VIRTUAL_PIXEL
from settings import WIDTH, HEIGHT


class Racket(pygame.Rect):
    def __init__(self):
        super().__init__((WIDTH // 2 - 4.5 * VIRTUAL_PIXEL, HEIGHT - VIRTUAL_PIXEL, 9 * VIRTUAL_PIXEL, VIRTUAL_PIXEL))

    def reset(self):
        self.x, self.y = WIDTH // 2 - 3 * VIRTUAL_PIXEL, HEIGHT - VIRTUAL_PIXEL

    def update(self):
        if self.x < 0:
            self.x = 0
        if self.x > (WIDTH - self.width):
            self.x = (WIDTH - self.width)

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, self.width, self.height))
        pass


class Block(pygame.Rect):
    def __init__(self, x, y):
        super().__init__((x, y, VIRTUAL_PIXEL * 4, VIRTUAL_PIXEL))
        self.is_destroyed = False

    def draw(self, screen):
        if not self.is_destroyed:
            pygame.draw.rect(screen, (255, 0, 255), (self.x, self.y, self.width, self.height))


class Ball(pygame.Rect):
    def __init__(self):
        super().__init__(WIDTH // 2 - VIRTUAL_PIXEL // 2, HEIGHT - 2 * VIRTUAL_PIXEL, VIRTUAL_PIXEL, VIRTUAL_PIXEL)
        self.x_speed = 0.35
        self.y_speed = -0.35
        # self.coefficient = 5

    def reset(self):
        self.x, self.y = WIDTH // 2 - VIRTUAL_PIXEL // 2, HEIGHT - 2 * VIRTUAL_PIXEL

    def update(self, delta):
        self.move_ip(self.x_speed * delta, self.y_speed * delta)

        if self.x >= WIDTH - VIRTUAL_PIXEL:
            self.x = WIDTH - VIRTUAL_PIXEL
            self.x_speed *= -1

        if self.x <= 0:
            self.x = 0
            self.x_speed *= -1

        if self.x_speed > 0 and self.x_speed > 1:
            self.x_speed -= 0.01
        elif self.x_speed < 0 and self.x_speed < -1:
            self.x_speed += 0.01

        if self.y >= (HEIGHT - VIRTUAL_PIXEL):
            return 1

        if self.y <= 2 * VIRTUAL_PIXEL:
            self.y_speed *= -1
        return 0

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))
        pass
