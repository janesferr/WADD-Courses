"""
Program: guess.py
Project 3.3

The computer guesses the user's number using the minimum
number of attempts.
"""

smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
count = 0
while True:
    count += 1
    print(smaller, larger)
    yourNumber = (smaller + larger) // 2
    print("Your number is", yourNumber)
    answer = input("Enter =, <, or >: ")
    if answer == "=":
        print("Hooray, I've got it in", count, "tries!")
        break
    elif answer == "<":
        larger = yourNumber - 1
    else:
        smaller = yourNumber + 1
