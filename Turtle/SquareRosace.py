import turtle
import math
from time import sleep
colors = ['teal']
t = turtle.Turtle()
t.screen.bgcolor("azure")
l,sides,angle=100,2.5,5
t.penup()
t.goto(0,100)
t.pendown()
t.speed(30)
for i in range (int(360/angle)):
  newcol=colors[(i//int(sides))%len(colors)]
  t.color(newcol)
  t.forward(l)
  t.right(360/sides)
  if i%sides ==sides-1:
    t.right(angle)
sleep(1)
t.forward(1000)
