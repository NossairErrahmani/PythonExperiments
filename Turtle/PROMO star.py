import turtle
import math
from time import sleep
t = turtle.Turtle()
t.color('teal')
t.screen.bgcolor("azure")
l,sides=50,8
t.penup()
t.goto(0,100)
t.pendown()
t.speed(3)
angle=360/sides
for i in range(100):
    t.right(angle/2)
    t.forward(100)
    t.left(1.5 * angle)
    t.backward(100)
    t.right(angle/2)
sleep(1)