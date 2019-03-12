"""
File: foursquares.py

Draws squares in the corners of a turtle window.
One square is black, another is gray, and the
remaining two are in random colors.
"""

from turtle import Turtle
import random

def drawSquare(t, x, y, length):
    t.up()
    t.goto(x, y)
    t.setheading(270)
    t.down()
    for count in range(4):
        t.forward(length)
        t.left(90)

def main():
    t = Turtle()
    t.hideturtle()
    # Length of square
    length = 40
    # Relative distances to corners from origin
    width = t.screen.window_width() // 2
    height = t.screen.window_height() // 2
    # Upper left corner
    drawSquare(t, -width, height, length)
    # Gray
    t.pencolor(127, 127, 127)
    # Lower left corner
    drawSquare(t, -width, length - height, length)
    # First random color
    t.pencolor(random.randint(0, 255),
               random.randint(0, 255),
               random.randint(0, 255))
    # Upper right corner
    drawSquare(t, width - length, height, length)
    # Second random color
    t.pencolor(random.randint(0, 255),
               random.randint(0, 255),
               random.randint(0, 255))
    # Lower right corner
    drawSquare(t, width - length,
               length - height, length)
   
main()
