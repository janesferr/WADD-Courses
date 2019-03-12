"""
File: mondrian.py
Project 7.4

This program displays a Mondrian-like painting with 
the user's input level.
"""

from turtle import Turtle
import random

def fillRectangle(t, x1, y1, x2, y2):
    """Fills a rectangle with the given corner points
    using a random color."""
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    t.pencolor(red, green, blue)
    t.fillcolor(red, green, blue)
    t.begin_fill()
    t.up()
    t.goto(x1, y1)
    t.down()
    t.goto(x2, y1)
    t.goto(x2, y2)
    t.goto(x1, y2)
    t.goto(x1, y1)
    t.end_fill()

def mondrian(t, x1, y1, x2, y2, level):
    """Draws a Mondrian-like painting at the given level."""
    if level > 0:
        fillRectangle(t, x1, y1, x2, y2)

        vertical = random.randint(1, 2)
   
        if vertical == 1:   # Vertical split
            mondrian(t, x1, y1, (x2 - x1) / 3 + x1, y2,
                     level - 1)
            mondrian(t, (x2 - x1) / 3 + x1, y1, x2, y2, 
                     level - 1)

        else:               # Horizontal split

            mondrian(t, x1, y1, x2, (y2 - y1) / 3 + y1, 
                     level - 1)
            mondrian(t, x1, (y2 - y1) / 3 + y1, x2, y2, 
                     level - 1)

def main():
    level = int(input("Enter the level: "))
    t = Turtle()
    t.hideturtle()
    width = t.screen.window_width() // 2
    height = t.screen.window_height() // 2    
    mondrian(t, -width, height,
             width, -height, level)

main()

