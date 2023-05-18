import pygame
from pygame.time import Clock
from entities import Racket, Ball
from settings import WIDTH, HEIGHT, VIRTUAL_PIXEL, GameState
from loader import LevelLoader
from menu import Menu

pygame.init()
font = pygame.font.Font('freesansbold.ttf', 32)


class Arcanoid:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), flags=pygame.FULLSCREEN | pygame.SCALED)
        self.alpha_surface = pygame.Surface((WIDTH, HEIGHT))
        self.alpha_surface.set_alpha(40)
        self.menu = Menu(font)

        self.racket = Racket()
        self.ball = Ball()
        self.loader = LevelLoader()
        self.level_num = 2
        self.clock = Clock()

        self.score = 0
        self.scoreFont = font.render('{}'.format(self.score), True, (0, 255, 0), (0, 0, 255))
        self.scoreRect = self.scoreFont.get_rect()

        self.game_over = font.render('Game Over, press space for replaying, esc for exiting', True, (0, 255, 0),
                                     (0, 0, 255))
        self.game_overRect = self.game_over.get_rect()
        # set the center of the rectangular object.
        self.game_overRect.center = (WIDTH // 2, HEIGHT // 2)

        self.state = GameState.MENU
        self.touched = False

    def is_level_ended(self):
        for line in self.loader.campaign[self.level_num]:
            for block in line:
                if not block.is_destroyed:
                    return 0
        return 1

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.display.quit()
                    pygame.quit()
                    quit()
            elif event.type == pygame.MOUSEBUTTONDOWN: # and self.racket.collidepoint(event.pos):
                self.touched = True
                pygame.mouse.get_rel()
            elif event.type == pygame.MOUSEBUTTONUP:
                self.touched = False
                if self.menu.update(pygame.mouse.get_pos()) and self.state == GameState.MENU:
                    self.state = GameState.LEVEL

        key = pygame.key.get_pressed()
        if self.state == GameState.LEVEL:
            if self.is_level_ended():
                self.score = 0
                self.level_num += 1
                self.racket.x, self.racket.y = WIDTH // 2 - 3 * VIRTUAL_PIXEL, HEIGHT - VIRTUAL_PIXEL
                self.ball.x, self.ball.y = WIDTH // 2 - VIRTUAL_PIXEL // 2, HEIGHT - 2 * VIRTUAL_PIXEL

            if self.touched:
                self.racket.move_ip(pygame.mouse.get_rel()[0], 0)

            if key[pygame.K_a] or key[pygame.K_LEFT]:
                self.racket.x -= 1 * self.clock.get_time()
            if key[pygame.K_d] or key[pygame.K_RIGHT]:
                self.racket.x += 1 * self.clock.get_time()
            self.racket.update()

            if self.racket.colliderect(self.ball):
                if self.ball.x > (self.racket.centerx + VIRTUAL_PIXEL // 2) and self.ball.x_speed < 0:
                    self.ball.y_speed *= -1
                    self.ball.x_speed *= -1
                    if self.ball.x_speed < 0:
                        self.ball.x_speed -= 0.01
                    if self.ball.x_speed > 0:
                        self.ball.x_speed += 0.01

                elif self.ball.x < (self.racket.centerx - VIRTUAL_PIXEL // 2) and self.ball.x_speed > 0:
                    self.ball.y_speed *= -1
                    self.ball.x_speed *= -1
                    if self.ball.x_speed < 0:
                        self.ball.x_speed -= 0.01
                    if self.ball.x_speed > 0:
                        self.ball.x_speed += 0.01
                else:
                    self.ball.y_speed *= -1
            else:
                if self.ball.x_speed > 0 and self.ball.x_speed > 1:
                    self.ball.x_speed -= 0.01
                elif self.ball.x_speed < 0 and self.ball.x_speed < -1:
                    self.ball.x_speed += 0.01

            is_game_over = self.ball.update(self.clock.get_time())
            if is_game_over:
                self.state = GameState.GAME_OVER
            for line in self.loader.campaign[self.level_num]:
                for block in line:
                    if self.ball.colliderect(block) and not block.is_destroyed:
                        block.is_destroyed = True
                        self.score += 1

            self.scoreFont = font.render('{}'.format(self.score), True, (0, 255, 0), (0, 0, 255))
            self.scoreRect = self.scoreFont.get_rect()

        elif self.state == GameState.GAME_OVER:
            if key[pygame.K_SPACE]:
                self.state = GameState.LEVEL
                self.score = 0
                self.racket.x, self.racket.y = WIDTH // 2 - 3 * VIRTUAL_PIXEL, HEIGHT - VIRTUAL_PIXEL
                self.ball.x, self.ball.y = WIDTH // 2 - VIRTUAL_PIXEL // 2, HEIGHT - 2 * VIRTUAL_PIXEL
                self.loader = LevelLoader()

    def draw(self):
        # self.screen.fill((0, 0, 0))
        if self.state == GameState.MENU:
            self.menu.draw(self.screen)

        if self.state == GameState.LEVEL:
            self.screen.blit(self.alpha_surface, (0, 0))
            self.screen.blit(self.scoreFont, self.scoreRect)

            self.racket.draw(self.screen)
            self.ball.draw(self.screen)
            self.loader.draw(self.screen, self.level_num)

        if self.state == GameState.GAME_OVER:
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.game_over, self.game_overRect)

        pygame.display.update()

    def run(self):
        print(self.is_level_ended())
        while True:
            self.update()
            self.draw()
            self.clock.tick(30.0)


game = Arcanoid()
game.run()
