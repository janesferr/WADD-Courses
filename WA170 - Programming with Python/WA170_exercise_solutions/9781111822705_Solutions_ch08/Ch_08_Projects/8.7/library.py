"""
File: library.py
Project 8.7

This module defines the Book, Patron, and Library classes.
"""
import pickle

class Patron(object):
    """This class represents a patron
    with a name and a number of books checked out."""

    MAX_BOOKS_OUT = 3
        
    def __init__(self, name):
        self._name = name
        self._numBooksOut = 0

    def __str__(self):
        result = self._name + ', ' + str(self._numBooksOut) + \
                 " books out"
        return result

    def getName(self):
        return self._name

    def getNumBooksOut(self):
        return self._numBooksOut

    def inc(self):
        """Increments the number of books out."""
        self._numBooksOut += 1

    def dec(self):
        """Decrements the number of books out."""
        self._numBooksOut -= 1

        
class Book(object):
    """This class represents a book with a title, author,
    a patron to whom the book is check out, and a wait list
    of patrons for it."""

    def __init__(self, title, author):
        """Creates a new book with the given title and author."""
        self._title = title
        self._author = author
        self._patron = None
        self._waitList = []

    def __str__(self):
        result =  'Title:  ' + self._title + '\n' 
        result += 'Author: ' + self._author + '\n'
        if self._patron:
            result += "Checked out to: " + str(self._patron) + '\n'
        else:
            result += "Not checked out\n"
        result += "Wait list:\n"
        for patron in self._waitList:
            result += str(patron) + '\n'
        return result

    def getTitle(self):
        return self._title

    def getAuthor(self):
        return self._author

    def getPatron(self):
        return self._patron

    def borrowMe(self, patron):
        """Attempts to loan book to patron."""
        if patron.getNumBooksOut() == Patron.MAX_BOOKS_OUT:
            return "This patron cannot borrow more books"
        elif self._patron:
            self._waitList.append(patron)
            return "This book is already checked out"
        else:
            patron.inc()
            self._patron = patron
            return None

    def returnMe(self):
        """Current patron returns book, attempts to loan it
        to a qualified waiting patron."""
        if self._patron is None:
            return "The book is not checked out"
        self._patron.dec()
        self._patron = None
        index = 0
        while index < len(self._waitList):
            waitingPatron = self._waitList[index]
            result = self.borrowMe(waitingPatron)
            if result is None:
                self._waitList.pop(index)
                return "Book loaned to a waiting patron"
        return "Book returned"
            
        
class Library(object):
    """This class represents a library with books and patrons."""

    def __init__(self, bookName = None, patronName = None):
        """Creates new dictionaries to hold books and patrons."""
        self._bookName = bookName
        self._patronName = patronName
        self._books = {}
        self._patrons = {}
        if bookName != None and patronName != None:
            bookFileObj = open(bookName, 'rb')
            while True:
                try:
                    book = pickle.load(bookFileObj)
                    self.addBook(book)
                except(EOFError):
                    bookFileObj.close()
                    break
            patronFileObj = open(patronName, 'rb')
            while True:
                try:
                    patron = pickle.load(patronFileObj)
                    self.addPatron(patron)
                except(EOFError):
                    patronFileObj.close()
                    break

    def addBook(self, book):
        """Inserts a book using its title as a key."""
        self._books[book.getTitle()] = book

    def getBook(self, title):
        """Returns the book or None."""
        return self._books.get(title, None)

    def removeBook(self, title):
        """Removes the book if it's there and updates
        it's borrower's count if there is one."""
        book = self._books.pop(title, None)
        if book == None:
            return "Book's title is not in the library"
        elif book.getPatron() != None:
            book.getPatron().dec()
        return None

    def getPatron(self, name):
        """Returns the patron or None."""
        return self._patrons.get(name, None)

    def addPatron(self, patron):
        """Inserts a patron using its name as a key."""
        self._patrons[patron.getName()] = patron

    def removePatron(self, name):
        """Removes the patron if it's there and returns its
        borrowed books if there are any."""
        patron = self._patrons.pop(name, None)
        if patron == None:
            return "Patron's name is not in the library"
        elif patron.getNumBooksOut() > 0:
            for book in self._books.values():
                if patron == book.getPatron():
                    book.returnMe()
        return None

    def getBooksString(self):
        "Returns a string representation of the books."""
        result = "Books:\n"
        result += '\n'.join(map(str, self._books.values()))
        return result
    
    def getPatronsString(self):
        "Returns a string representation of the patrons."""
        result = "Patrons:\n"
        result += '\n'.join(map(str, self._patrons.values()))
        return result
    
    def __str__(self):
        """Return the string rep of the entire library."""
        return self.getBooksString() + "\n" + self.getPatronsString()

    def save(self, bookName = None, patronName = None):
        """Saves pickled books and patrons files.  The parameters
        allow the user to change file names."""
        if bookName != None:
            self._bookName = bookName
        elif self._bookName is None:
            return
        if patronName != None:
            self._patronName = patronName
        elif self._patronName is None:
            return
        bookFileObj = open(self._bookName, 'wb')
        for book in self._books.values():
            pickle.dump(book, bookFileObj)
        bookFileObj.close()
        patronFileObj = open(self._patronName, 'wb')
        for patron in self._patrons.values():
            pickle.dump(patron, patronFileObj)
        patronFileObj.close()   
