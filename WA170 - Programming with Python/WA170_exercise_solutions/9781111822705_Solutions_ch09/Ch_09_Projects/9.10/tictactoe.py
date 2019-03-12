"""
File: tictactoe.py
Project 9.10

Plays the game of tic tac toe with the user.
"""

from tkinter import *
import tkinter.messagebox
import random

class TicTacToe(Frame):

    def __init__(self):
        """Set up the window and widgets."""
        Frame.__init__(self)
        self.master.title("Tic Tac Toe")
        self.master.geometry("200x200")
        self.master.resizable(0, 0)
        self.grid()
        # A list of buttons for the marks
        self._buttons = []
        for row in range(3):
            for column in range(3):
                b = Button(self, text = "")
                b.grid(row = row, column = column)
                self._buttons.append(b)
        self._buttons[0]["command"] = self._one
        self._buttons[1]["command"] = self._two
        self._buttons[2]["command"] = self._three
        self._buttons[3]["command"] = self._four
        self._buttons[4]["command"] = self._five
        self._buttons[5]["command"] = self._six
        self._buttons[6]["command"] = self._seven
        self._buttons[7]["command"] = self._eight
        self._buttons[8]["command"] = self._nine
        self._reset = Button(self, text = "Reset",
                             command = self._clear)
        self._reset.grid(row = 3, column = 0, columnspan = 3)
        self._yourMark = "X"
        self._myMark ="O"

    def _yourMove(self, index):
        """Attempts to place your mark.  If successful,
        checks for a win and displays if so.  If no win,
        places my mark."""
        if self._buttons[index]["text"] == "":
            self._buttons[index]["text"] = self._yourMark
            if self._hasWon(self._yourMark):
                tkinter.messagebox.showinfo(message = "You win!",
                                            parent = self)
            else:
                self._myMove()
                if self._hasWon(self._myMark):
                    tkinter.messagebox.showinfo(message = "I win!",
                                                parent = self)

    def _hasWon(self, mark):
        """Returns True if the player with mark has won
        or False otherwise."""
        return self._buttons[0]["text"] == mark and \
               self._buttons[1]["text"] == mark and \
               self._buttons[2]["text"] == mark or \
               self._buttons[3]["text"] == mark and \
               self._buttons[4]["text"] == mark and \
               self._buttons[5]["text"] == mark or \
               self._buttons[6]["text"] == mark and \
               self._buttons[7]["text"] == mark and \
               self._buttons[8]["text"] == mark or \
               self._buttons[0]["text"] == mark and \
               self._buttons[3]["text"] == mark and \
               self._buttons[6]["text"] == mark or \
               self._buttons[1]["text"] == mark and \
               self._buttons[4]["text"] == mark and \
               self._buttons[7]["text"] == mark or \
               self._buttons[2]["text"] == mark and \
               self._buttons[5]["text"] == mark and \
               self._buttons[8]["text"] == mark or \
               self._buttons[0]["text"] == mark and \
               self._buttons[4]["text"] == mark and \
               self._buttons[8]["text"] == mark or \
               self._buttons[6]["text"] == mark and \
               self._buttons[4]["text"] == mark and \
               self._buttons[2]["text"] == mark
               
    def _myMove(self):
        """Attempts to place my mark in a random button."""
        while True:
            b = random.choice(self._buttons)
            if b["text"] == "":
                b["text"] = self._myMark
                break

    # Event handling methods
    
    def _one(self):
        self._yourMove(0)
  
    def _two(self):
        self._yourMove(1)
        
    def _three(self):
        self._yourMove(2)
        
    def _four(self):
        self._yourMove(3)
        
    def _five(self):
        self._yourMove(4)
        
    def _six(self):
        self._yourMove(5)
        
    def _seven(self):
        self._yourMove(6)
        
    def _eight(self):
        self._yourMove(7)
        
    def _nine(self):
        self._yourMove(8)

    def _clear(self):
        """Returns the GUI to its original state."""
        for b in self._buttons:
            b["text"] = ""

def main():
    TicTacToe().mainloop()

main()

