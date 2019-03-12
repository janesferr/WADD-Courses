"""
File: manager.py
Project 8.8

This module defines the Manager class and its application.

Allows a library manager to manage a library.

Functions include: print all books and patrons, print the current book,
find a book, find a patron, add a new book, remove a book, add a new patron,
remove a patron, borrow a book, return a book.

To test, launch from Idle and run

>>> createBank(5)
>>> main()

Can be modified to run as a script after a library has been saved.
"""
from library import *

class Manager(object):
    """This class represents terminal-based library manager functions."""

    def __init__(self, library):
        self._book = None
        self._patron = None
        self._library = library
        self._methods = {}          # Jump table for commands
        self._methods["1"] = self._printAllBooks
        self._methods["2"] = self._printAllPatrons
        self._methods["3"] = self._printCurrentBook
        self._methods["4"] = self._printCurrentPatron
        self._methods["5"] = self._findBook
        self._methods["6"] = self._findPatron
        self._methods["7"] = self._addBook
        self._methods["8"] = self._addPatron
        self._methods["9"] = self._removeBook
        self._methods["10"] = self._removePatron
        self._methods["11"] = self._borrowBook
        self._methods["12"] = self._returnBook
        self._methods["13"] = self._quit

    def run(self):
        """A menu-driven command processor for a manager."""
        while True:
            print(" 1  View all books")
            print(" 2  View all patrons")
            print(" 3  View current book")
            print(" 4  View current patron")
            print(" 5  Find a book")
            print(" 6  Find a patron")
            print(" 7  Add a book")
            print(" 8  Add a patron")
            print(" 9  Remove a book")
            print("10  Remove a patron")
            print("11  Borrow a book")
            print("12  Return a book")
            print("13  Quit\n")
            number = input("Enter a number: ")
            theMethod = self._methods.get(number, None)
            if theMethod == None:
                print("Unrecognized number")
            else:
                theMethod()
                if theMethod == self._quit:
                    break

    def _printAllBooks(self):
        """Prints all of the books."""
        print(self._library.getBooksString())


    def _printAllPatrons(self):
        """Prints all of the books."""
        print(self._library.getPatronsString())

    def _printCurrentBook(self):
        """Prints the current book."""
        if self._book is None:
            print("No book is current")
        else:
            print(self._book)

    def _printCurrentPatron(self):
        """Prints the current patron."""
        if self._patron is None:
            print("No patron is current")
        else:
            print(self._patron)

    def _findBook(self):
        """Attempts to find a book."""
        title = input("Enter a title: ")
        book = self._library.getBook(title)
        if book is None:
            print("Title is not in the library")
        else:
            self._book = book
            print(self._book)

    def _findPatron(self):
        """Attempts to find a patron."""
        name = input("Enter a name: ")
        patron = self._library.getPatron(name)
        if patron is None:
            print("Name is not in the library")
        else:
            self._patron = patron
            print(self._patron)
   
    def _addBook(self):
        """Adds a new book."""
        title = input("Enter the book's title: ")
        author = input("Enter the author's name: ")
        self._book = Book(title, author)
        self._library.addBook(self._book)
        print("New book added")

    def _addPatron(self):
        """Adds a new book."""
        name = raw_input("Enter the patron's name: ")
        self._patron = Patron(name)
        self._library.addPatron(self._patron)
        print("New patron added")

    def _removeBook(self):
        """Removes the current book."""
        if self._book is None:
            print("No book is current")
        else:
            self._library.removeBook(self._book.getTitle())
            self._book = None
            print("Book removed")
    
    def _removePatron(self):
        """Removes the current patron."""
        if self._patron is None:
            print("No patron is current")
        else:
            self._library.removePatron(self._patron.getName())
            self._patron = None
            print("Patron removed")

    def _borrowBook(self):
        """The current patron attempts to borrow the current book."""
        if self._book is None:
            print("No book is current")
        elif self._patron is None:
            print("No patron is current")
        else:
            result = self._book.borrowMe(self._patron)
            if result is None:
                print("Book successfully borrowed")
            else:
                print(result)
    
    def _returnBook(self):
        """The attempts to return the current book."""
        if self._book is None:
            print("No book is current")
        else:
            print(self._book.returnMe())

    def _quit(self):
        """Saves the library to a file and prints a signoff."""
        self._library.save()
        self._book = None
        print("Have a nice day!")

# Top-level functions
def main():
    """Instantiate an ATM and run it."""
    library = Library("books.dat", "patrons.dat")
    manager = Manager(library)
    manager.run()

main()
