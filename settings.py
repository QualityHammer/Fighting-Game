import pygame as pg
from os import path

# Game variables
GAME_NAME = 'Title WIP'
VERSION = ' TEST'
TITLE = GAME_NAME + VERSION
WIDTH = 900
HEIGHT = 700
SIZE = (WIDTH, HEIGHT)
CENTER = (WIDTH / 2, HEIGHT / 2)
FPS = 60
DEBUG = True

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)
LBLUE = (0, 0, 245)
LRED = (245, 0, 0)

# Keys
LEFT = pg.K_LEFT
RIGHT = pg.K_RIGHT
DOWN = pg.K_DOWN
UP = pg.K_UP
SPACE = pg.K_SPACE
C = pg.K_c

# Paths
DIR = path.dirname(__file__)
IMG = path.join(DIR, 'img')
FIGHTERS = path.join(IMG, 'fighters')
