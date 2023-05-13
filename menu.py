import pygame
from settings import WIDTH, HEIGHT, VIRTUAL_PIXEL


class Menu:
    def __init__(self, font):
        self.play_button = font.render('Play', True, (0, 255, 0), (0, 0, 255))
        self.play_button_rect = self.play_button.get_rect()
        # set the center of the rectangular object.
        self.play_button_rect.center = (WIDTH // 2, HEIGHT // 2 - VIRTUAL_PIXEL)

        self.exit_button = font.render('Exit', True, (0, 255, 0), (0, 0, 255))
        self.exit_button_rect = self.exit_button.get_rect()
        # set the center of the rectangular object.
        self.exit_button_rect.center = (WIDTH // 2, HEIGHT // 2 + VIRTUAL_PIXEL)

    def update(self, pos):
        if self.exit_button_rect.collidepoint(pos):
            pygame.quit()
        else:
            self.play_button_rect.collidepoint(pos)
            return 1
        return 0

    def draw(self, screen):
        screen.blit(self.play_button, self.play_button_rect)
        screen.blit(self.exit_button, self.exit_button_rect)
