import pygame
from pygame.time import Clock as clock
from entities import Racket, Ball
from settings import WIDTH, HEIGHT
from loader import LevelLoader


class Arcanoid:
	def __init__(self):
		pygame.init() #
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT), flags=pygame.FULLSCREEN)
		self.racket = Racket()
		self.ball = Ball()
		self.running = True
		self.clock = clock()
		self.level = LevelLoader()
		pass

	def update(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()

		key = pygame.key.get_pressed()
		if key[pygame.K_a] or key[pygame.K_LEFT]:
			self.racket.rect.left -= 1 * self.clock.get_time()
		if key[pygame.K_d] or key[pygame.K_RIGHT]:
			self.racket.rect.right += 1 * self.clock.get_time()

		if self.racket.rect.colliderect(self.ball.rect):
			self.ball.y_speed *= -1
			self.ball.x_speed *= -1

		#self.racket.update()
		self.ball.update(self.clock.get_time())

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


game = Arcanoid()
game.run()
