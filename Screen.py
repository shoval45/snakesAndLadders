import pygame
import consts

WINDOW = pygame.display.set_mode((consts.WIDTH,consts.HEIGHT))
pygame.display.set_caption("SNAKES AND LADDERS")

def draw_grid(player_soldier):
    WINDOW.fill(consts.BLACK)
    blockSize = 20  # Set the size of the grid block
    for x in range(0, consts.WIDTH, blockSize):
        for y in range(0, consts.HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(WINDOW, consts.GREEN, rect, 1)
    WINDOW.blit(consts.SOLDIER, (player_soldier.x, player_soldier.y))
    pygame.display.update()

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.quit():
                run = False
    pygame.quit()

if __name__ == '__main__':
    main()
