"""
File: convertgui.py
Project 9.2

A GUI-based temperature converter.

Converts from degree Fahrenheit to degrees Celsius or
from degree Celsius to degrees Fahrenheit.
"""

from tkinter import *

class ConvertGUI(Frame):

    def __init__(self):
        """Set up the window and widgets."""
        Frame.__init__(self)
        self.master.title("Temperature Converter")
        self.grid()
        self._fahrVar = DoubleVar()
        self._celsiusVar = DoubleVar()
        self._fahrVar.set(32.0)
        self._celsiusVar.set(0.0)
        self._fahrLabel = Label(self, text = "Fahrenheit")
        self._fahrLabel.grid(row = 0, column = 0)
        self._fahrEntry = Entry(self, textvariable = self._fahrVar)
        self._fahrEntry.grid(row = 1, column = 0)
        self._celsiusLabel = Label(self, text = "Celsius")
        self._celsiusLabel.grid(row = 0, column = 1)
        self._celsiusEntry = Entry(self, textvariable = self._celsiusVar)
        self._celsiusEntry.grid(row = 1, column = 1)
        self._toCelsiusButton = Button(self, text = ">>>>",
                                       command = self._toCelsius)
        self._toCelsiusButton.grid(row = 2, column = 0)
        self._toFahrButton = Button(self, text = "<<<<",
                                    command = self._toFahr)
        self._toFahrButton.grid(row = 2, column = 1)

    def _toCelsius(self):
        """Event handler for the toCelsius button."""
        fahr = self._fahrVar.get()
        celsius = (fahr - 32) * 5 / 9
        self._celsiusVar.set(celsius)

    def _toFahr(self):
        """Event handler for the toFahr button."""
        celsius = self._celsiusVar.get()
        fahr = celsius * 9 / 5 + 32
        self._fahrVar.set(fahr)

def main():
    ConvertGUI().mainloop()

main()
