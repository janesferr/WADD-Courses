"""
File: sharpen.py
Project 7.10

Defines and tests a function to sharpen an image.
"""

from images import Image

def sharpen(image, degree, threshold):
    """Builds and returns a sharpened image.  Expects an image
    and two integers (the degree to which the image should be sharpened and the
    threshold used to detect edges) as arguments."""
    
    def average(triple):
        """Returns the average of the values in the tuple."""
        (r,g,b) = triple
        return (r+g+b) // 3
    
    new = image.clone()                     # Make changes to a copy
    for y in range(image.getHeight() - 1):  # Work inside the borders
        for x in range(1, image.getWidth()):
            # Obtain average values of current, left, and
            # bottom pixels
            oldPixel = image.getPixel(x, y)
            leftPixel = image.getPixel(x - 1, y)
            bottomPixel = image.getPixel(x, y + 1)
            oldLum = average(oldPixel)
            leftLum = average(leftPixel)
            bottomLum = average(bottomPixel)
            # Detect an edge at current pixel
            if abs(oldLum - leftLum) > threshold or \
               abs(oldLum - bottomLum) > threshold:
                # Darken that edge
                new.setPixel(x, y,
                             (max(oldPixel[0] - degree, 0),
                              max(oldPixel[1] - degree, 0),
                              max(oldPixel[2] - degree, 0)))
    return new

def main():
    filename = input("Enter the image file name: ")
    image = Image(filename)
    print("Close the window to view the changes to the image.")
    image.draw()
    newimage = sharpen(image, 20, 15)
    newimage.draw()

main()

