"""
File: tidbitgui.py
Project 9.6

GUI for tidbit program.

Inputs: purchase price and annual interest rate.
"""

from tkinter import *
from tidbit import Tidbit

class TidbitGUI(Frame):

    def __init__(self):
        """Set up the window and widgets."""
        Frame.__init__(self)
        self.master.title("Tidbit Loan Scheduler")
        self.grid()
        # Input fields
        self._priceLabel = Label(self, text = "Purchase Price")
        self._priceLabel.grid(row = 0, column = 0)
        self._priceVar = DoubleVar()
        self._priceEntry = Entry(self,
                                  textvariable = self._priceVar)
        self._priceEntry.grid(row = 0, column = 1)
        self._rateLabel = Label(self, text = "Annual Interest Rate")
        self._rateLabel.grid(row = 1, column = 0)
        self._rateVar = IntVar()
        self._rateEntry = Entry(self,
                                 textvariable = self._rateVar)
        self._rateEntry.grid(row = 1, column = 1)
        # Command button
        self._button = Button(self,
                              text = "Compute",
                              command = self._computeSchedule)
        self._button.grid(row = 2, column = 0, columnspan = 2)
        # Output text box
        self._outputArea = Text(self,
                                width = 85,
                                height = 21)
        self._outputArea.grid(row = 3, column = 0,
                              columnspan = 2,
                              sticky = W+E+N+S)

    def _computeSchedule(self):
        self._outputArea.delete("1.0", END)
        """Event handler for the Compute button."""
        schedule = str(Tidbit(self._priceVar.get(), self._rateVar.get()))
        self._outputArea.insert("1.0", schedule)

def main():
    TidbitGUI().mainloop()

main()

