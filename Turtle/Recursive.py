from turtle import *
import math
from time import sleep

##Shape spiral
def shape(len,sides):
    if len>0:
        for i in range(sides):
            forward(len)
            right(360/sides)
        right(180/sides)
        shape(len-10,sides)

shape(100,4)
sleep(2)

