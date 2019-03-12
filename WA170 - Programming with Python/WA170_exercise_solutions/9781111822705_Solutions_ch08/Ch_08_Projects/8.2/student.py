"""
File: student.py
Project 8.2
Resources to manage a student's name and test scores.
Includes methods for comparisons and testing for equality.
Tests the class by putting students into random order in a list
and then sorting them.
"""

from functools import reduce

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self._name = name
        self._scores = []
        for count in range(number):
            self._scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self._name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self._scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self._scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        sum = reduce(lambda x, y: x + y, self._scores)
        return sum / len(self._scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return reduce(lambda x, y: max(x, y), self._scores)
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self._name  + "\nScores: " + \
               " ".join(map(str, self._scores))

    def __lt__(self, other):
        """Returns self < other, with respect
        to names."""
        return self._name < other._name

    def __gt__(self, other):
        """Returns self > other, with respect
        to names."""
        return not (self == other or self < other)

    def __le__(self, other):
        """Returns self <= other, with respect
        to names."""
        return self == other or self < other

    def __ge__(self, other):
        """Returns self >= other, with respect
        to names."""
        return self == other or self > other

    def __eq__(self, other):
        """Tests for equality."""
        if self is other: 
            return True
        elif type(self) != type(other):
            return False
        else:
            return self._name == other._name

import random

def main():
    """Tests sorting."""
    # Create the list and put 5 students into it
    lyst = []
    for count in range(5):
        s = Student("Name" + str(count + 1), 10)
        lyst.append(s)
    # Shuffle and print the contents
    random.shuffle(lyst)
    print("Unsorted list of students:")
    for s in lyst:
        print(s)
    # Sort and print the contents
    lyst.sort()
    print("\nSorted list of students:")
    for s in lyst:
        print(s)
        
    

main()



