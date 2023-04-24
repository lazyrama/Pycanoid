import pygame
from entities import Racket, Ball
from settings import WIDTH, HEIGHT
class Arcanoid:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT), flags=pygame.SCALED)
		self.racket = Racket()
		self.ball = Ball()
		self.running = True
		pass
	def update(self):
		pass
	def draw(self):
		self.screen.fill((0, 0, 0))
		self.racket.draw(self.screen)
		self.ball.draw(self.screen)
		pygame.display.update()
	def run(self):
		while self.running:
			self.draw()

game = Arcanoid()
game.run()