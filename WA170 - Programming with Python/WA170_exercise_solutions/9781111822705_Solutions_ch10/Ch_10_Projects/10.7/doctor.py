"""
Module: doctor.py
Project 10.7

Data model class to conduct an interactive session of
nondirective psychotherapy.

Includes a history of earlier patient inputs.
"""

import random

class Doctor(object):
    """A doctor gives a greeting, replies to patient's statements,
    and gives a signoff."""

    HEDGES = ("Please tell me more.",
              "Many of my patients tell me the same thing.",
              "Please coninue.")

    QUALIFIERS = ("Why do you say that ",
                  "You seem to think that ",
                  "Can you explain why ")

    REPLACEMENTS = {"I":"you", "ME":"you", "MY":"your",
                    "WE":"you", "US":"you", "MINE":"yours",
                    "YOURS":"mine"}

    def __init__(self):
        self._history = []

    def greeting(self):
        """Returns a greeting."""
        return "Good morning, I hope you are well today.\n" + \
               "What can I do for you?"

    def signoff(self):
        """Returns a signoff message."""
        return "Have a nice day!"

    def reply(self, sentence):
        """Implements three different reply strategies."""
        probability = random.randint(1, 3)
        if probability == 1:
            result = random.choice(Doctor.HEDGES)
        elif probability == 2 and len(self._history) > 3:
            result = "Earlier you said that " + \
                     self._changePerson(random.choice(self._history))
        else:
            result = random.choice(Doctor.QUALIFIERS) + \
                     self._changePerson(sentence)
        self._history.append(sentence)
        return result

    def _changePerson(self, sentence):
        """Replaces first person pronouns with second person
        pronouns."""
        words = sentence.split()
        replyWords = []
        for word in words:
            replyWords.append(Doctor.REPLACEMENTS.get(word.upper(), word))
        return " ".join(replyWords) 
