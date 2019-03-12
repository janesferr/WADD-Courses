"""
File: chatrecord.py
Project 10.5

Represents the record of a chat.  The record's data
are loaded from a text file at instantiation.  The file
is updated after each add.

The format of the text file is

<message-1>
*SEP*
<message-2>
*SEP*
.
.
<message-n>
*SEP*

"""

class ChatRecord:

    def __init__(self, filename):
        """Loads the record from the text file."""
        self._data = []
        self._filename = filename
        self._load()
        

    def add(self, s):
        """Adds s to the record and saves it to the file."""
        self._data.append(s)
        self._save(s)

    def __str__(self):
        """Returns a string representation."""
        if len(self._data) == 0:
            return 'No messages yet!'
        else:
            return '\n'.join(self._data)

    def _load(self):
        """Reads data from the file into the record."""
        f = open(self._filename, 'r')
        while True:
            nextLine = f.readline()
            if nextLine == "":      # Stop at end of file
                break
            message = ""
            while nextLine != "*SEP*\n":  # Check for separator
                message += nextLine
                nextLine = f.readline()
                if nextLine == "":
                    break
            self._data.append(message)

    def _save(self, s):
        """Saves a string to the file by appending it."""
        f = open(self._filename, 'a')
        f.write(s)
        f.write("\n")
        f.close()
            
                
                
   
