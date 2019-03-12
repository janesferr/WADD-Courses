"""
Module: phonebook.py
Project 10.8

Data model class to maintain a phone book.

"""

class PhoneBook(object):
    """Represents a phone book."""

    def __init__(self):
        self._entries = {}

    def add(self, name, number):
        """Adds the name and number to the phone book."""
        self._entries[name] = number

    def get(self, name):
        """Returns the number if name is in the phone book,
        or None otherwise."""
        return self._entries.get(name, None)

    def __str__(self):
        """Returns the string representation of the phone book."""
        result = ""
        keys = list(self._entries.keys())
        keys.sort()
        for key in keys:
            result += key + ":" + self._entries[key] + "\n"
        return result


def test():
    """Testing function for PhoneBook."""
    book = PhoneBook()
    for name in range(10):
        book.add("Name" + str(name), "524-4682")
    print(book)
    for name in range(10):
        print(book.get("Name" + str(name)))
