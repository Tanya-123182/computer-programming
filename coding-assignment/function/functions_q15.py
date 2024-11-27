#Function to Check if a Number is a Perfect Number

def is_perfect(n):
    return sum(divisors(n)) == n
