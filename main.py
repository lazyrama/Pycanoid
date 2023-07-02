# Todo
# * add new levels
# * think about graphics enchantments
# * maybe add bonus for bigger ball?
# * add bonus for multiple balls
# * add bonus stacking
# * add menu for choosing level?
# * add choosing levels file?
# * add saves?
# * add color changing that shows that level is completed
import pygame
from pygame.time import Clock
from entities import Racket, Ball
from settings import WIDTH, HEIGHT, VIRTUAL_PIXEL, GameState
from loader import LevelLoader
from menu import Menu, Level, GameOver, GameEnd

pygame.init()
font = pygame.font.Font('freesansbold.ttf', 32)


class Arcanoid:
    def __init__(self):

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), flags=pygame.SCALED) #pygame.FULLSCREEN |
        self.alpha_surface = pygame.Surface((WIDTH, HEIGHT))
        self.alpha_surface.set_alpha(40)
        self.menu = Menu(font)
        self.game_over = GameOver(font)
        self.game_end = GameEnd(font)

        self.is_game_over = False
        self.level_num = 0
        self.score = 0

        self.racket = Racket()
        self.ball = Ball()
        self.loader = LevelLoader()
        self.level = Level(self.loader, self.level_num, self.score, font)
        self.clock = Clock()

        self.state = GameState.MENU
        self.touched = False

    def is_level_ended(self):
        for line in self.level.level:
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
                if event.key == pygame.K_ESCAPE and self.state == GameState.MENU:
                    pygame.display.quit()
                    pygame.quit()
                    quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
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
                if self.level_num < len(self.loader.campaign):
                    self.level_num += 1
                    self.level.update(self.level_num, self.score, font)
                else:
                    self.state = GameState.END
                self.ball.reset()
                self.racket.reset()

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

            self.is_game_over = self.ball.update(self.clock.get_time())
            if self.is_game_over:
                self.state = GameState.GAME_OVER
            for line in self.level.level:
                for block in line:
                    if self.ball.colliderect(block) and not block.is_destroyed:
                        block.is_destroyed = True
                        self.score += 1
                        self.level.update(self.level_num, self.score, font)

        elif self.state == GameState.GAME_OVER:
            if key[pygame.K_SPACE]:
                self.racket.reset()
                self.ball.reset()
                self.is_game_over = False
                self.score = 0
                self.level.update(self.level_num, self.score, font)

                for line in self.level.level:
                    for block in line:
                        block.is_destroyed = False

                self.state = GameState.LEVEL
            elif key[pygame.K_ESCAPE]:
                self.racket.reset()
                self.ball.reset()
                self.is_game_over = False
                self.score = 0
                self.level.update(self.level_num, self.score, font)

                for line in self.level.level:
                    for block in line:
                        block.is_destroyed = False

                self.state = GameState.MENU

        elif self.state == GameState.END:
            if key[pygame.K_ESCAPE]:
                self.racket.reset()
                self.ball.reset()
                self.is_game_over = False
                self.score = 0

                for line in self.level.level:
                    for block in line:
                        block.is_destroyed = False

                self.level = Level(self.loader, self.level_num, self.score, font)
                self.state = GameState.MENU

    def draw(self):
        if self.state == GameState.MENU:
            self.screen.fill((0, 0, 0))
            self.menu.draw(self.screen)

        if self.state == GameState.LEVEL:
            self.screen.blit(self.alpha_surface, (0, 0))
            self.level.draw(self.screen)
            self.racket.draw(self.screen)
            self.ball.draw(self.screen)

        if self.state == GameState.GAME_OVER:
            self.screen.fill((0, 0, 0))
            self.game_over.draw(self.screen)

        if self.state == GameState.END:
            self.screen.fill((0, 0, 0))
            self.game_end.draw(self.screen)

        pygame.display.update()

    def run(self):
        while True:
            self.update()
            self.draw()
            self.clock.tick(30.0)


game = Arcanoid()
game.run()
