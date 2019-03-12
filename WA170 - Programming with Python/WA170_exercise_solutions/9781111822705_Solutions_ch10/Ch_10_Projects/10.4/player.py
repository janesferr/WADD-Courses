"""
File: player.py
Project 10.4

This module defines a Player class to play the game of craps.
A player now tracks a the most recent roll and does one
roll at a time.  The roll method returns "WIN", "LOSE", or
"CONTINUE", depending on the result.
"""

from die import Die

class Player(object):

    def __init__(self):
        """Has a pair of dice and an empty rolls list."""
        self._die1 = Die()
        self._die2 = Die()
        self._lastRoll = None
        self._initialSum = 0
        self._rollCount = 0

    def __str__(self):
        """Returns a string representation of the list of rolls."""
        result = ""
        (v1, v2) = self._lastRoll
        result = result + str((v1, v2)) + " " + \
                 str(v1 + v2) + "\n"
        return result

    def getNumberOfRolls(self):
        """Returns the number of the rolls."""
        return self._rollCount

    def roll(self):
        """Makes a roll, saves that roll, 
        and returns WIN, LOSE, or CONTINUE."""
        self._rollCount += 1
        self._die1.roll()
        self._die2.roll()
        (v1, v2) = (self._die1.getValue(),
                    self._die2.getValue())
        self._lastRoll = (v1, v2)
        if self._initialSum == 0:
            initialSum = v1 + v2
            if initialSum in (2, 3, 12):
                return "LOSE"
            elif initialSum in (7, 11):
                return "WIN"
            else:
                return "CONTINUE"
        else:
            sum = v1 + v2
            if sum == 7:
                return "LOSE"
            elif sum == initialSum:
                return "WIN"
            else:
                return "CONTINUE"

    def reset(self):
        """Returns player to original state."""
        self._lastRoll = None
        self._initialSum = 0
        self._rollCount = 0

def playOneGame():
    """Plays a single game and prints the results."""
    player = Player()
    while True:
        result = player.roll()
        print(player)
        print(result)
        if result == "WIN" or result == "LOSE":
            break
