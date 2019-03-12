"""
File: shapes.py
Project 8.10

Defines classes for line segments, circles, and rectangles using a turtle
object to draw them.

"""

import math

class Shape(object):
    """Represents a shape with a color and a turtle."""

    def __init__(self, turtle, color):
        self._turtle = turtle
        self._color = color

    def getColor(self):
        return self._color

    def setColor(self, color):
        self._color = color
        

class Line(Shape):
    """Represents a line segment."""

    def __init__(self, x1, y1, x2, y2, turtle, color):
        Shape.__init__(self, turtle, color)
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

    def draw(self):
        """Draws a line."""
        (r, g, b) = self._color
        self._turtle.up()
        self._turtle.goto(self._x1, self._y1)
        self._turtle.pencolor(r, g, b)
        self._turtle.down()
        self._turtle.goto(self._x2, self._y2)


class Circle(Shape):
    """Represents a circle."""

    def __init__(self, x, y, radius, turtle, color):
        Shape.__init__(self, turtle, color)
        self._x = x
        self._y = y
        self._radius = radius

    def draw(self):
        """Draws a circle."""
        (r, g, b) = self._color
        amount = 2.0 * math.pi * self._radius / 120.0
        self._turtle.up()
        self._turtle.goto(self._x + self._radius, self._y)
        self._turtle.setheading(90)
        self._turtle.down()
        self._turtle.pencolor(r, g, b)
        for count in range(120):
            self._turtle.left(3)
            self._turtle.forward(amount)

class Rectangle(Shape):
    """Represents a rectangle."""

    def __init__(self, x, y, width, height, turtle, color):
        Shape.__init__(self, turtle, color)
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def draw(self):
        """Draws a rectangle."""
        (r, g, b) = self._color
        self._turtle.up()
        self._turtle.goto(self._x, self._y)
        self._turtle.setheading(0)
        self._turtle.down()
        self._turtle.pencolor(r, g, b)
        self._turtle.forward(self._width)
        self._turtle.left(-90)
        self._turtle.forward(self._height)
        self._turtle.left(-90)
        self._turtle.forward(self._width)
        self._turtle.left(-90)
        self._turtle.forward(self._height)

