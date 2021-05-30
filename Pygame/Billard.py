import sys
import time
import pygame
from pygame.locals import *
import random
import math
from playsound import  playsound
import threading

def sound(filename):
    threading.Thread(target=playsound, args=(filename,), daemon=True).start()

pygame.init()

fps =60
fpsClock = pygame.time.Clock()

width, height = 1200, 600
screen = pygame.display.set_mode((width, height))
black = (0,0,0)
white = (255,255,255)
red = (255, 0, 0)
green = (0, 155, 0)
blue = (0, 0, 255)
colors=[black,red,green,blue]

ballpos=(width//2,height//2)
clickpos=(0,0)
speed_amount=9
speed = [speed_amount,speed_amount]
radius = 20

def getPos():
    pos = pygame.mouse.get_pos()
    return (pos)

def draw_ball(pos,radius):
    pygame.draw.circle(screen, white, pos, radius)

def ball_angle(ballposition, clickposition):
    dx = ballposition[0] - clickposition[0]
    dy = ballposition[1] - clickposition[1]
    dist= math.sqrt(math.pow(dx,2)+math.pow(dy,2))
    return(dx/dist, dy/dist)

def update_ball(ballposition, delta):
    return (ballposition[0]+delta[0],ballposition[1]+delta[1])

def hit_bounds(ballposition,radius,speedvector,w,h):
    if (ballposition[0]-radius<0) or (ballposition[0]+radius>w):
        sound('BillardSounds/bound.wav')
        return (-speedvector[0],speedvector[1])

    if (ballposition[1] - radius < 0) or (ballposition[1] + radius > h):
        sound('BillardSounds/bound.wav')
        return (speedvector[0], -speedvector[1])
    return speedvector

def dist_two_points(ballposition, targetposition):
    return math.sqrt(math.pow(ballposition[0]-targetposition[0],2)+math.pow(ballposition[1]-targetposition[1],2))

delta=(0,0)


def targets_level(n):
    target_activation={}
    target_list=[]
    for i in range(n):
        t=(random.randint(target_radius,width-target_radius),random.randint(target_radius,height-target_radius))
        while t in target_list:
            t = (random.randint(target_radius, width - target_radius), random.randint(target_radius, height - target_radius))
        target_list.append(t)
    for t in target_list:
        target_activation[t]=1
    return target_list,target_activation

target_radius = 10
target_activation = {}
level = 2
level_done = 1

# Game loop.
while True:
    screen.fill(black)
    delta = hit_bounds(ballpos, radius, delta, width, height)
    ballpos=(ballpos[0]+delta[0],ballpos[1]+delta[1])
    draw_ball(ballpos,radius)

    if level_done==1:
        targets,target_activation=targets_level(level)
        level+=1
        level_done=0

    for targ in targets:
        if dist_two_points(ballpos,targ) < radius + target_radius and target_activation[targ]==1:
            target_activation[targ]=0
            sound('BillardSounds/bling.wav')
        if target_activation[targ]==1:
            draw_ball(targ,target_radius)

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            angle = ball_angle(ballpos, getPos())
            delta = (angle[0] * speed[0], angle[1] * speed[1])
            sound('BillardSounds/go.wav')
        if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            angle = ball_angle(ballpos, getPos())
            delta = (- angle[0] * speed[0],- angle[1] * speed[1])
            sound('BillardSounds/back.wav')

    score=0
    for t in targets:
        score+=target_activation[t]
    if score == 0:
        level_done=1
        sound('BillardSounds/win.wav')

    # Update.


    pygame.display.flip()
    fpsClock.tick(fps)