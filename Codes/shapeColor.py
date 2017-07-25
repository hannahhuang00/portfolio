from turtle import *
import turtle
turtle.penup ()
import math
setx(0)
sety(0)
turtle.penup
begin_fill()
shapeColor = input('What color?')
shapeSides = int(input('How many sides?'))
fillcolor(shapeColor)
pencolor(shapeColor)
turtle.pendown()
for x in range(shapeSides):
    turtle.left(360/shapeSides)
    turtle.fd(800/shapeSides)
end_fill()

exitonclick()
