import turtle
import math

t = turtle.Turtle()
l=70
i=0

while(1):
  print(i)
  t.forward(l)
  t.right(120)
  if i%4==0:
    l*=1.2
  i+=1
