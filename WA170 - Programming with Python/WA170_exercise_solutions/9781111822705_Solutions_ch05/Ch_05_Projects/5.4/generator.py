"""
File: generator.py
Project 5.4
Generates and displays sentences using a simple grammar
and vocabulary.  Words are chosen at random.  Adds optional
adjectives to noun phrases, optional prepositional phrases,
and optional independent clauses connected by conjunctions.
"""

import random

articles = ("A", "THE")

nouns = ("BOY", "GIRL", "BAT", "BALL")

verbs = ("HIT", "SAW", "LIKED")

prepositions = ("WITH", "BY")

adjectives = ("RED", "LITTLE")

conjunctions = ("AND", "BUT")

def sentence():
    """Builds and returns a sentence.
    Now allows for optional independent clauses
    connected by conjunctions."""
    first = independentClause()
    if random.randint(1, 5) == 1:
        return first + " " + random.choice(conjunctions) + \
               " " + independentClause()
    else:
        return first

def independentClause():
    """Builds and returns an independent clause."""
    return nounPhrase() + " " + verbPhrase()

def nounPhrase():
    """Builds and returns a noun phrase.
    Now includes an optional adjective."""
    if random.randint(1, 2) == 1:
        adj = random.choice(adjectives) + " "
    else:
        adj = ""
    return random.choice(articles) + " " + adj + random.choice(nouns)

def verbPhrase():
    """Builds and returns a verb phrase.
    The prepositional phrase is now optional."""
    if random.randint(1, 3) == 1:
        prepPhrase = " " + prepositionalPhrase()
    else:
        prepPhrase = ""
    return random.choice(verbs) + " " + nounPhrase() + prepPhrase

def prepositionalPhrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase()

def main():
    """Allows the user to input the number of sentences
    to generate."""
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())

main()
