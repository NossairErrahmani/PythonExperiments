import sys
import time
import pygame
from pygame.locals import *
import random

pygame.init()

fps =12
fpsClock = pygame.time.Clock()

width, height = 900, 600
screen = pygame.display.set_mode((width, height))
black = (0,0,0)
white = (255,255,255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
colors=[black,red,green,blue]

def click_action(files,rows,rec_number):
    w,h=width//files,height//rows
    for i in range (rec_number):
        pygame.draw.rect(screen, random.choice(colors), pygame.Rect(random.randint(0, files) * w, random.randint(0, rows) * h, w, h))


def click_trigger():
    p1, p2, p3 = pygame.mouse.get_pressed()
    if p1:
        click_action(20,20,1)

def drawing():
    click_trigger()

# Game loop.
while True:
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
            pygame.quit()
    # Update.

    drawing()
    click_action(20,20,20)

    pygame.display.flip()
    fpsClock.tick(fps)