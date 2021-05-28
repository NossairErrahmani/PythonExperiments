import sys
import time
import pygame
from pygame.locals import *
import random
from copy import copy

pygame.init()

fps =60
fpsClock = pygame.time.Clock()

width, height = 900, 600
screen = pygame.display.set_mode((width, height))
black = (0,0,0)
white = (255,255,255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
colors=[green,blue]
color_weights=[90,10]
f,r=50,50
points=[[f//2,r//2]]

def add_point(points):
    starting_point = random.choice(points)
    new_point = copy(starting_point)
    while(new_point in points):
        starting_point = random.choice(points)
        xy = random.choice([0, 1])
        delta = random.choice([-1, +1])
        new_point = copy(starting_point)
        new_point[xy] += delta
    points.append(new_point)
    return points

def drawing(files,rows,points):
    points=add_point(points)
    print(points)
    w,h=width//files,height//rows
    for p in points:
        col=random.choices(colors,weights=color_weights,k=1)
        pygame.draw.rect(screen, col[0], pygame.Rect(p[0] * w, p[1] * h, w, h))



# Game loop.
while True:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
            pygame.quit()
    # Update.

    drawing(f,r,points)

    pygame.display.flip()
    fpsClock.tick(fps)

#Analyze 'enclosed spots', see the evolution of the number of enclosed spots as the creature grows
#Can be used as a 'map generator'. Can be modified to have land and water colors where each water spot has more
# probability of spawning a nearby water spot, in order to create rivers and lakes etc
