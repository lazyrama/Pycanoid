import pygame
from pygame.time import Clock
from entities import Racket, Ball
from settings import WIDTH, HEIGHT, VIRTUAL_PIXEL
from loader import LevelLoader


class Arcanoid:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), flags=pygame.FULLSCREEN)
        self.racket = Racket()
        self.ball = Ball()
        self.running = True
        self.clock = Clock()
        self.level = LevelLoader()
        font = pygame.font.Font('freesansbold.ttf', 32)
        self.text = font.render('Game Over', True, (0, 255, 0), (0, 0, 255))
        self.textRect = self.text.get_rect()

        # set the center of the rectangular object.
        self.textRect.center = (WIDTH // 2, HEIGHT // 2)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    pygame.display.quit()
                    pygame.quit()
                    quit()
        key = pygame.key.get_pressed()
        if key[pygame.K_a] or key[pygame.K_LEFT]:
            self.racket.x -= 1 * self.clock.get_time()
        if key[pygame.K_d] or key[pygame.K_RIGHT]:
            self.racket.x += 1 * self.clock.get_time()

        if self.racket.colliderect(self.ball):
            if self.ball.x > (self.racket.centerx + VIRTUAL_PIXEL // 2):
                self.ball.y_speed *= -1
                self.ball.x_speed *= -1
                if self.ball.x_speed < 0:
                    self.ball.x_speed -= 0.01
                if self.ball.x_speed > 0:
                    self.ball.x_speed += 0.01

            elif self.ball.x < (self.racket.centerx - VIRTUAL_PIXEL // 2):
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

        is_gameOver = self.ball.update(self.clock.get_time())
        if is_gameOver:
            self.running = False
        for line in self.level.campaign[0]:
            for block in line:
                if self.ball.colliderect(block):
                    block.is_destroyed = True

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.racket.draw(self.screen)
        self.ball.draw(self.screen)
        self.level.draw(self.screen)
        pygame.display.update()

    def run(self):
        while self.running:
            self.update()
            self.draw()
            self.clock.tick(30.0)

        self.screen.fill((0, 0, 0))
        self.screen.blit(self.text, self.textRect)
        pygame.display.update()

        while not self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.display.quit()
                    pygame.quit()
                    quit()


game = Arcanoid()
game.run()
