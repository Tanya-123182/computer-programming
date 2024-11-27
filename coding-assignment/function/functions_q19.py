#Function to Find the GCD (Greatest Common Divisor)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
