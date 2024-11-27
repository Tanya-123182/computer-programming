#Capitalize the first letter of every word:

def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())

print(capitalize_words("hello world"))  # "Hello World"
