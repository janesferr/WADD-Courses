"""
File: newtongui.py
Project 9.3

A GUI-based program for viewing approximations of square roots using
znewton's method.

"""

from tkinter import *
import tkinter.messagebox

class NewtonGUI(Frame):

    def __init__(self):
        """Set up the window, widgets, and data model."""
        Frame.__init__(self)
        self.master.title("Square Root Approximations")
        self.grid()
        self._numVar = DoubleVar()
        self._guessVar = DoubleVar()
        self._numVar.set(0.0)
        self._guessVar.set(0.0)
        self._numLabel = Label(self, text = "Number")
        self._numLabel.grid(row = 0, column = 0)
        self._numEntry = Entry(self, textvariable = self._numVar)
        self._numEntry.grid(row = 1, column = 0)
        self._guessLabel = Label(self, text = "Approximation")
        self._guessLabel.grid(row = 0, column = 1)
        self._guessEntry = Entry(self, textvariable = self._guessVar)
        self._guessEntry.grid(row = 1, column = 1)
        self._resetButton = Button(self, text = "Reset",
                                   command = self._reset)
        self._resetButton.grid(row = 2, column = 0)
        self._guessButton = Button(self, text = "Estimate",
                                   command = self._estimate)
        self._guessButton.grid(row = 2, column = 1)
        # The data model
        self._tolerance = 0.000000001
        self._guess = 0.0
        self._num = 0.0

    def _reset(self):
        """Event handler for the reset button."""
        self._guess = 0.0
        self._num = 0.0
        self._numVar.set(0.0)
        self._guessVar.set(0.0)

    def _estimate(self):
        """Event handler for the etimate button."""
        if self._guess == 0.0:
            # Starting a new process
            self._num = self._numVar.get()
            self._guess = self._num / 2
        elif abs(self._num - self._guess ** 2) <= self._tolerance:
            # Ending a process, can't go further
            tkinter.messagebox(message = "Tolerance reached!",
                               parent = self)
        else:
            # Compute another estimate
            self._guess = (self._guess + self._num / self._guess) / 2
        self._guessVar.set(self._guess)

def main():
    NewtonGUI().mainloop()

main()
