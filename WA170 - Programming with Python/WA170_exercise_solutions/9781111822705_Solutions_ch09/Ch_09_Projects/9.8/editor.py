"""
File: editor.py
Project 9.8

GUI for text editor program.
"""

from tkinter import *
import tkinter.messagebox
import os.path

class Editor(Frame):

    def __init__(self):
        """Set up the window and widgets."""
        Frame.__init__(self)
        self.master.title("Text Editor")
        self.grid()
        # Input fields
        self._fileLabel = Label(self, text = "Filename")
        self._fileLabel.grid(row = 0, column = 0)
        self._fileVar = StringVar()
        self._fileEntry = Entry(self,
                                textvariable = self._fileVar)
        self._fileEntry.grid(row = 0, column = 1)
        # Command buttons
        self._newBtn = Button(self,
                              text = "New",
                              command = self._newFile)
        self._newBtn.grid(row = 1, column = 0)
        self._openBtn = Button(self,
                              text = "Open",
                              command = self._openFile)
        self._openBtn.grid(row = 1, column = 1)
        self._saveBtn = Button(self,
                              text = "Save",
                              command = self._saveFile)
        self._saveBtn.grid(row = 1, column = 2)
        # Frame for text box and scrollbar
        self._textPane = Frame(self)
        self._textPane.grid(row = 2, column = 0,
                            columnspan = 3,
                            sticky = N+S+E+W)
        self._yScroll = Scrollbar(self._textPane,
                                  orient = VERTICAL)
        self._yScroll.grid(row = 0, column = 1,
                           sticky = N+S)
        self._outputArea = Text(self._textPane,
                                width = 80,
                                height = 20,
                                yscrollcommand = self._yScroll.set)
        self._outputArea.grid(row = 0, column = 0,
                              sticky = W+E+N+S)
        self._yScroll["command"] = self._outputArea.yview

    def _newFile(self):
        self._filename= ""
        self._fileVar.set("")
        self._outputArea.delete("1.0", END)

    def _openFile(self):
        self._filename = self._fileVar.get()
        if os.path.exists(self._filename):
            self._file = open(self._filename, 'r')
            self._outputArea.delete("1.0", END)
            self._outputArea.insert("1.0", self._file.read())
        else:
            tkinter.messagebox.showerror(message = "File does not exist!",
                                         parent = self)


    def _saveFile(self):
        self._filename = self._fileVar.get()
        if self._filename != '':
            self._file = open(self._filename, 'w')
            self._file.write(self._outputArea.get("1.0", END))
            self._file.close()
        else:
            tkinter.messagebox.showerror(message = "Must enter a file name!",
                                         parent = self)

def main():
    Editor().mainloop()

main()

