from turtle import *
import math
from time import sleep

speed(30)
##Shape around the center point, then ++ the size and angle
def shape(len,sides,angle):
    setheading(angle)
    right(180/sides)
    for i in range(sides):
        forward(len)
        right(360/sides)
    right(180/sides)
    shape(len+10,sides,angle + 5)

shape(10,4,90)
sleep(2)

