"""
File: testbandw.py
Tests a function for converting a color image to
black and white.
"""

from images import Image

def blackAndWhite(image):
    """Converts the argument image to black and white."""
    blackPixel = (0, 0, 0)
    whitePixel = (255, 255, 255)
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            average = (r + g + b) / 3
            if average < 128:
                image.setPixel(x, y, blackPixel)
            else:
                image.setPixel(x, y, whitePixel)

def main(filename = "smokey.gif"):
    image = Image(filename)
    print("Close the image window to continue. ")
    image.draw()
    blackAndWhite(image)
    print("Close the image window to quit. ")
    image.draw()

main()
