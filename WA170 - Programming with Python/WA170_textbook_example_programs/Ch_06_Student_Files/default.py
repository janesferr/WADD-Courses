def repToInt(repString, base = 2):
    decimal = 0
    exponent = len(repString) - 1
    for digit in repString:
        decimal = decimal + int(digit) * base ** exponent
        exponent = exponent - 1
    return decimal


def example(required, option1 = 2, option2 = 3):
   print(required, option1, option2)


