"""
File: posterize.py
Project 7.5

Defines and tests a function for posterizing images.
"""

from images import Image

def posterize(image, color = (0, 0, 0)):
    """Converts a color image to two-colors,
    one of which it white and the other of which is
    either a default of black or a user-specified
    RGB value."""
    whitePixel = (255, 255, 255)
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            average = (r + g + b) // 3
            if average < 128:
                image.setPixel(x, y, color)
            else:
                image.setPixel(x, y, whitePixel)

def main():
    filename = input("Enter the image file name: ")
    red = int(input("Enter an integer [0..255] for red: "))
    green = int(input("Enter an integer [0..255] for green: "))
    blue = int(input("Enter an integer [0..255] for blue: "))                    
    image = Image(filename)
    posterize(image, (red, green, blue))
    image.draw()

main()

