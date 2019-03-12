"""
File: enlarge.py
Project 7.11

Defines and tests a function to enlarge an image.
"""

from images import Image

def enlarge(image, factor):
    """Builds and returns a copy of the image which is larger
    by the factor."""
    oldWidth = image.getWidth()
    oldHeight = image.getHeight()
    new = Image(oldWidth * factor, oldHeight * factor)
    oldY = 0
    newY = 0
    while oldY < oldHeight:
        for countY in range(factor):
            oldLeft = 0
            oldRight = oldWidth - 1
            newLeft = 0
            newRight = new.getWidth() - 1
            while oldLeft < oldRight:
                leftPixel = image.getPixel(oldLeft, oldY)
                rightPixel = image.getPixel(oldRight, oldY)
                for count in range(factor):
                    new.setPixel(newLeft, newY, leftPixel)
                    new.setPixel(newRight, newY, rightPixel)
                    newLeft += 1
                    newRight -= 1
                oldLeft += 1
                oldRight -= 1
            newY += 1
        oldY += 1
    return new

def main():
    filename = input("Enter the image file name: ")
    image = Image(filename)
    print("Close the window to view the changes to the image.")
    image.draw()
    newimage = enlarge(image, 2)
    newimage.draw()

main()

