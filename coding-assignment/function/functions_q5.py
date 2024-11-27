#Function to Find the Length of a String Without Using len()

def string_length(s):
    count = 0
    for char in s:
        count += 1
    return count
