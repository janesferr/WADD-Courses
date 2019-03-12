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

    def getNumBooksOut(self):
        """Returns the number of books out."""

    def inc(self):
        """Increments the number of books out."""

    def dec(self):
        """Decrements the number of books out."""

        
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

    def borrowMe(self, patron):
        """Attempts to loan book to patron."""

    def returnMe(self):
        """Current patron returns book, attempts to loan it
        to a qualified waiting patron."""


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
