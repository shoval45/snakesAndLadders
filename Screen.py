import pygame
import time
import os
import consts

WIN = pygame.display.set_mode((consts.WIDTH,consts.HEIGHT))
pygame.display.set_caption("SNAKES AND LADDERS")

pygame.font.init()

def draw_board():
    WIN.fill(consts.WHITE)
    WIN.blit(consts.GAME_BOARD, (0, 0))
    WIN.blit(consts.PLAYER_RIGHT, (0, 600))
    pygame.display.update()

def draw_grid():
    WIN.fill(consts.WHITE)
    blockSize = 100  # Set the size of the grid block
    for x in range(0, consts.WIDTH, blockSize):
        for y in range(0, consts.HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(WIN, consts.BLACK, rect, 1)
    pygame.display.update()

def draw_lose_message():
    draw_message(consts.LOSE_MESSAGE, consts.LOSE_FONT_SIZE,
                 consts.LOSE_COLOR, consts.LOSE_LOCATION)

def draw_win_message():
    draw_message(consts.WIN_MESSAGE, consts.WIN_FONT_SIZE,
                 consts.WIN_COLOR, consts.WIN_LOCATION)


def draw_message(message, font_size, color, location):
    WIN.fill(consts.WHITE)
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    WIN.blit(text_img, location)

# def draw_game(game_state):
#     draw_board()
#     if game_state["pressed_key_enter"]:
#         draw_grid()
#         time.sleep(1)
#
#     elif game_state["state"] == consts.LOSE_STATE:
#         draw_lose_message()
#         time.sleep(3)
#
#     elif game_state["state"] == consts.WIN_STATE:
#         draw_win_message()
#         time.sleep(3)
#
#     pygame.display.flip()



def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_board()

    pygame.quit()

if __name__ == '__main__':
    main()
