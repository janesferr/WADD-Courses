"""
File: managergui.py
Project 9.5

This module defines the BankManagerGUI class, which provides a window
for bank managers to maintain accounts.
"""

from tkinter import *
from bank import SavingsAccount, Bank

class BankManagerGUI(Frame):
    """
    This class supports a manager's view of and interaction with
    a bank.  The user navigates through a list of accounts that is
    sorted by pin by pressing a Next or a Previous button.
    The current account's information is displayed in editable fields.  
    Other functions include:
    New Account
    Update Account (saves changes to an account)
    Remove Account
    Compute Interest 
    """

    ### Instance variables
    # self._bank - the bank
    # self._account - the currently selected account
    # self._pins - a sorted list of pins
    # self._cursor - the position of the currently selected account

    def __init__(self, bank):
        """Initialize the frame, its grid, and the data model.
        The model consists of a bank and a current account
        object.
        To support navigation through the accounts,
        the manager also maintains a list of pins and 
        a current position in this list."""
        Frame.__init__(self)
        self.master.title("Bank Manager")
        self.grid()
        self._bank = bank
        self._pins = bank.getPins()
        if len(self._pins) == 0:
            self._account = None
            self._cursor = -1
        else:
            self._cursor = 0
            self._account = self._bank.get(self._pins[self._cursor])
        # Create and add the widgets to the frame.
        self._nameVar = StringVar()
        self._pinVar = StringVar()
        self._balanceVar = DoubleVar()
        self._statusVar = StringVar()
        self._nameLabel = Label(self, text = "Name")
        self._nameLabel.grid(row = 0, column = 0)
        self._pinLabel = Label(self, text = "Pin")
        self._pinLabel.grid(row = 1, column = 0)
        self._balanceLabel = Label(self, text = "Balance $")
        self._balanceLabel.grid(row = 2, column = 0)
        self._statusLabel = Label(self, text = "Status")
        self._statusLabel.grid(row = 3, column = 0)
        self._nameEntry = Entry(self, textvariable = self._nameVar,
                                justify = CENTER)
        self._nameEntry.grid(row = 0, column = 1)
        self._pinEntry = Entry(self, textvariable = self._pinVar,
                               justify = CENTER)
        self._pinEntry.grid(row = 1, column = 1)
        self.balanceEntry = Entry(self, textvariable = self._balanceVar,
                                  justify = CENTER)
        self.balanceEntry.grid(row = 2, column = 1)
        self._statusEntry = Entry(self, textvariable = self._statusVar,
                                  justify = CENTER)
        self._statusEntry.grid(row = 3, column = 1)
        self._newButton = Button(self, text = "New Account",
                                 command = self._newAccount)
        self._newButton.grid(row = 0, column = 2)
        self._updateButton = Button(self, text = "Update Account",
                                    command = self._updateAccount)
        self._updateButton.grid(row = 1, column = 2)
        self._removeButton = Button(self, text = "Remove Account",
                                    command = self._removeAccount)
        self._removeButton.grid(row = 2, column = 2)
        self._interestButton = Button(self, text = "Compute Interest",
                                      command = self._interest)
        self._interestButton.grid(row = 3, column = 2)
        self._previousButton = Button(self, text = "Previous",
                                      command = self._previousAccount)
        self._previousButton.grid(row = 4, column = 0)
        self._nextButton = Button(self, text = "Next",
                                  command = self._nextAccount)
        self._nextButton.grid(row = 4, column = 1)
        self._displayAccount()

    def _displayAccount(self):
        """Updates view with current account's info."""
        if self._account == None:
            self._nameVar.set('')
            self._pinVar.set('')
            self._balanceVar.set(0.0)
            self._interestButton["state"] = DISABLED
            self._nextButton["state"] = DISABLED
            self._previousButton["state"] = DISABLED
            self._updateButton["state"] = DISABLED
            self._removeButton["state"] = DISABLED
        else:
            self._nameVar.set(self._account.getName())
            self._pinVar.set(self._account.getPin())
            self._balanceVar.set(self._account.getBalance())
            self._interestButton["state"] = NORMAL
            self._nextButton["state"] = NORMAL
            self._previousButton["state"] = NORMAL
            self._removeButton["state"] = NORMAL

    def _newAccount(self):
        """Clears the current account and the view."""
        self._account = None
        self._displayAccount()
        self._updateButton["state"] = NORMAL

    def _updateAccount(self):
        """Saves the edited account or the new to the bank."""
        name = self._nameVar.get()
        pin = self._pinVar.get()
        balance = self._balanceVar.get()
        if name == '':
            self._statusVar.set('Error', 'Enter a name!')
            return
        elif pin in self._pins \
             or int(pin) < 1000 or int(pin) > 9999:
            self._statusVar.set('Error', 'Pin in use!')
            return
        elif self._account != None:
            self._bank._remove(self._account.getPin())
        self._account = SavingsAccount(name, pin, balance)
        self._bank.add(self._account)
        self._pins = self._bank.getPins()
        self.cursor = self._pins.index(pin)
        self._displayAccount()
        self._statusVar.set('Account updated')

    def _removeAccount(self):
        """Removes the current account from the bank."""
        self._bank.remove(self._account.getPin())
        self._bank.save()
        self._pins = self._bank.getPins()
        if len(self._pins) == 0:
            self.cursor = -1
            self._account = None
        elif self.cursor > 0:
            self._cursor -= 1
            self._account = self._bank.get(self._pins[self._cursor])
        else:
            self._account = self._bank.get(self._pins[self._cursor])
        self._displayAccount()
        self._statusVar.set('Account removed')
        
    def _interest(self):
        """Computes interest for the bank and updates the view."""
        interest = self._bank.computeInterest()
        self._displayAccount()
        self._statusVar.set('Interest is $' + str(interest))

    def _nextAccount(self):
        """Moves to next account and disables next if necessary."""
        if len(self._pins) < 2:
            return
        self._previousButton["state"] = NORMAL
        self._cursor += 1
        self._account = self._bank.get(self._pins[self._cursor])
        self._displayAccount()
        self._statusVar.set('')
        if self._cursor >= len(self._pins) - 1:
            self._nextButton["state"] = DISABLED

    def _previousAccount(self):
        """Moves to previous account and disables previous if necessary."""
        if len(self._pins) < 2:
            return
        self._nextButton["state"] = NORMAL
        self._cursor -= 1
        self._account = self._bank.get(self._pins[self._cursor])
        self._displayAccount()
        self._statusVar.set('')
        if self._cursor <= 0:
            self._previousButton["state"] = DISABLED

def main():
    bank = Bank("bank.dat")
    BankManagerGUI(bank).mainloop()
    bank.save()

main()

