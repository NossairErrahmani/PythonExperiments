import turtle
import math

##colors = ['blue','magenta','red','orange','lime','green','cyan']
colors = ['blue','red']
t = turtle.Turtle()
t.speed(10)
l,ang,sides=70,0,6
for i in range (100):
  t.forward(l)
  t.right(360/sides)
  if i%sides==0:
    newcol=colors[(i//sides)%len(colors)]
    t.color(newcol)
    l*=1.1
    ang+=1

