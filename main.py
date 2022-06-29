import turtle
from turtle import *
import colorsys

turtle.color("white")
speed(-40)
pensize(3)
bgcolor('black')
hue = 0.0

for i in range(250):
    col = colorsys.hsv_to_rgb(hue, 0.9, 1)
    pencolor(col)
    hue += 0.003
    circle(5-i, 100)
    lt(110)
    circle(5-i, 100)
    rt(900)
done()
