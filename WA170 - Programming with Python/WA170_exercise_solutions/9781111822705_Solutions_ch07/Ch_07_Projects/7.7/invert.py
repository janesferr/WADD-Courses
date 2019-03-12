"""
File: invert.py
Project 7.7

Defines and tests a function for inverting images.
"""

from images import Image

def invert(image):
    """Inverts an image to its negative."""
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            image.setPixel(x, y, (255 - r, 255 - g, 255 - b))

def blackAndWhite(image):
    """Converts an image to black and white."""
    blackPixel = (0, 0, 0)
    whitePixel = (255, 255, 255)
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            average = (r + g + b) // 3
            if average < 128:
                image.setPixel(x, y, blackPixel)
            else:
                image.setPixel(x, y, whitePixel)

def grayscale(image):
    """Converts an image to grayscale."""
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            r = int(r * 0.299)
            g = int(g * 0.587)
            b = int(b * 0.114)
            lum = r + g + b
            image.setPixel(x, y, (lum, lum, lum))

def main():
    filename = input("Enter the image file name: ")
    image = Image(filename)
    grayscale(image)
    invert(image)
    image.draw()

main()

