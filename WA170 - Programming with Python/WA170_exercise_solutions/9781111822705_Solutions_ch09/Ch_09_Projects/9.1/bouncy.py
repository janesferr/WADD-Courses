"""
File: bouncygui.py
Project 9.1

Determines the distance traveled by a bouncing ball.

Inputs: Initial height, bounciness index, and number of bounces
"""

from tkinter import *

def computeDistance(height, index, bounces):
    """Computes the total distance traveled by the ball,
    given an initial height, bounciness index, and
    number of bounces."""
    total = 0
    for x in range(bounces):
        total += height
        height *= index
        total += height
    return total

class BouncyGUI(Frame):

    def __init__(self):
        """Set up the window and widgets."""
        Frame.__init__(self)
        self.master.title("Bouncy")
        self.grid()
        self._heightLabel = Label(self, text = "Initial height")
        self._heightLabel.grid(row = 0, column = 0)
        self._heightVar = DoubleVar()
        self._heightEntry = Entry(self,
                                  textvariable = self._heightVar)
        self._heightEntry.grid(row = 0, column = 1)
        self._indexLabel = Label(self, text = "Bounciness index")
        self._indexLabel.grid(row = 1, column = 0)
        self._indexVar = DoubleVar()
        self._indexEntry = Entry(self,
                                 textvariable = self._indexVar)
        self._indexEntry.grid(row = 1, column = 1)
        self._bouncesLabel = Label(self, text = "Number of bounces")
        self._bouncesLabel.grid(row = 2, column = 0)
        self._bouncesVar = IntVar()
        self._bouncesEntry = Entry(self,
                                   textvariable = self._bouncesVar)
        self._bouncesEntry.grid(row = 2, column = 1)
        self._button = Button(self,
                              text = "Compute",
                              command = self._computeDistance)
        self._button.grid(row = 3, column = 0, columnspan = 2)
        self._distanceLabel = Label(self, text = "Total distance")
        self._distanceLabel.grid(row = 4, column = 0)
        self._distanceVar = DoubleVar()
        self._distanceEntry = Entry(self,
                                    textvariable = self._distanceVar)
        self._distanceEntry.grid(row = 4, column = 1)

    def _computeDistance(self):
        """Event handler for the Compute button."""
        height = self._heightVar.get()
        index = self._indexVar.get()
        bounces = self._bouncesVar.get()
        distance = computeDistance(height, index, bounces)
        self._distanceVar.set(distance)

def main():
    BouncyGUI().mainloop()

main()

