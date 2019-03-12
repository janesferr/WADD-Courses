"""
File: atmserver.py
Project 10.9

Server for an ATM.  Handles multiple clients for a single
bank concurrently and saves the bank to a file.

Loads bank object from a file at startup and saves at shutdown.

Commands sent by the client are BALANCE, DEPOSIT, WTHDRAW, and QUIT.
When these commands are received, the server receives other data as
necessary, performs the appropriate action on the bank, and sends a
reply.

"""

from socket import *
from codecs import decode
from threading import Thread
from bank import Bank

BUFSIZE = 1024
CODE = 'ascii'

class ClientHandler(Thread):
    """Handles a session."""
    def __init__(self, client, bank):
        Thread.__init__(self)
        self._client = client
        self._bank = bank

    def run(self):
        name = decode(self._client.recv(BUFSIZE), CODE)
        pin = decode(self._client.recv(BUFSIZE), CODE)
        self._account = self._bank.get(pin)
        if self._account == None:
            self._client.send(bytes("ERROR: unrecognized pin", CODE))
            self._client.close()
            return
        elif self._account.getName() != name:
            self._client.send(bytes("ERROR: unrecognized name", CODE))
            self._client.close()
            return
        else:
            self._client.send(bytes("Welcome to the bank", CODE))
        while True:
            message = decode(self._client.recv(BUFSIZE), CODE)
            if not message or message.upper().strip() == "QUIT":
                print('Client disconnected')
                self._client.close()
                break
            elif message.upper().strip() == "BALANCE":
                balance = self._account.getBalance()
                self._client.send(bytes(str(balance), CODE))
            elif message.upper().strip() == "DEPOSIT":
                amount = decode(self._client.recv(BUFSIZE), CODE)
                amount = float(amount.strip())
                message = self._account.deposit(amount)
                if message == None:
                    message = "Deposit successful"
                self._client.send(bytes(str(message), CODE))
            else:  # command is WITHDRAW
                amount = decode(self._client.recv(BUFSIZE), CODE)
                amount = float(amount.strip())
                message = self._account.withdraw(amount)
                if message == None:
                    message = "Withdrawal successful"
                self._client.send(bytes(str(message), CODE))

class ATMServer(Thread):
    """Server for the ATM application."""
    
    def __init__(self, bank):
        """Includes Boolean flag to shut down."""
        Thread.__init__(self)
        self._done = False
        self._bank = bank

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
            handler = ClientHandler(client, self._bank)
            handler.start()
        server.close()

    def quit(self):
        """Stops the server loop."""
        self._done = True

def main():
    """Loads a bank, starts the server thread with that bank,
    and waits for the user to signal to quit."""
    bank = Bank("bank.dat")
    server = ATMServer(bank)
    server.start()
    input("Press enter to quit.")
    server.quit()
    print("Server shutting down.")
    bank.save()

main()
