
from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(500,300)
x_pos = 0
y_pos = 100
t.setposition(x_pos, y_pos)

### Write your code below:
x_pos = x_pos + 100
t.setposition(x_pos, y_pos)

y_pos = y_pos - 100
t.setposition(x_pos, y_pos)

x_pos = x_pos - 100
t.setposition(x_pos, y_pos)

x_pos = x_pos + 50
y_pos = y_pos - 10
t.setposition(x_pos, y_pos)

x_pos = x_pos + 50
y_pos = y_pos + 10
t.setposition(x_pos, y_pos)
# Close window on click.
exitonclick()
