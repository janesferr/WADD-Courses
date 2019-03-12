"""
File: fontdemo.py

Displays text with font attributes.
"""

from tkinter import *
from tkinter.font import *

class FontDemo(Frame):

    def __init__(self):
        """Sets up the window and widgets."""
        Frame.__init__(self)
        self.master.title("Font Demo")
        self.grid()
        font = Font(family = "Verdana",
                    size = 20, slant = "italic")
        self._label = Label(self, font = font,
                            text = "Hello world!")
        self._label.grid()

def main():
    """Instantiate and pop up the window."""
    FontDemo().mainloop()

main()
