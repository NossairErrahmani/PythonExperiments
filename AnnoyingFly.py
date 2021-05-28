import sys
import time
import pygame
from pygame.locals import *
import random

pygame.init()

fps = 120
fpsClock = pygame.time.Clock()

buzzing = 1
squishing =1

flywconst,flyhconst = 40,40
flyw,flyh = 40,40

width, height = 900, 600
screen = pygame.display.set_mode((width, height))
black = (0,0,0)
white = (255,255,255)
x,y=300,300
def drawing(x,y,a,b):
    pygame.draw.rect(screen, white, pygame.Rect(x, y, a, b))
dx,dy=0,0
while True:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
            pygame.quit()

    drawing(x,y,flyw,flyh)
    x=x+random.randint(-buzzing,buzzing)
    y=y+random.randint(-buzzing,buzzing)
    if flyw < flywconst:
        flyw += 2
    if flyh < flyhconst:
        flyh += 2
    if flyw > flywconst:
        flyw += -2
    if flyh > flyhconst:
        flyh += -2

    p1, p2, p3 = pygame.mouse.get_pressed()
    if p1:
        dx = list(pygame.mouse.get_pos())[0]-x
        dy = list(pygame.mouse.get_pos())[1]-y
        x+=dx//50
        y+=dy//50
        if flyw > flywconst // 2:
            flyw += abs(dx) // 140
        if flyh>flyhconst//2:
            flyh += abs(dy) // 140

    pygame.display.flip()
    fpsClock.tick(fps)