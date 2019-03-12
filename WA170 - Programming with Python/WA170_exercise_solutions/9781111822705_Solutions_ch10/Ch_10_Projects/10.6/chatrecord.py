"""
File: chatrecord.py

Represents the record of a chat.  
"""

class ChatRecord:

    def __init__(self):
        self.data = []

    def add(self, s):
        """Adds s to the record."""
        self.data.append(s)

    def __str__(self):
        """Returns a string representation."""
        if len(self.data) == 0:
            return 'No messages yet!'
        else:
            return '\n'.join(self.data)
   
