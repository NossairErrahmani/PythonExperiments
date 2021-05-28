import sys
import time
import pygame
from pygame.locals import *

pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

width, height = 900, 600
screen = pygame.display.set_mode((width, height))
black = (0,0,0)
white = (255,255,255)

def draw_grid1():
    for i in range(width//20):
        for j in range(height//20):
            if (i+j)%2 == 0:
                pygame.draw.rect(screen, black, pygame.Rect(i*20, j*20, 20, 20))
            else:
                pygame.draw.rect(screen, white, pygame.Rect(i*20, j*20, 20, 20))
def draw_grid2():
    for i in range(width//20):
        for j in range(height//20):
            if (i+j)%2 == 0:
                pygame.draw.rect(screen, white, pygame.Rect(i*20, j*20, 20, 20))
            else:
                pygame.draw.rect(screen, black, pygame.Rect(i*20, j*20, 20, 20))


# Game loop.
while True:
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
            pygame.quit()
    # Update.

    draw_grid1()
    p1, p2, p3 = pygame.mouse.get_pressed()
    if p1:
        draw_grid2()

    pygame.display.flip()
    fpsClock.tick(fps)