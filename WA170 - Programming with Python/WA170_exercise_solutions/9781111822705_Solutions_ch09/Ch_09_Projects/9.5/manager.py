"""
File: atm.py
Project 8.5

This module defines the Manager class and its application.

Allows a bank manager to load a bank from a file and manage accounts.
Functions include: print all accounts, print the current account,
find an account, edit an account, add a new account, remove an account.

To test, launch from Idle and run

>>> createBank(5)
>>> main()

Can be modified to run as a script after a bank has been saved.
"""
from bank import Bank, SavingsAccount

class Manager(object):
    """This class represents terminal-based bank manager functions."""

    def __init__(self, bank):
        self._account = None
        self._bank = bank
        self._methods = {}          # Jump table for commands
        self._methods["1"] = self._printAll
        self._methods["2"] = self._printCurrent
        self._methods["3"] = self._find
        self._methods["4"] = self._edit
        self._methods["5"] = self._add
        self._methods["6"] = self._remove
        self._methods["7"] = self._quit

    def run(self):
        """A menu-driven command processor for a manager."""
        while True:
            print("1  View all accounts")
            print("2  View current account")
            print("3  Find an account")
            print("4  Edit an account")
            print("5  Add an account")
            print("6  Remove an account")
            print("7  Quit\n")
            number = input("Enter a number: ")
            theMethod = self._methods.get(number, None)
            if theMethod == None:
                print("Unrecognized number")
            else:
                theMethod()
                if theMethod == self._quit:
                    break

    def _printAll(self):
        """Prints all of the accounts."""
        print(self._bank)


    def _printCurrent(self):
        """Prints the current account."""
        if self._account == None:
            print("No account is current")
        else:
            print(self._account)

    def _printCurrent(self):
        """Prints the current account."""
        if self._account == None:
            print("No account is current")
        else:
            print(self._account)

    def _find(self):
        """Attempts to find an account."""
        pin = input("Enter a PIN: ")
        account = self._bank.get(pin)
        if account == None:
            "PIN is not in the bank"
        else:
            self._account = account
            print(self._account)

    def _edit(self):
        """Edits the balance and name of the current account."""
        if self._account == None:
            print("No account is current")
        else:
            name = self._account.getName()
            pin = self._account.getPin()
            balance = self._account.getBalance()
            while True:
                print("1  Change the name")
                print("2  Change the balance")
                print("3  Quit\n")
                number = input("Enter a number: ")
                if number == "1":
                    name = input("Enter the new name: ")
                elif number == "2":
                    balance = float(input("Enter the balance: "))
                elif number == "3":
                    break
                else:
                    print("Unrecognized number")
            self._account = SavingsAccount(name, pin, balance)
            self._bank.add(self._account)
    
    def _add(self):
        """Adds a new account."""
        balance = float(input("Enter the initial balance: "))
        name = input("Enter the name: ")
        while True:
            pin = input("Enter the PIN: ")
            if self._bank.get(pin):
                print("PIN is already in the bank")
            else:
                self._account = SavingsAccount(name, pin, balance)
                self._bank.add(self._account)
                print("New account added")
                break

    def _remove(self):
        """Removes the current account."""
        if self._account == None:
            print("No account is current")
        else:
            self._bank.remove(self._account.getPin())
            self._account = None
            print("Account removed")
    
    def _quit(self):
        """Saves the bank to a file and prints a signoff."""
        self._bank.save()
        self._account = None
        print("Have a nice day!")

# Top-level functions
def main():
    """Instantiate an ATM and run it."""
    bank = Bank("bank.dat")
    manager = Manager(bank)
    manager.run()

def createBank(number = 0):
    """Saves a bank with the specified number of accounts.
    Used during testing."""
    bank = Bank()
    for i in range(number):
        bank.add(SavingsAccount('Name' + str(i + 1),
                                str(1000 + i),
                                100.00))
    bank.save("bank.dat")
