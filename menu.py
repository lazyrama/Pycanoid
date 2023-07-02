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


class LevelChooser:
    def __init__(self, font):
        pass

    def update(self):
        pass

    def draw(self, screen):
        pass


class Level:
    def __init__(self, loader, level_num, score, font):
        self.uiFont = font.render(f'Score:{score}  Level:{level_num+1}',
                                  True, (0, 255, 0), (0, 0, 255))
        self.uiRect = self.uiFont.get_rect()
        self.score = 0
        self.level = loader.campaign[level_num].copy()

    def update(self, level_num, score, font):
        self.uiFont = font.render(f'Score:{score}  Level:{level_num+1}',
                                  True, (0, 255, 0), (0, 0, 255))
        self.uiRect = self.uiFont.get_rect()

    def draw(self, screen):
        screen.blit(self.uiFont, self.uiRect)
        for line in self.level:
            for block in line:
                block.draw(screen)


class GameOver:
    def __init__(self, font):
        self.uiFont = font.render('Game Over. To restart press SPACE. To exit to menu press ESC.',
                                    True, (0, 255, 0), (0, 0, 255))
        self.uiRect = self.uiFont.get_rect()
        # set the center of the rectangular object.
        self.uiRect.center = (WIDTH // 2, 8 * VIRTUAL_PIXEL)

    def draw(self, screen):
        screen.blit(self.uiFont, self.uiRect)


class GameEnd:
    def __init__(self, font):
        self.uiFont = font.render('Game End. Congratulations! Thank you for walkthrough',
                                   True, (0, 255, 0), (0, 0, 255))
        self.uiRect = self.uiFont.get_rect()
        # set the center of the rectangular object.
        self.uiRect.center = (WIDTH // 2, 8 * VIRTUAL_PIXEL)

        self.uiFont2 = font.render('To exit to menu press ESC.', True, (0, 255, 0), (0, 0, 255))
        self.uiRect2 = self.uiFont2.get_rect()
        # set the center of the rectangular object.
        self.uiRect2.center = (WIDTH // 2, 11 * VIRTUAL_PIXEL)

    def draw(self, screen):
        screen.blit(self.uiFont, self.uiRect)
        screen.blit(self.uiFont2, self.uiRect2)
