"""
File: testshapes.py
Project 8.10

Draws a stick figure and a house using shape classes.

"""

from shapes import Circle, Line, Rectangle
from turtle import Turtle

def main():
    """Draws a house and stick figure."""
    black = (0, 0, 0)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    turtle = Turtle()
    turtle.hideturtle()

    # Draw the stick figure
    face = Circle(100, 0, 10, turtle, black)
    body = Line(100, -10, 100, - 80, turtle, black)
    arms = Line(80, -40, 120, -40, turtle, black)
    leftLeg = Line(100, -80, 80, -100, turtle, black)
    rightLeg = Line(100, -80, 120, -100, turtle, black)
    face.draw()
    body.draw()
    arms.draw()
    leftLeg.draw()
    rightLeg.draw()

    # Draw the house
    front = Rectangle(-180, 0, 120, 60, turtle, black)
    door = Rectangle(-100, -30, 15, 30, turtle, blue)
    roof1 = Line(-180, 0, -160, 20, turtle, red)
    roof2 = Line(-160, 20, -80, 20, turtle, red)
    roof3 = Line(-80, 20, -60, 0, turtle, red)
    front.draw()
    door.draw()
    roof1.draw()
    roof2.draw()
    roof3.draw()

main()

