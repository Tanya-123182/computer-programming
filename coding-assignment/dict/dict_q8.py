#Write a Python program to create a dictionary where the key is a letter and the value is the frequency of the letter in a string.

my_string = "hello"
letter_freq = {}
for letter in my_string:
    letter_freq[letter] = letter_freq.get(letter, 0) + 1
print(letter_freq)  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
