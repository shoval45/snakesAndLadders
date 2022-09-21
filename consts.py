import pygame
import os

WIDTH = 700
HEIGHT = 700

BLACK = (0,0,0)
WHITE = (255,255,255)

PLAYER_IMAGE_RIGHT = pygame.image.load(os.path.join('Assets', 'snake1.png'))
PLAYER_RIGHT = pygame.transform.scale(PLAYER_IMAGE_RIGHT, (100,100))
PLAYER_IMAGE_LEFT = pygame.image.load(os.path.join('Assets', 'snake1.png'))
PLAYER_LEFT = pygame.transform.scale(PLAYER_IMAGE_RIGHT, (100,100))



FONT_NAME = "Calibri"

LOSE_MESSAGE = "You Lost!"
LOSE_FONT_SIZE = int(0.15 * WIDTH)
LOSE_COLOR = BLACK
LOSE_LOCATION = \
    (0.2 * WIDTH, HEIGHT / 2 - (LOSE_FONT_SIZE / 2))

WIN_MESSAGE = "You Won!"
WIN_FONT_SIZE = LOSE_FONT_SIZE
WIN_COLOR = (89, 89, 89)
WIN_LOCATION = \
    (0.2 * WIDTH, HEIGHT / 2 - (WIN_FONT_SIZE / 2))
LENGTH_GRID = 7
RUNNING_STATE = 1
LOSE_STATE = 2
WIN_STATE = 3
