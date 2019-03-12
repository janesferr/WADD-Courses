sum = 0.0
data = input("Enter a number: ")
while data != "":
    number = float(data)
    sum += number
    data = input("Enter the next number: ")
print("The sum is", sum)
