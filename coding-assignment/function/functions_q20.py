#Function to Calculate the Power of a Number

def power(x, n):
    result = 1
    for _ in range(abs(n)):
        result *= x
    return result if n >= 0 else 1 / result
