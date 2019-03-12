"""
File: library.py
Project 8.6

This module defines the Book and Patron classes.
"""

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
        self._patron.dec()
        self._patron = None
        index = 0
        while index < len(self._waitList):
            waitingPatron = self._waitList[index]
            result = self.borrowMe(waitingPatron)
            if result == None:
                self._waitList.pop(index)
                return "Book loaned to a waiting patron"
        return "Book returned"
            
        
def main():
    """Tests the Patron and Book classes."""
    p1 = Patron("Ken")
    p2 = Patron("Martin")
    b1 = Book("Atonement", "McEwan")
    b2 = Book("The March", "Doctorow")
    b3 = Book("Beach Music", "Conroy")
    b4 = Book("Thirteen Moons", "Frazier")
    print(b1.borrowMe(p1))
    print(b2.borrowMe(p1))
    print(b3.borrowMe(p1))
    print(b1.borrowMe(p2))
    print(b4.borrowMe(p1))
    print(p1)
    print(b1)
    print(b4)
    print(b1.returnMe())
    print(b2.returnMe())
    print(b1)
    print(b2)

main()

   