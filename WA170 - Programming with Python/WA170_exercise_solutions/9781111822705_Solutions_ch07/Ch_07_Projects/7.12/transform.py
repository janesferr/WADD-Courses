"""
File: transform.py
Project 7.12

Defines a transform function that represents a general
pattern for traversing an image and modifying its pixels.

Tests this function by using it to define grayscale and
black and white functions.
"""

from images import Image

    
def transform(image, function):
    """Traverses the image and resets each pixel with the result
    of applying the function to it."""
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            image.setPixel(x, y, function(image.getPixel(x, y)))

def grayscale(image):
    """Converts an image to grayscale using the
    psychologically accurate transformations."""
    
    def change(triple):
        """Converts a pixel to grayscale."""
        (r, g, b) = triple
        r = int(r * 0.299)
        g = int(g * 0.587)
        b = int(b * 0.114)
        lum = r + g + b
        return (lum, lum, lum)
    
    transform(image, change)

def blackAndWhite(image):
    """Converts an image to black and white."""
    
    def change(triple):
        """Converts a pixel to black and white."""
        (r, g, b) = triple
        average = (r + g + b) // 3
        if average < 128:
            return (0, 0, 0)
        else:
            return (255, 255, 255)
        
    transform(image, change)

def main():
    filename = input("Enter the image file name: ")
    image = Image(filename)
    grayscale(image)
    # blackAndWhite(image)
    image.draw()

main()

