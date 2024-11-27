#Function to Check for Armstrong Number

def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    return sum(int(digit) ** power for digit in digits) == num
