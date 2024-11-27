#Remove all non-alphabetical characters:

def remove_non_alphabets(s):
    return ''.join(filter(str.isalpha, s))

print(remove_non_alphabets("hello123!"))  # "hello"
