from enum import Enum

import pygame

WIDTH, HEIGHT = 1080, 768
SCORE_PER_BLOCK = 100
LOAD_CUSTOM = False
VIRTUAL_PIXEL = 18


class GameState(Enum):
    MENU = 0
    LEVEL = 1
    GAME_OVER = 2
