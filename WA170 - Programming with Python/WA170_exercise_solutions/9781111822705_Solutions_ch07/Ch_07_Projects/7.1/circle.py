"""
File: circle.py
Project 7.1

Draws a circle.

1. The inputs are the coourdinates of the center point and the radius.

"""

import math
from turtle import Turtle

def drawCircle(t, x, y, radius):
    """Draws a circle with the given center point and radius."""
    t.up()
    t.goto(x + radius, y)
    t.setheading(90)
    t.down()
    for count in range(120):
        t.left(3)
        t.forward(2.0 * math.pi * radius / 120.0)
    

def main():
    """Allows the user to enter the center point and the radius."""
    x = int(input("Enter the x coordinate of the center point: "))
    y = int(input("Enter the y coordinate of the center point: "))
    radius = int(input("Enter the radius: "))
    drawCircle(Turtle(), x, y, radius)

main()

