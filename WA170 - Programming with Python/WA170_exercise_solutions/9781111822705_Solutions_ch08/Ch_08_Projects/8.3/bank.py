"""
File: bank.py
Project 8.3

This module defines the SavingsAccount and Bank classes.
Modifed to return a Bank's string with the accounts in
alphabetical order by name.
"""
import pickle

class SavingsAccount(object):
    """This class represents a savings account
    with the owner's name, PIN, and balance."""

    RATE = 0.02
        
    def __init__(self, name, pin, balance = 0.0):
        self._name = name
        self._pin = pin
        self._balance = balance

    def __str__(self):
        result =  'Name:    ' + self._name + '\n' 
        result += 'PIN:     ' + self._pin + '\n' 
        result += 'Balance: ' + str(self._balance)
        return result

    def getBalance(self):
        return self._balance

    def getName(self):
        return self._name

    def getPin(self):
        return self._pin

    def deposit(self, amount):
        """Deposits the given amount."""
        self._balance += amount
        return self._balance

    def withdraw(self, amount):
        """Withdraws the given amount.
        Returns None if successful, or an
        error message if unsuccessful."""
        if amount < 0:
            return 'Amount must be >= 0'
        elif self._balance < amount:
            return 'Insufficient funds'
        else:
            self._balance -= amount
            return None

    def computeInterest(self):
        """Computes, deposits, and returns the interest."""
        interest = self._balance * SavingsAccount.RATE
        self.deposit(interest)
        return interest

    # Added to support sorted lists of accounts
    def __eq__(self, other):
        """Tests for equality."""
        return cmp(self._name, other._name)

    def __lt__(self, other):
        """Returns self < other, with respect
        to names."""
        return self._name < other._name

class Bank(object):
    """This class represents a bank as a dictionary of
    accounts.  An optional file name is also associated
    with the bank, to allow transfer of accounts to and
    from permanent file storage."""

    def __init__(self, fileName = None):
        """Creates a new dictionary to hold the accounts.
        If a file name is provided, loads the accounts from
        a file of pickled accounts."""
        self._accounts = {}
        self.fileName = fileName
        if fileName != None:
            fileObj = open(fileName, 'rb')
            while True:
                try:
                    account = pickle.load(fileObj)
                    self.add(account)
                except(EOFError):
                    fileObj.close()
                    break

    def add(self, account):
        """Inserts an account using its PIN as a key."""
        self._accounts[account.getPin()] = account

    def remove(self, pin):
        return self._accounts.pop(pin)

    def get(self, pin):
        return self._accounts.get(pin, None)

    def computeInterest(self):
        """Computes interest for each account and
        returns the total."""
        total = 0
        for account in self._accounts.values():
            total += account.computeInterest()
        return total

    def __str__(self):
        """Return the string rep of the entire bank."""
        # Sorts the accounts before mapping str
        lyst = list(self._accounts.values())
        lyst.sort()
        return '\n'.join(map(str, lyst))

    def save(self, fileName = None):
        """Saves pickled accounts to a file.  The parameter
        allows the user to change file names."""
        if fileName != None:
            self.fileName = fileName
        elif self.fileName == None:
            return
        fileObj = open(self.fileName, 'wb')
        for account in self._accounts.values():
            pickle.dump(account, fileObj)
        fileObj.close()
        
def testBank(number = 0):
    """Returns a bank with the specified number of accounts and/or
    the accounts loaded from the specified file name."""
    bank = Bank()
    for i in range(number):
        bank.add(SavingsAccount('Name' + str(i + 1),
                                str(1000 + i),
                                100.00))
    return bank


   
