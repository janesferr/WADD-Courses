"""
File: colorfilter.py
Project 7.9

Defines and tests a function for color filtering.  Uses this
function to define functions for lightening and darkening images.
"""

from images import Image

def colorFilter(image, rgbTriple):
    """Adds the given rgb values to each pixel after normalizing."""
    
    def baseValue(value, offset):
        """Normalizes value so that 0 <= value <= 255."""
        if offset == 0:
            return value
        elif offset < 0:
            return max(value + offset, 0)
        else:
            return min(value + offset, 255)
        
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            r = baseValue(r, rgbTriple[0])
            g = baseValue(g, rgbTriple[1])
            b = baseValue(b, rgbTriple[2])
            image.setPixel(x, y, (r, g, b))

def lighten(image, amount):
    """Lightens image by amount."""
    colorFilter(image, (amount, amount, amount))

def darken(image, amount):
    """Darkens image by amount."""
    colorFilter(image, (-amount, -amount, -amount))

def main():
    filename = input("Enter the image file name: ")
    image = Image(filename)
    print("Close the window to view the changes to the image")
    image.draw()
    lighten(image, 20)
    # darken(image, 20)
    image.draw()

main()

