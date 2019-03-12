"""
File: phoneclient.py
Project 10.8

Client for a phone book application.

Sends the commands ADD, FIND, or QUIT to the server.
"""

from socket import *
from codecs import decode

BUFSIZE = 1024
CODE = 'ascii'

class PhoneClient(object):

    def __init__(self, server):
        self._server = server
        self._done = False
        self._methods = {}          # Jump table for commands
        self._methods["1"] = self._find
        self._methods["2"] = self._add
        self._methods["3"] = self._quit

    def _find(self):
        """Looks up a name in the phone book."""
        self._server.send(bytes("FIND", CODE))
        self._server.recv(BUFSIZE)
        name = input("Enter the name: ")
        self._server.send(bytes(name, CODE))
        reply = decode(self._server.recv(BUFSIZE), CODE)
        if not reply:
            print("Server disconnected")
            self._done = True
        else:
            print(reply)
        
    def _add(self):
        """Adds a name and number to the phone book."""
        self._server.send(bytes("ADD", CODE))
        self._server.recv(BUFSIZE)             # Consume a newline
        name = input("Enter the name: ")
        self._server.send(bytes(name, CODE))
        number = input("Enter the phone number: ")
        self._server.send(bytes(number, CODE))        
        reply = decode(self._server.recv(BUFSIZE), CODE)
        if not reply:
            print("Server disconnected")
            self._done = True
        else:
            print(reply)

    def _quit(self):
        """Stops the client's loop."""
        self._server.send(bytes("QUIT", CODE))
        self._done = True

    def run(self):
        """A menu-driven command processor for a manager."""
        print(decode(self._server.recv(BUFSIZE), CODE))
        while not self._done:
            print("1  Find a name/number")
            print("2  Add a name/number")
            print("3  Quit\n")
            number = input("Enter a number: ")
            theMethod = self._methods.get(number, None)
            if theMethod == None:
                print("Unrecognized number")
            else:
                theMethod()
                if theMethod == self._quit:
                    break

def main():
    """Connects to server, starts up client, run it,
    and closes server when client is done."""
    HOST = 'localhost'
    PORT = 5000
    ADDRESS = (HOST, PORT)
    
    server = socket(AF_INET, SOCK_STREAM)
    server.connect(ADDRESS)
    
    client = PhoneClient(server)
    client.run()
    server.close()

main()
