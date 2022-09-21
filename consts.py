import pygame
import os

WIDTH = 700
HEIGHT = 700

BLACK = (0,0,0)
WHITE = (255,255,255)

GAME_BOARD_IMAGE = pygame.image.load(os.path.join('Assets', 'game_board.jpg'))
GAME_BOARD = pygame.transform.scale(GAME_BOARD_IMAGE, (700,700))
PLAYER_IMAGE_RIGHT = pygame.image.load(os.path.join('Assets', 'player_right.png'))
PLAYER_RIGHT = pygame.transform.scale(PLAYER_IMAGE_RIGHT, (100,100))
PLAYER_IMAGE_LEFT = pygame.image.load(os.path.join('Assets', 'player_left.png'))
PLAYER_LEFT = pygame.transform.scale(PLAYER_IMAGE_RIGHT, (100,100))

DICE1_IMAGE = pygame.image.load(os.path.join('dice', 'dice1.jpg'))
DICE1 = pygame.transform.scale(DICE1_IMAGE, (100,100))

DICE2_IMAGE = pygame.image.load(os.path.join('dice', 'dice2.jpg'))
DICE2 = pygame.transform.scale(DICE2_IMAGE, (100,100))

DICE3_IMAGE = pygame.image.load(os.path.join('dice', 'dice3.jpg'))
DICE3 = pygame.transform.scale(DICE3_IMAGE, (100,100))

DICE4_IMAGE = pygame.image.load(os.path.join('dice', 'dice4.jpg'))
DICE4 = pygame.transform.scale(DICE4_IMAGE, (100,100))

DICE5_IMAGE = pygame.image.load(os.path.join('dice', 'dice5.jpg'))
DICE5 = pygame.transform.scale(DICE5_IMAGE, (100,100))

DICE6_IMAGE = pygame.image.load(os.path.join('dice', 'dice6.jpg'))
DICE6 = pygame.transform.scale(DICE6_IMAGE, (100,100))



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
