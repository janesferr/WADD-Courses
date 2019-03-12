"""
File: calculator.py
Project 9.7

Simulates a calculator with +, -, *, /, =, and C.
"""

from tkinter import *

class Calculator(Frame):

    def __init__(self):
        """Set up the window and widgets."""
        Frame.__init__(self)
        self.master.title("Calculator")
        self.grid()
        self._dataVar = StringVar()
        self._dataEntry = Entry(self,
                                textvariable = self._dataVar)
        self._dataEntry.grid(row = 0, column = 0,
                             columnspan = 4)
        self._sevenBtn = Button(self, text = "7",
                                command = self._seven)
        self._sevenBtn.grid(row = 1, column = 0)
        self._eightBtn = Button(self, text = "8",
                                command = self._eight)
        self._eightBtn.grid(row = 1, column = 1)
        self._nineBtn = Button(self, text = "9",
                                command = self._nine)
        self._nineBtn.grid(row = 1, column = 2)
        self._divBtn = Button(self, text = "/",
                                command = self._div)
        self._divBtn.grid(row = 1, column = 3)
        self._fourBtn = Button(self, text = "4",
                                command = self._four)
        self._fourBtn.grid(row = 2, column = 0)
        self._fiveBtn = Button(self, text = "5",
                                command = self._five)
        self._fiveBtn.grid(row = 2, column = 1)
        self._sixBtn = Button(self, text = "6",
                                command = self._six)
        self._sixBtn.grid(row = 2, column = 2)
        self._mulBtn = Button(self, text = "*",
                                command = self._mul)
        self._mulBtn.grid(row = 2, column = 3)
        self._oneBtn = Button(self, text = "1",
                                command = self._one)
        self._oneBtn.grid(row = 3, column = 0)
        self._twoBtn = Button(self, text = "2",
                                command = self._two)
        self._twoBtn.grid(row = 3, column = 1)
        self._threeBtn = Button(self, text = "3",
                                command = self._three)
        self._threeBtn.grid(row = 3, column = 2)
        self._subBtn = Button(self, text = "-",
                                command = self._sub)
        self._subBtn.grid(row = 3, column = 3)
        self._zeroBtn = Button(self, text = "0",
                                command = self._zero)
        self._zeroBtn.grid(row = 4, column = 0)
        self._equalsBtn = Button(self, text = "=",
                                command = self._equals)
        self._equalsBtn.grid(row = 4, column = 1)
        self._clearBtn = Button(self, text = "C",
                                command = self._clear)
        self._clearBtn.grid(row = 4, column = 2)
        self._addBtn = Button(self, text = "+",
                                command = self._add)
        self._addBtn.grid(row = 4, column = 3)
        self._clear()

    def _zero(self):
        self._insert("0")

    def _one(self):
        self._insert("1")

    def _two(self):
        self._insert("2")
        
    def _three(self):
        self._insert("3")
        
    def _four(self):
        self._insert("4")
        
    def _five(self):
        self._insert("5")
        
    def _six(self):
        self._insert("6")

    def _seven(self):
        self._insert("7")
        
    def _eight(self):
        self._insert("8")
        
    def _nine(self):
        self._insert("9")

    def _add(self):
        self._setOperator("+")

    def _sub(self):
        self._setOperator("-")

    def _mul(self):
        self._setOperator("*")

    def _div(self):
        self._setOperator("/")

    def _equals(self):
        self._calculate()

    def _clear(self):
        """Restores the calculator to its startup state."""
        self._number1 = 0
        self._number2 = None
        self._operator = None
        self._dataVar.set(str(self._number1))

    def _insert(self, s):
        """Updates the first number or the second number with
        the next digit and then updates the field."""
        if self._number2 == None:
            # Adjust number1
            if self._number1 == 0:
                # Was just 0, so replace it
                self._number1 = int(s)
            else:
                # Was not 0, so append to it
                self._number1 = int(str(self._number1) + s)
            self._dataVar.set(str(self._number1))
        else:
            # Adjust number2
            self._number2 = int(str(self._number2) + s)
            self._dataVar.set(str(self._number2))

    def _setOperator(self, op):
        """Sets the operator symbol and makes the second number active."""
        self._operator = op
        self._number2 = 0

    def _calculate(self):
        """Computes the result and displays it in the field.
        The result is also placed in the first number for further
        calculations."""
        # No effect if not ready for = yet
        if self._number2 is None or self._operator is None:
            return
        # Assume an error until proven OK
        result = "ERR"
        # Attempt to calculate a result
        if self._operator == '+':
            result = self._number1 + self._number2
        elif self._operator == '-':
            result = self._number1 - self._number2
        elif self._operator == '*':
            result = self._number1 * self._number2
        elif self._operator == '/' and self._number2 != 0:
            result = self._number1 / self._number2
        # Not an error, then put result in first number
        # for further calculations
        if result != "ERR":
            self._number1 = result
            self._number2 = None
            self._operator = None
        # Display result or ERR
        self._dataVar.set(str(result))
  
def main():
    Calculator().mainloop()

main()

