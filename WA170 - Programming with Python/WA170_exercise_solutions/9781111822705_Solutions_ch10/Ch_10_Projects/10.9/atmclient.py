"""
File: atmclient.py
Project 10.9

This module defines the ATMClient class and its application.

"""
from socket import *
from codecs import decode

BUFSIZE = 1024
CODE = 'ascii'

class ATMClient(object):
    """This class represents terminal-based ATM transactions."""
        
    def __init__(self, server):
        self._server = server
        self._methods = {}          # Jump table for commands
        self._methods["1"] = self._getBalance
        self._methods["2"] = self._deposit
        self._methods["3"] = self._withdraw
        self._methods["4"] = self._quit

    def run(self):
        """Logs in a user and processes its accounts."""
        name = input("Enter your name: ")
        self._server.send(bytes(name, CODE))
        pin = input("Enter your PIN: ")
        self._server.send(bytes(pin, CODE))
        message = decode(self._server.recv(BUFSIZE), CODE)
        print(message)
        if message.split()[0] == "ERROR:":
            return
        else:
            self._processAccount()

    def _processAccount(self):
        """A menu-driven command processor for a user."""
        self._done = False
        while not self._done:
            print("1  View your balance")
            print("2  Make a deposit")
            print("3  Make a withdrawal")
            print("4  Quit\n")
            number = input("Enter a number: ")
            theMethod = self._methods.get(number, None)
            if theMethod == None:
                print("Unrecognized number")
            else:
                theMethod()

    def _getBalance(self):
        """Gets the balance."""
        self._server.send(bytes("BALANCE", CODE))
        balance = decode(self._server.recv(BUFSIZE), CODE)
        print("Your balance is $", balance)

    def _deposit(self):
        self._server.send(bytes("DEPOSIT", CODE))
        amount = input("Enter the amount to deposit: ")
        self._server.send(bytes(amount, CODE))
        message = decode(self._server.recv(BUFSIZE), CODE)
        print(message)

    def _withdraw(self):
        self._server.send(bytes("WITHDRAW", CODE))
        amount = input("Enter the amount to withdraw: ")
        self._server.send(bytes(amount, CODE))
        message = decode(self._server.recv(BUFSIZE), CODE)
        print(message)

    def _quit(self):
        self._server.send(bytes("QUIT", CODE))
        print("Have a nice day!")
        self._done = True

def main():
    """Connects to server, starts up client, run it,
    and closes server when client is done."""
    HOST = 'localhost'
    PORT = 5000
    ADDRESS = (HOST, PORT)
    
    server = socket(AF_INET, SOCK_STREAM)
    server.connect(ADDRESS)
    
    client = ATMClient(server)
    client.run()
    server.close()

main()
