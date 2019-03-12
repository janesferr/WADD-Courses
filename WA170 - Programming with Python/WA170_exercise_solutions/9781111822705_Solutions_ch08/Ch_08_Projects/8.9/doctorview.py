"""
Program: doctorview.py
Project 8.9

View class to conduct an interactive session of
nondirective psychotherapy.
"""

from doctor import Doctor

class DoctorView(object):
    """Class to handle interaction with the user."""

    def run(self):
        """Runs a session with a Doctor object."""
        doctor = Doctor()
        print(doctor.greeting())
        while True:
            sentence = input("\n>> ")
            if sentence.upper() == "QUIT":
                print(doctor.signoff())
                break
            print(doctor.reply(sentence))

# Instantiate and run a DoctorView
DoctorView().run()
