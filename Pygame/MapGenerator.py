import sys
import time
import pygame
from pygame.locals import *
import random
from copy import copy


pygame.init()

fps =240
fpsClock = pygame.time.Clock()

width, height = 900, 600
screen = pygame.display.set_mode((width, height))

black = (0,0,0)
white = (255,255,255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

colors=[green,blue]
color_weights_land=[97,3]
color_weights_water=[25,75]

f,r=100,100

points=[[f//2,r//2]]
point_colors={tuple(i):green for i in points}


def add_point(points): #Add an adjacent point to a random existing point
    starting_point = random.choice(points)
    new_point = copy(starting_point)
    while(new_point in points): #we'll avoid adding an already existing point
        starting_point = random.choice(points)
        xy = random.choice([0, 1])
        delta = random.choice([-1, +1])
        new_point = copy(starting_point)
        new_point[xy] += delta #xy and delta let us decide whether we add the new point up, down, left or right
    if point_colors[tuple(starting_point)]==green:
        point_colors[tuple(new_point)]=random.choices(colors,weights=color_weights_land,k=1)[0]
    else:
        point_colors[tuple(new_point)] = random.choices(colors, weights=color_weights_water, k=1)[0]
    points.append(new_point)
    return points

def drawing(files,rows,points):
    points=add_point(points)
    print(points)
    w,h=width//files,height//rows
    for p in points:
        pygame.draw.rect(screen,point_colors[tuple(p)], pygame.Rect(p[0] * w, p[1] * h, w, h))


frame = 0
# Game loop.
while True:
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
            pygame.quit()
    # Update.

    drawing(f,r,points)
    frame+=1
    if frame == 1000 :
        pygame.image.save(screen,'map.jpg')
        sys.exit()
        pygame.quit()
    pygame.display.flip()
    fpsClock.tick(fps)

#Analyze 'enclosed spots', see the evolution of the number of enclosed spots as the creature grows
#Can be used as a 'map generator'. Can be modified to have land and water colors where each water spot has more
# probability of spawning a nearby water spot, in order to create rivers and lakes etc
