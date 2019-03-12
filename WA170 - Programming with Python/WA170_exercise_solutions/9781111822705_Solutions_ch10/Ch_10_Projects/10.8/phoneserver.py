"""
File: phoneserver.py
Project 10.8

Server for an online phone book.  Handles multiple clients for a single
phonebook concurrently and saves the phonebook to a file.

Loads phone book object from a file at startup and saves at shutdown.

Commands sent by the client are ADD, FIND, and QUIT.  When these commands
are received, the server then receives a name and number for ADD, a name for
FIND, or just closes the connection for QUIT.  The server returns a message
to the client in two cases:

ADD: "Name and number added."
FIND: The number or "Name not found."
"""

from socket import *
from codecs import decode
from threading import Thread
from phonebook import PhoneBook
import pickle
import os.path

BUFSIZE = 1024
CODE = 'ascii'

class ClientHandler(Thread):
    """Handles a session."""
    def __init__(self, client, book):
        Thread.__init__(self)
        self._client = client
        self._book = book

    def run(self):
        self._client.send(bytes("Welcome to the phone book", CODE))
        while True:
            message = decode(self._client.recv(BUFSIZE), CODE)
            self._client.send(bytes("/n", CODE))
            if not message or message.upper().strip() == "QUIT":
                print('Client disconnected')
                self._client.close()
                break
            elif message.upper().strip() == "ADD":
                name = decode(self._client.recv(BUFSIZE), CODE)
                number = decode(self._client.recv(BUFSIZE), CODE)
                self._book.add(name.strip(), number.strip())
                self._client.send(bytes("Name and number added.", CODE))
            else:
                name = decode(self._client.recv(BUFSIZE), CODE)
                number = self._book.get(name.strip())
                if number == None:
                    self._client.send(bytes("Name not found.", CODE))
                else:
                    self._client.send(bytes(number, CODE))
                


class PhoneServer(Thread):
    """Server for the phone book application."""
    
    def __init__(self, book):
        """Includes Boolean flag to shut down."""
        Thread.__init__(self)
        self._done = False
        self._book = book

    def run(self):
        """Runs until signaled to shut down.  At least
        one client must connect after the signal is sent."""
        HOST = 'localhost'
        PORT = 5000
        ADDRESS = (HOST, PORT)

        server = socket(AF_INET, SOCK_STREAM)
        server.bind(ADDRESS)
        server.listen(5)

        while not self._done:
            print('Waiting for connection . . .')
            client, address = server.accept()
            print('... connected from:', address)
            handler = ClientHandler(client, self._book)
            handler.start()
        server.close()

    def quit(self):
        """Stops the server loop."""
        self._done = True

def main():
    """Creates a phone book, starts the server thread with that book,
    and waits for the user to signal to quit."""
    filename = "phonebook.dat"
    if os.path.exists(filename):
        fileObj = open(filename, 'rb')
        book = pickle.load(fileObj)
    else:
        book = PhoneBook()
    server = PhoneServer(book)
    server.start()
    input("Press enter to quit.")
    server.quit()
    print("Server shutting down.")
    fileObj = open(filename, 'wb')
    pickle.dump(book, fileObj)
    fileObj.close()

main()
