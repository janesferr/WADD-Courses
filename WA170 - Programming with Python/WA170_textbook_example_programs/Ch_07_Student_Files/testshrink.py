"""
File: testshrink.py
Tests a function for reducing an image's size.
"""

from images import Image

def shrink(image, factor):
    """Builds and returns a new image which is smaller
    copy of the argument image, by the factor argument."""
    width = image.getWidth()
    height = image.getHeight()
    new = Image(width // factor, height // factor)
    oldY = 0
    newY = 0
    while oldY < height - factor:
        oldX = 0
        newX = 0
        while oldX < width - factor:
            oldP = image.getPixel(oldX, oldY)
            new.setPixel(newX, newY, oldP)
            oldX += factor
            newX += 1
        oldY += factor
        newY += 1
    return new

def main(filename = "smokey.gif"):
    image = Image(filename)
    print("Close the image window to continue. ")
    image.draw()
    image2 = shrink(image, 2)
    print("Close the image window to continue. ")
    image2.draw()
    image3 = shrink(image, 3)
    print("Close the image window to continue. ")
    image3.draw()
    print("Close the image window to quit. ")

main()
