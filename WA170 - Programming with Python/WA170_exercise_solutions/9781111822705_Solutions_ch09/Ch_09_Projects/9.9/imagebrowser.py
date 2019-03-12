"""
File: imagebrowser.py
Project 9.9

Browser for image (.gif) files.
"""

from tkinter import *
import os
import os.path

class ImageBrowser(Frame):

    def __init__(self):
        """Sets up the window and the widgets."""
        Frame.__init__(self)
        self.master.title("Image Browser")
        self.master.rowconfigure(0, weight = 1)
        self.master.columnconfigure(0, weight = 1)
        self.grid(sticky = W+E+N+S)

        # Set up the pane and add the list box and its
        # scroll bar
        self._listPane = Frame(self)
        self._listPane.grid(row = 0, column = 0,
                            sticky = N+S)
        self._yScroll = Scrollbar(self._listPane,
                                  orient = VERTICAL)
        self._yScroll.grid(row = 0, column = 1,
                           sticky = N+S)
        self._listBox = Listbox(self._listPane,
                                width = 20,
                                height = 10,
                                selectmode = SINGLE,
                                yscrollcommand = \
                                self._yScroll.set)
        self._listBox.grid(row = 0, column = 0,
                           sticky = N+S)
        self._yScroll["command"] = self._listBox.yview

        # Set up the input field, image label, and button
        self._pathVar = StringVar()
        self._input = Entry(self,
                            textvariable = self._pathVar,
                            width = 70)
        self._input.grid(row = 0, column = 1,
                         sticky = N)
        self._imageLabel = Label(self, text = "")
        self._imageLabel.grid(row = 1, column = 1)
        self._goButton = Button(self,
                                  text = "Go",
                                  command = self._go)
        self._goButton.grid(row = 1, column = 0)

        # Configure the list pane to expand
        self.rowconfigure(0, weight = 1)
        self._listPane.rowconfigure(0, weight = 1)

        self._getPathAndFiles()

    def _getPathAndFiles(self):
        """Sets the field and the list box with the path of the cwd
        and the directories and the .gif files in that directory,
        respectively."""
        self._path = os.getcwd()
        self._pathVar.set(self._path)
        fileList = filter(lambda f: ".gif" in f or os.path.isdir(f),
                          os.listdir(self._path))
        index = self._listBox.size() - 1
        while self._listBox.size() > 0:
            self._listBox.delete(index)
            index -= 1
        self._listBox.insert(END, "..")
        for f in fileList:
            self._listBox.insert(END, f)
        self._listBox.activate(0)

    def _go(self):
        """Moves to a directory or shows an image."""
        (index) = self._listBox.curselection()
        item = self._listBox.get(index)
        if os.path.isfile(item):
            # It's a file, so load the image
            self._image = PhotoImage(file = item)
            self._imageLabel["image"] = self._image
        else:
            # It's a directory, so move to it and refresh the view
            os.chdir(item)
            self._getPathAndFiles()
            self._imageLabel["image"] = None
            self._image = None

def main():
    """Instantiate and pop up the window."""
    ImageBrowser().mainloop()

main()
